import matplotlib
matplotlib.use('Agg')
from threading import Thread
import numpy as np
from PIL import Image
from django.db import models
from matplotlib import pyplot as plt
from thesaurus.utils import generate_mask, stringify_all_words, grey_color_func
from treasuryofwords.settings import BASE_DIR
from wordcloud import WordCloud


class Word(models.Model):

	word = models.CharField(max_length=30, unique=True)

	def __str__(self):
		return self.word

	def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
		self.word = self.word.lower()
		super(Word, self).save(force_insert, force_update, using, update_fields)
		# thread = WordCloudThread()
		# thread.start()

	def generate_word_cloud(self):
		text = stringify_all_words()
		background = (233, 236, 239)
		mask = np.array(Image.open(BASE_DIR + '/assets/mask.png'))

		word_cloud = WordCloud(background_color=background, mask=mask)
		word_cloud.generate(text)

		default_colours = word_cloud.to_array()

		plt.imshow(word_cloud.recolor(color_func=grey_color_func, random_state=3),
		           interpolation="bilinear")
		word_cloud.to_file(BASE_DIR + '/assets/word_cloud.png')


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


