import factory
from factory.django import DjangoModelFactory
from blogers.models import Bloger, Blog, Post, Comment
import random


class BlogerFactory(DjangoModelFactory):
    class Meta:
        model = Bloger

    email = factory.Faker("email")
    login = factory.Faker("user_name")


class BlogFactory(DjangoModelFactory):
    class Meta:
        model = Blog

    name = factory.Faker("company")
    description = factory.Faker("paragraph")
    owner_id = factory.SubFactory(BlogerFactory)


class PostFactory(DjangoModelFactory):
    class Meta:
        model = Post

    header = factory.Faker("sentence")
    text = factory.Faker("paragraph", nb_sentences=5)
    author_id = factory.SubFactory(BlogerFactory)
    blog_id = factory.SubFactory(BlogFactory)


class CommentFactory(DjangoModelFactory):
    class Meta:
        model = Comment

    text = factory.Faker("paragraph", nb_sentences=5)
    author_id = factory.LazyFunction(lambda: Bloger.objects.get(id=random.randint(1, 30)))
    post_id = factory.LazyFunction(lambda: Post.objects.get(id=random.randint(1, 20)))
