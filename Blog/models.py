from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='property_images/')
    likes = models.IntegerField()
    shares = models.IntegerField()

    def __str__(self):
        return self.title 

    def total_comments(self):
        return self.comments.count()

class Comment(models.Model):
    post = models.ForeignKey(BlogPost, related_name="comments", on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    profile_image = models.ImageField(upload_to='property_images/', blank=True, null=True)


    def __str__(self):
        return f"Maoni ya {self.user.username} kwenye {self.post.title}"

