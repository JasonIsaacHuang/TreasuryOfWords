from threading import Thread
from thesaurus.utils import generate_mask, generate_word_cloud

class WordCloudThread(Thread):

	def run(self):
		generate_mask()
		generate_word_cloud()