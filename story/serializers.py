from rest_framework import serializers
from story.models import StoryNode


def get_url_or_None(file):
    try:
        return file.url.replace('client/assets', '')
    except:
        return None


class StoryNodeSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField('get_image_url')
    voiceover_ogg = serializers.SerializerMethodField('get_voiceover_ogg_url')
    voiceover_mp3 = serializers.SerializerMethodField('get_voiceover_mp3_url')

    def get_image_url(self, obj):
        return get_url_or_None(obj.image)

    def get_voiceover_ogg_url(self, obj):
        return get_url_or_None(obj.voiceover_ogg)

    def get_voiceover_mp3_url(self, obj):
        return get_url_or_None(obj.voiceover_mp3)

    class Meta:
        model = StoryNode
