import pytest
from fb_post.utils import create_post
from fb_post.models import User, Post
from fb_post.exceptions import InvalidUserException, InvalidPostContent

@pytest.mark.django_db
def test_create_post_with_invalid_user_id_raises_invalid_user_exception(user_factory):
    # arrange
    user_id = 2
    post_content = "post_1"
    empty_string = ""
    # act
    with pytest.raises(InvalidUserException) as error_exception:
        assert create_post(user_id, post_content)
    # assert
    assert str(error_exception.value) == empty_string

@pytest.mark.django_db
def test_create_post_with_invalid_post_content_raises_invalid_post_content(
        user_factory):
    # arrange
    user_id = 1
    post_content = ""
    empty_string = ""
    # act
    with pytest.raises(InvalidPostContent) as error_exception:
        assert create_post(user_id, post_content)
    # assert
    assert str(error_exception.value) == empty_string

@pytest.mark.django_db
def test_create_post_with_valid_details_returns_post_id(user_factory):
    user_id = 1
    post_content = "post_1"
    # act
    post_id = create_post(user_id, post_content)
    # assert
    # extra
    post = Post.objects.get(id=post_id)
    assert post.posted_by == user_factory
