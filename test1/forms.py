from django import forms
from test1.models import Messages

class MessagesForm(forms.ModelForm):
    class Meta:
        fields = ('chat','message',)
        model = Messages