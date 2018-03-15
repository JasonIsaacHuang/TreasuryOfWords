from django import forms
from .models import Synonym


class QueryForm(forms.ModelForm):
	query = forms.CharField(
		label='',
		required=True,
		widget=forms.TextInput(
			attrs={
				'class': 'search-query form-control',
				'placeholder': 'Search'
			}
		)
	)

	class Meta:
		model = Synonym
		fields = ['query']
