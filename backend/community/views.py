import requests
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import (
    api_view,
    authentication_classes,
    permission_classes
)
from rest_framework.status import (
    HTTP_201_CREATED,
    HTTP_403_FORBIDDEN,
    HTTP_204_NO_CONTENT
)
from rest_framework.permissions import IsAuthenticated

from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from .models import Review, Comment
from .serializers import ReviewSerializer, CommentSerializer
from .forms import CommentForm

@api_view(['GET', 'POST'])
@authentication_classes([JSONWebTokenAuthentication]) # token이 유효한지 검사
@permission_classes([IsAuthenticated]) # 인증 확인
def review_list_create(request):
    if request.method == 'GET':
        reviews = Review.objects.all()
        serializer = ReviewSerializer(reviews, many=True)
        # HTML => JSON
        return Response(serializer.data)
    else:
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data, status=HTTP_201_CREATED)


@api_view(['PUT', 'DELETE'])
@authentication_classes([JSONWebTokenAuthentication]) # token이 유효한지 검사
@permission_classes([IsAuthenticated]) # 인증 확인
def review_update_delete(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    
    if review.user != request.user:
        return Response({ 'detail': '권한이 없습니다.'}, status=HTTP_403_FORBIDDEN)

    if request.method == 'PUT':
        serializer = ReviewSerializer(review, data=request.data)
    
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            
            return Response(serializer.data)
    else:
        
        review.delete()
        return Response({ 'id': review_id })


@api_view(['GET', 'POST'])
@authentication_classes([JSONWebTokenAuthentication]) # token이 유효한지 검사
@permission_classes([IsAuthenticated]) # 인증 확인
def comment_list_create(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    
    if request.method == 'POST':
        review, created = Review.objects.get_or_create(id=review_id)
        comment = Comment(content=request.data.get('content'), review=review, user=request.user)
        comment.save()
        serializer = CommentSerializer(comment)
        return Response(serializer.data, status=HTTP_201_CREATED)
    else:
        comments = Comment.objects.filter(review_id=review_id)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)


@api_view(['GET', 'DELETE'])
@authentication_classes([JSONWebTokenAuthentication]) # token이 유효한지 검사
@permission_classes([IsAuthenticated]) # 인증 확인
def comment_update_delete(request, review_id, comment_id):
    
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.method == 'GET':
        serializer = CommentSerializer(comment)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        if request.user == comment.user:
        
            comment.delete()
            return Response(status=HTTP_204_NO_CONTENT)