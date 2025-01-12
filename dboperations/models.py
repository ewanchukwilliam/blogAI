from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    post_author = models.ForeignKey('authentication.User', on_delete=models.CASCADE, related_name='posts')
    statistics = models.JSONField(default=dict)

    def __str__(self):
        return self.title
    
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    comment_author = models.ForeignKey('authentication.User', on_delete=models.CASCADE, related_name='comments')
    statistics = models.JSONField(default=dict)

    def __str__(self):
        return self.content

class Heart(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    heart_author = models.ForeignKey('authentication.User', on_delete=models.CASCADE, related_name='hearts')

    def __str__(self):
        return self.author

class Follow(models.Model):
    follower = models.ForeignKey('authentication.User', on_delete=models.CASCADE, related_name='following')
    followee = models.ForeignKey('authentication.User', on_delete=models.CASCADE, related_name='followers')

    def __str__(self):
        return self.follower






# Create your models here.

