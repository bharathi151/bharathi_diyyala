from django.test import TestCase
from freezegun import freeze_time
from .utils import *
from .models import *
from .exceptions import *
import pytest
pytestmark = pytest.mark.django_db
@pytest.fixture
@freeze_time('2020-04-18 05:36:59.091819')
@pytest.mark.django_db 
def user():
    user  =  User.objects.create(name  =  "user_1")
    return user
    
@pytest.fixture
@freeze_time('2020-04-18 05:36:59.091819')
@pytest.mark.django_db 
def users(user):
    user  =  [User(name  =  "user_1"),
        User(name  =  "user_2")
    ]
    User.objects.bulk_create(user)
    return User.objects.all()
    
@pytest.fixture
@freeze_time('2020-04-18 05:36:59.091819')
@pytest.mark.django_db 
def post(user):
    post  =  Post.objects.create(posted_by  =  user,content  =  "post_2")
    return post
    
    
    
@pytest.fixture
@freeze_time('2020-04-18 05:36:59.091819')
@pytest.mark.django_db 
def another_post(users):
    post  =  Post.objects.create(posted_by  =  users[1],content  =  "post_2")
    return post
    
    
    
@pytest.fixture
@freeze_time('2020-04-18 05:36:59.091819')
@pytest.mark.django_db 
def post_reactions(users,post):
    user_list  =  users
    reaction = [Reaction(reacted_by_id  =  user_list[1].id,post_id  =  post.id,reaction  =  "LIT"),
        Reaction(reacted_by_id  =  user_list[2].id,post_id  =  post.id,reaction  =  "HAHA")
    ]
    Reaction.objects.bulk_create(reaction)
    return Reaction.objects.all()


@pytest.fixture
@freeze_time('2020-04-18 05:36:59.091819')
@pytest.mark.django_db
def post_reaction(user,post):
    reaction_type = "WOW"
    reaction  =  Reaction.objects.create(reacted_by_id  =  user.id,post_id  =  post.id,reaction  =  reaction_type)
    
@pytest.fixture
@freeze_time('2020-04-18 05:36:59.091819')
@pytest.mark.django_db 
def comment(user,post):
    comment_content  =  "group_1"
    comment_id   =   create_comment(user.id,post.id,comment_content)
    comment = Comment.objects.get(id = comment_id)
    return comment
    
    
@pytest.fixture
@freeze_time('2020-04-18 05:36:59.091819')
@pytest.mark.django_db
def comment_reaction(user,comment):
    reaction_type = "LIT"
    reaction = Reaction.objects.create(reacted_by_id = user.id,comment_id = comment.id,reaction = reaction_type)


@pytest.fixture
@freeze_time('2020-04-18 05:36:59.091819')
@pytest.mark.django_db
def another_comment_reaction(users,comment):
    reaction_type = "HAHA"
    reaction = Reaction.objects.create(reacted_by_id = users[1].id,comment_id = comment.id,reaction = reaction_type)


@pytest.fixture
@freeze_time('2020-04-18 05:36:59.091819')
@pytest.mark.django_db
def comment_reply(users,comment):
    reply = [Comment(commented_by_id = users[1].id,post_id = comment.post_id,parent_comment_id = comment.id,content = "reply 1"),
     Comment(commented_by_id = users[2].id,post_id = comment.post_id,parent_comment_id = comment.id,content = "reply 2")]
    Comment.objects.bulk_create(reply)
    return Comment.objects.all()
    
@pytest.fixture
@freeze_time('2020-04-18 05:36:59.091819')
@pytest.mark.django_db
def reply_comment_reaction(user,comment_reply):
    reaction_type  =  "HAHA"
    reaction = Reaction.objects.create(reacted_by_id  =  user.id,comment_id  =  comment_reply[1].id,reaction  =  reaction_type)
    


    
