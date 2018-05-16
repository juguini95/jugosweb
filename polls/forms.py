from django import forms
from polls.models import Document
#SUBIR DOCUMENTO Y DESCRIPCION
class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('description', 'document', )