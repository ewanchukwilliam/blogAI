from django.conf import settings
from django.db import models


def default_statistics():
    return {"total_likes": 0, "total_comments": 0, "total_replies": 0}


class Blog(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="blogs"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    statistics = models.JSONField(default=default_statistics)

    def __str__(self):
        return self.title


class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    gold_star = models.BooleanField(default=False)

    def __str__(self):
        return f'Comment by {self.author.username} on "{self.blog.title}"'

    def award_gold_star(self):
        self.gold_star = True
        self.save()
