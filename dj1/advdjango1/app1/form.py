from django import forms
from .models import Student


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'rollno', 'marks']

    def clean_marks(self):
            marks=self.cleaned_data.get('marks')
            if marks<0 or marks>100:
                raise forms.ValidationError('Marks should be between 0 and 100')
            return marks
