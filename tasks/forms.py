from django import forms

class TareaForm(forms.Form):
    tarea = forms.CharField(
        max_length= 100,
        label="",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'id': 'prueba',
            'placeholder': "Tarea",
            'name':'tarea',
        })
        )