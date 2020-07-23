import pytest
from fb_post.utils import get_post, get_user_posts

@pytest.mark.django_db
def test_get_post_when_post_have_no_reaplies_to_comments_returns_only_post_details_and_comments(comment, post_reactions, comment_reaction):
    #arrange
    post_id = 1
    expected_post_dict = {
        'post_id': 1,
        'posted_by': {'name': 'user_1', 'user_id': 1, 'profile_pic': ''},
        'posted_at': '2020-04-18 05:36:59.091819',
        'post_content': 'post_2',
        'reactions': {'count': 2, 'type': ['LIT', 'HAHA']},
        'comments': [
            {'comment_id': 1,
             'commenter': {'user_id': 1, 'name': 'user_1', 'profile_pic': ''},
             'commented_at': '2020-04-18 05:36:59.091819',
             'comment_content': 'group_1',
             'reactions': {'count': 1, 'type': ['LIT']},
             'replies_count': 0,
             'replies': []}],
        'comments_count': 1}

    #act
    post_dict = get_post(post_id)

    #assert
    assert len(post_dict) == len(expected_post_dict)
    assert post_dict["comments_count"] == expected_post_dict["comments_count"]
    assert post_dict["post_id"] == expected_post_dict["post_id"]
    assert post_dict["posted_by"] == expected_post_dict["posted_by"]
    assert post_dict["posted_at"] == expected_post_dict["posted_at"]
    assert post_dict["post_content"] == expected_post_dict["post_content"]
    check_comment(post_dict["comments"], expected_post_dict["comments"])
    check_reactions(post_dict["reactions"], expected_post_dict["reactions"])

@pytest.mark.django_db
def test_get_post_with_valid_details_returns_post_details_dict(comment,
                                                               post_reactions,
                                                               comment_reply,
                                                               comment_reaction,
                                                               reply_comment_reaction):
    #arrange
    post_id = 1
    expected_post_dict = {
        'post_id': 1,
        'posted_by': {'name': 'user_1', 'user_id': 1, 'profile_pic': ''},
        'posted_at': '2020-04-18 05:36:59.091819',
        'post_content': 'post_2',
        'reactions': {'count': 2, 'type': ['LIT', 'HAHA']},
        'comments': [
            {'comment_id': 1,
             'commenter': {'user_id': 1, 'name': 'user_1', 'profile_pic': ''},
             'commented_at': '2020-04-18 05:36:59.091819',
             'comment_content': 'group_1',
             'reactions': {'count': 1, 'type': ['LIT']},
             'replies_count': 2,
             'replies': [
                 {'comment_id': 2,
                  'commenter': {'user_id': 2, 'name': 'user_1', 'profile_pic': ''},
                  'commented_at': '2020-04-18 05:36:59.091819',
                  'comment_content': 'reply 1',
                  'reactions': {'count': 1, 'type': ['HAHA']}},
                 {'comment_id': 3,
                  'commenter': {'user_id': 3, 'name': 'user_2', 'profile_pic': ''},
                  'commented_at': '2020-04-18 05:36:59.091819',
                  'comment_content': 'reply 2',
                  'reactions': {'count': 0, 'type': []}}]}],
        'comments_count': 1}

    #act
    post_dict = get_post(post_id)

    #assert
    assert len(post_dict) == len(expected_post_dict)
    assert post_dict["comments_count"] == expected_post_dict["comments_count"]
    assert post_dict["post_id"] == expected_post_dict["post_id"]
    assert post_dict["posted_by"] == expected_post_dict["posted_by"]
    assert post_dict["posted_at"] == expected_post_dict["posted_at"]
    assert post_dict["post_content"] == expected_post_dict["post_content"]
    check_comment(post_dict["comments"], expected_post_dict["comments"])
    check_reactions(post_dict["reactions"], expected_post_dict["reactions"])

@pytest.mark.django_db
def test_get_user_posts_with_valid_details_returns_post_details_list(comment,
                                                                     post_reactions,
                                                                     comment_reply,
                                                                     comment_reaction):
    #arrange
    user_id = 1
    expected_result = [{
        'post_id': 1,
        'posted_by': {'name': 'user_1', 'user_id': 1, 'profile_pic': ''},
        'posted_at': '2020-04-18 05:36:59.091819',
        'post_content': 'post_2',
        'reactions': {'count': 2, 'type': ['LIT', 'HAHA']},
        'comments': [
            {'comment_id': 1,
             'commenter': {'user_id': 1, 'name': 'user_1', 'profile_pic': ''},
             'commented_at': '2020-04-18 05:36:59.091819',
             'comment_content': 'group_1',
             'reactions': {'count': 1, 'type': ['LIT']},
             'replies_count': 2,
             'replies': [
                 {'comment_id': 2,
                  'commenter': {'user_id': 2, 'name': 'user_1',
                                'profile_pic': ''},
                  'commented_at': '2020-04-18 05:36:59.091819',
                  'comment_content': 'reply 1',
                  'reactions': {'count': 0, 'type': []}},
                 {'comment_id': 3,
                  'commenter': {'user_id': 3, 'name': 'user_2', 'profile_pic': ''},
                  'commented_at': '2020-04-18 05:36:59.091819',
                  'comment_content': 'reply 2',
                  'reactions': {'count': 0, 'type': []}}]}],
        'comments_count': 1}]

    #act
    posts_list = get_user_posts(user_id)

    #assert
    assert len(posts_list) == len(expected_result)
    for item in range(len(expected_result)):
        assert posts_list[item]["comments_count"] == expected_result[item]["comments_count"]
        assert posts_list[item]["post_id"] == expected_result[item]["post_id"]
        assert posts_list[item]["posted_by"] == expected_result[item]["posted_by"]
        assert posts_list[item]["posted_at"] == expected_result[item]["posted_at"]
        assert posts_list[item]["post_content"] == expected_result[item]["post_content"]
        check_comment(posts_list[item]["comments"], expected_result[item]["comments"])
        check_reactions(posts_list[item]["reactions"], expected_result[item]["reactions"])