@pytest.mark.django_db
def test_create_post_with_invalid_user_id_raises_InvalidUserException(user):
    #arrange
    user_id = 2
    post_content = "post_1"
    #act
    with pytest.raises(InvalidUserException) as e:
        assert create_post(user_id,post_content)
    
    #assert
    #extra
    user = User.objects.filter(id = user_id)
    
    assert str(e.value)  ==  ""
    assert len(user)  ==  0
    

@pytest.mark.django_db
def test_create_post_with_invalid_post_content_raises_InvalidPostCotent(user):
    user_id = 1
    post_content = ""
    #act
    with pytest.raises(InvalidPostContent) as e:
        assert create_post(user_id,post_content)
    
    #assert
    assert str(e.value)   ==   ""
    assert post_content   ==   ""

@pytest.mark.django_db
def test_create_post_with_valid_details_returns_post_id(user):
    user_id = 1
    post_content = "post_1"
    #act        
    post_id = create_post(user_id,post_content)
    
    #assert
    #extra
    post = Post.objects.get(id = post_id)
    
    assert post.posted_by  ==  user
    assert post.content == post_content

    
@pytest.mark.django_db
def test_create_comment_with_invalid_user_id_raises_InvalidUserException(user,post):
    #arrange
    user_id = 2
    post_id = 1
    comment_content = "post1_comment1"
    #act
    with pytest.raises(InvalidUserException) as e:
        assert create_comment(user_id,post_id,comment_content)
    
    #assert
    user = User.objects.filter(id = user_id)
    
    assert str(e.value)   ==   ""
    assert len(user)   ==   0
    
    
@pytest.mark.django_db
def test_create_comment_with_invalid_post_id_raises_InvalidPostException(user,post):
    #arrange
    user_id = 1
    post_id = 3
    comment_content = "post1_comment1"
    #act
    with pytest.raises(InvalidPostException) as e:
        assert create_comment(user_id,post_id,comment_content)
    
    #assert
    post = Post.objects.filter(id = post_id)
    
    assert str(e.value)   ==   ""
    assert len(post)   ==   0
    
    
@pytest.mark.django_db
def test_create_comment_with_invalid_comment_content_raises_InvalidCommentContent(user,post):
    user_id = 1
    post_id = 1
    comment_content = ""
    #act
    with pytest.raises(InvalidCommentContent) as e:
        assert create_comment(user_id,post_id,comment_content)
    
    #assert
    assert str(e.value)   ==   ""
    assert     comment_content   ==   ""
    
    
@pytest.mark.django_db
def test_create_comment_with_valid_details_returns_comment_id(user,post):
    user_id = 1
    post_id = 1
    comment_content = "post1_comment1"
    #act
    comment_id = create_comment(user_id,post_id,comment_content)
    
    #assert
    #extra
    comment = Comment.objects.get(id = comment_id)
    
    assert comment.commented_by  ==  user
    assert comment.post  ==  post
    assert comment.content  ==  comment_content
    assert comment.parent_comment_id  ==  None
    
@pytest.mark.django_db
def test_reply_to_comment_with_invalid_user_id_raise_InvalidUserException(user,comment):
    #arrange
    user_id = 2
    comment_id = 1
    reply_content = "comment1_reply"
    #act
    with pytest.raises(InvalidUserException) as e:
        assert reply_to_comment(user_id,comment_id,reply_content)
    
    #assert
    user = User.objects.filter(id = user_id)
    
    assert str(e.value)   ==   ""
    assert len(user)   ==   0
    
@pytest.mark.django_db
def test_reply_to_comment_with_invalid_comment_id_raise_InvalidCommentException(user,comment):
    #arrange
    user_id = 1
    comment_id = 2
    reply_content = "comment1_reply"
    #act
    with pytest.raises(InvalidCommentException) as e:
        assert reply_to_comment(user_id,comment_id,reply_content)
    
    #assert
    comment = Comment.objects.filter(id = comment_id)
    
    assert str(e.value)   ==   ""
    assert len(comment)   ==   0
    
