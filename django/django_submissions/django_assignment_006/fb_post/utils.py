from fb_post.models import *
from fb_post.exceptions import *
from django.db.models import Q
import datetime
from django.db.models import *

def create_post(user_id, post_content):
    try :
        user=User.objects.get(id=user_id)
        if post_content=='':
            raise InvalidPostContent
        else:
            p=Post.objects.create(content=post_content,posted_by_id=user_id)
            return p.id
    
    except User.DoesNotExist:raise InvalidUserException
    

def create_comment(user_id, post_id, comment_content):
    try :
        user=User.objects.get(id=user_id)
        post=Post.objects.get(id=post_id)
        if comment_content=='':
            raise InvalidCommentContent
        else:
            return Comment.objects.create(content=comment_content,commented_by_id=user_id,post_id=post_id).id
            
    
    except User.DoesNotExist:raise InvalidUserException
    except Post.DoesNotExist:raise InvalidPostException
    
    

def reply_to_comment(user_id, comment_id, reply_content):
    try :
        user=User.objects.get(id=user_id)
        comment=Comment.objects.select_related('post','parent_comment').get(id=comment_id)
        if reply_content=='':
            raise InvalidReplyContent
        else:
            if comment.parent_comment_id==None:
                return Comment.objects.create(content=reply_content,commented_by_id=user_id,parent_comment_id=comment_id,post_id=comment.post_id).id
            else:
                return Comment.objects.create(content=reply_content,commented_by_id=user_id,parent_comment_id=comment.parent_comment_id,post_id=comment.post_id).id
            
    
    except User.DoesNotExist:raise InvalidUserException
    except Comment.DoesNotExist:raise InvalidCommentException
    


#task 5
def react_to_post(user_id, post_id, reaction_type):
    try:
        user=User.objects.get(id=user_id)
        post=Post.objects.get(id=post_id)
        react=['WOW','LIT','LOVE','HAHA','THUMBS-UP','THUMBS-DOWN','ANGRY','SAD']
        
        if reaction_type in react:
            existed=Reaction.objects.get(reacted_by_id=user_id,post_id=post_id)
            
            if existed.reaction==reaction_type:
                existed.delete()
                    
            else:
                existed.reaction=reaction_type
                existed.save()
            
        else:
            raise InvalidReactionTypeException


    except Reaction.DoesNotExist:Reaction.objects.create(reaction=reaction_type,reacted_by_id=user_id,post_id=post_id)
    except User.DoesNotExist:raise InvalidUserException
    except Post.DoesNotExist:raise InvalidPostException
    
#task 6
def react_to_comment(user_id, comment_id, reaction_type):
    try:
        user=User.objects.get(id=user_id)
        comment=Comment.objects.get(id=comment_id)
        react=['WOW','LIT','LOVE','HAHA','THUMBS-UP','THUMBS-DOWN','ANGRY','SAD']
        
        if reaction_type in react:
            existed=Reaction.objects.get(reacted_by_id=user_id,comment_id=comment_id)
            
            if existed.reaction==reaction_type:
                existed.delete()
                    
            else:
                existed.reaction=reaction_type
                existed.save()
            
        else:
            raise InvalidReactionTypeException
            
    except Reaction.DoesNotExist:Reaction.objects.create(reaction=reaction_type,reacted_by_id=user_id,comment_id=comment_id)
    except User.DoesNotExist:raise InvalidUserException
    except Comment.DoesNotExist:raise InvalidCommentException

def get_total_reaction_count():
    
    return Reaction.objects.aggregate(count=Count('id'))


def get_reaction_metrics(post_id):
    try:
        post=Post.objects.get(id=post_id)
        r1=Reaction.objects.filter(post=post).values('reaction').annotate(count=Count('reaction')).values_list('reaction','count')
        
        return dict(r1)
        
    except Post.DoesNotExist:raise InvalidPostException

