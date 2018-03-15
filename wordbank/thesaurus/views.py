from django.views.generic.edit import FormView
from rest_framework import viewsets
from .forms import QueryForm
from .models import Word, Synonym
from .serializer import WordSerializer, SynonymSerializer


class WordViewSet(viewsets.ReadOnlyModelViewSet):

	queryset = Word.objects.all()
	serializer_class = WordSerializer


class SynonymViewSet(viewsets.ReadOnlyModelViewSet):

	queryset = Synonym.objects.all()
	serializer_class = SynonymSerializer


class QueryView(FormView):
	form_class = QueryForm
	template_name = 'query.html'