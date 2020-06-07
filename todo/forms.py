from django import forms
from datetime import datetime, timedelta, tzinfo

class DateInput(forms.DateInput):
    input_type='date'

class TodoForm(forms.Form):
    text = forms.CharField(max_length=200,
        widget=forms.TextInput(
            attrs={'class' : 'column form-control', 'placeholder' : 'add task', 'aria-label' : 'Todo', 'aria-describedby' : 'add-btn'}))

    priority = forms.CharField(max_length=8,
        widget=forms.TextInput(
            attrs={'class' : 'column form-control', 'placeholder' : 'Enter priority' , 'aria-describedby' : 'add-btn'}))

    type = forms.CharField(max_length=20,
        widget=forms.TextInput(
            attrs={'class' : 'column form-control', 'placeholder' : 'type:-school/home..' , 'aria-describedby' : 'add-btn'}))

    duedate = forms.DateTimeField(widget=DateInput)
    #duetime = forms.DateTimeField(widget=DateTimeInput)