def delete_post(user_id, post_id):
    try:
        post=Post.objects.get(id=post_id)
        user=User.objects.get(id=user_id)
        if post.posted_by_id!=user_id:
            raise UserCannotDeletePostException
        else:
            post.delete()
            
    except Post.DoesNotExist:raise InvalidPostException
    except User.DoesNotExist:raise InvalidUserException

def get_posts_with_more_positive_reactions():
    positive=Count('reaction',filter=Q(reaction__in=['WOW','LOVE','LIT','HAHA','THUMBS-UP']))
    negative=Count('reaction',filter=Q(reaction__in=['ANGRY','SAD','THUMBS-DOWN']))
    p=Reaction.objects.values('post').annotate(positive=positive,
                    negative=negative).filter(positive__gt=negative).values_list('post_id',flat=True).distinct()
    return list(p)
    
def get_posts_reacted_by_user(user_id):
    try:
        user=User.objects.get(id=user_id)
        p=Reaction.objects.filter(reacted_by__id=user_id).values_list('post_id',flat=True).distinct()
        return list(p)
    except User.DoesNotExist:raise InvalidUserException

def get_reactions_to_post(post_id):
    try:
        post=Post.objects.get(id=post_id)
        r=Reaction.objects.filter(post_id=post_id).select_related('reacted_by').distinct()
        list=[]
        for react in r:
            list.append({
                "user_id":react.reacted_by_id,
                "name":react.reacted_by.name,
                "profile_pic":react.reacted_by.profile_pic,
                "reaction":react.reaction
                
            })
        return list
            
    except Post.DoesNotExist:raise InvalidPostException
def get_post(post_id):
    try:
        details=Post.objects.prefetch_related('reactions',Prefetch('comments',queryset=Comment.objects.filter(post_id=post_id).select_related('commented_by'),to_attr='post_comments'),'post_comments__reactions').select_related('posted_by').get(id=post_id)
        
        return get_post_details(details)
        
    except Post.DoesNotExist:raise InvalidPostException
    
    
def get_user_posts(user_id):
    try:
        posts=[]
        user=User.objects.get(id=user_id)
        details=Post.objects.filter(posted_by_id=user_id).prefetch_related('reactions',Prefetch('comments',queryset=Comment.objects.all().select_related('commented_by'),to_attr='post_comments'),'post_comments__reactions').select_related('posted_by')   
        for post in details:
           posts.append(get_post_details(post))
        return posts
           
    except User.DoesNotExist:raise InvalidUserException
    
    
    
def get_replies_for_comment(comment_id):
    try:
        c=Comment.objects.get(id=comment_id)
        replies=Comment.objects.filter(parent_comment_id=comment_id).select_related('commented_by')
        list=[]
        for reply in replies:
            dt=reply.commented_at
            user={
                "user_id":reply.commented_by_id,
                "name":reply.commented_by.name,
                "profile_pic":reply.commented_by.profile_pic
            }
            list.append({
                "comment_id":reply.id,
                "commenter":user,
                "commented_at":dt.strftime("%Y-%m-%d %H:%M:%S.%f"),
                "comment_content":reply.content
            })
        return list
        
    except Comment.DoesNotExist:raise InvalidCommentException
    
def get_post_details(post):
    
    post_dict={}

    comment_list,post_reaction=[],[]
    comment_count=0
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
        if comment.parent_comment_id==None:
            comment_count=comment_count+1
            reply_count=0
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
                "replies_count":reply_count,
                "replies":reply_list
            }
            comment_list.append(comment_dict)
            for react in comment.reactions.all():
                if react.reaction not in comment_reaction:
                    comment_reaction.append(react.reaction)
            for reply in post.post_comments:
                reply_reaction=[]
                if comment.id==reply.parent_comment_id:
                    reply_count=reply_count+1
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
                            
                comment_dict["replies_count"]=reply_count
            
    post_dict["comments_count"]=comment_count
                
        
    
    return post_dict