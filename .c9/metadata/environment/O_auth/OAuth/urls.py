{"filter":false,"title":"urls.py","tooltip":"/O_auth/OAuth/urls.py","undoManager":{"mark":10,"position":10,"stack":[[{"start":{"row":15,"column":0},"end":{"row":21,"column":0},"action":"remove","lines":["from django.contrib import admin","from django.urls import path","","urlpatterns = [","    path('admin/', admin.site.urls),","]",""],"id":2}],[{"start":{"row":15,"column":0},"end":{"row":22,"column":1},"action":"insert","lines":["from django.contrib import admin","from django.urls import path, include","","urlpatterns = [","    path('admin/', admin.site.urls),","    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),","    path('', include('<app_name>.urls')),","]"],"id":3}],[{"start":{"row":21,"column":30},"end":{"row":21,"column":31},"action":"remove","lines":["e"],"id":4},{"start":{"row":21,"column":29},"end":{"row":21,"column":30},"action":"remove","lines":["m"]},{"start":{"row":21,"column":28},"end":{"row":21,"column":29},"action":"remove","lines":["a"]},{"start":{"row":21,"column":27},"end":{"row":21,"column":28},"action":"remove","lines":["n"]},{"start":{"row":21,"column":26},"end":{"row":21,"column":27},"action":"remove","lines":["_"]},{"start":{"row":21,"column":25},"end":{"row":21,"column":26},"action":"remove","lines":["p"]},{"start":{"row":21,"column":24},"end":{"row":21,"column":25},"action":"remove","lines":["p"]},{"start":{"row":21,"column":23},"end":{"row":21,"column":24},"action":"remove","lines":["a"]}],[{"start":{"row":21,"column":23},"end":{"row":21,"column":24},"action":"insert","lines":["a"],"id":5},{"start":{"row":21,"column":24},"end":{"row":21,"column":25},"action":"insert","lines":["u"]},{"start":{"row":21,"column":25},"end":{"row":21,"column":26},"action":"insert","lines":["t"]},{"start":{"row":21,"column":26},"end":{"row":21,"column":27},"action":"insert","lines":["h"]}],[{"start":{"row":21,"column":27},"end":{"row":21,"column":28},"action":"remove","lines":[">"],"id":6},{"start":{"row":21,"column":26},"end":{"row":21,"column":27},"action":"remove","lines":["h"]},{"start":{"row":21,"column":25},"end":{"row":21,"column":26},"action":"remove","lines":["t"]},{"start":{"row":21,"column":24},"end":{"row":21,"column":25},"action":"remove","lines":["u"]},{"start":{"row":21,"column":23},"end":{"row":21,"column":24},"action":"remove","lines":["a"]},{"start":{"row":21,"column":22},"end":{"row":21,"column":23},"action":"remove","lines":["<"]}],[{"start":{"row":21,"column":22},"end":{"row":21,"column":23},"action":"insert","lines":["m"],"id":7},{"start":{"row":21,"column":23},"end":{"row":21,"column":24},"action":"insert","lines":["y"]}],[{"start":{"row":21,"column":22},"end":{"row":21,"column":24},"action":"remove","lines":["my"],"id":8},{"start":{"row":21,"column":22},"end":{"row":21,"column":28},"action":"insert","lines":["my_app"]}],[{"start":{"row":21,"column":27},"end":{"row":21,"column":28},"action":"remove","lines":["p"],"id":9},{"start":{"row":21,"column":26},"end":{"row":21,"column":27},"action":"remove","lines":["p"]},{"start":{"row":21,"column":25},"end":{"row":21,"column":26},"action":"remove","lines":["a"]},{"start":{"row":21,"column":24},"end":{"row":21,"column":25},"action":"remove","lines":["_"]}],[{"start":{"row":21,"column":24},"end":{"row":21,"column":25},"action":"insert","lines":["s"],"id":10}],[{"start":{"row":21,"column":24},"end":{"row":21,"column":25},"action":"remove","lines":["s"],"id":11}],[{"start":{"row":21,"column":24},"end":{"row":21,"column":25},"action":"insert","lines":["a"],"id":12},{"start":{"row":21,"column":25},"end":{"row":21,"column":26},"action":"insert","lines":["p"]},{"start":{"row":21,"column":26},"end":{"row":21,"column":27},"action":"insert","lines":["p"]}]]},"ace":{"folds":[],"scrolltop":82,"scrollleft":0,"selection":{"start":{"row":22,"column":1},"end":{"row":22,"column":1},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":3,"state":"qqstring3","mode":"ace/mode/python"}},"timestamp":1588415037511,"hash":"1d0088c7bff5a9d213b86ceb5905e62e2d99a02f"}