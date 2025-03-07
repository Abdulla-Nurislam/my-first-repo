from django import forms
from .models import Todo
from django.utils import timezone
from datetime import datetime

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['title', 'description', 'due_date']
        widgets = {
            'due_date': forms.DateTimeInput(
                attrs={'type': 'datetime-local', 'min': datetime.now().strftime('%Y-%m-%dT%H:%M')},
            ),
            'description': forms.Textarea(attrs={'rows': 4}),
        }

    def clean_due_date(self):
        due_date = self.cleaned_data.get('due_date')
        now = timezone.now()
        
        if due_date and due_date < now:
            raise forms.ValidationError('Нельзя создать задачу с датой в прошлом!')
        
        return due_date 