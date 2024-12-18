from django.db import models

# Create your models here.
# 영상 관리
class Video(models.Model):
    video_name = models.CharField(max_length=100) # 영상이름 # varChar
    video_path = models.CharField(max_length=255) # 영상 경로 # varChar
    video_created_at = models.DateField(auto_now_add=True) # 영상 생성날짜
    video_script = models.BooleanField(default=False) # 영상 자막 여부 # boolean
    video_channel = models.CharField(max_length=30) # 영상 언론사
    video_thumbnail_path = models.CharField(max_length=255) # 썸네일 이미지 경로
    video_status = models.CharField(max_length=30) # 영상 인코딩 상태
    video_producer = models.ForeignKey('Producer', max_length=30, on_delete=models.CASCADE) # 영상 제작사 이름
    # Ref: video.video_producer > producer.pk

# 스트리밍
class Streaming(models.Model):
    streaming_name = models.CharField(max_length=100) # 스트리밍 이름
    streaming_path = models.CharField(max_length=255) # 스트리밍 경로
    streaming_created_at = models.DateField(auto_now_add=True) # 비디오 생성날짜
    streaming_channel = models.CharField(max_length=30) # 스트리밍 언론사
    streaming_description = models.TextField() # 스트리밍 설명
    streaming_is_live = models.BooleanField(default=False) # 스트리밍 여부
    streaming_producer = models.CharField(max_length=30) # 스트리밍 제작자 이름

    
# 영상 게시글
class VideoArticle(models.Model):
    video_pk = models.ForeignKey(Video, on_delete=models.CASCADE) # 영상 코드
    # Ref: video_article.video_pk > video.pk
    video_article_title = models.CharField(max_length=100) # 게시물 제목
    video_article_deleted = models.BooleanField(default=False) # 게시물 삭제
    video_article_updated_at = models.DateField(auto_now=True) # 게시물 수정
    video_article_created_at = models.DateField(auto_now_add=True) # 게시물 생성날짜
    video_article_content = models.CharField(max_length=255) # 게시물 내용
    # video_channel = models.CharField(max_length=30) # 영상 언론사 -> 프로듀서 명 선택하면 자동으로 따라오도록? 아니면 반대로 해야하려나?
    view_count = models.IntegerField(default=0) # 조회수 # default=0 ?

    video_producer = models.ForeignKey('Producer',max_length=30, on_delete=models.CASCADE) # 영상 제작자 이름

    def increment_view_count(self):
       self.view_count += 1
       self.save()

    @property
    def video_channel(self):
        return self.video_producer.producer_channel


# 스트리밍 게시글
class StreamingArticle(models.Model):
    streaming_pk = models.OneToOneField(Streaming, on_delete=models.CASCADE) # 스트리밍 코드
    # Ref: streaming_article.streaming_pk - streaming.pk
    streaming_article_title = models.CharField(max_length=100) # 스트리밍 게시글 제목
    streaming_article_deleted = models.BooleanField(default=False) # 스트리밍 게시글 삭제
    streaming_article_updated_at = models.DateField(auto_now=True) # 스트리밍 게시글 수정
    streaming_article_created_at = models.DateField(auto_now_add=True) # 스트리밍 게시글 생성 날짜
    streaming_article_content = models.CharField(max_length=255) # 스트리밍 게시글 내용 # TextField ?
    streaming_article_channel = models.CharField(max_length=30) # 스트리밍 게시글 언론사
    view_count = models.IntegerField() # 조회수 # default=0 ?
    streaming_article_producer = models.ForeignKey('Producer', max_length=30, on_delete=models.CASCADE) # 영상 제작자 이름
    # Ref: streaming_article.streaming_article_producer > producer.pk


# 영상 게시글 댓글
class ArticleComment(models.Model):
    article_pk = models.ForeignKey('VideoArticle', on_delete=models.CASCADE) # 게시글 코드
    # Ref: article_comment.article_pk > video_article.pk
    comment_content = models.TextField() # 댓글 내용



# 스트리밍 게시글 댓글
class StreamingArticleComment(models.Model):
    streaming_article = models.ForeignKey('StreamingArticle', on_delete=models.CASCADE) # 스트리밍 게시글 코드
    # Ref: streaming_article_comment.streaming_article_pk > streaming_article.pk
    streaming_comment_content = models.TextField() # 스트리밍 댓글 내용

# 프로듀서
class Producer(models.Model):
    producer_name = models.CharField(max_length=100) # 프로듀서 이름
    producer_channel = models.ForeignKey('Channel',max_length=100, on_delete=models.CASCADE) # 프로듀서 소속 언론사
    # Ref: producer.producer_channel > channel.pk
    def __str__(self):
            # 필드명과 값을 출력하는 방법
            return self.producer_name
    
    # 언론사
class Channel(models.Model):
    channel_name = models.CharField(max_length=100) # 스트리밍 이름

    def __str__(self):
            # 필드명과 값을 출력하는 방법
            return self.channel_name