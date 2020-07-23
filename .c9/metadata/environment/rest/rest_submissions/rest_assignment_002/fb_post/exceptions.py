{"filter":false,"title":"exceptions.py","tooltip":"/rest/rest_submissions/rest_assignment_002/fb_post/exceptions.py","undoManager":{"mark":1,"position":1,"stack":[[{"start":{"row":0,"column":0},"end":{"row":21,"column":1},"action":"remove","lines":["\"\"\"rest_assignment_002 URL Configuration","","The `urlpatterns` list routes URLs to views. For more information please see:","    https://docs.djangoproject.com/en/3.0/topics/http/urls/","Examples:","Function views","    1. Add an import:  from my_app import views","    2. Add a URL to urlpatterns:  path('', views.home, name='home')","Class-based views","    1. Add an import:  from other_app.views import Home","    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')","Including another URLconf","    1. Import the include() function: from django.urls import include, path","    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))","\"\"\"","from django.contrib import admin","from django.urls import path, include","","urlpatterns = [","    path('admin/', admin.site.urls),","    path('fb_post/', include('fb_post.urls')),","]"],"id":2}],[{"start":{"row":0,"column":0},"end":{"row":30,"column":0},"action":"insert","lines":["class InvalidUserException(Exception):","    pass","","class InvalidCommentContent(Exception):","    pass","","class InvalidPostContent(Exception):","    pass","","class InvalidPostException(Exception):","    pass","","class InvalidCommentException(Exception):","    pass","","class InvalidReplyContent(Exception):","    pass","","class InvalidReactionTypeException(Exception):","    pass","","class UserCannotDeletePostException(Exception):","    pass","","","class InvalidOffSetValueException(Exception):","    pass","","class InvalidLimitSetValueException(Exception):","    pass",""],"id":3}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":30,"column":0},"end":{"row":30,"column":0},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1588323903892,"hash":"a16a9ef14b6e39bf0e4ff8cf1e2f1a3f6feba10e"}