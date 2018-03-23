from threading import Thread

from django.db import models

from thesaurus.utils import generate_mask, generate_word_cloud


class Word(models.Model):

	word = models.CharField(max_length=30, unique=True)

	def __str__(self):
		return self.word

	def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
		self.word = self.word.lower()
		super(Word, self).save(force_insert, force_update, using, update_fields)
		# thread = WordCloudThread()
		# thread.start()


class Synonym(models.Model):

	synonym = models.ManyToManyField(Word)

	def __str__(self):
		string = ''
		for syn in self.synonym.all().order_by('word'):
			string += str(syn) + ', '
		string = string.rstrip(', ')
		return string


class WordCloudThread(Thread):

	def run(self):
		generate_mask()
		generate_word_cloud()