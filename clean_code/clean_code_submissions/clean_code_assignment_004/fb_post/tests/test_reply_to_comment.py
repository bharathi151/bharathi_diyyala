import pytest
from fb_post.utils import reply_to_comment
from fb_post.models import User, Comment
from fb_post.exceptions import InvalidUserException
from fb_post.exceptions import InvalidCommentException
from fb_post.exceptions import InvalidReplyContent


@pytest.mark.django_db
def test_reply_to_comment_with_invalid_user_id_raise_invalid_user_exception(user, comment):
    #arrange
    user_id = 2
    comment_id = 1
    reply_content = "comment1_reply"
    zero = 0
    empty_string = ""

    #act
    with pytest.raises(InvalidUserException) as error_exception:
        assert reply_to_comment(user_id, comment_id, reply_content)

    #assert
    user = User.objects.filter(id=user_id)

    assert str(error_exception.value) == empty_string
    assert len(user) == zero


@pytest.mark.django_db
def test_reply_to_comment_with_invalid_comment_id_raise_invalid_comment_exception(user, comment):
    #arrange
    user_id = 1
    comment_id = 2
    reply_content = "comment1_reply"
    zero = 0
    empty_string = ""

    #act
    with pytest.raises(InvalidCommentException) as error_exception:
        assert reply_to_comment(user_id, comment_id, reply_content)

    #assert
    comment = Comment.objects.filter(id=comment_id)

    assert str(error_exception.value) == empty_string
    assert len(comment) == zero


@pytest.mark.django_db
def test_reply_to_comment_with_invalid_comment_content_raise_invalid_reply_content_exception(user, comment):
    #arrange
    user_id = 1
    comment_id = 1
    reply_content = ""
    empty_string = ""

    #act
    with pytest.raises(InvalidReplyContent) as error_exception:
        assert reply_to_comment(user_id, comment_id, reply_content)

    #assert
    assert str(error_exception.value) == empty_string
    assert reply_content == empty_string


@pytest.mark.django_db
def test_reply_to_comment_with_valid_details_returns_comment_id(user, comment):
    #arrange
    user_id = 1
    comment_id = 1
    reply_content = "comment1_reply"

    #act
    comment_id = reply_to_comment(user_id, comment_id, reply_content)

    #assert
    #extra
    new_comment = Comment.objects.get(id=comment_id)

    assert new_comment.commented_by == user
    assert new_comment.parent_comment == comment
    assert new_comment.content == reply_content
