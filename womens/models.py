from django.db import models

class Wost(models.Model):
    logo = models.ImageField(upload_to='post')
    name = models.CharField(max_length = 150)
    merchant = models.CharField(max_length = 150)
    price = models.CharField(max_length = 150)
    discount = models.CharField(max_length = 150)
    description = models.TextField(max_length = 1500)
    youtube = models.CharField(max_length = 200)
    share = models.CharField(max_length = 200)
    url = models.CharField(max_length = 450)

    def __unicode__(self):
        return self.name
