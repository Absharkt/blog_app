from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from blog_user.forms import CreateProfile,PostForm
from .models import Profile,Post
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user
# Create your views here.


def index(request):
    return render(request,'blog_user/base.html')

@login_required(login_url='login')
def home(request):
    form = PostForm
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False) #add user to profile model
            post.author = request.user
            post.save()

    user_posts = Post.objects.filter(author=request.user)

    profile = Profile.objects.get(user=request.user)
    friends = profile.friends.all()


    context = {'form':form,'posts':user_posts,'friends': friends}
    return render(request,'blog_user/home.html',context)

@unauthenticated_user
def signup(request):
    form = CreateProfile

    if request.method == 'POST':
        form = CreateProfile(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            user = form.save()

            Profile.objects.create(
                user = user,
                username = username,
                email = email
            )

            return redirect('home')
    return render(request,'blog_user/signup.html',{'form':form})


@unauthenticated_user
def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request,username = username,password = password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.info(request,"Username or Password Incorrect !")

    return render(request,'blog_user/login.html')


def user_logout(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def friend_blog(request,frnd_id):
    friend = Profile.objects.get(id = frnd_id)
    user_id = friend.user
    posts = Post.objects.filter(author = user_id) #author is foriegn key,(id)

    context = {'friend':friend,'posts':posts}
    return render(request,'blog_user/friend.html',context)


def edit_blog(request,blog_id):
    blog = Post.objects.get(id = blog_id)
    
    form = PostForm(instance=blog)
    if request.method == 'POST':
        form = PostForm(request.POST,instance=blog)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'blog':blog,'form':form}
    return render(request,'blog_user/edit-blog.html',context)