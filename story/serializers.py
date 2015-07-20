from rest_framework import serializers
from story.models import StoryNode


class StoryNodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = StoryNode
