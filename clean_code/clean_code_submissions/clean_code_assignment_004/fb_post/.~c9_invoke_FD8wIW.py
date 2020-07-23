from django.test import TestCase
from .utils import *
from .models import *
from .exceptions import *
import pytest

@pytest.fixture
@pytest.mark.django_db 
def user1():
    user=User.objects.create(name="user_1")
    return user
    
@pytest.fixture
@pytest.mark.django_db 
def users():
    user=[User(name = "user_1"),
        User(name = "user_2")
    ]
    User.objects.bulk_create(user)
    return User.objects.all()
    
@pytest.fixture
@pytest.mark.django_db 
def post1(user1):
    post1=Post.objects.create(posted_by=user1,content="post_2")
    return post1
    
@pytest.fixture
@pytest.mark.django_db 
def post1_reactions(users,post1):
    user_list=users
    reaction=[Reaction(reacted_by_id=user_list[0].id,post_id=post1.id,reaction="HAHA"),
        Reaction(reacted_by_id=user_list[1].id,post_id=post1.id,reaction="WOW")
    ]
    Reaction.objects.bulk_create(reaction)
    return Reaction.objects.all()

@pytest.fixture
@pytest.mark.django_db 
def group(user1):
    name="group_1"
    member_ids=[]
    group_id=create_group(user1,name,member_ids)
    group=Group.objects.get(id=group_id)
    
    return group
  
@pytest.fixture
@pytest.mark.django_db
def post_reaction1(user1,post1):
    reaction_type="HAHA"
    reaction=Reaction.objects.create(reacted_by_id=user1.id,post_id=post1.id,reaction=reaction_type)
    
@pytest.fixture
@pytest.mark.django_db 
def comment1(user1,post1):
    comment_content="group_1"
    comment_id=create_comment(user1.id,post1.id,comment_content)
    comment=Comment.objects.get(id=comment_id)
    
    return comment
@pytest.fixture
@pytest.mark.django_db
def comment_reaction1(user1,comment1):
    reaction_type="HAHA"
    reaction=Reaction.objects.create(reacted_by_id=user1.id,comment_id=comment1.id,reaction=reaction_type)
    

    
@pytest.mark.django_db
def test_create_post_with_invalid_user_id_raises_InvalidUserException(user1):
    #arrange
    user_id=2
    post_content="post_1"
    #act
    with pytest.raises(InvalidUserException) as e:
        assert create_post(user_id,post_content)
    
    #assert
    assert str(e.value) == ""
    

@pytest.mark.django_db
def test_create_post_with_invalid_post_content_raises_InvalidPostCotent(user1):
    user_id=1
    post_content=""
    #act
    with pytest.raises(InvalidPostContent) as e:
        assert create_post(user_id,post_content)
    
    #assert
    assert str(e.value) == ""

@pytest.mark.django_db
def test_create_post_with_valid_details_returns_post_id(user1):
    user_id=1
    post_content="post_1"
    #act
    post_id=create_post(user_id,post_content)
    
    #assert
    #extra
    post=Post.objects.get(id=post_id)
    
    assert post.posted_by==user1
    
@pytest.mark.django_db
def test_create_comment_with_invalid_user_id_raises_InvalidUserException(user1,post1):
    #arrange
    user_id=2
    post_id=1
    comment_content="post1_comment1"
    #act
    with pytest.raises(InvalidUserException) as e:
        assert create_comment(user_id,post_id,comment_content)
    
    #assert
    assert str(e.value) == ""
    
@pytest.mark.django_db
def test_create_comment_with_invalid_post_id_raises_InvalidPostException(user1,post1):
    #arrange
    user_id=1
    post_id=3
    comment_content="post1_comment1"
    #act
    with pytest.raises(InvalidPostException) as e:
        assert create_comment(user_id,post_id,comment_content)
    
    #assert
    assert str(e.value) == ""
    
    
@pytest.mark.django_db
def test_create_comment_with_invalid_comment_content_raises_InvalidPostCotent(user1,post1):
    user_id=1
    post_id=1
    comment_content=""
    #act
    with pytest.raises(InvalidCommentContent) as e:
        assert create_comment(user_id,post_id,comment_content)
    
    #assert
    assert str(e.value) == ""

@pytest.mark.django_db
def test_create_comment_with_valid_details_returns_post_id(user1,post1):
    user_id=1
    post_id=1
    comment_content="post1_comment1"
    #act
    comment_id=create_comment(user_id,post_id,comment_content)
    
    #assert
    #extra
    comment=Comment.objects.get(id=comment_id)
    
    assert comment.commented_by==user1
    assert comment.post==post1
    assert comment.content==comment_content
    
