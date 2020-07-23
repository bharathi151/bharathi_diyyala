import pytest
from fb_post.utils import get_post, get_user_posts
from fb_post.models import Post, User
from fb_post.exceptions import InvalidPostException, InvalidUserException

@pytest.mark.django_db
def test_get_user_posts_with_invalid_post_id_raises_invalid_post_exception():
    #arrange
    post_id = 1
    zero = 0
    empty_string = ""
    #act
    with pytest.raises(InvalidPostException) as error_exception:
        assert get_post(post_id)

    #assert
    post = Post.objects.filter(id=post_id)

    assert str(error_exception.value) == empty_string
    assert len(post) == zero

@pytest.mark.django_db
def test_get_user_posts_when_user_have_no_posts_returns_empty_list(user):
    #arrange
    user_id = 1
    expected_list = []

    #act
    posts_list = get_user_posts(user_id)

    #assert
    assert expected_list == posts_list

@pytest.mark.django_db
def test_get_post_when_post_have_no_comments_and_reactions_returns_only_post_details(post):
    #arrange
    post_id = 1
    expected_post_dict = {
        'post_id': 1,
        'posted_by': {'name': 'user_1', 'user_id': 1, 'profile_pic': ''},
        'posted_at': '2020-04-18 05:36:59.091819',
        'post_content': 'post_2',
        'reactions': {'count': 0, 'type': []},
        'comments': [],
        'comments_count': 0}

    #act
    post_dict = get_post(post_id)

    #assert
    assert len(post_dict) == len(expected_post_dict)
    assert post_dict["comments_count"] == expected_post_dict["comments_count"]
    assert post_dict["post_id"] == expected_post_dict["post_id"]
    assert post_dict["posted_by"] == expected_post_dict["posted_by"]
    assert post_dict["posted_at"] == expected_post_dict["posted_at"]
    assert post_dict["post_content"] == expected_post_dict["post_content"]
    assert post_dict["comments"] == expected_post_dict["comments"]
    assert post_dict["reactions"] == expected_post_dict["reactions"]

@pytest.mark.django_db
def test_get_user_posts_with_invalid_post_id_raises_invalid_user_exception():
    #arrange
    user_id = 1
    zero = 0
    empty_string = ""

    #act
    with pytest.raises(InvalidUserException) as error_exception:
        assert get_user_posts(user_id)

    #assert
    user = User.objects.filter(id=user_id)

    assert str(error_exception.value) == empty_string
    assert len(user) == zero

@pytest.mark.django_db
def test_get_user_posts_when_post_have_no_comments_and_reactions_returns_only_post_details(post):
    #arrange
    user_id = 1
    expected_post_list = [{
        'post_id': 1,
        'posted_by': {'name': 'user_1', 'user_id': 1, 'profile_pic': ''},
        'posted_at': '2020-04-18 05:36:59.091819',
        'post_content': 'post_2',
        'reactions': {'count': 0, 'type': []},
        'comments': [],
        'comments_count': 0}]

    #act
    posts_list = get_user_posts(user_id)

    #assert
    assert expected_post_list == posts_list
