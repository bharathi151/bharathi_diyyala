import pytest
from fb_post.utils import get_reactions_to_post, get_replies_for_comment
from fb_post.models import Comment
from fb_post.exceptions import InvalidCommentException


@pytest.mark.django_db
def test_get_reactions_to_post_when_there_is_reactions_to_post_returns_reaction_details_list(post_reactions):
    # arrange
    post_id = 1
    result = [{'user_id': 2, 'name': 'user_1', 'profile_pic': '', 'reaction': 'LIT'},
              {'user_id': 3, 'name': 'user_2', 'profile_pic': '', 'reaction': 'HAHA'}]

    # act

    reactions = get_reactions_to_post(post_id)

    # assert
    assert reactions == result


@pytest.mark.django_db
def test_get_replies_for_comment_with_invalid_comment_id_raises_invalid_comment_exception(comment_reply):
    # arrange
    comment_id = 4
    empty_string = ""
    zero = 0

    # act
    with pytest.raises(InvalidCommentException) as error_exception:
        assert get_replies_for_comment(comment_id)

    # assert
    comment = Comment.objects.filter(id=comment_id)

    assert str(error_exception.value) == empty_string
    assert len(comment) == zero

@pytest.mark.django_db
def test_get_replies_for_comment_with_valid_comment_id_returns_reply_list(comment_reply):
    # arrange
    comment_id = 3
    expected_list = []

    # act

    reply_list = get_replies_for_comment(comment_id)

    # assert
    assert reply_list == expected_list


@pytest.mark.django_db
def test_get_replies_for_comment_when_comment_have_no_replies_returns_empty_list(comment_reply):
    # arrange
    comment_id = 1
    expected_result = get_expected_result()


    # act

    reply_list = get_replies_for_comment(comment_id)

    # assert
    assert reply_list == expected_result


def get_expected_result():
    expected_result = [{
        'comment_id': 2,
        'commenter': {
            'user_id': 2,
            'name': 'user_1',
            'profile_pic': ''},
        'commented_at': '2020-04-18 05:36:59.091819',
        'comment_content': 'reply 1'}]

    expected_result.append({
        'comment_id': 3,
        'commenter': {
            'user_id': 3,
            'name': 'user_2',
            'profile_pic': ''
        },
        'commented_at': '2020-04-18 05:36:59.091819',
        'comment_content': 'reply 2'
        })
    return expected_result
