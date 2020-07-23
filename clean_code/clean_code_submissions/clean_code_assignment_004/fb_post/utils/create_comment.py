from fb_post.models import Comment
from .validation import check_for_user, check_for_post
from .validation import is_valid_comment_content

def create_comment(user_id, post_id, comment_content):
    check_for_user(user_id)
    check_for_post(post_id)
    is_valid_comment_content(comment_content)

    comment_id = Comment.objects.create(content=comment_content,
                                        commented_by_id=user_id,
                                        post_id=post_id).id
    return comment_id
