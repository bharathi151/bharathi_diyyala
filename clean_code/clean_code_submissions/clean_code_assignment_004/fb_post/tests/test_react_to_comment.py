import pytest
from fb_post.utils import react_to_comment
from fb_post.models import User, Reaction, Comment
from fb_post.exceptions import InvalidUserException
from fb_post.exceptions import InvalidReactionTypeException
from fb_post.exceptions import InvalidCommentException

@pytest.mark.django_db
def test_react_to_comment_with_invalid_user_id_raises_invalid_user_exception(user, comment):
    #arrange
    user_id = 2
    comment_id = 1
    reaction_type = "HAHA"
    zero = 0
    empty = ""

    #act
    with pytest.raises(InvalidUserException) as error_exception:
        assert react_to_comment(user_id, comment_id, reaction_type)

    #assert
    user = User.objects.filter(id=user_id)

    assert str(error_exception.value) == empty
    assert len(user) == zero

@pytest.mark.django_db
def test_react_comment_with_invalid_comment_id_raises_invalid_comment_exception(user, comment):
    #arrange
    user_id = 1
    comment_id = 3
    reaction_type = "HAHA"
    empty = ""
    zero = 0
    #act
    with pytest.raises(InvalidCommentException) as error_exception:
        assert react_to_comment(user_id, comment_id, reaction_type)

    #assert
    comment = Comment.objects.filter(id=comment_id)

    assert str(error_exception.value) == empty
    assert len(comment) == zero

@pytest.mark.django_db
def test_react_to_comment_with_invalid_reaction_type_raises_invalid_reaction_type_exception(user, comment):
    #arrange
    user_id = 1
    comment_id = 1
    reaction_type = "LIKE"
    empty = ""
    #act
    with pytest.raises(InvalidReactionTypeException) as error_exception:
        assert react_to_comment(user_id, comment_id, reaction_type)

    #assert
    assert str(error_exception.value) == empty

@pytest.mark.django_db
def test_react_to_comment_with_valid_details_creates_new_reaction(user,
                                                                  comment):

    #arrange
    user_id = 1
    comment_id = 1
    reaction_type = "HAHA"

    #act
    react_to_comment(user_id, comment_id, reaction_type)


    #assert
    #extra
    reaction = Reaction.objects.get(reacted_by_id=user_id,
                                    comment_id=comment_id,
                                    reaction=reaction_type)

    assert reaction.reacted_by == user
    assert reaction.comment == comment
    assert reaction.reaction == reaction_type

@pytest.mark.django_db
def test_react_to_comment_with_same_reaction_deletes_reaction(user, comment,
                                                              comment_reaction):

    #arrange
    user_id = 1
    comment_id = 1
    reaction_type = "LIT"
    zero = 0

    #act
    react_to_comment(user_id, comment_id, reaction_type)

    #assert
    #extra
    reaction = Reaction.objects.filter(reacted_by_id=user.id,
                                       comment_id=comment.id,
                                       reaction=reaction_type)

    assert len(reaction) == zero

@pytest.mark.parametrize("my_user_id, new_reaction_type",
                         [(1, "ANGRY"), (3, "WOW")])
@pytest.mark.django_db
def test_react_to_comment_with_different_reaction_updates_reaction(users,
                                                                   comment,
                                                                   comment_reaction,
                                                                   new_reaction_type,
                                                                   my_user_id):

    #arrange
    user_id = my_user_id
    comment_id = 1
    reaction_type = new_reaction_type

    #act
    react_to_comment(user_id, comment_id, reaction_type)

    #assert
    #extra
    reaction = Reaction.objects.get(reacted_by_id=user_id,
                                    comment_id=comment_id,
                                    reaction=reaction_type)

    assert reaction.reacted_by_id == my_user_id
    assert reaction.comment == comment
    assert reaction.reaction == reaction_type
