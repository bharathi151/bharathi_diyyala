import datetime
import factory
import random
from fb_post.models import *

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    name = "John"
    profile_pic = "profile_pic"

class PostFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Post

    content = factory.Sequence(lambda n: "post_content %d" %n)
    posted_at = factory.LazyFunction(datetime.now)
    posted_by = factory.SubFactory(UserFactory,
        name=factory.LazyAttribute(lambda obj:"AuthorOf %s" %obj.factory_parent.content))

class CommentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Comment

    content = factory.Sequence(lambda n: "comment_content %d" %n)
    commented_at = factory.LazyFunction(datetime.now)
    commented_by = factory.SubFactory(UserFactory,
        name=factory.LazyAttribute(lambda obj:"CommenterOf %s" %obj.factory_parent.content))
    post = factory.SubFactory(PostFactory)

class ReplyFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Comment

    content = factory.Sequence(lambda n: "comment_content %d" %n)
    commented_at = factory.LazyFunction(datetime.now)
    commented_by = factory.SubFactory(UserFactory,
        name=factory.LazyAttribute(lambda obj:"CommenterOf %s" %obj.factory_parent.content))
    post = factory.SubFactory(PostFactory)
    parent_comment = factory.SubFactory(CommentFactory)

class PostReactionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Reaction

    post = factory.SubFactory(PostFactory)
    reaction = factory.Iterator(["WOW", "LIT", "LOVE", "HAHA", "THUMBS-UP", "THUMBS-DOWN", "ANGRY", "SAD"])
    reacted_at = factory.LazyFunction(datetime.now)
    reacted_by = factory.SubFactory(UserFactory,
        name=factory.LazyAttribute(lambda obj:"ReacterOfPost %s" %obj.factory_parent.reaction))

class CommentReactionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Reaction

    comment = factory.SubFactory(CommentFactory)
    reaction = factory.Iterator(["WOW", "LIT", "LOVE", "HAHA", "THUMBS-UP", "THUMBS-DOWN", "ANGRY", "SAD"])
    reacted_at = factory.LazyFunction(datetime.now)
    reacted_by = factory.SubFactory(UserFactory,
        name=factory.LazyAttribute(lambda obj:"ReacterOfComment %s" %obj.factory_parent.reaction))

class ReplyReactionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Reaction

    comment = factory.SubFactory(ReplyFactory)
    reaction = factory.Iterator(["WOW", "LIT", "LOVE", "HAHA", "THUMBS-UP", "THUMBS-DOWN", "ANGRY", "SAD"])
    reacted_at = factory.LazyFunction(datetime.now)
    reacted_by = factory.SubFactory(UserFactory,
        name=factory.LazyAttribute(lambda obj:"ReacterOfComment %s" %obj.factory_parent.reaction))
