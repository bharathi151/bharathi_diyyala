from fb_post.models import Reaction
from .validation import check_for_user, check_for_comment
from .validation import is_valid_reaction_type

def react_to_comment(user_id, comment_id, reaction_type):
    check_for_comment(comment_id)
    check_for_user(user_id)
    is_valid_reaction_type(reaction_type)
    try:
        existed_reaction = Reaction.objects.get(reacted_by_id=user_id,
                                                comment_id=comment_id)

    except Reaction.DoesNotExist:
        Reaction.objects.create(reaction=reaction_type,
                                reacted_by_id=user_id,
                                comment_id=comment_id)
        return

    make_undo_or_redo_to_reaction(existed_reaction, reaction_type)


def make_undo_or_redo_to_reaction(existed_reaction, reaction_type):
    is_undo = existed_reaction.reaction == reaction_type
    if is_undo:
        existed_reaction.delete()
    else:
        existed_reaction.reaction = reaction_type
        existed_reaction.save()
