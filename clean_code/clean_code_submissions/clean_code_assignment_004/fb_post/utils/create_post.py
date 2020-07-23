from fb_post.models import Post
from .validation import check_for_user, is_valid_post_content


def create_post(user_id, post_content):
    check_for_user(user_id)
    is_valid_post_content(post_content)

    post_id = Post.objects.create(posted_by_id=user_id,
                                  content=post_content).id
    return post_id
