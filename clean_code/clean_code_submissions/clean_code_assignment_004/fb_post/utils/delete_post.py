from fb_post.exceptions import UserCannotDeletePostException
from .validation import check_for_post, check_for_user

def delete_post(user_id, post_id):
    post = check_for_post(post_id)
    check_for_user(user_id)

    can_user_delete_post = post.posted_by_id == user_id
    if can_user_delete_post:
        post.delete()
    else:
        raise UserCannotDeletePostException
