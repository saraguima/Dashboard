from django import forms

class fUploadFileForm(forms.Form):
    file = forms.FileField()