from django.db import models


class StoryNode(models.Model):
    text = models.TextField()
    choice_a_label = models.CharField(max_length=255)
    choice_a = models.OneToOneField('self', related_name='parent_a', null=True, blank=True)
    choice_b_label = models.CharField(max_length=255)
    choice_b = models.OneToOneField('self', related_name='parent_b', null=True, blank=True)

    def __unicode__(self):
        return self.text

    class Meta:
        ordering = ['id']
