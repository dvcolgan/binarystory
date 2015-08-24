from django.db import models


class StoryNode(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()

    voiceover_mp3 = models.FileField(upload_to='client/assets/story-voiceovers-mp3', blank=True)
    voiceover_ogg = models.FileField(upload_to='client/assets/story-voiceovers-ogg', blank=True)

    image = models.ImageField(upload_to='client/assets/story-images/', blank=True)
    choice_a_label = models.CharField(max_length=255, blank=True)
    choice_a = models.OneToOneField('self', related_name='parent_a', null=True, blank=True)
    choice_b_label = models.CharField(max_length=255, blank=True)
    choice_b = models.OneToOneField('self', related_name='parent_b', null=True, blank=True)

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['id']
