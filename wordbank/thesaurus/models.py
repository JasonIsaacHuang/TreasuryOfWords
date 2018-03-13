from django.db import models


# Create your models here.

class Word(models.Model):

	word = models.CharField(max_length=30)


class Synonym(models.Model):

	synonym = models.ManyToManyField(Word)
