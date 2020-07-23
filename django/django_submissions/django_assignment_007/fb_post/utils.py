from fb_post.models import *
from fb_post.exceptions import *
from django.db.models import Q
import datetime
from django.db.models import *
#task 2
def create_group(user_id, name, member_ids):
    try:
        admin=User.objects.get(id=user_id)
        if name=='':
            raise InvalidGroupNameException
        member_ids=list(set(member_ids))    
        members=User.objects.filter(id__in=member_ids)
        if len(member_ids)!=len(members):
            raise InvalidMemberException
        else:
            group=Group.objects.create(name=name)
            existed_members,regular_members=[],[]
            Membership.objects.create(group_id=group.id,member_id=user_id,is_admin=True)
            if len(members)!=len(member_ids):
                raise InvalidMemberException
            for member in members:
                if member.id!=user_id:
                    regular_members.append(Membership(group_id=group.id,member_id=member.id,is_admin=False)) 
                
                    
            Membership.objects.bulk_create(regular_members)
    
        return group.id
        
    except User.DoesNotExist:raise InvalidUserException
    
#task 3  
def add_member_to_group(user_id, new_member_id, group_id):
    try:
        admin=User.objects.get(id=user_id)
        group=Group.objects.get(id=group_id)
        group_member=Membership.objects.get(member_id=user_id,group_id=group_id)
        new_member=User.objects.filter(id=new_member_id)
        if new_member:
            admin_member=Membership.objects.filter(member_id=user_id,group_id=group_id,is_admin=True)
            if admin_member:
                existed=Membership.objects.filter(member_id=new_member_id,group_id=group_id)
                if not existed:
                    Membership.objects.create(member_id=new_member_id,group_id=group_id,is_admin=False)
            else:
                raise UserIsNotAdminException
        else:
            raise InvalidMemberException
        
    except User.DoesNotExist:raise InvalidUserException
    except Group.DoesNotExist:raise InvalidGroupException
    except Membership.DoesNotExist:raise UserNotInGroupException
    


#task  4
def remove_member_from_group(user_id, member_id, group_id):
    try:
        admin=User.objects.get(id=user_id)
        group=Group.objects.get(id=group_id)
        group_member=Membership.objects.filter(member_id=user_id,group_id=group_id)
        if group_member:
            member=User.objects.filter(id=member_id)
            if member:
                admin_member=Membership.objects.filter(group_id=group_id,member_id=user_id,is_admin=True)
                if admin_member:
                    remove_member=Membership.objects.filter(member_id=member_id,group_id=group_id)
                    if remove_member:
                        remove_member.delete()
                    else:
                        raise MemberNotInGroupException
                        
                else:
                    raise UserIsNotAdminException
            else:
                raise InvalidMemberException
        else:raise UserNotInGroupException
    except User.DoesNotExist:raise InvalidUserException
    except Group.DoesNotExist:raise InvalidGroupException
     
    
#task 5
def make_member_as_admin(user_id, member_id, group_id):
    try:
        admin=User.objects.get(id=user_id)
        group=Group.objects.get(id=group_id)
        member=User.objects.filter(id=member_id)
        if member:
            group_member=Membership.objects.filter(member_id=user_id,group_id=group_id)
            if group_member:
                admin_member=Membership.objects.filter(member_id=user_id,group_id=group_id,is_admin=True)
                if admin_member:
                    make_member=Membership.objects.filter(member_id=member_id,group_id=group_id)
                    if make_member:
                        make_member.update(is_admin=True)
                        
                    else:raise MemberNotInGroupException
                else:
                    raise UserIsNotAdminException
                    
            else:
                raise UserNotInGroupException
        else:
            raise InvalidMemberException
        
    except User.DoesNotExist:raise InvalidUserException
    except Group.DoesNotExist:raise InvalidGroupException

    
    

#task 6
def create_post(user_id, post_content, group_id=None):
    try:
        admin=User.objects.get(id=user_id)
        if post_content!='':
            if group_id!=None:
                group=Group.objects.filter(id=group_id)
                if group:
                    group_member=Membership.objects.filter(member_id=user_id,group_id=group_id)
                    if group_member:
                        p=Post.objects.create(posted_by_id=user_id,group_id=group_id,content=post_content)
                        return p.id   
                    else:
                        raise UserNotInGroupException
                else:raise InvalidGroupException
            else:
                p=Post.objects.create(posted_by_id=user_id,content=post_content)
                return p.id
                
        else:
            raise InvalidPostContent
            
    except User.DoesNotExist:raise InvalidUserException
        
#task 7
def get_group_feed(user_id, group_id, offset, limit):
    try:
        user=User.objects.get(id=user_id)
        group=Group.objects.get(id=group_id)
        group_member=Membership.objects.filter(member_id=user_id,id=group_id)
        if group_member:
            if offset<0:
                raise InvalidOffSetValueException
            else:
                if limit<=0:
                    raise InvalidLimitSetValueException
                else:
                    details=Post.objects.filter(posted_by_id=user_id,group_id=group_id).prefetch_related('reactions',Prefetch('comments',queryset=Comment.objects.all().select_related('commented_by'),to_attr='post_comments'),'post_comments__reactions').select_related('posted_by').order_by('-posted_by')[offset:offset+limit]  
                    final_post_list=[]
                    for post in details:
                        final_post_list.append(get_post_details(post))
                    return final_post_list
        
        else:
            raise UserNotInGroupException
    except User.DoesNotExist:raise InvalidUserException
    except Group.DoesNotExist:raise InvalidGroupException


#task 8
def get_posts_with_more_comments_than_reactions():
    post_ids=Post.objects.annotate(comment=Count('comments'),reaction=Count('reactions')).filter(comment__gt=F('reaction')).values_list('id',flat=True)
    return list(post_ids)

#task 9
def get_user_posts(user_id):
    try:
        posts=[]
        user=User.objects.get(id=user_id)
        details=Post.objects.filter(posted_by_id=user_id).prefetch_related('reactions',Prefetch('comments',queryset=Comment.objects.all().select_related('commented_by'),to_attr='post_comments'),'post_comments__reactions').select_related('posted_by')   
        for post in details:
          posts.append(get_user_post_details(post))
        return posts
           
    except User.DoesNotExist:raise InvalidUserException
    
#task 10
def get_silent_group_members(group_id):
    try:
        group=Group.objects.get(id=group_id)
        list_ids=Membership.objects.filter(group_id=group_id).exclude(member_id__in=list(Post.objects.filter(group_id=group_id).values_list('posted_by_id',flat=True))).values_list('member_id',flat=True)  
        return list(list_ids)
    except Group.DoesNotExist:raise InvalidGroupException
 
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
    
def get_user_post_details(post):
    
    post_dict={}
    if post.group_id!=None:
        group_dict={
                "group_id":post.group_id,
                "name":post.group.name
                
            }
    else:
        group_dict=None
    
    comment_list,post_reaction=[],[]
    comment_count=0
    post_dict={
        "post_id":post.id,
        "group":group_dict,
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
    
