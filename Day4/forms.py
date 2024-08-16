from django import forms
class InputForm(forms.Form):
    firstname = forms.CharField(label='Name', max_length=100)
    lastname = forms.CharField(label='Surname', max_length=100)
    roll_no = forms.IntegerField(label='Roll No')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
