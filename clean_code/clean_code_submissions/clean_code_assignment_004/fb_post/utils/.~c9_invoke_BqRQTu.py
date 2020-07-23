from django.db.models import Prefetch
from fb_post.models import Post, Comment, Reaction
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

    post_dict = {}
    comment_list, post_reactions_list = [], []
    post_dict = construct_post_details_dict(post, post_reactions_list,
                                            comment_list)

    for react in post.reactions.all():
        if react.reaction not in post_reactions_list:
            post_reactions_list.append(react.reaction)

    for comment in post.post_comments:
        is_comment = not comment.parent_comment_id
        if is_comment:
            comment_dict = get_comment_dict(comment, post.post_comments)
            comment_list.append(comment_dict)

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
        "posted_at": post.posted_at.strftime("%Y-%m-%d %H:%M:%S.%f"),
        "post_content": post.content,
        "reactions": {
            "count": len(post.reactions.all()),
            "type": post_reactions_list
        },
        "comments": comment_list,
    }

    return post_details_dict

def get_comment_dict(comment, post_comments):

    replies_list, comment_reaction = [], []
    comment_dict = construct_comment_details_dict(comment, replies_list,
                                                  comment_reaction)

    for react in comment.reactions.all():
        new_reaction = react.reaction not in comment_reaction
        if new_reaction:
            comment_reaction.append(react.reaction)

        replies_list = [add_reply_details_dict_to_replies_list(reply, 
                                                    comment, replies_list
                                    ) for reply in post_comments]

    comment_dict["replies_count"] = len(replies_list)

    return comment_dict

def construct_comment_details_dict(comment, reply_list, comment_reaction):

    commented_time = comment.commented_at.strftime("%Y-%m-%d %H:%M:%S.%f")

    comment_dict = {
        "comment_id": comment.id,
        "commenter": get_user_dict(comment.commented_by),
        "commented_at": commented_time,
        "comment_content": comment.content,
        "reactions": {
            "count": len(comment.reactions.all()),
            "type": comment_reaction
        },
        "replies_count": len(reply_list),
        "replies": reply_list
    }

    return comment_dict

def add_reply_details_dict_to_replies_list(reply, comment, replies_list):

    is_reply = comment.id is reply.parent_comment_id
    if is_reply:
        reply_reaction_list = []
        reaction_dict = {
            "count": len(reply.reactions.all()),
            "type": reply_reaction_list
        }

        replies_list.append({
            "comment_id": reply.id,
            "commenter": get_user_dict(reply.commented_by),
            "commented_at": reply.commented_at.strftime("%Y-%m-%d %H:%M:%S.%f"),
            "comment_content": reply.content,
            "reactions": reaction_dict,
        })

        for react in reply.reactions.all():
            if react.reaction not in reply_reaction_list:
                reply_reaction_list.append(react.reaction)

    return replies_list




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
