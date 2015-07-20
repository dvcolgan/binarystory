from django.contrib import admin
from story.models import StoryNode

class StoryNodeAdmin(admin.ModelAdmin):
    list_display = ('id', 'text', 'choice_a_label', 'choice_b_label', 'get_a_id', 'get_b_id')

    def get_a_id(self, obj):
        if obj.choice_a is not None:
            return obj.choice_a.id
        else:
            return None
    def get_b_id(self, obj):
        if obj.choice_b is not None:
            return obj.choice_b.id
        else:
            return None
    get_a_id.short_description = 'Choice a id'
    get_b_id.short_description = 'Choice b id'


admin.site.register(StoryNode, StoryNodeAdmin)
