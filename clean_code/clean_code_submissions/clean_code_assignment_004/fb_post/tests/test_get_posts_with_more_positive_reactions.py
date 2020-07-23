import pytest
from fb_post.utils import get_posts_with_more_positive_reactions

@pytest.mark.django_db
def test_get_posts_with_more_positive_reactions_when_there_no_posts_having_more_posite_reactions_returns_empty_list(post):
    #arrange
    empty_list = []

    #act
    post_ids = get_posts_with_more_positive_reactions()

    #assert
    assert post_ids == empty_list

@pytest.mark.django_db
def test_get_posts_with_more_positive_reactions_when_posts_having_more_posite_reactions_returns_post_ids_list(post, post_reaction):
    #arrange
    post_id_list = [1]
    #act
    post_ids = get_posts_with_more_positive_reactions()

    #assert
    assert post_ids == post_id_list