@pytest.mark.django_db
def test_get_user_posts_when_post_have_no_replies_to_comments_returns_only_post_details_and_comments(
    get_post_factory
    ):
    #arrange
    user_id = 1
    expected_result = [{
        'post_id': 1,
        'posted_by': {'name': 'John', 'user_id': 1, 'profile_pic': 'profile_pic'},
        'posted_at': '2020-04-18 05:36:59.091819',
        'post_content': 'post_content 0',
        'reactions': {'count': 1, 'type': ['WOW']},
        'comments': [
            {'comment_id': 1,
             'commenter': {'user_id': 2, 'name': 'CommenterOf comment_content 0', 'profile_pic': 'profile_pic'},
             'commented_at': '2020-04-18 05:36:59.091819',
             'comment_content': 'comment_content 0',
             'reactions': {'count': 1, 'type': ['WOW']},
             'replies_count': 0,
             'replies': []}],
        'comments_count': 1}]

    #act
    posts_list = get_user_posts(user_id)

    #assert
    # assert posts_list == expected_result
    # snapshot.assert_match(len(posts_list))
    # for item in range(len(posts_list)):
    #     snapshot.assert_match(posts_list[item]["comments_count"])
    #     snapshot.assert_match(posts_list[item]["post_id"])
    #     snapshot.assert_match(posts_list[item]["posted_by"])
    #     snapshot.assert_match(posts_list[item]["posted_at"])
    #     snapshot.assert_match(posts_list[item]["post_content"])
    #     check_comment(posts_list[item]["comments"], snapshot)
    #     check_reactions(posts_list[item]["reactions"], snapshot)
    assert len(posts_list) == len(expected_result)
    for item in range(len(expected_result)):
        assert posts_list[item]["comments_count"] == expected_result[item]["comments_count"]
        assert posts_list[item]["post_id"] == expected_result[item]["post_id"]
        assert posts_list[item]["posted_by"] == expected_result[item]["posted_by"]
        assert posts_list[item]["posted_at"] == expected_result[item]["posted_at"]
        assert posts_list[item]["post_content"] == expected_result[item]["post_content"]
        check_comment(posts_list[item]["comments"], expected_result[item]["comments"])
        check_reactions(posts_list[item]["reactions"], expected_result[item]["reactions"])

def check_comment(expected_post_comments, post_commments):
    for expected_comments, result_commments in zip(expected_post_comments,
                                                  post_commments):
        check_commenter(expected_comments["commenter"],
                        result_commments["commenter"])
        check_reactions(expected_comments["reactions"],
                        result_commments["reactions"])
        check_replies(expected_comments["replies"],
                      result_commments["replies"])
        assert expected_comments["comment_id"] == result_commments["comment_id"]
        assert expected_comments["commented_at"] == result_commments["commented_at"]
        assert expected_comments["comment_content"] == result_commments["comment_content"]

# def check_comment(post_commments, snapshot):
#     for expected_comments, result_commments in post_commments:
#         check_commenter(result_commments["commenter"], snapshot)
#         check_reactions(result_commments["reactions"], snapshot)
#         check_replies(result_commments["replies"], snapshot)
#         snapshot.assert_match(result_commments["comment_id"])
#         snapshot.assert_match(result_commments["commented_at"])
#         snapshot.assert_match(result_commments["comment_content"])

# def check_reactions(result_reactions, snapshot):
#     snapshot.assert_match(result_reactions["count"])
#     snapshot.assert_match(result_reactions["type"])

# def check_commenter(result_commenter, snapshot):
#     snapshot.assert_match(result_commenter["user_id"])
#     snapshot.assert_match(result_commenter["name"])
#     snapshot.assert_match(result_commenter["profile_pic"])

# def check_replies(result_replies, snapshot):
#     for result_commments in result_replies:
#         check_commenter(result_commments["commenter"], snapshot)
#         check_reactions(result_commments["reactions"], snapshot)
#         snapshot.assert_match(result_commments["comment_id"])
#         snapshot.assert_match(result_commments["commented_at"])
#         snapshot.assert_match(result_commments["comment_content"])

def check_reactions(expected_reactions, result_reactions):
    assert expected_reactions["count"] == result_reactions["count"]
    assert expected_reactions["type"] == result_reactions["type"]

def check_commenter(expected_commenter, result_commenter):
    assert expected_commenter["user_id"] == result_commenter["user_id"]
    assert expected_commenter["name"] == result_commenter["name"]
    assert expected_commenter["profile_pic"] == result_commenter["profile_pic"]

def check_replies(expected_replies, result_replies):
    for expected_comments, result_commments in zip(expected_replies,
                                                  result_replies):
        check_commenter(expected_comments["commenter"],
                        result_commments["commenter"])
        check_reactions(expected_comments["reactions"],
                        result_commments["reactions"])
        assert expected_comments["comment_id"] == result_commments["comment_id"]
        assert expected_comments["commented_at"] == result_commments["commented_at"]
        assert expected_comments["comment_content"] == result_commments["comment_content"]
