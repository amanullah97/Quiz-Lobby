from django import forms
from django.forms.widgets import RadioSelect
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Contact, Applicants, Student, Course



class QuestionForm(forms.Form):
    def __init__(self, question, *args, **kwargs):
        super(QuestionForm, self).__init__(*args, **kwargs)
        choice_list = [x for x in question.get_answers_list()]
        self.fields["answers"] = forms.ChoiceField(choices=choice_list, widget=RadioSelect)

class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=50, required=True, help_text='make a unique username.')
    first_name = forms.CharField(max_length=50, required=True, help_text='Optional.')
    last_name = forms.CharField(max_length=50, required=True, help_text='Optional.')
    email = forms.EmailField(max_length=255, help_text='Required. Inform a valid email address.')
    password1 = forms.CharField(widget=forms.PasswordInput, required=True)
    password2 = forms.CharField(widget=forms.PasswordInput, required=True)


    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Email already exists!")
        return email

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords do not match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user



class ContactForm(forms.ModelForm):
    name_widgets = forms.TextInput(
        attrs={
            'placeholder': 'Your Name',
            'class': 'form-control',
            'id': 'name',
            'data-rule': 'minlen:4',
            'data - msg': 'Please enter at least 4 chars'


        }
    )

    email_widgets = forms.EmailInput(
        attrs={
            'placeholder': 'Your Email',
            'class': 'form-control',
            'id': 'email',
            'data-rule': 'email',
            'data - msg': 'Please enter Valid email!'

        }
    )

    subject_widgets = forms.TextInput(
        attrs={
            'placeholder': 'Your Subject',
            'class': 'form-control',
            'id': 'subject',

        }
    )

    question_widgets = forms.Textarea(
        attrs={
            'placeholder': 'Message',
            'class': 'form-control',
            'id': 'message',
            'data-rule': 'required',
            'data - msg': 'Please write something for us',
            'rows': '5',

        }
    )

    full_name = forms.CharField(widget=name_widgets, required=True)
    email = forms.EmailField(widget=email_widgets, required=True)
    subject = forms.CharField(widget=subject_widgets, required=False)
    question = forms.CharField(widget=question_widgets, required=True)

    class Meta:
        model = Contact
        fields = ('full_name' , 'email' , 'subject', 'question')


class ApplicationForm(forms.ModelForm):
    full_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter-Full-Name',
                                                              'class': 'form-control'}), required=True)
    contact_no = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': 'Enter-Contact-Number',
                                                                  'class': 'form-control'}), required=True)
    email = forms.CharField(widget=forms.EmailInput(attrs={'placeholder': 'Email',
                                                           'class': 'form-control'}), required=True)
    cv = forms.FileField(widget=forms.FileInput(attrs={'class': 'form-control',
                                                         'id':'formFile'}),)
    course = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter Course You Want to Teach!',
                                                    'class': 'form-control'}), required=True)


    class Meta:
        model = Applicants
        fields = ('full_name', 'contact_no', 'email', 'course','cv')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if Applicants.objects.filter(email=email).exists():
            raise forms.ValidationError("Email already exists!")
        return email

class Course_Selection(forms.ModelForm):
    select_courses = forms.Select(attrs={
        'class': 'form-control',
        'name': 'course_rel',
    })
    course_rel = forms.ChoiceField(choices=[(obj.pk, obj.course_name) for obj in Course.objects.all()],
                                   widget=select_courses, help_text="Select Courses!")
    class Meta:
        model = Student
        fields = ('course_rel',)

