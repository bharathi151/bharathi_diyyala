from fb_post.exceptions import (InvalidUserException, InvalidPostException,
                                InvalidCommentException, InvalidCommentContent,
                                InvalidPostContent, InvalidReplyContent,
                                InvalidReactionTypeException
                               )
from fb_post.models import User, Post, Comment
from fb_post.constants import ReactionTypes

def check_for_user(user_id):
    try:
        user = User.objects.get(id=user_id)

    except User.DoesNotExist:
        raise InvalidUserException

    return user

def check_for_post(post_id):
    try:
        post = Post.objects.get(id=post_id)

    except Post.DoesNotExist:
        raise InvalidPostException

    return post

def check_for_comment(comment_id):
    try:
        comment = Comment.objects.get(id=comment_id)

    except Comment.DoesNotExist:
        raise InvalidCommentException

    return comment

def is_valid_comment_content(comment_content):
    is_not_valid = not comment_content
    if is_not_valid:
        raise InvalidCommentContent

def is_valid_post_content(post_content):
    is_not_valid = not post_content
    if is_not_valid:
        raise InvalidPostContent

def is_valid_reaction_type(reaction_type):
    valid_reaction_types = ReactionTypes.values
    is_not_valid = reaction_type not in valid_reaction_types
    if is_not_valid:
        raise InvalidReactionTypeException

def is_valid_reply_content(reply_content):
    is_not_valid = not reply_content
    if is_not_valid:
        raise InvalidReplyContent