@pytest.mark.django_db
def test_reply_to_comment_with_invalid_comment_content_raise_InvalidReplyContentException(user,comment):
    #arrange
    user_id = 1
    comment_id = 1
    reply_content = ""
    #act
    with pytest.raises(InvalidReplyContent) as e:
        assert reply_to_comment(user_id,comment_id,reply_content)
    
    #assert
    assert str(e.value)   ==   ""
    assert reply_content  ==  ""
    
@pytest.mark.django_db
def test_reply_to_comment_with_valid_details_returns_comment_id(user,comment):
    user_id = 1
    comment_id = 1
    reply_content = "comment1_reply"
    #act
    comment_id = reply_to_comment(user_id,comment_id,reply_content)
    
    #assert
    #extra
    new_comment = Comment.objects.get(id = comment_id)
    
    assert new_comment.commented_by  ==  user
    assert new_comment.parent_comment  ==  comment
    assert new_comment.content  ==  reply_content

@pytest.mark.django_db
def test_react_to_post_with_invalid_user_id_raises_InvalidUserException(user,post):
    #arrange
    user_id = 2
    post_id = 1
    reaction_type = "HAHA"
    #act
    with pytest.raises(InvalidUserException) as e:
        assert react_to_post(user_id,post_id,reaction_type)
    
    #assert
    user = User.objects.filter(id = user_id)
    
    assert str(e.value)   ==   ""
    assert len(user)   ==   0
    
@pytest.mark.django_db
def test_react_post_with_invalid_post_id_raises_InvalidPostException(user,post):
    #arrange
    user_id = 1
    post_id = 3
    reaction_type = "HAHA"
    #act
    with pytest.raises(InvalidPostException) as e:
        assert react_to_post(user_id,post_id,reaction_type)
    
    #assert
    post = Post.objects.filter(id = post_id)
    
    assert str(e.value)   ==   ""
    assert len(post)   ==   0
    
    
@pytest.mark.django_db
def test_react_to_post_with_invalid_reaction_type_raises_InvalidReactionTypeException(user,post):
    #arrange
    user_id = 1
    post_id = 1
    reaction_type = "LIKE"
    #act
    with pytest.raises(InvalidReactionTypeException) as e:
        assert react_to_post(user_id,post_id,reaction_type)
    
    #assert
    assert str(e.value)   ==   ""
    # assert reaction_type not in ['WOW','LIT','LOVE','HAHA','THUMBS-UP','THUMBS-DOWN','ANGRY','SAD']

@pytest.mark.django_db
def test_react_to_post_with_valid_details_creates_new_reaction(user,post):
    #arrange
    user_id = 1
    post_id = 1
    reaction_type = "HAHA"
    #act
    react_to_post(user_id,post_id,reaction_type)
    
    #assert
    #extra
    reaction = Reaction.objects.get(reacted_by_id = user_id,post_id = post_id,reaction = reaction_type)
    
    assert reaction.reacted_by  ==  user
    assert reaction.post  ==  post
    assert reaction.reaction  ==  reaction_type
    # assert reaction.reaction in ['WOW','LIT','LOVE','HAHA','THUMBS-UP','THUMBS-DOWN','ANGRY','SAD']
    
@pytest.mark.django_db
def test_react_to_post_with_same_reaction_deletes_reaction(user,post,post_reaction):
    #arrange
    user_id = 1
    post_id = 1
    reaction_type = "WOW"
    length_before_delete = len(Reaction.objects.filter(reacted_by_id = user_id,post_id = post_id,reaction = reaction_type))
    #act
    react_to_post(user_id,post_id,reaction_type)
    
    #assert
    #extra
    reaction = Reaction.objects.filter(reacted_by_id = user_id,post_id = post_id,reaction = reaction_type)
    
    assert len(reaction)  ==  0
    assert length_before_delete   ==   1
    
@pytest.mark.parametrize("new_reaction_type", [("HAHA"),("SAD"),("ANGRY")

 ])   
