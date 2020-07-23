from django.urls import path

from .views import *

urlpatterns = [
    path('post/<int:post_id>/', get_post_in_db),
    path('comment/<int:comment_id>/reply/create/', reply_to_comment_in_db),
    path('post/<int:post_id>/react/', react_to_post_in_db),
    path('comment/<int:comment_id>/react/', react_to_comment_in_db),
    path('post/<int:post_id>/delete/', delete_post_in_db),
    path('comment/<int:post_id>/create/', create_comment_in_db),
    path('post/', create_post_in_db),
    path('post/<int:post_id>/details/', get_only_post_in_db),
    
]