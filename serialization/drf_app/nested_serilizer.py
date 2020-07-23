from rest_framework import serializers
from datetime import datetime


class User():
    def __init__(self, username, email):
        self.username = username
        self.email = email


class Comment(object):
    def __init__(self, content, created=None, user=None):
        self.user = user
        self.content = content
        self.created = created or datetime.now()


class UserSerializer(serializers.Serializer):
    email = serializers.EmailField()
    username = serializers.CharField(max_length=100)

class CommentSerializer(serializers.Serializer):
    user = UserSerializer(required=False)
    content = serializers.CharField(max_length=200)
    created = serializers.DateTimeField()

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = User(**user_data)
        comment = Comment(user = user,**validated_data)
        return user, comment

    def update(self, instance, validated_data):
        instance.user = validated_data.get('user', instance.user)
        instance.content = validated_data.get('content', instance.content)
        instance.created = validated_data.get('created', instance.created)
        return instance