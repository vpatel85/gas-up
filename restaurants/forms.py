from django import forms
from gas_up.forms import BootstrapTextInput, BootstrapTextArea
from .models import Comment, SubComment, UserProfile
from django.contrib.auth.models import User
from django.contrib.admin.widgets import FilteredSelectMultiple

class SearchForm(forms.Form):
     search = forms.CharField(widget=BootstrapTextInput, label='Search by address')

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

class UserProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(UserProfileForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True
        self.fields['email'].required = True

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
        widgets = {
                'first_name': BootstrapTextInput,
                'last_name': BootstrapTextInput,
                'email': BootstrapTextInput,
                }
