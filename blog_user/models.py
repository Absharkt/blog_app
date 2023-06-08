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

    def __str__(self):
        return self.username

    # Add other profile-related fields like profile picture, location, etc.

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200,null=True)
    content = models.TextField(blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True,blank=True,null=True)

    def __str__(self):
        return f"{self.title} : {self.author}"

    # Add other post-related fields like tags, likes, etc.


# class Friends(models.Model):
#     friend1 = models.ForeignKey(User,on_delete=models.CASCADE,related_name='user1_friends')
#     friend2 = models.ForeignKey(User,on_delete=models.CASCADE,related_name='user2_friends')

#     def __str__(self):
#         return f'{self.friend1} - {self.friend2}'

# class Comment(models.Model):
#     post = models.ForeignKey(Post, on_delete=models.CASCADE)
#     author = models.ForeignKey(User, on_delete=models.CASCADE)
#     content = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)
    # Add other comment-related fields like likes, replies, etc.