@pytest.mark.django_db
def test_reply_to_comment_with_invalid_user_id_raise_InvalidUserException(user1,comment1):
    #arrange
    user_id=2
    comment_id=1
    reply_content="comment1_reply"
    #act
    with pytest.raises(InvalidUserException) as e:
        assert reply_to_comment(user_id,comment_id,reply_content)
    
    #assert
    assert str(e.value) == ""
    
@pytest.mark.django_db
def test_reply_to_comment_with_invalid_comment_id_raise_InvalidCommentException(user1,comment1):
    #arrange
    user_id=1
    comment_id=2
    reply_content="comment1_reply"
    #act
    with pytest.raises(InvalidCommentException) as e:
        assert reply_to_comment(user_id,comment_id,reply_content)
    
    #assert
    assert str(e.value) == ""
    
@pytest.mark.django_db
def test_reply_to_comment_with_invalid_comment_content_raise_InvalidReplyContentException(user1,comment1):
    #arrange
    user_id=1
    comment_id=1
    reply_content=""
    #act
    with pytest.raises(InvalidReplyContent) as e:
        assert reply_to_comment(user_id,comment_id,reply_content)
    
    #assert
    assert str(e.value) == ""
    
@pytest.mark.django_db
def test_reply_to_comment_with_valid_details_returns_post_id(user1,comment1):
    user_id=1
    comment_id=1
    reply_content="comment1_reply"
    #act
    comment_id=reply_to_comment(user_id,comment_id,reply_content)
    
    #assert
    #extra
    comment=Comment.objects.get(id=comment_id)
    
    assert comment.commented_by==user1
    assert comment.parent_comment==comment1
    assert comment.content==reply_content

@pytest.mark.django_db
def test_react_to_post_with_invalid_user_id_raises_InvalidUserException(user1,post1):
    #arrange
    user_id=2
    post_id=1
    reaction_type="HAHA"
    #act
    with pytest.raises(InvalidUserException) as e:
        assert react_to_post(user_id,post_id,reaction_type)
    
    #assert
    assert str(e.value) == ""
    
@pytest.mark.django_db
def test_react_post_with_invalid_post_id_raises_InvalidPostException(user1,post1):
    #arrange
    user_id=1
    post_id=3
    reaction_type="HAHA"
    #act
    with pytest.raises(InvalidPostException) as e:
        assert react_to_post(user_id,post_id,reaction_type)
    
    #assert
    assert str(e.value) == ""
    
    
@pytest.mark.django_db
def test_react_to_post_with_invalid_reaction_type_raises_InvalidReactionTypeException(user1,post1):
    #arrange
    user_id=1
    post_id=1
    reaction_type="LIKE"
    #act
    with pytest.raises(InvalidReactionTypeException) as e:
        assert react_to_post(user_id,post_id,reaction_type)
    
    #assert
    assert str(e.value) == ""

@pytest.mark.django_db
def test_react_to_post_with_valid_details_creates_new_reaction(user1,post1):
    #arrange
    user_id=1
    post_id=1
    reaction_type="HAHA"
    #act
    react_to_post(user_id,post_id,reaction_type)
    
    #assert
    #extra
    reaction=Reaction.objects.get(reacted_by_id=user_id,post_id=post_id,reaction=reaction_type)
    
    assert reaction.reacted_by==user1
    assert reaction.post==post1
    assert reaction.reaction==reaction_type
    
@pytest.mark.django_db
def test_react_to_post_with_valid_details_deletes_same_reaction(user1,post1,post_reaction1):
    #arrange
    user_id=1
    post_id=1
    reaction_type="HAHA"
    #act
    react_to_post(user_id,post_id,reaction_type)
    
    #assert
    #extra
    reaction=Reaction.objects.filter(reacted_by_id=user_id,post_id=post_id,reaction=reaction_type)
    
    assert len(reaction)==0
    
@pytest.mark.django_db
def test_react_to_post_with_valid_details_updates_reaction(user1,post1,post_reaction1):
    #arrange
    user_id=1
    post_id=1
    reaction_type="WOW"
    #act
    react_to_post(user_id,post_id,reaction_type)
    
    #assert
    #extra
    reaction=Reaction.objects.get(reacted_by_id=user_id,post_id=post_id,reaction=reaction_type)
    
    assert reaction.reacted_by==user1
    assert reaction.post==post1
    assert reaction.reaction==reaction_type
    
