from django.shortcuts import render
# from oauth2_provider.contrib.rest_framework import OAuth2Authentication
# from oauth2_provider.decorators import protected_resource
from rest_framework.decorators import api_view
#authentication_classes
from rest_framework.response import Response
from rest_framework import serializers
from .models import *
from .utils import *
from .constants import ReactionTypes
# Create your views here.
class CreateContentRequest:
    def __init__(self, user_id, content):
        self.user_id = user_id
        self.content = content


class CreateContentRequestSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()
    content = serializers.CharField(max_length=1000)
    def create(self, validated_data):
        return CreateContentRequest(**validated_data)

class CreatePostResponseClass:
    def __init__(self, post_id):
        self.post_id = post_id


class CreatePostResponseSerializer(serializers.Serializer):
    post_id = serializers.IntegerField()

    def create(self, validated_data):
        return CreatePostResponseClass(**validated_data)

@api_view(['POST'])
# @authentication_classes([OAuth2Authentication])
# @protected_resource(['superuser'])
def create_post_in_db(request):
    serializer = CreateContentRequestSerializer(data=request.data)
    is_invalid_request_data = not serializer.is_valid()

    if is_invalid_request_data:
        return Response(status=400)

    request_obj = serializer.save()
    try:
        new_post_id = create_post(request_obj.user_id, request_obj.content)
    except InvalidUserException:
        return Response(status=404)
    new_post_obj = CreatePostResponseClass(new_post_id)
    response_serializer = CreatePostResponseSerializer(new_post_obj)
    return Response(response_serializer.data,status=201)


class UserResponseSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    user_id = serializers.IntegerField()
    profile_pic = serializers.URLField()

class ReactionResponseSerializer(serializers.Serializer):
    count = serializers.IntegerField()
    type = serializers.ListField(allow_empty=True)

class ReplyResponseSerializerDict(serializers.DictField):
    comment_id = serializers.IntegerField()
    commenter = UserResponseSerializer()
    commented_at = serializers.DateTimeField()
    comment_content = serializers.CharField(max_length=1000)
    reactions = ReactionResponseSerializer()

class ReplyResponseSerializerList(serializers.ListField):
    replies = ReplyResponseSerializerDict()

class CommentResponseSerializerDict(ReplyResponseSerializerDict):
    replies_count = serializers.IntegerField()

class CommentResponseSerializerList(serializers.ListField):
    comments = CommentResponseSerializerDict()

class PostResponseSerializer(serializers.Serializer):
    post_id = serializers.IntegerField
    posted_by = UserResponseSerializer()
    posted_at = serializers.DateTimeField()
    post_content = serializers.CharField(max_length=1000)
    reactions = ReactionResponseSerializer()
    comments = CommentResponseSerializerList()
    comments_count = serializers.IntegerField()

@api_view(['GET'])
def get_post_in_db(request,post_id):
    try:
        post_details = get_post(post_id)
    except InvalidPostException:
        return Response(status=404)
    response_serializer = PostResponseSerializer(post_details)
    return Response(response_serializer.data,status=200)

class GetOnlyPostResponseSerializer(serializers.Serializer):
    post_id = serializers.IntegerField()
    posted_by_id = serializers.IntegerField()
    posted_at = serializers.DateTimeField()
    post_content = serializers.CharField(max_length=1000)
    tzinfo = serializers.CharField(max_length=100)

class TimezoneRequestClass:
    def __init__(self, timezone):
        self.timezone = timezone

class TimezoneRequestSerializer(serializers.Serializer):
    timezone = serializers.CharField(max_length=100)

    def create(self, validated_data):
        return TimezoneRequestClass(**validated_data)

@api_view(['POST'])
def get_only_post_in_db(request,post_id):
    serializer = TimezoneRequestSerializer(data=request.data)
    is_invalid_request_data = not serializer.is_valid()

    if is_invalid_request_data:
        return Response(status=400)

    request_obj = serializer.save()
    try:
        post_details = get_only_post(post_id, request_obj.timezone)
    except InvalidPostException:
        return Response(status=404)
    
    response_serializer = GetOnlyPostResponseSerializer(post_details)
    return Response(response_serializer.data,status=200)

