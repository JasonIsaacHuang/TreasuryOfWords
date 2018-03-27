import matplotlib
matplotlib.use('Agg')
from threading import Thread
import numpy as np
from PIL import Image, ImageFont, ImageDraw
from django.db import models
from matplotlib import pyplot as plt
from thesaurus.utils import concatenate_all_words
from treasuryofwords.settings import BASE_DIR, APP_NAME
from wordcloud import WordCloud


class Word(models.Model):

	word = models.CharField(max_length=30, unique=True)

	def __str__(self):
		return self.word

	def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
		self.word = self.word.lower()
		super(Word, self).save(force_insert, force_update, using, update_fields)
		thread = WordCloudThread()
		thread.start()


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
		self.generate_mask()
		self.generate_word_cloud()

	def generate_mask(self):
		text = APP_NAME
		font_name = 'Impact.ttf'
		font_size = 700
		font = ImageFont.truetype(font_name, font_size)

		background = (255, 255, 255)
		text_colour = (0, 0, 0)
		text_width, text_height = self._text_size(text, font)

		img_width, img_height = (text_width, text_height)

		img = Image.new("RGBA", (img_width, img_height), background)
		draw = ImageDraw.Draw(img)
		draw.text((0, 0), text, text_colour, font=font)
		draw = ImageDraw.Draw(img)
		img.save("assets/mask.png")

	def generate_word_cloud(self):
		text = concatenate_all_words()
		background = (233, 236, 239)
		mask = np.array(Image.open(BASE_DIR + '/assets/mask.png'))

		word_cloud = WordCloud(background_color=background, mask=mask)
		word_cloud.generate(text)

		default_colours = word_cloud.to_array()

		plt.imshow(word_cloud.recolor(color_func=self.grey_color_func, random_state=3),
		           interpolation="bilinear")
		word_cloud.to_file(BASE_DIR + '/assets/word_cloud.png')

	def grey_color_func(self, word, font_size, position, orientation, random_state=None, **kwargs):
		return "hsl(0, 0%%, %d%%)" % 0

	def _text_size(self, text, font):
		img = Image.new("RGBA", (1, 1))
		draw = ImageDraw.Draw(img)
		return draw.textsize(text, font)
