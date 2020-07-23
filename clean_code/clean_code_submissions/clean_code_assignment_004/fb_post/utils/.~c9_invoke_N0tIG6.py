from fb_post.models import User, Post
from fb_post.exceptions import InvalidUserException, InvalidPostException
from fb_post.exceptions import UserCannotDeletePostException

def delete_post(user_id, post_id):
    postcheck_for_post(post_id)
    check_for_user(user_id)
    post = Post.
    is_post_user_and_user_same(post, user_id)
    
    

def delete_post_if_user_is_same(post, user_id):
    if post.posted_by_id is user_id:
        post.delete()
    else:
        raise UserCannotDeletePostException
