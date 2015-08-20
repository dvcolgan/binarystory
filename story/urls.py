from django.conf.urls import patterns, url
from story import views


urlpatterns = patterns('story.views',
    url(
        r'^story-node/(?P<pk>\d+)/$',
        views.StoryNodeRetrieveAPIView.as_view(),
        name='api_storynode_retrieve'
    ),
    url(
        r'^story-node/images/$',
        views.AllImagesAPIView.as_view(),
        name='api_storynode_images'
    ),
)
