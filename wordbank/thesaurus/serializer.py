from rest_framework import serializers
from .models import Word, Synonym


class WordSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Word
		fields = ['word']


class SynonymSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Synonym
		fields = ['synonym']