class CreateReplyResponseClass:
    def __init__(self, reply_id):
        self.reply_id = reply_id


class CreateReplyResponseSerializer(serializers.Serializer):
    reply_id = serializers.IntegerField()

    def create(self, validated_data):
        return CreatePostResponseClass(**validated_data)

@api_view(['POST'])
def reply_to_comment_in_db(request, comment_id):
    serializer = CreateContentRequestSerializer(data=request.data)
    is_invalid_request_data = not serializer.is_valid()

    if is_invalid_request_data:
        return Response(status=400)

    request_obj = serializer.save()
    try:
        new_reply_id = reply_to_comment(request_obj.user_id, comment_id, request_obj.content)
    except InvalidUserException:
        return Response(status=404)
    except InvalidCommentException:
        return Response(status=404)
    new_reply_obj = CreateReplyResponseClass(new_reply_id)
    response_serializer = CreateReplyResponseSerializer(new_reply_obj)
    return Response(response_serializer.data,status=201)

class CreateReactRequestClass:
    def __init__(self, user_id, reaction_type):
        self.user_id = user_id
        self.reaction_type = reaction_type

class CreateReactRequestSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()
    reaction_type = serializers.ChoiceField(choices=ReactionTypes.values)

    def create(self, validated_data):
        return CreateReactRequestClass(**validated_data)

@api_view(['POST'])
def react_to_post_in_db(request, post_id):
    serializer = CreateReactRequestSerializer(data=request.data)
    is_invalid_request_data = not serializer.is_valid()

    if is_invalid_request_data:
        return Response(status=400)

    request_obj = serializer.save()
    try:
        react_to_post(request_obj.user_id, post_id, request_obj.reaction_type)
    except InvalidUserException:
        return Response(status=404)
    except InvalidPostException:
        return Response(status=404)
    return Response(status=201)

@api_view(['POST'])
def react_to_comment_in_db(request, comment_id):
    serializer = CreateReactRequestSerializer(data=request.data)
    is_invalid_request_data = not serializer.is_valid()

    if is_invalid_request_data:
        return Response(status=400)

    request_obj = serializer.save()
    try:
        react_to_comment(request_obj.user_id, comment_id, request_obj.reaction_type)
    except InvalidUserException:
        return Response(status=404)
    except InvalidCommentException:
        return Response(status=404)
    return Response(status=201)

class CreateDeleteRequestClass:
    def __init__(self, user_id):
        self.user_id = user_id

class CreateDeleteRequestSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()

    def create(self, validated_data):
        return CreateDeleteRequestClass(**validated_data)

@api_view(['POST'])
def delete_post_in_db(request, post_id):
    serializer = CreateDeleteRequestSerializer(data=request.data)
    is_invalid_request_data = not serializer.is_valid()

    if is_invalid_request_data:
        return Response(status=400)

    request_obj = serializer.save()
    try:
        delete_post(request_obj.user_id, post_id)
    except InvalidUserException:
        return Response(status=404)
    except InvalidPostException:
        return Response(status=404)
    except UserCannotDeletePostException:
        return Response(status=403)
    return Response(status=200)

class CreateCommentResponseClass:
    def __init__(self, comment_id):
        self.comment_id = comment_id

class CreateCommentResponseSerializer(serializers.Serializer):
    comment_id = serializers.IntegerField()

    def create(self, validated_data):
        return CreateCommentResponseClass(**validated_data)

@api_view(['POST'])
def create_comment_in_db(request, post_id):
    serializer = CreateContentRequestSerializer(data=request.data)
    is_invalid_request_data = not serializer.is_valid()

    if is_invalid_request_data:
        return Response(status=400)

    request_obj = serializer.save()
    try:
        new_comment_id = create_comment(request_obj.user_id, post_id, request_obj.content)
    except InvalidUserException:
        return Response(status=404)
    except InvalidPostException:
        return Response(status=404)
    new_comment_obj = CreateCommentResponseClass(new_comment_id)
    response_serializer = CreateCommentResponseSerializer(new_comment_obj)
    return Response(response_serializer.data,status=201)