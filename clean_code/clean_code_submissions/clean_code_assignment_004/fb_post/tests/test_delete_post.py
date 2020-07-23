import pytest
from fb_post.utils import delete_post
from fb_post.models import User, Post
from fb_post.exceptions import InvalidUserException
from fb_post.exceptions import InvalidPostException
from fb_post.exceptions import UserCannotDeletePostException


@pytest.mark.django_db
def test_delete_post_with_inavlid_user_id_raises_inavalid_user_exception(post_factory):
    # arrange
    user_id = 2
    post_id = 1
    empty = ""

    # act
    with pytest.raises(InvalidUserException) as error_exception:
        assert delete_post(user_id, post_id)

    # assert
    assert str(error_exception.value) == empty

@pytest.mark.django_db
def test_delete_post_with_inavlid_post_id_raises_inavalid_post_exception(
    post_factory):
    # arrange
    user_id = 1
    post_id = 2
    empty_string = ""

    # act
    with pytest.raises(InvalidPostException) as error_exception:
        assert delete_post(user_id, post_id)

    # assert
    assert str(error_exception.value) == empty_string

@pytest.mark.django_db
def test_delete_post_when_post_id_not_created_by_user_id_raises_user_cannot_delete_post_exception(
    users_factory, post_factory):
    # arrange
    user_id = 3
    post_id = 1
    empty_string = ""

    # act
    with pytest.raises(UserCannotDeletePostException) as error_exception:
        assert delete_post(user_id, post_id)

    # assert
    # extra
    post = Post.objects.get(id=post_id)

    assert str(error_exception.value) == empty_string
    assert post.posted_by_id != user_id

@pytest.mark.django_db
def test_delete_post_with_valid_details_deletes_post(post_factory):
    # arrange
    user_id = 1
    post_id = 1
    zero = 0
    one = 1
    before_delete_post = len(Post.objects.filter(posted_by=user_id, id=post_id))

    # act
    delete_post(user_id, post_id)

    # assert
    # extra
    after_delete_post = len(Post.objects.filter(posted_by=user_id, id=post_id))

    assert before_delete_post == one
    assert after_delete_post == zero
