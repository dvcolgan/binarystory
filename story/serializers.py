from rest_framework import serializers
from story.models import StoryNode


class StoryNodeSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField('get_image_url')

    def get_image_url(self, obj):
        try:
            return obj.image.url.replace('client/assets', '')
        except:
            return None

    class Meta:
        model = StoryNode
