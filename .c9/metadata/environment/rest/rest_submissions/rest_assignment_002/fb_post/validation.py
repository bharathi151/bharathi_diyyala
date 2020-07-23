{"filter":false,"title":"validation.py","tooltip":"/rest/rest_submissions/rest_assignment_002/fb_post/validation.py","undoManager":{"mark":16,"position":16,"stack":[[{"start":{"row":0,"column":0},"end":{"row":283,"column":0},"action":"remove","lines":["from fb_post.models import *","from fb_post.exceptions import *","from django.db.models import Q","import datetime","from django.db.models import *","","","#task 6","def create_post(user_id, post_content):","    try:","        admin=User.objects.get(id=user_id)","        if post_content:","            p=Post.objects.create(posted_by_id=user_id,content=post_content)","            return p.id","        else:","            raise InvalidPostContent","            ","    except User.DoesNotExist:raise InvalidUserException","        ","","#task 9","def get_user_posts(user_id):","    try:","        posts=[]","        user=User.objects.get(id=user_id)","        details=Post.objects.filter(posted_by_id=user_id).prefetch_related('reactions',Prefetch('comments',queryset=Comment.objects.all().select_related('commented_by'),to_attr='post_comments'),'post_comments__reactions').select_related('posted_by')   ","        for post in details:","          posts.append(get_post_details(post))","        return posts","           ","    except User.DoesNotExist:raise InvalidUserException","    ","","def get_post_details(post):","    ","    post_dict={}","","    comment_list,post_reaction=[],[]","    comment_count=[]","    post_dict={","        \"post_id\":post.id,","        \"posted_by\":{","            \"name\":post.posted_by.name,","            \"user_id\":post.posted_by_id,","            \"profile_pic\":post.posted_by.profile_pic","        },","        \"posted_at\":post.posted_at.strftime(\"%Y-%m-%d %H:%M:%S.%f\"),","        \"post_content\":post.content,","        \"reactions\":{","            \"count\":len(post.reactions.all()),","            \"type\":post_reaction","        },","        \"comments\":comment_list,","    }","    for react in post.reactions.all():","        if react.reaction not in post_reaction:","            post_reaction.append(react.reaction)","    for comment in post.post_comments:","        if not comment.parent_comment_id:","            comment_count.append(comment.id)","            reply_count=[]","            reply_list=[]","            comment_reaction=[]","            comment_dict={","                \"comment_id\":comment.id,","                \"commenter\":{","                    \"user_id\":comment.commented_by_id,","                    \"name\":comment.commented_by.name,","                    \"profile_pic\":comment.commented_by.profile_pic","                },","                \"commented_at\":comment.commented_at.strftime(\"%Y-%m-%d %H:%M:%S.%f\"),","                \"comment_content\":comment.content,","                \"reactions\":{","                    \"count\":len(comment.reactions.all()),","                    \"type\":comment_reaction","                },","                \"replies_count\":len(reply_count),","                \"replies\":reply_list","            }","            comment_list.append(comment_dict)","            for react in comment.reactions.all():","                if react.reaction not in comment_reaction:","                    comment_reaction.append(react.reaction)","            for reply in post.post_comments:","                reply_reaction=[]","                if comment.id is reply.parent_comment_id:","                    reply_count.append(reply.id)","                    reply_list.append({","                        \"comment_id\":reply.id,","                        \"commenter\":{","                            \"user_id\":reply.commented_by_id,","                            \"name\":reply.commented_by.name,","                            \"profile_pic\":reply.commented_by.profile_pic","                        },","                        \"commented_at\":reply.commented_at.strftime(\"%Y-%m-%d %H:%M:%S.%f\"),","                        \"comment_content\":reply.content,","                        \"reactions\":{","                            \"count\":len(reply.reactions.all()),","                            \"type\":reply_reaction","                        },","                    })","                    for react in reply.reactions.all():","                        if react.reaction not in reply_reaction:","                            reply_reaction.append(react.reaction)","                            ","                comment_dict[\"replies_count\"]=len(reply_count)","            ","    post_dict[\"comments_count\"]=len(comment_count)","                ","        ","    ","    return post_dict","    ","","def create_comment(user_id, post_id, comment_content):","    check_for_user(user_id)","    check_for_post(post_id)","    is_valid_comment_content(comment_content)","","    comment_id = Comment.objects.create(content=comment_content,","                                        commented_by_id=user_id,","                                        post_id=post_id).id","    return comment_id","","","def reply_to_comment(user_id, comment_id, reply_content):","    try :","        user=User.objects.get(id=user_id)","        comment=Comment.objects.select_related('post','parent_comment').get(id=comment_id)","        if not reply_content:","            raise InvalidReplyContent","        else:","            if not comment.parent_comment_id:","                return Comment.objects.create(content=reply_content,commented_by_id=user_id,parent_comment_id=comment_id,post_id=comment.post_id).id","            else:","                return Comment.objects.create(content=reply_content,commented_by_id=user_id,parent_comment_id=comment.parent_comment_id,post_id=comment.post_id).id","            ","    ","    except User.DoesNotExist:raise InvalidUserException","    except Comment.DoesNotExist:raise InvalidCommentException","    ","","","#task 5","def react_to_post(user_id, post_id, reaction_type):","    try:","        user=User.objects.get(id=user_id)","        post=Post.objects.get(id=post_id)","        react=['WOW','LIT','LOVE','HAHA','THUMBS-UP','THUMBS-DOWN','ANGRY','SAD']","        ","        if reaction_type in react:","            existed=Reaction.objects.get(reacted_by_id=user_id,post_id=post_id)","            ","            if existed.reaction == reaction_type:","                existed.delete()","                    ","            else:","                existed.reaction=reaction_type","                existed.save()","            ","        else:","            raise InvalidReactionTypeException","","","    except Reaction.DoesNotExist:Reaction.objects.create(reaction=reaction_type,reacted_by_id=user_id,post_id=post_id)","    except User.DoesNotExist:raise InvalidUserException","    except Post.DoesNotExist:raise InvalidPostException","    ","#task 6","def react_to_comment(user_id, comment_id, reaction_type):","    try:","        user=User.objects.get(id=user_id)","        comment=Comment.objects.get(id=comment_id)","        react=['WOW','LIT','LOVE','HAHA','THUMBS-UP','THUMBS-DOWN','ANGRY','SAD']","        ","        if reaction_type in react:","            existed=Reaction.objects.get(reacted_by_id=user_id,comment_id=comment_id)","            ","            if existed.reaction == reaction_type:","                existed.delete()","                    ","            else:","                existed.reaction=reaction_type","                existed.save()","            ","        else:","            raise InvalidReactionTypeException","            ","    except Reaction.DoesNotExist:Reaction.objects.create(reaction=reaction_type,reacted_by_id=user_id,comment_id=comment_id)","    except User.DoesNotExist:raise InvalidUserException","    except Comment.DoesNotExist:raise InvalidCommentException","","def get_total_reaction_count():","    ","    return Reaction.objects.aggregate(count=Count('id'))","","","def get_reaction_metrics(post_id):","    try:","        post=Post.objects.get(id=post_id)","        r1=Reaction.objects.filter(post=post).values('reaction').annotate(count=Count('reaction')).values_list('reaction','count')","        ","        return dict(r1)","        ","    except Post.DoesNotExist:raise InvalidPostException","","def delete_post(user_id, post_id):","    try:","        post=Post.objects.get(id=post_id)","        user=User.objects.get(id=user_id)","        if post.posted_by_id is user_id:","            post.delete()","            ","        else:","            raise UserCannotDeletePostException","            ","    except Post.DoesNotExist:raise InvalidPostException","    except User.DoesNotExist:raise InvalidUserException","","def get_posts_with_more_positive_reactions():","    positive=Count('reaction',filter=Q(reaction__in=['WOW','LOVE','LIT','HAHA','THUMBS-UP']))","    negative=Count('reaction',filter=Q(reaction__in=['ANGRY','SAD','THUMBS-DOWN']))","    p=Reaction.objects.values('post').annotate(positive=positive,","                    negative=negative).filter(positive__gt=negative).values_list('post_id',flat=True).distinct()","    return list(p)","    ","def get_posts_reacted_by_user(user_id):","    try:","        user=User.objects.get(id=user_id)","        p=Reaction.objects.filter(reacted_by__id=user_id).values_list('post_id',flat=True).distinct()","        return list(p)","    except User.DoesNotExist:raise InvalidUserException","","def get_reactions_to_post(post_id):","    try:","        post=Post.objects.get(id=post_id)","        r=Reaction.objects.filter(post_id=post_id).select_related('reacted_by').distinct()","        list=[]","        for react in r:","            list.append({","                \"user_id\":react.reacted_by_id,","                \"name\":react.reacted_by.name,","                \"profile_pic\":react.reacted_by.profile_pic,","                \"reaction\":react.reaction","                ","            })","        return list","            ","    except Post.DoesNotExist:raise InvalidPostException","def get_post(post_id):","    try:","        details=Post.objects.prefetch_related('reactions',Prefetch('comments',queryset=Comment.objects.filter(post_id=post_id).select_related('commented_by'),to_attr='post_comments'),'post_comments__reactions').select_related('posted_by').get(id=post_id)","        ","        return get_post_details(details)","        ","    except Post.DoesNotExist:raise InvalidPostException","    ","    ","","    ","    ","def get_replies_for_comment(comment_id):","    try:","        c=Comment.objects.get(id=comment_id)","        replies=Comment.objects.filter(parent_comment_id=comment_id).select_related('commented_by')","        list=[]","        for reply in replies:","            dt=reply.commented_at","            user={","                \"user_id\":reply.commented_by_id,","                \"name\":reply.commented_by.name,","                \"profile_pic\":reply.commented_by.profile_pic","            }","            list.append({","                \"comment_id\":reply.id,","                \"commenter\":user,","                \"commented_at\":dt.strftime(\"%Y-%m-%d %H:%M:%S.%f\"),","                \"comment_content\":reply.content","            })","        return list","        ","    except Comment.DoesNotExist:raise InvalidCommentException","    ",""],"id":2}],[{"start":{"row":0,"column":0},"end":{"row":55,"column":0},"action":"insert","lines":["from fb_post.exceptions import (InvalidUserException, InvalidPostException,","                                InvalidCommentException, InvalidCommentContent,","                                InvalidPostContent, InvalidReplyContent,","                                InvalidReactionTypeException","                               )","from fb_post.constants import ReactionTypes","from fb_post.models import User, Post, Comment","","def check_for_user(user_id):","    try:","        user = User.objects.get(id=user_id)","","    except User.DoesNotExist:","        raise InvalidUserException","","    return user","","def check_for_post(post_id):","    try:","        post = Post.objects.get(id=post_id)","","    except Post.DoesNotExist:","        raise InvalidPostException","","    return post","","def check_for_comment(comment_id):","    try:","        comment = Comment.objects.get(id=comment_id)","","    except Comment.DoesNotExist:","        raise InvalidCommentException","","    return comment","","def is_valid_comment_content(comment_content):","    is_not_valid = not comment_content","    if is_not_valid:","        raise InvalidCommentContent","","def is_valid_post_content(post_content):","    is_not_valid = not post_content","    if is_not_valid:","        raise InvalidPostContent","","def is_valid_reaction_type(reaction_type):","    valid_reaction_types = ReactionTypes.values","    is_not_valid = reaction_type not in valid_reaction_types","    if is_not_valid:","        raise InvalidReactionTypeException","","def is_valid_reply_content(reply_content):","    is_not_valid = not reply_content","    if is_not_valid:","        raise InvalidReplyContent",""],"id":3}],[{"start":{"row":5,"column":0},"end":{"row":5,"column":43},"action":"remove","lines":["from fb_post.constants import ReactionTypes"],"id":4},{"start":{"row":4,"column":32},"end":{"row":5,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":5,"column":46},"end":{"row":6,"column":0},"action":"insert","lines":["",""],"id":68},{"start":{"row":6,"column":0},"end":{"row":6,"column":1},"action":"insert","lines":["d"]}],[{"start":{"row":6,"column":0},"end":{"row":6,"column":1},"action":"remove","lines":["d"],"id":69}],[{"start":{"row":6,"column":0},"end":{"row":6,"column":1},"action":"insert","lines":["f"],"id":70},{"start":{"row":6,"column":1},"end":{"row":6,"column":2},"action":"insert","lines":["r"]}],[{"start":{"row":6,"column":0},"end":{"row":6,"column":2},"action":"remove","lines":["fr"],"id":71},{"start":{"row":6,"column":0},"end":{"row":6,"column":4},"action":"insert","lines":["from"]}],[{"start":{"row":6,"column":4},"end":{"row":6,"column":5},"action":"insert","lines":[" "],"id":72},{"start":{"row":6,"column":5},"end":{"row":6,"column":6},"action":"insert","lines":["d"]},{"start":{"row":6,"column":6},"end":{"row":6,"column":7},"action":"insert","lines":["b"]}],[{"start":{"row":6,"column":6},"end":{"row":6,"column":7},"action":"remove","lines":["b"],"id":73},{"start":{"row":6,"column":5},"end":{"row":6,"column":6},"action":"remove","lines":["d"]}],[{"start":{"row":6,"column":5},"end":{"row":6,"column":6},"action":"insert","lines":["f"],"id":74},{"start":{"row":6,"column":6},"end":{"row":6,"column":7},"action":"insert","lines":["b"]}],[{"start":{"row":6,"column":5},"end":{"row":6,"column":7},"action":"remove","lines":["fb"],"id":75},{"start":{"row":6,"column":5},"end":{"row":6,"column":12},"action":"insert","lines":["fb_post"]}],[{"start":{"row":6,"column":12},"end":{"row":6,"column":13},"action":"insert","lines":["."],"id":76},{"start":{"row":6,"column":13},"end":{"row":6,"column":14},"action":"insert","lines":["c"]},{"start":{"row":6,"column":14},"end":{"row":6,"column":15},"action":"insert","lines":["o"]},{"start":{"row":6,"column":15},"end":{"row":6,"column":16},"action":"insert","lines":["n"]}],[{"start":{"row":6,"column":13},"end":{"row":6,"column":16},"action":"remove","lines":["con"],"id":77},{"start":{"row":6,"column":13},"end":{"row":6,"column":22},"action":"insert","lines":["constants"]}],[{"start":{"row":6,"column":22},"end":{"row":6,"column":23},"action":"insert","lines":[" "],"id":78},{"start":{"row":6,"column":23},"end":{"row":6,"column":24},"action":"insert","lines":["i"]},{"start":{"row":6,"column":24},"end":{"row":6,"column":25},"action":"insert","lines":["m"]}],[{"start":{"row":6,"column":23},"end":{"row":6,"column":25},"action":"remove","lines":["im"],"id":79},{"start":{"row":6,"column":23},"end":{"row":6,"column":29},"action":"insert","lines":["import"]}],[{"start":{"row":6,"column":29},"end":{"row":6,"column":30},"action":"insert","lines":[" "],"id":80},{"start":{"row":6,"column":30},"end":{"row":6,"column":31},"action":"insert","lines":["R"]}],[{"start":{"row":6,"column":30},"end":{"row":6,"column":31},"action":"remove","lines":["R"],"id":81},{"start":{"row":6,"column":30},"end":{"row":6,"column":43},"action":"insert","lines":["ReactionTypes"]}]]},"ace":{"folds":[],"scrolltop":266.13940799702436,"scrollleft":0,"selection":{"start":{"row":6,"column":43},"end":{"row":6,"column":43},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":14,"state":"start","mode":"ace/mode/python"}},"timestamp":1588394987406,"hash":"e78f7c79efe04ad36d1848fb72b89dd95f2436dc"}