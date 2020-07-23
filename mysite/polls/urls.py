from django.urls import path

from . import views
app_name = 'polls'
urlpatterns = [
    #path('specifics/<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('hello-world/',views.index1,name='index1'),
    path('now/',views.index2,name='index2'),
    path('request_id/',views.index3,name='index3'),
    path('home_page/',views.index4,name='index4'),
    path('', views.index, name='index'),

]
