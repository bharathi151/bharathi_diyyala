import pytest
from fb_post.utils import get_total_reaction_count

@pytest.mark.django_db
def test_get_total_reaction_count_when_reactions_present_returns_count_of_all_reactions(post_reaction, comment_reaction):

    # arrange
    react_count = 2

    # act
    total_count = get_total_reaction_count()

    # assert
    assert total_count["count"] == react_count

@pytest.mark.django_db
def test_get_total_reaction_count_when_no_reactions_present_returns_count_as_zero():

    # arrange
    react_count = 0

    # act
    total_count = get_total_reaction_count()

    # assert
    assert total_count["count"] == react_count
