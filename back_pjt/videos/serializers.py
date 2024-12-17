from rest_framework import serializers

from .models import Video, Producer, Channel, VideoArticle

# 영상 목록 조회
class VideoListSerializer(serializers.ModelSerializer):
    class Meta:
        model=Video
        fields=('__all__')

# 영상 게시글 생성
class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model=VideoArticle
        fields=('video_article_title','video_article_content', 'video_channel', 'video_producer')