from django.urls import path

from .views import (create_snippet, create_dummy_snippet, check_view,
                    update_snippet, delete_snippet, get_snippet, get_list_of_snippets)

urlpatterns = [
    path('check/', check_view),
    path('create/', create_snippet),
    path('<int:snippet_id>/update/', update_snippet),
    path('<int:snippet_id>/delete/', delete_snippet),
    path('<int:snippet_id>/get/', get_snippet),
    path('all/', get_list_of_snippets),
    path('', create_dummy_snippet),
]