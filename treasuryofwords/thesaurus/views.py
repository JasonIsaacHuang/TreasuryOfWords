from django.shortcuts import get_object_or_404
from django.views.generic import ListView
from django.views.generic.edit import FormView, FormMixin
from rest_framework import viewsets
from .forms import QueryForm
from .models import Word, Synonym
from .serializer import WordSerializer, SynonymSerializer
from treasuryofwords.settings import APP_NAME, WORDCLOUD_LOGO


class WordViewSet(viewsets.ReadOnlyModelViewSet):
	queryset = Word.objects.all()
	serializer_class = WordSerializer


class SynonymViewSet(viewsets.ReadOnlyModelViewSet):
	queryset = Synonym.objects.all()
	serializer_class = SynonymSerializer


class QueryView(FormView):
	form_class = QueryForm
	template_name = 'query.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['app_name'] = APP_NAME
		context['wordcloud'] = WORDCLOUD_LOGO
		context['word_count'] = Word.objects.count()
		return context


class SynonymView(ListView, FormMixin):
	form_class = QueryForm
	model = Synonym
	template_name = 'synonym.html'

	def get_query(self):
		return self.request.GET.get('query').lower()

	def get_context_data(self, *, object_list=None, **kwargs):
		context = super().get_context_data(object_list=object_list, **kwargs)
		context['app_name'] = APP_NAME
		context['query'] = self.get_query()
		return context

	def get_queryset(self):
		word = get_object_or_404(Word, word=self.get_query())
		return Synonym.objects.filter(synonym=word)

class FourZeroFour(FormView):
	form_class = QueryForm
	template_name = '404.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['app_name'] = APP_NAME
		return context
