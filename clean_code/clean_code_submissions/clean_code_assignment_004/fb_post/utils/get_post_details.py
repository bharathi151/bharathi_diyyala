from django.db.models import Prefetch
from fb_post.models import Post, Comment, Reaction
from fb_post.constants import convert_date_time_into_strf_format
from .validation import check_for_user, check_for_post


def get_post(post_id):

    check_for_post(post_id)

    queryset = Comment.objects.filter(post_id=post_id).\
                    select_related('commented_by')

    post_object = Post.objects\
                .prefetch_related(
                    'reactions',
                    Prefetch('comments',
                             queryset=queryset,
                             to_attr='post_comments'),
                    'post_comments__reactions'
                ).select_related('posted_by').get(id=post_id)

    return get_post_details_dict(post_object)


def get_user_posts(user_id):

    check_for_user(user_id)

    post_objects = get_post_objs_of_a_user(user_id)

    posts_list = [get_post_details_dict(post) for post in post_objects]

    return posts_list

def get_post_objs_of_a_user(user_id):

    queryset = Comment.objects.all().select_related('commented_by')

    posts = Post.objects.filter(posted_by_id=user_id).\
                prefetch_related(
                    'reactions',
                    Prefetch('comments',
                             queryset=queryset,
                             to_attr='post_comments'),
                    'post_comments__reactions'
                ).select_related('posted_by')

    return posts

def get_post_details_dict(post):

    comment_list, post_reactions_list = [], []
    post_dict = construct_post_details_dict(post, post_reactions_list,
                                            comment_list)

    for react in post.reactions.all():
        if react.reaction not in post_reactions_list:
            post_reactions_list.append(react.reaction)

    for comment in post.post_comments:
        is_comment = not comment.parent_comment_id
        if is_comment:
            comment_list.append(get_comment_dict_with_all_details(
                comment, post.post_comments))

    post_dict["comments_count"] = len(comment_list)

    return post_dict

def construct_post_details_dict(post, post_reactions_list, comment_list):

    post_details_dict = {
        "post_id": post.id,
        "posted_by": {
            "name": post.posted_by.name,
            "user_id": post.posted_by_id,
            "profile_pic": post.posted_by.profile_pic
        },
        "posted_at": convert_date_time_into_strf_format(post.posted_at),
        "post_content": post.content,
        "reactions": {
            "count": len(post.reactions.all()),
            "type": post_reactions_list
        },
        "comments": comment_list,
    }

    return post_details_dict

def get_comment_dict_with_all_details(comment, post_comments):

    comment_dict = get_comment_dict_with_reactions(comment)

    replies_list = get_replies_list_to_a_comment(post_comments, comment)
    comment_dict["replies_count"] = len(replies_list)
    comment_dict["replies"] = replies_list

    return comment_dict

def get_replies_list_to_a_comment(post_comments, comment):
    replies_list = []
    for reply in post_comments:
        is_reply = comment.id is reply.parent_comment_id
        if is_reply:
            replies_list.append(get_comment_dict_with_reactions(reply))

    return replies_list


def get_comment_dict_with_reactions(comment):
    comment_reaction_list = []
    commented_date_time = convert_date_time_into_strf_format(
        comment.commented_at
    )
    comment_dict_with_reactions = {
        "comment_id": comment.id,
        "commenter": get_user_dict(comment.commented_by),
        "commented_at": commented_date_time,
        "comment_content": comment.content,
        "reactions": {
            "count": len(comment.reactions.all()),
            "type": comment_reaction_list
        }
    }
    for react in comment.reactions.all():
        if react.reaction not in comment_reaction_list:
            comment_reaction_list.append(react.reaction)
    return comment_dict_with_reactions

def get_user_dict(user):
    user_dict = {
        "user_id": user.id,
        "name": user.name,
        "profile_pic": user.profile_pic
    }
    return user_dict


def get_reactions_to_post(post_id):

    check_for_post(post_id)

    reactions = Reaction.objects.filter(post_id=post_id)\
                    .select_related('reacted_by').distinct()

    reactions_list = [get_user_dict_of_reaction(react) for react in reactions]

    return reactions_list

def get_user_dict_of_reaction(reaction):

    reacted_user_dict = get_user_dict(reaction.reacted_by)
    reacted_user_dict["reaction"] = reaction.reaction

    return reacted_user_dict
