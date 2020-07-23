from fb_post.models import *
from fb_post.exceptions import *
from django.db.models import Q
import datetime
from typing import Dict, Any
import pytz
from django.db.models import *
from .validation import *


#task 6
def create_post(user_id, post_content):
    check_for_user(user_id)
    is_valid_post_content(post_content)

    post_id = Post.objects.create(posted_by_id=user_id,
                                  content=post_content).id
    return post_id

def reply_to_comment(user_id, comment_id, reply_content):
    try:
        check_for_user(user_id)

        comment = Comment.objects.\
                        select_related(
                            'parent_comment', 'post'
                        ).get(id=comment_id)

    except Comment.DoesNotExist:
        raise InvalidCommentException

    new_comment_id = comment_creation(user_id, comment_id,
                                      reply_content, comment)
    return new_comment_id

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


def comment_creation(user_id, comment_id, reply_content, comment):
    is_valid_reply_content(reply_content)

    if comment.parent_comment_id:
        parent_comment_id = comment.parent_comment_id

        reply_id = Comment.objects.create(content=reply_content,
                                          commented_by_id=user_id,
                                          parent_comment_id=parent_comment_id,
                                          post_id=comment.post_id).id
        return reply_id

    comment_id = Comment.objects.create(content=reply_content,
                                        commented_by_id=user_id,
                                        parent_comment_id=comment_id,
                                        post_id=comment.post_id).id
    return comment_id

def create_comment(user_id, post_id, comment_content):
    check_for_user(user_id)
    check_for_post(post_id)
    is_valid_comment_content(comment_content)

    comment_id = Comment.objects.create(content=comment_content,
                                        commented_by_id=user_id,
                                        post_id=post_id).id
    return comment_id

def delete_post(user_id, post_id):
    post = check_for_post(post_id)
    check_for_user(user_id)

    can_user_delete_post = post.posted_by_id == user_id
    if can_user_delete_post:
        post.delete()
    else:
        raise UserCannotDeletePostException
# #task 5
# def get_total_reaction_count():
    
#     return Reaction.objects.aggregate(count=Count('id'))


# def get_reaction_metrics(post_id):
#     try:
#         post=Post.objects.get(id=post_id)
#         r1=Reaction.objects.filter(post=post).values('reaction').annotate(count=Count('reaction')).values_list('reaction','count')
        
#         return dict(r1)
        
#     except Post.DoesNotExist:raise InvalidPostException

# def delete_post(user_id, post_id):
#     try:
#         post=Post.objects.get(id=post_id)
#         user=User.objects.get(id=user_id)
#         if post.posted_by_id is user_id:
#             post.delete()
            
#         else:
#             raise UserCannotDeletePostException
            
#     except Post.DoesNotExist:raise InvalidPostException
#     except User.DoesNotExist:raise InvalidUserException

# def get_posts_with_more_positive_reactions():
#     positive=Count('reaction',filter=Q(reaction__in=['WOW','LOVE','LIT','HAHA','THUMBS-UP']))
#     negative=Count('reaction',filter=Q(reaction__in=['ANGRY','SAD','THUMBS-DOWN']))
#     p=Reaction.objects.values('post').annotate(positive=positive,
#                     negative=negative).filter(positive__gt=negative).values_list('post_id',flat=True).distinct()
#     return list(p)

# #task 9
# def get_user_posts(user_id):
#     try:
#         posts=[]
#         user=User.objects.get(id=user_id)
#         details=Post.objects.filter(posted_by_id=user_id).prefetch_related('reactions',Prefetch('comments',queryset=Comment.objects.all().select_related('commented_by'),to_attr='post_comments'),'post_comments__reactions').select_related('posted_by')   
#         for post in details:
#           posts.append(get_post_details(post))
#         return posts
           
#     except User.DoesNotExist:raise InvalidUserException
    
def get_only_post(post_id: int, tzinfo) -> Dict:
    try:
        post = Post.objects.get(id=post_id)
    except Post.DoesNotExist:
        raise InvalidPostException
    string_time = post.posted_at.astimezone(pytz.timezone(tzinfo))
    only_post_dict = {
        "post_id": post.id,
        "posted_by_id": post.posted_by_id,
        "post_content": post.content,
        "posted_at": string_time.strftime("%Y-%m-%d %H:%M:%S.%f"),
        "tzinfo": tzinfo
    }
    return only_post_dict



