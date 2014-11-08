from django import forms
from gas_up.forms import BootstrapTextInput, BootstrapTextArea
from .models import Comment, SubComment

class SearchForm(forms.Form):
     search = forms.CharField(widget=BootstrapTextInput)

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        widgets = {
                'user': forms.HiddenInput,
                'restaurant': forms.HiddenInput,
                'comment': BootstrapTextArea,
                }

class SubCommentForm(forms.ModelForm):
    class Meta:
        model = SubComment
        widgets = {
                'user': forms.HiddenInput,
                'parent': forms.HiddenInput,
                'comment': BootstrapTextArea,
                }
