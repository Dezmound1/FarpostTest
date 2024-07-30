from django.db import models
from logs.models import Logs, EventType


class Bloger(models.Model):
    email = models.EmailField(unique=True)
    login = models.CharField(max_length=50, unique=True)

    class Meta:
        db_table = "users"

    @staticmethod
    def get_all_posts(login: str):
        post_user = Post.objects.filter(author_id=Bloger.objects.get(login=login))

        return (Bloger.objects.get(login=login), post_user)


class Blog(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    owner_id = models.ForeignKey(Bloger, on_delete=models.CASCADE)

    class Meta:
        db_table = "blog"


class Post(models.Model):
    header = models.CharField(max_length=200)
    text = models.CharField(max_length=2000)
    author_id = models.ForeignKey(Bloger, on_delete=models.CASCADE)
    blog_id = models.ForeignKey(Blog, on_delete=models.CASCADE)

    class Meta:
        db_table = "post"


class Comment(models.Model):
    text = models.CharField(max_length=2000)
    author_id = models.ForeignKey(Bloger, on_delete=models.CASCADE)
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)

    class Meta:
        db_table = "comment"
