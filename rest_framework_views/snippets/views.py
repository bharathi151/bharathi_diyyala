from django.shortcuts import render
from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
# Create your views here.

class CreateSnippetRequest:
    def __init__(self, code, title=''):
        self.title = title
        self.code = code


class CreateSnippetRequestSerializer(serializers.Serializer):
    title = serializers.CharField(required=False, allow_blank=True,
                                  max_length=100)
    code = serializers.CharField()

    def create(self, validated_data):
        return CreateSnippetRequest(**validated_data)

class CreateSnippetResponseClass:
    def __init__(self, id, title, code):
        self.id = id
        self.title = title
        self.code = code


class CreateSnippetResponseSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(required=False, allow_blank=True,
                                  max_length=100)
    code = serializers.CharField()

    def create(self, validated_data):
        return CreateSnippetResponseClass(**validated_data)

def create_snippet_in_db(title, code):
    """
    Create and return a new `Snippet` instance, given the validated data.
    """
    from snippets.models import Snippet
    return Snippet.objects.create(title=title, code=code)

def update_snippet_in_db(id, title, code):
    """
    Create and return a new `Snippet` instance, given the validated data.
    """
    from snippets.models import Snippet
    try:
        snippet_obj = Snippet.objects.get(id=id)
    except Snippet.DoesNotExist:
        return "Snippet not found!"
    snippet_obj.title = title
    snippet_obj.code = code
    snippet_obj.save()
    return snippet_obj

def delete_snippet_in_db(id):
    """
    Create and return a new `Snippet` instance, given the validated data.
    """
    from snippets.models import Snippet
    try:
        snippet_obj = Snippet.objects.get(id=id)
        snippet_obj.delete()
    except Snippet.DoesNotExist:
        return "cannot delete"
    return "successfully deleted"

def get_snippet_in_db(id):
    """
    Create and return a new `Snippet` instance, given the validated data.
    """
    from snippets.models import Snippet
    try:
        snippet_obj = Snippet.objects.get(id=id)
    except Snippet.DoesNotExist:
        return "Snippet DoesNotExist"
    return snippet_obj

@api_view(['POST'])
def create_dummy_snippet(request):
    """
    Create a new snippet.
    """
    
    serializer = CreateSnippetRequestSerializer(data=request.data)
    if serializer.is_valid():
        request_obj = serializer.save()
        
        dummy_snippet_object = CreateSnippetResponseClass(
            id=1,
            title="",
            code="print(123)"
        )
        
        response_serializer = CreateSnippetResponseSerializer(dummy_snippet_object)
        return Response(response_serializer.data)

@api_view(['POST'])
def check_view(request):
    """
    Create a new snippet.
    """
    print("Dummy_snippet")
    return Response()

@api_view(['POST'])
def create_snippet(request):
    serializer = CreateSnippetRequestSerializer(data=request.data)
    is_invalid_request_data = not serializer.is_valid()

    if is_invalid_request_data:
        return Response(status=400)

    request_obj = serializer.save()

    new_snippet_obj = create_snippet_in_db(
        title=request_obj.title,
        code=request_obj.code
    )

    response_serializer = CreateSnippetResponseSerializer(new_snippet_obj)
    return Response(response_serializer.data)

@api_view(['PUT'])
def update_snippet(request,snippet_id):
    serializer = CreateSnippetRequestSerializer(data=request.data)
    is_invalid_request_data = not serializer.is_valid()

    if is_invalid_request_data:
        return Response(status=400)

    request_obj = serializer.save()

    status = update_snippet_in_db(
        id=snippet_id,
        title=request_obj.title,
        code=request_obj.code
    )
    is_object_found = status!="Snippet not found!"
    if is_object_found:
        response_serializer = CreateSnippetResponseSerializer(status)
        return Response(response_serializer.data)
    return Response(status)

@api_view(['DELETE'])
def delete_snippet(request,snippet_id):
    msg = delete_snippet_in_db(
        id=snippet_id
    )

    return Response(msg)


@api_view(['GET'])
def get_snippet(request,snippet_id):
    status = get_snippet_in_db(id=snippet_id)
    is_snippet_found = status != "Snippet DoesNotExist"
    if is_snippet_found:
        response_serializer = CreateSnippetResponseSerializer(status)
        return Response(response_serializer.data)
    return Response(status)

@api_view(['GET'])
def get_list_of_snippets(request):
    snippets = Snippet.objects.all().order_by('-id')
    response_serializer = CreateSnippetResponseSerializer(snippets,many=True)
    return Response(response_serializer.data)
