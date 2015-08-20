from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import RetrieveAPIView
from story.serializers import StoryNodeSerializer
from story.models import StoryNode


class StoryNodeRetrieveAPIView(RetrieveAPIView):
    queryset = StoryNode.objects.all()
    serializer_class = StoryNodeSerializer


class AllImagesAPIView(APIView):
    def get(self, request, *args, **kwargs):
        images = [
            image.replace('client/assets', '')
            for image in StoryNode.objects.exclude(
                image=''
            ).values_list('image', flat=True)
        ]
        return Response(images)