@pytest.mark.django_db
def test_react_to_post_with_different_reaction_updates_reaction(user,post,post_reaction,new_reaction_type):
    #arrange
    user_id = 1
    post_id = 1
    reaction_type = new_reaction_type
    #act
    react_to_post(user_id,post_id,reaction_type)
    
    #assert
    #extra
    reaction = Reaction.objects.get(reacted_by_id = user_id,post_id = post_id,reaction = reaction_type)
    
    assert reaction.reacted_by  ==  user
    assert reaction.post  ==  post
    assert reaction.reaction  ==  reaction_type
    # assert reaction.reaction in ['WOW','LIT','LOVE','HAHA','THUMBS-UP','THUMBS-DOWN','ANGRY','SAD']
@pytest.mark.django_db
def test_react_to_comment_with_invalid_user_id_raises_InvalidUserException(user,comment):
    #arrange
    user_id = 2
    comment_id = 1
    reaction_type = "HAHA"
    #act
    with pytest.raises(InvalidUserException) as e:
        assert react_to_comment(user_id,comment_id,reaction_type)
    
    #assert
    user = User.objects.filter(id = user_id)
    
    assert str(e.value)   ==   ""
    assert len(user)   ==   0
    
@pytest.mark.django_db
def test_react_comment_with_invalid_comment_id_raises_InvalidCommentException(user,comment):
    #arrange
    user_id = 1
    comment_id = 3
    reaction_type = "HAHA"
    #act
    with pytest.raises(InvalidCommentException) as e:
        assert react_to_comment(user_id,comment_id,reaction_type)
    
    #assert
    comment = Comment.objects.filter(id = comment_id)
    
    assert str(e.value)   ==   ""
    assert len(comment)   ==   0

    
    
@pytest.mark.django_db
def test_react_to_comment_with_invalid_reaction_type_raises_InvalidReactionTypeException(user,comment):
    #arrange
    user_id = 1
    comment_id = 1
    reaction_type = "LIKE"
    #act
    with pytest.raises(InvalidReactionTypeException) as e:
        assert react_to_comment(user_id,comment_id,reaction_type)
    
    #assert
    assert str(e.value)   ==   ""
    # assert reaction_type not in ['WOW','LIT','LOVE','HAHA','THUMBS-UP','THUMBS-DOWN','ANGRY','SAD']

@pytest.mark.django_db
def test_react_to_comment_with_valid_details_creates_new_reaction(user,comment):
    
    #arrange
    user_id = 1
    comment_id = 1
    reaction_type = "HAHA"
    
    #act
    react_to_comment(user_id,comment_id,reaction_type)
    
    
    #assert
    #extra
    reaction = Reaction.objects.get(reacted_by_id = user_id,comment_id = comment_id,reaction = reaction_type)
    
    assert reaction.reacted_by  ==  user
    assert reaction.comment  ==  comment
    assert reaction.reaction  ==  reaction_type
    # assert reaction.reaction in ['WOW','LIT','LOVE','HAHA','THUMBS-UP','THUMBS-DOWN','ANGRY','SAD']
    
@pytest.mark.django_db
def test_react_to_comment_with_same_reaction_deletes_reaction(user,comment,comment_reaction):
    
    #arrange
    user_id = 1
    comment_id = 1
    reaction_type = "LIT"
    
    #act
    react_to_comment(user_id,comment_id,reaction_type)
    
    #assert
    #extra
    reaction = Reaction.objects.filter(reacted_by_id = user.id,comment_id = comment.id,reaction = reaction_type)
    
    
    assert len(reaction)  ==  0
    
#@pytest.mark.django_db
@pytest.mark.parametrize("my_user_id,new_reaction_type", [(1,"ANGRY"), (3,"WOW")])


