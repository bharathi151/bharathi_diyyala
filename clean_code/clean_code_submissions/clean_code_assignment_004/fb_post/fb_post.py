import pytest
from django.test import TestCase
from freezegun import freeze_time
from .utils import *
from .models import User, Comment, Post, Reaction
from .exceptions import *

pytestmark = pytest.mark.django_db
@pytest.fixture
@freeze_time('2020-04-18 05:36:59.091819')
@pytest.mark.django_db 


@pytest.mark.django_db
def test_get_post_with_invalid_post_id_raises_InvalidPostException():
    #arrange
    post_id = 1
    zero = 0
    empty_string = ""
    #act
    with pytest.raises(InvalidPostException) as error_exception:
        assert get_post(post_id)

    #assert
    post = Post.objects.filter(id = post_id)

    assert str(error_exception.value) == empty_string
    assert len(post) == zero
    

@pytest.mark.django_db
def test_get_user_posts_when_user_have_no_posts_returns_empty_list(user):
    #arrange
    user_id = 1
    result = []
  
    #act
    dict = get_user_posts(user_id)
    
    #assert
    assert dict   ==   result
        
@pytest.mark.django_db
def test_get_user_posts_with_invalid_post_id_raises_InvalidUserException():
    #arrange
    user_id  =  1
    
    #act
    with pytest.raises(InvalidUserException) as e:
        assert get_user_posts(user_id)
        
    #assert
    user = User.objects.filter(id = user_id)
    
    assert str(e.value)   ==   ""
    assert len(user)   ==   0


    
    
def check_comment(expected_post_comments,post_commments):
    for expected_comments,result_commments in zip(expected_post_comments,post_commments):
        check_commenter(expected_comments["commenter"],result_commments["commenter"])
        check_reactions(expected_comments["reactions"],result_commments["reactions"])
        check_replies(expected_comments["replies"],result_commments["replies"])
        assert expected_comments["comment_id"] == result_commments["comment_id"]
        assert expected_comments["commented_at"] == result_commments["commented_at"]
        assert expected_comments["comment_content"] == result_commments["comment_content"]    
    
def check_reactions(expected_reactions,result_reactions):
    assert expected_reactions["count"] == result_reactions["count"]
    assert expected_reactions["type"] == result_reactions["type"]
    
def check_commenter(expected_commenter,result_commenter):
    assert expected_commenter["user_id"] == result_commenter["user_id"]
    assert expected_commenter["name"] == result_commenter["name"]
    assert expected_commenter["profile_pic"] == result_commenter["profile_pic"]
    
def check_replies(expected_replies,result_replies):
    for expected_comments,result_commments in zip(expected_replies,result_replies):
        check_commenter(expected_comments["commenter"],result_commments["commenter"])
        check_reactions(expected_comments["reactions"],result_commments["reactions"])
        assert expected_comments["comment_id"] == result_commments["comment_id"]
        assert expected_comments["commented_at"] == result_commments["commented_at"]
        assert expected_comments["comment_content"] == result_commments["comment_content"]    