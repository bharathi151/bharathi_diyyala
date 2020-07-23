from django.db.models import Q, Count
from fb_post.models import Reaction
from fb_post.constants import PositiveReactions, NegativeReactions
from .validation import check_for_post, check_for_user

def get_total_reaction_count():
    total_reaction_count = Reaction.objects.aggregate(count=Count('id'))
    return total_reaction_count

def get_reaction_metrics(post_id):
    check_for_post(post_id)

    reaction = Reaction.objects.filter(post_id=post_id).values('reaction').\
                    annotate(
                        count=Count('reaction')
                    ).values_list('reaction', 'count')

    reaction_metrics_dict = dict(reaction)
    return reaction_metrics_dict


def get_posts_with_more_positive_reactions():
    positive = Count('reaction', filter=Q(
        reaction__in=PositiveReactions.values)
                    )
    negative = Count('reaction', filter=Q(
        reaction__in=NegativeReactions.values)
                    )

    post_ids = Reaction.objects.values('post').\
                    annotate(
                        positive=positive, negative=negative
                    ).filter(
                        positive__gt=negative
                    ).values_list(
                        'post_id', flat=True
                    ).distinct()
    post_ids_list = list(post_ids)
    return post_ids_list

def get_posts_reacted_by_user(user_id):
    check_for_user(user_id)

    post_ids = Reaction.objects.filter(
                reacted_by__id=user_id
                ).values_list(
                    'post_id', flat=True
                ).distinct()
    post_ids_list = list(post_ids)
    return post_ids_list