@pytest.mark.django_db
def test_react_to_comment_with_different_reaction_updates_reaction(users,comment,comment_reaction,new_reaction_type,my_user_id):
    
    #arrange
    user_id = my_user_id
    comment_id = 1
    reaction_type = new_reaction_type
    
    #act
    react_to_comment(user_id,comment_id,reaction_type)
    
    #assert
    #extra
    reaction = Reaction.objects.get(reacted_by_id = user_id,comment_id = comment_id,reaction = reaction_type)
    
    assert reaction.reacted_by_id  ==  my_user_id
    assert reaction.comment  ==  comment
    assert reaction.reaction  ==  reaction_type 
    # assert reaction.reaction in ['WOW','LIT','LOVE','HAHA','THUMBS-UP','THUMBS-DOWN','ANGRY','SAD']

@pytest.mark.django_db
def test_get_total_reaction_count_when_reactions_present_returns_count_of_all_reactions(post_reaction,comment_reaction):
    
    #arrange
    react_count = 2
    
    #act
    total_count = get_total_reaction_count()
    
    #assert
    assert total_count["count"]  ==  react_count
    
@pytest.mark.django_db
def test_get_total_reaction_count_when_no_reactions_present_returns_count_as_zero():
    
    #arrange
    react_count = 0
    
    #act
    total_count = get_total_reaction_count()
    
    #assert
    assert total_count["count"]  ==  react_count
    
    
@pytest.mark.django_db
def test_get_reaction_metrics_when_post_exits_returns_post_reaction_metrics(post_reaction):
    
    #arrange
    wow_count = 1
    post_id = 1
    
    #act
    total_count = get_reaction_metrics(post_id)
    
    #assert
    assert total_count["WOW"]   ==   wow_count
    
@pytest.mark.django_db
def test_get_reaction_metrics_with_invalid_post_id_raises_InvalidPostException(post_reaction):
    
    #arrange
    haha_count = 1
    post_id = 2
    
    #act
    with pytest.raises(InvalidPostException) as e:
        assert get_reaction_metrics(post_id)
    
    
    #assert
    post = Post.objects.filter(id = post_id)
    
    assert str(e.value)   ==   ""
    assert len(post)   ==   0
    
    
@pytest.mark.django_db
def test_get_reaction_metrics_when_there_is_no_reactions_to_post_returns_empty_dict(post):
    
    #arrange
    haha_count  =  1
    post_id  =  1
    empty_dict  =  {}
    #act
    total_count = get_reaction_metrics(post_id)
    
    #assert
    assert total_count   ==   empty_dict
    
@pytest.mark.django_db
def test_delete_post_with_inavlid_user_id_raises_InavalidUserException(user,post):
    #arrange
    user_id  =  2
    post_id  =  1
    
    #act
    with pytest.raises(InvalidUserException) as e:
        assert delete_post(user_id,post_id)
    
    #assert
    user = User.objects.filter(id = user_id)
    
    assert str(e.value)   ==   ""
    assert len(user)   ==   0
    
@pytest.mark.django_db
def test_delete_post_with_inavlid_post_id_raises_InavalidPostException(user,post):
    #arrange
    user_id  =  1
    post_id  =  2
    
    #act
    with pytest.raises(InvalidPostException) as e:
        assert delete_post(user_id,post_id)
    
    #assert
    post = Post.objects.filter(id = post_id)
    
    assert str(e.value)   ==   ""
    assert len(post)   ==   0
    
@pytest.mark.django_db
def test_delete_post_when_post_id_not_created_by_user_id_raises_UserCannotDeletePostException(users,post):
    #arrange
    user_id  =  2
    post_id  =  1
    
    #act
    with pytest.raises(UserCannotDeletePostException) as e:
        assert delete_post(user_id,post_id)
    
    #assert
    #extra
    post = Post.objects.get(id = post_id)
    
    assert str(e.value)   ==   ""
    assert post.posted_by_id !=  user_id
    
@pytest.mark.django_db
def test_delete_post_with_valid_details_deletes_post(users,post):
    #arrange
    user_id  =  1
    post_id  =  1
    before_delete_post = len(Post.objects.filter(posted_by  =  user_id , id  =  post_id))
    #act
    
    delete_post(user_id,post_id)
    
    #assert
    #extra
    after_delete_post  =  len(Post.objects.filter(posted_by  =  user_id , id  =  post_id))
    
    assert before_delete_post   ==   1
    assert after_delete_post   ==   0
