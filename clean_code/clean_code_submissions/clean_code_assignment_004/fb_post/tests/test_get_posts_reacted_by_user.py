import pytest
from fb_post.utils import get_posts_reacted_by_user
from fb_post.models import User
from fb_post.exceptions import InvalidUserException


@pytest.mark.django_db
def test_get_posts_reacted_by_user_with_invalid_user_id_raises_invalid_user_exception(user, post_reaction):
    #arrange
    user_id = 2
    empty_string = ""
    zero = 0

    #act
    with pytest.raises(InvalidUserException) as error_exception:
        assert get_posts_reacted_by_user(user_id)

    #assert
    user = User.objects.filter(id=user_id)

    assert str(error_exception.value) == empty_string
    assert len(user) == zero

@pytest.mark.django_db
def test_get_posts_reacted_by_user_with_when_user_posted_no_post_returns_empty_list(users, post_reaction):
    #arrange
    user_id = 2
    empty_list = []
    #act

    post_list = get_posts_reacted_by_user(user_id)

    #assert
    assert post_list == empty_list

@pytest.mark.django_db
def test_get_posts_reacted_by_user_when_no_reactions_to_post_returns_empty_list(users, post_reaction):
    #arrange
    user_id = 2
    empty_list = []

    #act

    post_list = get_posts_reacted_by_user(user_id)

    #assert
    assert post_list == empty_list

@pytest.mark.django_db
def test_get_posts_reacted_by_user_with_valid_user_reacted_to_psts_returns_post_ids_list(users, post_reaction):
    #arrange
    user_id = 1
    list = [1]

    #act

    post_list = get_posts_reacted_by_user(user_id)

    #assert
    assert post_list == list
