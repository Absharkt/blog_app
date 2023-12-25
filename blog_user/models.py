from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=50,blank=True,null=True)
    email = models.EmailField(max_length=50,blank=True,null=True)
    bio = models.TextField(max_length=200, blank=True,null=True)
    location = models.CharField(max_length=100,blank=True,null=True)
    friends = models.ManyToManyField('self', blank=True)
    requests_sent = models.ManyToManyField('self', blank=True, symmetrical=False, related_name='sent_friend_requests')
    requests_received = models.ManyToManyField('self', blank=True, symmetrical=False, related_name='received_friend_requests')

    def send_request(self, to_user):
        self.requests_sent.add(to_user)
        to_user.requests_received.add(self)
        print('requst send successfully')

    def accept_request(self, from_user):
        self.requests_received.remove(from_user)
        from_user.requests_sent.remove(self)
        self.friends.add(from_user)
        print('success')

    def __str__(self):
        return self.username


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200,null=True)
    content = models.TextField(blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True,blank=True,null=True)
    likes = models.ManyToManyField(Profile,blank=True)

    def __str__(self):
        return f"{self.title} : {self.author}"



# class Comment(models.Model):
#     post = models.ForeignKey(Post, on_delete=models.CASCADE)
#     author = models.ForeignKey(User, on_delete=models.CASCADE)
#     content = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)
