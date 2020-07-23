import pytest
from freezegun import freeze_time
from fb_post.utils import create_comment
from fb_post.post_factories import (UserFactory, PostFactory,
                                    PostReactionFactory, CommentFactory,
                                    ReplyFactory, CommentReactionFactory)
from fb_post.models import User, Comment, Post, Reaction

@pytest.fixture
@freeze_time('2020-04-18 05:36:59.091819')
def user_factory():
    user = UserFactory(name="user_1")
    UserFactory.reset_sequence(0)
    return user

@pytest.fixture
@freeze_time('2020-04-18 05:36:59.091819')
def post_factory():
    post = PostFactory(content="post_1")
    PostFactory.reset_sequence(0)
    return post

@pytest.fixture
@freeze_time('2020-04-18 05:36:59.091819')
def get_post_factory():
    user = UserFactory()
    post= PostFactory(posted_by=user)
    comment = CommentFactory(post=post)
    post_reaction_factory = PostReactionFactory(post=post)
    comment_reaction_factory = CommentReactionFactory(comment=comment)
    PostFactory.reset_sequence(0)
    return post_reaction_factory, comment_reaction_factory

@pytest.fixture
@freeze_time('2020-04-18 05:36:59.091819')
def users_factory(user_factory):
    users = UserFactory.create_batch(size=2)
    UserFactory.reset_sequence(0)
    return users

@pytest.fixture
@freeze_time('2020-04-18 05:36:59.091819')
def user():
    user = User.objects.create(name="user_1")
    return user


@pytest.fixture
@freeze_time('2020-04-18 05:36:59.091819')
def users(user):
    user = [
        User(name="user_1"),
        User(name="user_2")
    ]
    User.objects.bulk_create(user)
    return User.objects.all()


@pytest.fixture
@freeze_time('2020-04-18 05:36:59.091819')
def post(user):
    post_with_user = Post.objects.create(posted_by=user, content="post_2")
    return post_with_user


@pytest.fixture
@freeze_time('2020-04-18 05:36:59.091819')
def another_post(users):
    post = Post.objects.create(posted_by=users[1], content="post_2")
    return post


@pytest.fixture
@freeze_time('2020-04-18 05:36:59.091819')
def post_reactions(users, post):
    user_list = users
    reactions_haha_lit = [
        Reaction(reacted_by_id=user_list[1].id, post_id=post.id,
                 reaction="LIT"),
        Reaction(reacted_by_id=user_list[2].id, post_id=post.id,
                 reaction="HAHA")
    ]
    Reaction.objects.bulk_create(reactions_haha_lit)
    return Reaction.objects.all()


@pytest.fixture
@freeze_time('2020-04-18 05:36:59.091819')
def post_reaction(user, post):
    reaction_type = "WOW"
    post_reaction_wow = Reaction.objects.create(reacted_by_id=user.id,
                                                post_id=post.id,
                                                reaction=reaction_type)
    return post_reaction_wow


@pytest.fixture
@freeze_time('2020-04-18 05:36:59.091819')
def comment(user, post):
    comment_content = "group_1"
    comment_id = create_comment(user.id, post.id, comment_content)
    comment_obj = Comment.objects.get(id=comment_id)
    return comment_obj


@pytest.fixture
@freeze_time('2020-04-18 05:36:59.091819')
def comment_reaction(user, comment):
    reaction_type = "LIT"
    comment_reaction_lit = Reaction.objects.create(reacted_by_id=user.id,
                                                   comment_id=comment.id,
                                                   reaction=reaction_type)
    return comment_reaction_lit


@pytest.fixture
@freeze_time('2020-04-18 05:36:59.091819')
def another_comment_reaction(users, comment):
    reaction_type = "HAHA"
    comment_reaction_haha = Reaction.objects.create(reacted_by_id=users[1].id,
                                                    comment_id=comment.id,
                                                    reaction=reaction_type)
    return comment_reaction_haha


@pytest.fixture
@freeze_time('2020-04-18 05:36:59.091819')
def comment_reply(users, comment):
    replies = [
        Comment(commented_by_id=users[1].id, post_id=comment.post_id,
                parent_comment_id=comment.id, content="reply 1"),
        Comment(commented_by_id=users[2].id, post_id=comment.post_id,
                parent_comment_id=comment.id, content="reply 2")
    ]
    Comment.objects.bulk_create(replies)
    return Comment.objects.all()


@pytest.fixture
@freeze_time('2020-04-18 05:36:59.091819')
def reply_comment_reaction(user, comment_reply):
    reaction_type = "HAHA"
    reaction_haha = Reaction.objects.create(reacted_by_id=user.id,
                                            comment_id=comment_reply[1].id,
                                            reaction=reaction_type)
    return reaction_haha
