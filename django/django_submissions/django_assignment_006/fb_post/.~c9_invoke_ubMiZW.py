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
            p=Post.objects.create(content=post_content,posted_by=user)
            return p.id
    
    except User.DoesNotExist:raise InvalidUserException
    

def create_comment(user_id, post_id, comment_content):
    try :
        user=User.objects.get(id=user_id)
        post=Post.objects.get(id=post_id)
        if comment_content=='':
            raise InvalidCommentContent
        else:
            c=Comment.objects.create(content=comment_content,commented_by=user,post=post)
            return c.id
    
    except User.DoesNotExist:raise InvalidUserException
    except Post.DoesNotExist:raise InvalidPostException
    
    
#task5
def reply_to_comment(user_id, comment_id, reply_content):
    try :
        user=User.objects.get(id=user_id)
        comment=Comment.objects.get(id=comment_id)
        if reply_content=='':
            raise InvalidReplyContent
        else:
            r=Comment.objects.create(content=reply_content,commented_by=user,parent_comment=comment,post=comment.post)
            return r.id
    
    except User.DoesNotExist:raise InvalidUserException
    except Comment.DoesNotExist:raise InvalidCommentException
    


#task 6
def react_to_post(user_id, post_id, reaction_type):
    try:
        user=User.objects.get(id=user_id)
        post=Post.objects.get(id=post_id)
        react=['WOW','LIT','LOVE','HAHA','THUMB-UP','THUMB-DOWN','ANGRY','SAD']
        
        if reaction_type in react:
            existed=Reaction.objects.get(reacted_by_id=user_id,post_id=post_id)
            
            if existed.reaction==reaction_type:
                existed.delete()
                    
            else:
                existed.reaction=reaction_type
                existed.save()
            
        else:
            raise InvalidReactionTypeException


    except Reaction.DoesNotExist:Reaction.objects.create(reaction=reaction_type,reacted_by=user,post=post)
    except User.DoesNotExist:raise InvalidUserException
    except Post.DoesNotExist:raise InvalidPostException

def react_to_comment(user_id, comment_id, reaction_type):
    try:
        user=User.objects.get(id=user_id)
        comment=Comment.objects.get(id=comment_id)
        react=['WOW','LIT','LOVE','HAHA','THUMB-UP','THUMB-DOWN','ANGRY','SAD']
        
        if reaction_type in react:
            existed=Reaction.objects.get(reacted_by_id=user_id,comment_id=comment_id)
            
            if existed.reaction==reaction_type:
                existed.delete()
                    
            else:
                existed.reaction=reaction_type
                existed.save()
            
        else:
            raise InvalidReactionTypeException
            
    except Reaction.DoesNotExist:Reaction.objects.create(reaction=reaction_type,reacted_by=user,comment=comment)
    except User.DoesNotExist:raise InvalidUserException
    except Comment.DoesNotExist:raise InvalidCommentException

def get_total_reaction_count():
    c=Reaction.objects.aggregate(count=Count('id'))
    return c


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
    p=Reaction.objects.values('post').annotate(positive=positive,negative=negative).filter(positive__gt=negative).values_list('post_id',flat=True)
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

