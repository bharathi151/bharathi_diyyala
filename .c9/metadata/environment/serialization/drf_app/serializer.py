{"filter":false,"title":"serializer.py","tooltip":"/serialization/drf_app/serializer.py","undoManager":{"mark":0,"position":0,"stack":[[{"start":{"row":0,"column":0},"end":{"row":5,"column":41},"action":"insert","lines":["from rest_framework import serializers","","class CommentSerializer(serializers.Serializer):","    email = serializers.EmailField()","    content = serializers.CharField(max_length=200)","    created = serializers.DateTimeField()"],"id":1}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":5,"column":41},"end":{"row":5,"column":41},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":1,"state":"start","mode":"ace/mode/python"}},"timestamp":1588086594143,"hash":"851d6b98d5c7433906c4cd53019fd84523fd5a14"}