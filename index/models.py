from django.db import models

# Create your models here.
class Topic(models.Model):
    top_name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.top_name

class Webpage(models.Model):
    # django > 2.0 takes 2 params : models.ForeignKey('Category', on_delete=models.PROTECT)
    topic = models.ForeignKey(Topic, on_delete=models.PROTECT)
    name = models.CharField(max_length=50, unique=True)
    url = models.URLField(unique=True)

    def __str__(self):
        return self.name

class AccessRecord(models.Model):
    # django > 2.0 takes 2 params : models.ForeignKey('Category', on_delete=models.PROTECT)
    name = models.ForeignKey(Webpage, on_delete=models.PROTECT)
    date = models.DateField()

    def __str__(self):
        return str(self.date)