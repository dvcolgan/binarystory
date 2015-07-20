from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^api/story/', include('story.urls')),
    url(r'^api/admin/', include(admin.site.urls)),
]
