from fb_post.models import Reaction
from .validation import check_for_user, check_for_post
from .validation import is_valid_reaction_type
from .react_to_comment import make_undo_or_redo_to_reaction

def react_to_post(user_id, post_id, reaction_type):
    check_for_post(post_id)
    check_for_user(user_id)
    is_valid_reaction_type(reaction_type)
    try:
        existed_reaction = Reaction.objects.get(reacted_by_id=user_id,
                                                post_id=post_id)
    except Reaction.DoesNotExist:
        Reaction.objects.create(reaction=reaction_type,
                                reacted_by_id=user_id,
                                post_id=post_id)
        return

    make_undo_or_redo_to_reaction(existed_reaction, reaction_type)
