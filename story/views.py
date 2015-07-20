from django.shortcuts import render
from rest_framework.generics import RetrieveAPIView
from story.serializers import StoryNodeSerializer
from story.models import StoryNode


class StoryNodeRetrieveAPIView(RetrieveAPIView):
    queryset = StoryNode.objects.all()
    serializer_class = StoryNodeSerializer
