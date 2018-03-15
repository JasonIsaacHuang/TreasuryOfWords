from django import forms
from .models import Synonym


class QueryForm(forms.ModelForm):

	query = forms.CharField(label='')

	class Meta:
		model = Synonym
		fields = ['query']