from django.db import models


class Word(models.Model):

	word = models.CharField(max_length=30, unique=True)

	def __str__(self):
		return self.word

	def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
		self.word = self.word.lower()
		super(Word, self).save(force_insert, force_update, using, update_fields)


class Synonym(models.Model):

	synonym = models.ManyToManyField(Word)

	def __str__(self):
		string = ''
		for syn in self.synonym.all().order_by('word'):
			string += str(syn) + ', '
		string = string.rstrip(', ')
		return string