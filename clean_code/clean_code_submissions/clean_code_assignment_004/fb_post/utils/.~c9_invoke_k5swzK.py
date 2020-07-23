from fb_post.models import Comment
from fb_post.exceptions import InvalidCommentException
from .validation import check_for_user, is_valid_reply_content

def reply_to_comment(user_id, comment_id, reply_content):
    try:
        check_for_user(user_id)

        comment = Comment.objects.select_related('parent_comment',
                                                 'post').get(id=comment_id)

        new_comment_id = comment_creation(user_id, comment_id,
                                          reply_content, comment)
        return new_comment_id

    except Comment.DoesNotExist:
        raise InvalidCommentException

def comment_creation(user_id, comment_id, reply_content, comment):
    if comment.parent_comment_id:
        parent_comment_id = comment.parent_comment_id
        is_valid_reply_content(reply_content)
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
