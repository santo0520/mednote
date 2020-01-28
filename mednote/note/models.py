from django.db import models

# Create your models here.
class NoteText(models.Model):
    raw_text = models.TextField(max_length=3000,default="type in text to convert")
    coverted_text = models.TextField(max_length=3000,default="type in text to convert")
    pub_date = models.DateTimeField()


class AbbreviationList(models.Model):
    user = models.CharField(max_length=200)
    def __str__(self):
        return self.user




class Abbreviation(models.Model):
    abbreviation_list = models.ForeignKey(AbbreviationList, on_delete=models.CASCADE,default=AbbreviationList.objects.filter(user="sanders")[0])
    abbreviation = models.CharField(max_length=200, unique=True)
    full_form = models.CharField(max_length=400)
    def __str__(self):
        return self.abbreviation


