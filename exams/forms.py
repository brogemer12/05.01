from django import forms
from django.contrib.auth.models import Group, User
from .models import Exam

class ExamForm(forms.ModelForm):
    class Meta:
        model = Exam
        fields = ['title', 'date', 'image', 'users', 'groups', 'is_public']
        widgets = {
            'date': forms.DateTimeInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
            'users': forms.CheckboxSelectMultiple(attrs={'class': 'checkbox-list'}),
            'groups': forms.CheckboxSelectMultiple(attrs={'class': 'checkbox-list'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Ensure the date field accepts the datetime-local format
        self.fields['date'].input_formats = ('%Y-%m-%dT%H:%M',)

class GroupForm(forms.ModelForm):
    users = forms.ModelMultipleChoiceField(
        queryset=User.objects.all(),
        required=False,
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'checkbox-list'}),
        label='Пользователи'
    )

    class Meta:
        model = Group
        fields = ['name']
        labels = {
            'name': 'Название группы'
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance.pk:
            self.fields['users'].initial = self.instance.user_set.all()

    def save(self, commit=True):
        group = super().save(commit=commit)
        if commit:
            group.user_set.set(self.cleaned_data['users'])
        return group
