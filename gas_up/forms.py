from django import forms

class BootstrapWidget(object):
    def __init__(self, attrs=None, **kwargs):
        if not attrs:
            attrs = {'class':'form-control'}
        else:
            if not attrs.get('class'):
                attrs['class'] = 'form-control'

        super(BootstrapWidget, self).__init__(attrs, **kwargs)

class BootstrapTextInput(BootstrapWidget,forms.TextInput):
    pass

class BootstrapTextArea(BootstrapWidget,forms.Textarea):
    pass
