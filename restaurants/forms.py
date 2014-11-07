from django import forms
from gas_up.forms import BootstrapTextInput
from .models import Comment

class SearchForm(forms.Form):
     search = forms.CharField(widget=BootstrapTextInput)

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        widgets = {
                'user': forms.HiddenInput,
                'restaurant': forms.HiddenInput,
                #'comment': BootstrapTextInput,
                }
