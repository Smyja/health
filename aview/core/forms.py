from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=100, help_text='Last Name')
    last_name = forms.CharField(max_length=100, help_text='Last Name')
    address = forms.CharField(max_length=100, help_text='address')
    phonenumber = forms.CharField(
        max_length=100, help_text='Enter Phone number')
    email = forms.EmailField(max_length=150, help_text='Email')
    
    

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update(
        {'placeholder': ('Username')})
        self.fields['email'].widget.attrs.update(
        {'placeholder': ('Email')})
        self.fields['address'].widget.attrs.update(
            {'placeholder': ('Address')})
        self.fields['phonenumber'].widget.attrs.update(
            {'placeholder': ('Phone number')})
        self.fields['first_name'].widget.attrs.update(
            {'placeholder': ('First name')})
        self.fields['last_name'].widget.attrs.update(
            {'placeholder': ('Last name')})




        self.fields['password1'].widget.attrs.update({'placeholder': ('Password')})
        self.fields['password2'].widget.attrs.update({'placeholder': ('Repeat password')})
        self.fields['first_name'].widget.attrs.update({'class': 'log'})
        self.fields['last_name'].widget.attrs.update({'class': 'log'})
        self.fields['email'].widget.attrs.update({'class': 'log'})
        self.fields['phonenumber'].widget.attrs.update({'class': 'log'})
        self.fields['address'].widget.attrs.update({'class': 'log'})
        self.fields['username'].widget.attrs.update({'class': 'log'})
        self.fields['password1'].widget.attrs.update({'class': 'log swiy'})
        self.fields['password2'].widget.attrs.update({'class': 'log swiy'})

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'phonenumber',
                  'email', 'password1', 'password2', 'address')
      # Add this to check if both passwords are matching or not
  
class PatientForm(UserCreationForm):
    first_name = forms.CharField(max_length=100, help_text='First Name')
    last_name = forms.CharField(max_length=100, help_text='Last Name')
    address = forms.CharField(max_length=100, help_text='address')
    next_of_kin = forms.CharField(max_length=100, help_text='Next of kin')
    dob = forms.CharField(max_length=100, help_text='Date of birth')
    state = forms.CharField(max_length=100, help_text='State')
    phonenumber = forms.CharField(
        max_length=100, help_text='Enter Phone number')
    email = forms.EmailField(max_length=150, help_text='Email')
    
    

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update(
        {'placeholder': ('Username')})
        self.fields['email'].widget.attrs.update(
        {'placeholder': ('Email')})
        self.fields['address'].widget.attrs.update(
            {'placeholder': ('Address')})
        self.fields['phonenumber'].widget.attrs.update(
            {'placeholder': ('Phone number')})
        self.fields['first_name'].widget.attrs.update(
            {'placeholder': ('First name')})
        self.fields['last_name'].widget.attrs.update(
            {'placeholder': ('Last name')})
        
        

        self.fields['password1'].widget.attrs.update({'placeholder': ('Password')})
        self.fields['password2'].widget.attrs.update({'placeholder': ('Repeat password')})
        self.fields['dob'].widget.attrs.update({'placeholder': ('Date of birth')})
        self.fields['state'].widget.attrs.update({'placeholder': ('State')})
        self.fields['next_of_kin'].widget.attrs.update({'placeholder': ('Next of kin')})
        self.fields['first_name'].widget.attrs.update({'class': 'log'})
        self.fields['last_name'].widget.attrs.update({'class': 'log'})
        self.fields['email'].widget.attrs.update({'class': 'log'})
        self.fields['phonenumber'].widget.attrs.update({'class': 'log'})
        self.fields['address'].widget.attrs.update({'class': 'log'})
        self.fields['dob'].widget.attrs.update({'class': 'log'})
        self.fields['state'].widget.attrs.update({'class': 'log'})
        self.fields['next_of_kin'].widget.attrs.update({'class': 'log'})
        self.fields['username'].widget.attrs.update({'class': 'log'})
        self.fields['password1'].widget.attrs.update({'class': 'log swiy'})
        self.fields['password2'].widget.attrs.update({'class': 'log swiy'})

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'phonenumber',
                  'email', 'password1', 'password2', 'address','dob','state','next_of_kin')
    def clean(self):
        cleaned_data = super(PatientForm, self).clean()
        password = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')
        if password != password2:
            raise forms.ValidationError('Passwords do not match!')
    
    # Add this to check if the email already exists in your database or not

    def clean_email(self):
        username = self.cleaned_data.get('username')
        email = self.cleaned_data.get('email')
        if email and User.objects.filter(email=email).exclude(username=username).count():
            raise forms.ValidationError('This email is already in use! Try another email.')
        return email
       
     # Add this to check if the username already exists in your database or not     
    def clean_username(self):
        username = self.cleaned_data.get('username')
        email=self.cleaned_data.get('email')
        if username and User.objects.filter(username=username).exclude(email=email).count():
            raise forms.ValidationError('This username has already been taken!')
        return username  
 

class EditProfileForm(UserCreationForm):
    first_name = forms.CharField(max_length=100, help_text='First Name')
    last_name = forms.CharField(max_length=100, help_text='Last Name')
    address = forms.CharField(max_length=100, help_text='address')
    next_of_kin = forms.CharField(max_length=100, help_text='Next of kin')
    dob = forms.CharField(max_length=100, help_text='Date of birth')
    state = forms.CharField(max_length=100, help_text='State')
    phonenumber = forms.CharField(
        max_length=100, help_text='Enter Phone number')
    email = forms.EmailField(max_length=150, help_text='Email')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update(
            {'placeholder': ('Username')})
        self.fields['email'].widget.attrs.update(
            {'placeholder': ('Email')})
        self.fields['address'].widget.attrs.update(
            {'placeholder': ('Address')})
        self.fields['phonenumber'].widget.attrs.update(
            {'placeholder': ('Phone number')})
        self.fields['first_name'].widget.attrs.update(
            {'placeholder': ('First name')})
        self.fields['last_name'].widget.attrs.update(
            {'placeholder': ('Last name')})

        self.fields['password1'].widget.attrs.update(
            {'placeholder': ('Password')})
        self.fields['password2'].widget.attrs.update(
            {'placeholder': ('Repeat password')})
        self.fields['dob'].widget.attrs.update(
            {'placeholder': ('Date of birth')})
        self.fields['state'].widget.attrs.update({'placeholder': ('State')})
        self.fields['next_of_kin'].widget.attrs.update(
            {'placeholder': ('Next of kin')})
        self.fields['first_name'].widget.attrs.update({'class': 'log'})
        self.fields['last_name'].widget.attrs.update({'class': 'log'})
        self.fields['email'].widget.attrs.update({'class': 'log'})
        self.fields['phonenumber'].widget.attrs.update({'class': 'log'})
        self.fields['address'].widget.attrs.update({'class': 'log'})
        self.fields['dob'].widget.attrs.update({'class': 'log'})
        self.fields['state'].widget.attrs.update({'class': 'log'})
        self.fields['next_of_kin'].widget.attrs.update({'class': 'log'})
        self.fields['username'].widget.attrs.update({'class': 'log'})
        self.fields['password1'].widget.attrs.update({'class': 'log swiy'})
        self.fields['password2'].widget.attrs.update({'class': 'log swiy'})

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'phonenumber',
                  'email', 'password1', 'password2', 'address', 'dob', 'state', 'next_of_kin')