def get_post_details(post):
    
    post_dict={}

    comment_list,post_reaction=[],[]
    comment_count=[]
    post_dict={
        "post_id":post.id,
        "posted_by":{
            "name":post.posted_by.name,
            "user_id":post.posted_by_id,
            "profile_pic":post.posted_by.profile_pic
        },
        "posted_at":post.posted_at.strftime("%Y-%m-%d %H:%M:%S.%f"),
        "post_content":post.content,
        "reactions":{
            "count":len(post.reactions.all()),
            "type":post_reaction
        },
        "comments":comment_list,
    }
    for react in post.reactions.all():
        if react.reaction not in post_reaction:
            post_reaction.append(react.reaction)
    for comment in post.post_comments:
        if not comment.parent_comment_id:
            comment_count.append(comment.id)
            reply_count=[]
            reply_list=[]
            comment_reaction=[]
            comment_dict={
                "comment_id":comment.id,
                "commenter":{
                    "user_id":comment.commented_by_id,
                    "name":comment.commented_by.name,
                    "profile_pic":comment.commented_by.profile_pic
                },
                "commented_at":comment.commented_at.strftime("%Y-%m-%d %H:%M:%S.%f"),
                "comment_content":comment.content,
                "reactions":{
                    "count":len(comment.reactions.all()),
                    "type":comment_reaction
                },
                "replies_count":len(reply_count),
                "replies":reply_list
            }
            comment_list.append(comment_dict)
            for react in comment.reactions.all():
                if react.reaction not in comment_reaction:
                    comment_reaction.append(react.reaction)
            for reply in post.post_comments:
                reply_reaction=[]
                if comment.id is reply.parent_comment_id:
                    reply_count.append(reply.id)
                    reply_list.append({
                        "comment_id":reply.id,
                        "commenter":{
                            "user_id":reply.commented_by_id,
                            "name":reply.commented_by.name,
                            "profile_pic":reply.commented_by.profile_pic
                        },
                        "commented_at":reply.commented_at.strftime("%Y-%m-%d %H:%M:%S.%f"),
                        "comment_content":reply.content,
                        "reactions":{
                            "count":len(reply.reactions.all()),
                            "type":reply_reaction
                        },
                    })
                    for react in reply.reactions.all():
                        if react.reaction not in reply_reaction:
                            reply_reaction.append(react.reaction)
                            
                comment_dict["replies_count"]=len(reply_count)
            
    post_dict["comments_count"]=len(comment_count)

    return post_dict


# def get_posts_reacted_by_user(user_id):
#     try:
#         user=User.objects.get(id=user_id)
#         p=Reaction.objects.filter(reacted_by__id=user_id).values_list('post_id',flat=True).distinct()
#         return list(p)
#     except User.DoesNotExist:raise InvalidUserException

# def get_reactions_to_post(post_id):
#     try:
#         post=Post.objects.get(id=post_id)
#         r=Reaction.objects.filter(post_id=post_id).select_related('reacted_by').distinct()
#         list=[]
#         for react in r:
#             list.append({
#                 "user_id":react.reacted_by_id,
#                 "name":react.reacted_by.name,
#                 "profile_pic":react.reacted_by.profile_pic,
#                 "reaction":react.reaction
                
#             })
#         return list
            
#     except Post.DoesNotExist:raise InvalidPostException
def get_post(post_id):
    try:
        details=Post.objects.prefetch_related('reactions',Prefetch('comments',queryset=Comment.objects.filter(post_id=post_id).select_related('commented_by'),to_attr='post_comments'),'post_comments__reactions').select_related('posted_by').get(id=post_id)
        
        return get_post_details(details)
        
    except Post.DoesNotExist:raise InvalidPostException
    
    

    
    
# def get_replies_for_comment(comment_id):
#     try:
#         c=Comment.objects.get(id=comment_id)
#         replies=Comment.objects.filter(parent_comment_id=comment_id).select_related('commented_by')
#         list=[]
#         for reply in replies:
#             dt=reply.commented_at
#             user={
#                 "user_id":reply.commented_by_id,
#                 "name":reply.commented_by.name,
#                 "profile_pic":reply.commented_by.profile_pic
#             }
#             list.append({
#                 "comment_id":reply.id,
#                 "commenter":user,
#                 "commented_at":dt.strftime("%Y-%m-%d %H:%M:%S.%f"),
#                 "comment_content":reply.content
#             })
#         return list
        
#     except Comment.DoesNotExist:raise InvalidCommentException
    
