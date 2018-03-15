from django.views.generic.edit import FormView
from django.views.generic.list import ListView
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


class SynonymView(ListView):
	model = Synonym
	template_name = 'synonym.html'