@pytest.mark.django_db
def test_react_to_comment_with_invalid_user_id_raises_InvalidUserException(user1,comment1):
    #arrange
    user_id=2
    comment_id=1
    reaction_type="HAHA"
    #act
    with pytest.raises(InvalidUserException) as e:
        assert react_to_post(user_id,comment_id,reaction_type)
    
    #assert
    assert str(e.value) == ""
    
@pytest.mark.django_db
def test_react_comment_with_invalid_post_id_raises_InvalidPostException(user1,comment1):
    #arrange
    user_id=1
    comment_id=3
    reaction_type="HAHA"
    #act
    with pytest.raises(InvalidPostException) as e:
        assert react_to_post(user_id,comment_id,reaction_type)
    
    #assert
    assert str(e.value) == ""
    
    
@pytest.mark.django_db
def test_react_to_comment_with_invalid_reaction_type_raises_InvalidReactionTypeException(user1,comment1):
    #arrange
    user_id=1
    comment_id=1
    reaction_type="LIKE"
    #act
    with pytest.raises(InvalidReactionTypeException) as e:
        assert react_to_post(user_id,comment_id,reaction_type)
    
    #assert
    assert str(e.value) == ""

@pytest.mark.django_db
def test_react_to_comment_with_valid_details_creates_new_reaction(user1,comment1):
    
    #arrange
    user_id=1
    comment_id=1
    reaction_type="HAHA"
    
    #act
    react_to_comment(user_id,comment_id,reaction_type)
    
    
    #assert
    #extra
    reaction=Reaction.objects.get(reacted_by_id=user_id,comment_id=comment_id,reaction=reaction_type)
    
    assert reaction.reacted_by==user1
    assert reaction.comment==comment1
    assert reaction.reaction==reaction_type
    
@pytest.mark.django_db
def test_react_to_comment_with_valid_details_deletes_same_reaction(user1,comment1,comment_reaction1):
    
    #arrange
    user_id=1
    comment_id=1
    reaction_type="HAHA"
    
    #act
    react_to_comment(user_id,comment_id,reaction_type)
    
    #assert
    #extra
    reaction=Reaction.objects.filter(reacted_by_id=user1.id,comment_id=comment1.id,reaction=reaction_type)
    
    
    assert len(reaction)==0
    
@pytest.mark.django_db
def test_react_to_comment_with_valid_details_updates_reaction(user1,comment1,comment_reaction1):
    
    #arrange
    user_id=1
    comment_id=1
    reaction_type="WOW"
    
    #act
    react_to_comment(user_id,comment_id,reaction_type)
    
    #assert
    #extra
    reaction=Reaction.objects.get(reacted_by_id=user_id,comment_id=comment_id,reaction=reaction_type)
    
    assert reaction.reacted_by==user1
    assert reaction.comment==comment1
    assert reaction.reaction==reaction_type 

@pytest.mark.django_db
def test_get_total_reaction_count_when_reactions_present_returns_count_of_all_reactions(post_reaction1,comment_reaction1):
    
    #arrange
    react_count=2
    
    #act
    total_count=get_total_reaction_count()
    
    #assert
    assert total_count["count"]==react_count
    
@pytest.mark.django_db
def test_get_total_reaction_count_when_no_reactions_present_returns_count_as_zero():
    
    #arrange
    react_count=0
    
    #act
    total_count=get_total_reaction_count()
    
    #assert
    assert total_count["count"]==react_count
    
    
@pytest.mark.django_db
def test_get_reaction_metrics_when_post_exits_returns_post_reaction_metrics(post_reaction1):
    
    #arrange
    haha_count=1
    post_id=1
    
    #act
    total_count=get_reaction_metrics(post_id)
    
    #assert
    assert total_count["HAHA"] == haha_count
    
@pytest.mark.django_db
def test_get_reaction_metrics_with_invalid_post_id_raises_InvalidPostException(post_reaction1):
    
    #arrange
    haha_count=1
    post_id=2
    
    #act
    with pytest.raises(InvalidPostException) as e:
        assert get_reaction_metrics(post_id)
    
    
    #assert
    assert str(e.value) == ""
    
@pytest.mark.django_db
def test_get_reaction_metrics_when_there_is_no_reactions_to_post_returns_empty_dict(post1):
    
    #arrange
    haha_count = 1
    post_id = 1
    empty_dict = {}
    #act
    total_count=get_reaction_metrics(post_id)
    
    #assert
    assert total_count == empty_dict
    
