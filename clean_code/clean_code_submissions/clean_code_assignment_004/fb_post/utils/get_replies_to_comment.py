from fb_post.models import Comment
from fb_post.constants import convert_date_time_into_strf_format
from .validation import check_for_comment
from .get_post_details import get_user_dict


def get_replies_for_comment(comment_id):

    check_for_comment(comment_id)

    replies = Comment.objects.filter(
                parent_comment_id=comment_id
                ).select_related('commented_by')

    replies_list = []
    for reply in replies:
        reply_dict = get_reply_details_dict(reply)
        replies_list.append(reply_dict)

    return replies_list


def get_reply_details_dict(reply):

    reply_dict = {
        "comment_id": reply.id,
        "commenter": get_user_dict(reply.commented_by),
        "commented_at": convert_date_time_into_strf_format(reply.commented_at),
        "comment_content": reply.content
    }

    return reply_dict
