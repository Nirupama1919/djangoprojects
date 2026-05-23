from django import forms
from datetime import date

DEPARTMENT_CHOICES = [
    ('IT', 'IT'),
    ('CSE', 'CSE'),
    ('ECE', 'ECE'),
    ('EEE', 'EEE'),
    ('MECH', 'MECH'),
]

YEAR_CHOICES = [
    ('1st', '1st'),
    ('2nd', '2nd'),
    ('3rd', '3rd'),
    ('4th', '4th'),
]

STATE_CHOICES = [
    ('Andhra Pradesh', 'Andhra Pradesh'),
    ('Telangana', 'Telangana'),
    ('Karnataka', 'Karnataka'),
    ('Tamil Nadu', 'Tamil Nadu'),
]

class StudentForm(forms.Form):

    full_name = forms.CharField(
        min_length=3,
        widget=forms.TextInput(attrs={'class':'form-control'})
    )

    email = forms.EmailField()

    mobile = forms.CharField(max_length=10)

    dob = forms.DateField(
        widget=forms.DateInput(attrs={'type':'date'})
    )

    gender = forms.ChoiceField(
        choices=[
            ('Male','Male'),
            ('Female','Female'),
            ('Other','Other')
        ],
        widget=forms.RadioSelect
    )

    department = forms.ChoiceField(
        choices=DEPARTMENT_CHOICES
    )

    year = forms.ChoiceField(
        choices=YEAR_CHOICES
    )

    roll_number = forms.CharField()

    address = forms.CharField(
        widget=forms.Textarea
    )

    state = forms.ChoiceField(
        choices=STATE_CHOICES
    )

    pincode = forms.CharField(max_length=6)

    technical_skills = forms.MultipleChoiceField(
        choices=[
            ('Python','Python'),
            ('Java','Java'),
            ('C','C'),
            ('Web Development','Web Development')
        ],
        widget=forms.CheckboxSelectMultiple
    )

    learning_mode = forms.ChoiceField(
        choices=[
            ('Online','Online'),
            ('Offline','Offline'),
            ('Hybrid','Hybrid')
        ],
        widget=forms.RadioSelect
    )

    resume = forms.FileField()

    about = forms.CharField(
        widget=forms.Textarea
    )

    agree = forms.BooleanField()

    def clean_mobile(self):

        mobile = self.cleaned_data['mobile']

        if not mobile.isdigit() or len(mobile) != 10:
            raise forms.ValidationError(
                "Mobile number must contain exactly 10 digits"
            )

        return mobile

    def clean_dob(self):

        dob = self.cleaned_data['dob']

        if dob > date.today():
            raise forms.ValidationError(
                "Date of birth cannot be future date"
            )

        return dob

    def clean_resume(self):

        resume = self.cleaned_data['resume']

        if not resume.name.endswith(('.pdf','.doc','.docx')):
            raise forms.ValidationError(
                "Only PDF or DOC files allowed"
            )

        return resume