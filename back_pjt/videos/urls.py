from django.urls import path

from . import views

urlpatterns = [
    path('videos/', views.video_article_list),  # 영상 게시글 목록 조회 및 생성
    path('videos/<int:video_article_pk>', views.video_article_detail) # 영상 게시글 상세조회 및 수정 및 삭제
]
