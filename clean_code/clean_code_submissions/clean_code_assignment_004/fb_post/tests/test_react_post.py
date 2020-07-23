import pytest
from fb_post.utils import react_to_post
from fb_post.models import Reaction
from fb_post.exceptions import InvalidUserException
from fb_post.exceptions import InvalidReactionTypeException
from fb_post.exceptions import InvalidPostException


@pytest.mark.django_db
def test_react_to_post_with_invalid_user_id_raises_invalid_user_exception(user, post):
    # arrange
    user_id = 2
    post_id = 1
    reaction_type = "HAHA"
    empty_string = ""
    # act
    with pytest.raises(InvalidUserException) as error_exception:
        assert react_to_post(user_id, post_id, reaction_type)
    # assert
    assert str(error_exception.value) == empty_string


@pytest.mark.django_db
def test_react_post_with_invalid_post_id_raises_invalid_post_exception(user, post):
    # arrange
    user_id = 1
    post_id = 3
    reaction_type = "HAHA"
    empty_string = ""
    # act
    with pytest.raises(InvalidPostException) as error_exception:
        assert react_to_post(user_id, post_id, reaction_type)
    # assert
    assert str(error_exception.value) == empty_string


@pytest.mark.django_db
def test_react_to_post_with_invalid_reaction_type_raises_invalid_reaction_type_exception(user, post):
    # arrange
    user_id = 1
    post_id = 1
    reaction_type = "LIKE"
    empty_string = ""
    # act
    with pytest.raises(InvalidReactionTypeException) as error_exception:
        assert react_to_post(user_id, post_id, reaction_type)
    # assert
    assert str(error_exception.value) == empty_string

@pytest.mark.django_db
def test_react_to_post_with_valid_details_creates_new_reaction(user, post):
    # arrange
    user_id = 1
    post_id = 1
    reaction_type = "HAHA"
    # act
    react_to_post(user_id, post_id, reaction_type)
    # assert
    # extra
    reaction = Reaction.objects.get(reacted_by_id=user_id, post_id=post_id,
                                    reaction=reaction_type)
    assert reaction.reacted_by == user
    assert reaction.post == post
    assert reaction.reaction == reaction_type


@pytest.mark.django_db
def test_react_to_post_with_same_reaction_deletes_reaction(user, post,
                                                           post_reaction):
    # arrange
    user_id = 1
    post_id = 1
    zero = 0
    one = 1
    reaction_type = "WOW"
    length_before_delete = len(Reaction.objects.filter(reacted_by_id=user_id,
                                                       post_id=post_id,
                                                       reaction=reaction_type))
    # act
    react_to_post(user_id, post_id, reaction_type)
    # assert
    # extra
    reaction = Reaction.objects.filter(reacted_by_id=user_id,
                                       post_id=post_id, reaction=reaction_type)

    assert len(reaction) == zero
    assert length_before_delete == one

@pytest.mark.parametrize("new_reaction", [("HAHA"), ("SAD"), ("ANGRY")])
@pytest.mark.django_db
def test_react_to_post_with_different_reaction_updates_reaction(new_reaction,
                                                                post_reaction,
                                                                user, post):
    # arrange
    user_id = 1
    post_id = 1
    reaction_type = new_reaction
    # act
    react_to_post(user_id, post_id, reaction_type)
    # assert
    # extra
    reaction = Reaction.objects.get(reacted_by_id=user_id, post_id=post_id,
                                    reaction=reaction_type)
    assert reaction.reacted_by == user
    assert reaction.post == post
    assert reaction.reaction == reaction_type