@pytest.mark.django_db    
def test_get_posts_with_more_positive_reactions_when_there_no_posts_having_more_posite_reactions_returns_empty_list(post):
    #arrange
    empty_list  =  []
    
    #act
    post_ids = get_posts_with_more_positive_reactions()
    
    #assert
    assert post_ids   ==   empty_list
    
@pytest.mark.django_db   
def test_get_posts_with_more_positive_reactions_when_posts_having_more_posite_reactions_returns_post_ids_list(post,post_reaction):
    #arrange
    post_id_list  =  [1]
    
    #act
    post_ids  =  get_posts_with_more_positive_reactions()
    
    #assert
    assert post_ids   ==   post_id_list
@pytest.mark.django_db      
def test_get_posts_reacted_by_user_with_invalid_user_id_raises_InvalidUserException(user,post_reaction):
    #arrange
    user_id  =  2
    
    #act
    with pytest.raises(InvalidUserException) as e:
        assert get_posts_reacted_by_user(user_id)
    
    #assert
    user = User.objects.filter(id = user_id)
    
    assert str(e.value)   ==   ""
    assert len(user)   ==   0
    
    
@pytest.mark.django_db          
def test_get_posts_reacted_by_user_with_when_user_posted_no_post_returns_empty_list(users,post_reaction):
    #arrange
    user_id  =  2
    empty_list  =  []
    #act
    
    post_list = get_posts_reacted_by_user(user_id)
    
    #assert
    assert post_list   ==   empty_list
    
@pytest.mark.django_db          
def test_get_posts_reacted_by_user_when_no_reactions_to_post_returns_empty_list(users,post_reaction):
    #arrange
    user_id  =  2
    empty_list  =  []
    #act
    
    post_list = get_posts_reacted_by_user(user_id)
    
    #assert
    assert post_list   ==   empty_list
    
@pytest.mark.django_db          
def test_get_posts_reacted_by_user_with_valid_user_reacted_to_psts_returns_post_ids_list(users,post_reaction):
    #arrange
    user_id  =  1
    list  =  [1]
    #act
    
    post_list = get_posts_reacted_by_user(user_id)
    
    #assert
    assert post_list   ==   list
    
@pytest.mark.django_db
def test_get_reactions_to_post_with_inavlid_post_id_raises_InavlidPostException(post_reaction):
    #arrange
    post_id  =  2
    
    #act
    with pytest.raises(InvalidPostException) as e:
        assert get_reactions_to_post(post_id)
    
    #assert
    post = Post.objects.filter(id = post_id)
    
    assert str(e.value)   ==   ""
    assert len(post)   ==   0
    
@pytest.mark.django_db
def test_get_reactions_to_post_when_there_is_no_reactions_to_post_returns_empty_list(post):
    #arrange
    post_id  =  1
    empty_list  =  []
    #act

    reactions = get_reactions_to_post(post_id)
    
    #assert
    assert reactions   ==   empty_list
    
@pytest.mark.django_db
def test_get_reactions_to_post_when_there_is_reactions_to_post_returns_reaction_details_list(post_reactions):
    #arrange
    post_id  =  1
    result  =  [{'user_id': 2, 'name': 'user_1', 'profile_pic': '', 'reaction': 'LIT'},
 {'user_id': 3, 'name': 'user_2', 'profile_pic': '', 'reaction': 'HAHA'}]
    
    #act

    reactions = get_reactions_to_post(post_id)
    
    #assert
    assert reactions   ==   result
    
@pytest.mark.django_db
def test_get_replies_for_comment_with_invalid_comment_id_raises_InvalidCommentException(comment_reply):
    #arrange
    comment_id  =  4
    
    #act
    with pytest.raises(InvalidCommentException) as e:
        assert get_replies_for_comment(comment_id)
        
    #assert
    comment = Comment.objects.filter(id = comment_id)
    
    assert str(e.value)   ==   ""
    assert len(comment)   ==   0
    
