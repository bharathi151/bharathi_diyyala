import pytest
from fb_post.utils import get_reaction_metrics
from fb_post.exceptions import InvalidPostException
from fb_post.models import Post

@pytest.mark.django_db
def test_get_reaction_metrics_when_post_exits_returns_post_reaction_metrics(post_reaction):

    # arrange
    wow_count = 1
    post_id = 1

    # act
    total_count = get_reaction_metrics(post_id)

    # assert
    assert total_count["WOW"] == wow_count

@pytest.mark.django_db
def test_get_reaction_metrics_with_invalid_post_id_raises_invalid_post_exception(post_reaction):

    # arrange
    haha_count = 1
    post_id = 2
    zero = 0
    empty_string = ""

    # act
    with pytest.raises(InvalidPostException) as error_exception:
        assert get_reaction_metrics(post_id)

    # assert
    post = Post.objects.filter(id=post_id)

    assert str(error_exception.value) == empty_string
    assert len(post) == zero


@pytest.mark.django_db
def test_get_reaction_metrics_when_there_is_no_reactions_to_post_returns_empty_dict(post):

    # arrange
    post_id = 1
    empty_dict = {}
    # act
    total_count = get_reaction_metrics(post_id)

    # assert
    assert total_count == empty_dict
