from django import forms
from gas_up.forms import BootstrapTextInput

class SearchForm(forms.Form):
     search = forms.CharField(widget=BootstrapTextInput)
