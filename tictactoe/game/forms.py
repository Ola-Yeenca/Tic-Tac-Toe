from django import forms

class MoveForm(forms.Form):
    position = forms.IntegerField()
