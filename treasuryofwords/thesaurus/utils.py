import thesaurus.models


def concatenate_all_words():
	string = ''
	for word in thesaurus.models.Word.objects.all():
		string += str(word) + ' '
	return string


