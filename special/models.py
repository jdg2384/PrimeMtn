from django.db import models

class Enter(models.Model):
    urlone = models.CharField(max_length = 450)
    urltwo = models.CharField(max_length = 450)
    urlthere = models.CharField(max_length = 450)

    def __unicode__(self):
        return self.urlone
