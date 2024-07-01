from django import forms
from .models import Connection, Proto

class ConnectionForm(forms.ModelForm):
    class Meta:
        model = Connection
        fields = ['hostname', 'port', 'proto']
        widgets = {
            'port': forms.NumberInput(attrs={'min': 1, 'max': 65535})
        }

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        self.fields['proto'].queryset = Proto.objects.all()

    def save(self, commit=True):
        instance = super().save(commit=False)
        if self.user:
            instance.user = self.user
        if commit:
            instance.save()
        return instance