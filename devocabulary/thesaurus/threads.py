import matplotlib
matplotlib.use('Agg')
from threading import Thread
import numpy as np
from PIL import Image, ImageFont, ImageDraw
from matplotlib import pyplot as plt
from thesaurus.utils import concatenate_all_words
from devocabulary.settings import BASE_DIR, APP_NAME, WORDCLOUD_FONT_PATH, WORDCLOUD_SIZE, WORDCLOUD_MASK_PATH, WORDCLOUD_PATH
from wordcloud import WordCloud


class WordCloudThread(Thread):

	def __init__(self):
		super(WordCloudThread, self).__init__()
		self.text = APP_NAME
		self.font_path=WORDCLOUD_FONT_PATH
		self.font_size=WORDCLOUD_SIZE
		self.mask_path=WORDCLOUD_MASK_PATH
		self.word_cloud_path=WORDCLOUD_PATH

	def run(self):
		self.generate_mask()
		self.generate_word_cloud()

	def generate_mask(self):
		font = ImageFont.truetype(self.font_path, self.font_size)

		background = (255, 255, 255)
		text_colour = (0, 0, 0)
		text_width, text_height = self._text_size(self.text, font)

		img_width, img_height = (text_width, text_height)

		img = Image.new("RGBA", (img_width, img_height), background)
		draw = ImageDraw.Draw(img)
		draw.text((0, 0), self.text, text_colour, font=font)
		draw = ImageDraw.Draw(img)
		img.save(self.mask_path)

	def generate_word_cloud(self):
		text = concatenate_all_words()
		background = (233, 236, 239)
		mask = np.array(Image.open(self.mask_path))

		word_cloud = WordCloud(background_color=background, mask=mask)
		word_cloud.generate(text)

		default_colours = word_cloud.to_array()

		plt.imshow(word_cloud.recolor(color_func=self.grey_color_func, random_state=3),
		           interpolation="bilinear")
		word_cloud.to_file(self.word_cloud_path)

	@staticmethod
	def grey_color_func(word, font_size, position, orientation, random_state=None, **kwargs):
		return "hsl(0, 0%%, %d%%)" % 0

	@staticmethod
	def _text_size(text, font):
		img = Image.new("RGBA", (1, 1))
		draw = ImageDraw.Draw(img)
		return draw.textsize(text, font)