@pytest.mark.django_db
def test_delete_post_with_inavlid_user_id_raises_InavalidUserException(user1,post1):
    #arrange
    user_id = 2
    post_id = 1
    
    #act
    with pytest.raises(InvalidUserException) as e:
        assert delete_post(user_id,post_id)
    
    #assert
    assert str(e.value) == ""
    
@pytest.mark.django_db
def test_delete_post_with_inavlid_post_id_raises_InavalidPostException(user1,post1):
    #arrange
    user_id = 1
    post_id = 2
    
    #act
    with pytest.raises(InvalidPostException) as e:
        assert delete_post(user_id,post_id)
    
    #assert
    assert str(e.value) == ""
    
@pytest.mark.django_db
def test_delete_post_when_post_id_not_created_by_user_id_raises_UserCannotDeletePostException(users,post1):
    #arrange
    user_id = 2
    post_id = 1
    
    #act
    with pytest.raises(UserCannotDeletePostException) as e:
        assert delete_post(user_id,post_id)
    
    #assert
    assert str(e.value) == ""
    
@pytest.mark.django_db
def test_delete_post_with_valid_details_deletes_post(user1,users,post1):
    #arrange
    user_id = 1
    post_id = 1
    before_delete_post=len(Post.objects.filter(posted_by = user_id , id = post_id))
    #act
    
    delete_post(user_id,post_id)
    
    #assert
    #extra
    after_delete_post = len(Post.objects.filter(posted_by = user_id , id = post_id))
    
    assert before_delete_post == 1
    assert after_delete_post == 0
@pytest.mark.django_db    
def test_get_posts_with_more_positive_reactions_when_there_no_posts_having_more_posite_reactions_returns_empty_list(post1):
    #arrange
    empty_list = []
    
    #act
    post_ids=get_posts_with_more_positive_reactions()
    
    #assert
    assert post_ids == empty_list
    
@pytest.mark.django_db   
def test_get_posts_with_more_positive_reactions_when_posts_having_more_posite_reactions_returns_post_ids_list(post1,post_reaction1):
    #arrange
    post_id_list = [1]
    
    #act
    post_ids = get_posts_with_more_positive_reactions()
    
    #assert
    assert post_ids == post_id_list
@pytest.mark.django_db      
def test_get_posts_reacted_by_user_with_invalid_user_id_raises_InvalidUserException(user1,post_reaction1):
    #arrange
    user_id = 2
    
    #act
    with pytest.raises(InvalidUserException) as e:
        assert get_posts_reacted_by_user(user_id)
    
    #assert
    assert str(e.value) == ""
@pytest.mark.django_db          
def test_get_posts_reacted_by_user_with_valid_user_id_and_reacted_to_no_post_returns_empty_list(user1,users,post_reaction1):
    #arrange
    user_id = 2
    empty_list = []
    #act
    
    post_list=get_posts_reacted_by_user(user_id)
    
    #assert
    assert post_list == empty_list
    
@pytest.mark.django_db          
def test_get_posts_reacted_by_user_with_valid_user_reacted_to_psts_returns_post_ids_list(user1,users,post_reaction1):
    #arrange
    user_id = 1
    list = [1]
    #act
    
    post_list=get_posts_reacted_by_user(user_id)
    
    #assert
    assert post_list == list
    
@pytest.mark.django_db
def test_get_reactions_to_post_with_inavlid_post_id_raises_InavlidPostException(post_reaction1):
    #arrange
    post_id = 2
    
    #act
    with pytest.raises(InvalidPostException) as e:
        assert get_reactions_to_post(post_id)
    
    #assert
    assert str(e.value) == ""
    
@pytest.mark.django_db
def test_get_reactions_to_post_when_there_is_no_reactions_to_post_returns_empty_list(post1):
    #arrange
    post_id = 1
    empty_list = []
    #act

    reactions=get_reactions_to_post(post_id)
    
    #assert
    assert reactions == empty_list
    
@pytest.mark.django_db
def test_get_reactions_to_post_when_there_is_reactions_to_post_returns_reaction_details_list(post1_reactions):
    #arrange
    post_id = 1
    result = []
    for react in post1_reactions:
        result.append({
            "user_id" : react.reacted_by_id,
            "name" : react.reacted_by.name,
            "profile_pic" : react.reacted_by.profile_pic,
            "reaction" : react.reaction
            })
    #act

    reactions=get_reactions_to_post(post_id)
    
    #assert
    assert reactions == result
    
@pytest.mark.django_db
def test_g