@pytest.mark.django_db
def test_get_replies_for_comment_with_valid_comment_id_returns_reply_list(comment_reply):
    #arrange
    comment_id  =  3
    result  =  []
    
    
        
    #act
    
    reply_list = get_replies_for_comment(comment_id)
        
    #assert
    assert reply_list   ==   result
    
@pytest.mark.django_db
def test_get_replies_for_comment_when_comment_have_no_replies_returns_empty_list(comment_reply):
    #arrange
    comment_id  =  1
    result  =  [{'comment_id': 2,
  'commenter': {'user_id': 2, 'name': 'user_1', 'profile_pic': ''},
  'commented_at': '2020-04-18 05:36:59.091819',
  'comment_content': 'reply 1'},
 {'comment_id': 3,
  'commenter': {'user_id': 3, 'name': 'user_2', 'profile_pic': ''},
  'commented_at': '2020-04-18 05:36:59.091819',
  'comment_content': 'reply 2'}]
    

    #act
    
    reply_list = get_replies_for_comment(comment_id)
        
    #assert
    assert reply_list   ==   result
    
    
@pytest.mark.django_db
def test_get_post_with_invalid_post_id_raises_InvalidPostException():
    #arrange
    post_id  =  1
    
    #act
    with pytest.raises(InvalidPostException) as e:
        assert get_post(post_id)
        
    #assert
    post = Post.objects.filter(id = post_id)
    
    assert str(e.value)   ==   ""
    assert len(post)   ==   0

@pytest.mark.django_db
def test_get_post_when_post_have_no_comments_and_reactions_returns_only_post_details(post):
    #arrange
    post_id = 1
    result = {'post_id': 1,
 'posted_by': {'name': 'user_1', 'user_id': 1, 'profile_pic': ''},
 'posted_at': '2020-04-18 05:36:59.091819',
 'post_content': 'post_2',
 'reactions': {'count': 0, 'type': []},
 'comments': [],
 'comments_count': 0}
  
    #act
    dict = get_post(post_id)
    
    #assert
    assert dict   ==   result
    
@pytest.mark.django_db
def test_get_post_when_post_have_no_reaplies_to_comments_returns_only_post_details_and_comments(comment,post_reactions,comment_reaction):
    #arrange
    post_id = 1
    result = {
    'post_id': 1,
  'posted_by': {'name': 'user_1', 'user_id': 1, 'profile_pic': ''},
  'posted_at': '2020-04-18 05:36:59.091819',
  'post_content': 'post_2',
  'reactions': {'count': 2, 'type': ['LIT', 'HAHA']},
  'comments': [{'comment_id': 1,
    'commenter': {'user_id': 1, 'name': 'user_1', 'profile_pic': ''},
    'commented_at': '2020-04-18 05:36:59.091819',
    'comment_content': 'group_1',
    'reactions': {'count': 1, 'type': ['LIT']},
    'replies_count': 0,
    'replies': []}],
  'comments_count': 1}
  
    #act
    dict = get_post(post_id)
    
    #assert
    assert dict   ==   result

