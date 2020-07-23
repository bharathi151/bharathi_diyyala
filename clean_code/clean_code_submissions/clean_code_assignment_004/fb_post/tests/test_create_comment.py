import pytest
from fb_post.utils import create_comment
from fb_post.models import User, Comment, Post
from fb_post.exceptions import InvalidUserException, InvalidPostException
from fb_post.exceptions import InvalidCommentContent


@pytest.mark.django_db
def test_create_comment_with_invalid_user_id_raises_invalid_user_exception(post):
    # arrange
    user_id = 2
    post_id = 1
    empty_string = ""
    comment_content = "post1_comment1"
    # act
    with pytest.raises(InvalidUserException) as error_exception:
        assert create_comment(user_id, post_id, comment_content)
    # assert
    assert str(error_exception.value) == empty_string

@pytest.mark.django_db
def test_create_comment_with_invalid_post_id_raises_invalid_post_exception(user_factory,
                                                                           post):
    # arrange
    user_id = 1
    post_id = 3
    empty_string = ""
    comment_content = "post1_comment1"
    # act
    with pytest.raises(InvalidPostException) as error_exception:
        assert create_comment(user_id, post_id, comment_content)
    # assert
    assert str(error_exception.value) == empty_string

@pytest.mark.django_db
def test_create_comment_with_invalid_comment_content_raises_invalid_comment_content(user_factory, post):
    user_id = 1
    post_id = 1
    comment_content = ""
    empty_string = ""
    # act
    with pytest.raises(InvalidCommentContent) as error_exception:
        assert create_comment(user_id, post_id, comment_content)
    # assert
    assert str(error_exception.value) == empty_string

@pytest.mark.django_db
def test_create_comment_with_valid_details_returns_comment_id(user_factory, post):
    user_id = 1
    post_id = 1
    parent_comment_id = None
    comment_content = "post1_comment1"
    # act
    comment_id = create_comment(user_id, post_id, comment_content)
    # assert
    # extra
    comment = Comment.objects.get(id=comment_id)
    assert comment.commented_by == user_factory
    assert comment.post == post
    assert comment.content == comment_content
    assert comment.parent_comment_id == parent_comment_id
