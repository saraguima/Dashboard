from django import forms

class formularios_upload(forms.Form):
    file = forms.FileField()