@pytest.mark.django_db
def test_get_post_with_valid_details_returns_post_details_dict(comment,post_reactions,comment_reply,comment_reaction,reply_comment_reaction):
    #arrange
    post_id = 1
    
    result = {'post_id': 1,
 'posted_by': {'name': 'user_1', 'user_id': 1, 'profile_pic': ''},
 'posted_at': '2020-04-18 05:36:59.091819',
 'post_content': 'post_2',
 'reactions': {'count': 2, 'type': ['LIT', 'HAHA']},
 'comments': [{'comment_id': 1,
  'commenter': {'user_id': 1, 'name': 'user_1', 'profile_pic': ''},
  'commented_at': '2020-04-18 05:36:59.091819',
  'comment_content': 'group_1',
  'reactions': {'count': 1, 'type': ['LIT']},
  'replies_count': 2,
  'replies': [{'comment_id': 2,
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
    dict = get_post(post_id)
    
    #assert
    #assert dict   ==   result
    assert dict["comments"]   ==   result["comments"]
    assert dict["comments_count"]   ==   result["comments_count"]
    assert dict["post_id"]   ==   result["post_id"]
    assert dict["reactions"]   ==   result["reactions"]
    assert dict["posted_by"]   ==   result["posted_by"]
    assert dict["posted_at"]   ==   result["posted_at"]
    assert dict["post_content"]   ==   result["post_content"]    
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

@pytest.mark.django_db
def test_get_user_posts_with_valid_details_returns_post_details_list(comment,post_reactions,comment_reply,comment_reaction):
    #arrange
    user_id = 1
    result = [{
    'post_id': 1,
  'posted_by': {'name': 'user_1', 'user_id': 1, 'profile_pic': ''},
  'posted_at': '2020-04-18 05:36:59.091819',
  'post_content': 'post_2',
  'reactions': {'count': 2, 'type': ['LIT', 'HAHA']},
  'comments': [{'comment_id': 1,
    'commenter': {'user_id': 1, 'name': 'user_1', 'profile_pic': ''},
    'commented_at': '2020-04-18 05:36:59.091819',
    'comment_content': 'group_1',
    'reactions': {'count': 1, 'type': ['LIT']},
    'replies_count': 2,
    'replies': [{'comment_id': 2,
      'commenter': {'user_id': 2, 'name': 'user_1', 'profile_pic': ''},
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
    dict = get_user_posts(user_id)
    
    #assert
    #assert dict   ==   result
    assert len(dict)   ==   len(result)
    for item in range(len(result)):
        assert dict[item]["comments"]   ==   result[item]["comments"]
        assert dict[item]["comments_count"]   ==   result[item]["comments_count"]
        assert dict[item]["reactions"]   ==   result[item]["reactions"]
        assert dict[item]["post_id"]   ==   result[item]["post_id"]
        assert dict[item]["posted_by"]   ==   result[item]["posted_by"]
        assert dict[item]["posted_at"]   ==   result[item]["posted_at"]
        assert dict[item]["post_content"]   ==   result[item]["post_content"]
        check_comment(dict[item]["comments"],result[item]["comments"])
    
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
def test_get_user_posts_when_post_have_no_comments_and_reactions_returns_only_post_details(post):
    #arrange
    user_id = 1
    result = [{'post_id': 1,
 'posted_by': {'name': 'user_1', 'user_id': 1, 'profile_pic': ''},
 'posted_at': '2020-04-18 05:36:59.091819',
 'post_content': 'post_2',
 'reactions': {'count': 0, 'type': []},
 'comments': [],
 'comments_count': 0}]
  
    #act
    dict = get_user_posts(user_id)
    
    #assert
    assert dict   ==   result
    
@pytest.mark.django_db
def test_get_user_posts_when_post_have_no_reaplies_to_comments_returns_only_post_details_and_comments(comment,post_reactions,comment_reaction):
    #arrange
    user_id = 1
    result = [{
    'post_id': 1,
  'posted_by': {'name': 'user_1', 'user_id': 1, 'profile_pic': ''},
  'posted_at': '2020-04-18 05:36:59.091819',
  'post_content': 'post_2',
  'reactions': {'count': 2, 'type': ['LIT', 'HAHA']},
  'comments': [{'comment_id': 1,
    'commenter': {'user_id': 1, 'name': 'user_1', 'profile_pic': ''},
    'commented_at': '2020-04-18 05:36:59.091819',
    'comment_content': 'group_1',
    'reactions': {'count': 1, 'type': ['LIT']},
    'replies_count': 0,
    'replies': []}],
  'comments_count': 1}]
  
    #act
    dict = get_user_posts(user_id)
    
    #assert
    assert dict   ==   result
    
    
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