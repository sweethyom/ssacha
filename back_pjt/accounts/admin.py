from django.contrib import admin
from videos.models import VideoArticle, Producer, Channel
# Register your models here.

class VideoArticleAdmin(admin.ModelAdmin):
    fields = ('video_article_title', 'video_article_content', 'video_producer')  # Do not include producer_channel here
    list_display = ('video_article_title', 'get_producer_channel', 'video_producer')  # Use a method to display producer_channel
    search_fields = ('video_article_title',)

    def get_producer_channel(self, obj):
        return obj.video_producer.producer_channel.channel_name  # Adjust based on your Channel model
    get_producer_channel.short_description = 'Producer Channel'  # Column name in admin

admin.site.register(VideoArticle, VideoArticleAdmin)
admin.site.register(Producer)
admin.site.register(Channel)