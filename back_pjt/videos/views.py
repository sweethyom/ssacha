from django.shortcuts import get_list_or_404, get_object_or_404, render

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import VideoArticle
from .serializers import VideoListSerializer, VideoSerializer
# Create your views here.

# 영상 게시글 목록 및 생성
@api_view(['GET', 'POST'])
def video_article_list(request):
    # 목록조회
    if request.method == 'GET':
        articles = get_list_or_404(VideoArticle)
        serializer = VideoListSerializer(articles, many=True) 
        return Response(serializer.data)
    
    # 게시글 생성
    elif request.method == 'POST':
        serializer = VideoSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
# 영상 게시글 상세조회 및 수정 및 삭제
@api_view(['GET'])
def video_article_detail(request, video_article_pk):
    article = get_object_or_404(VideoArticle, pk=video_article_pk)
    # 상세조회
    if request.method == 'GET':
        serializer = VideoSerializer(article)
        return Response(serializer.data)
