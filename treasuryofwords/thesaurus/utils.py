import numpy as np
from PIL import Image, ImageDraw, ImageFont
from treasuryofwords.settings import APP_NAME
from wordcloud import WordCloud, STOPWORDS
from treasuryofwords.settings import BASE_DIR
from thesaurus.models import Word
import matplotlib.pyplot as plt


def stringify_all_words():
	string = ''
	for word in Word.objects.all():
		string += str(word) + ' '
	return string


def grey_color_func(word, font_size, position, orientation, random_state=None,
                    **kwargs):
	return "hsl(0, 0%%, %d%%)" % 0


def generate_mask():
	text = APP_NAME
	font_name = 'Impact.ttf'
	font_size = 700
	font = ImageFont.truetype(font_name, font_size)

	# background = (248, 249, 250)
	background = (255, 255, 255)
	text_colour = (0, 0, 0)
	text_width, text_height = _text_size(text, font)

	img_width, img_height = (text_width, text_height)

	img = Image.new("RGBA", (img_width, img_height), background)
	draw = ImageDraw.Draw(img)
	draw.text((0, 0), text, text_colour, font=font)
	draw = ImageDraw.Draw(img)
	img.save("assets/mask.png")


def _text_size(text, font):
	img = Image.new("RGBA", (1, 1))
	draw = ImageDraw.Draw(img)
	return draw.textsize(text, font)


def generate_word_cloud():
	text = stringify_all_words()
	background = (233, 236, 239)
	# text = "Hello World"
	mask = np.array(Image.open(BASE_DIR + '/assets/mask.png'))

	word_cloud = WordCloud(background_color=background, mask=mask)
	word_cloud.generate(text)

	default_colours = word_cloud.to_array()

	plt.imshow(word_cloud.recolor(color_func=grey_color_func, random_state=3),
	           interpolation="bilinear")
	word_cloud.to_file(BASE_DIR + '/assets/word_cloud.png')
