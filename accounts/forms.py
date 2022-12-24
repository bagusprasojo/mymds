from django import forms
from .models import Account, UserProfile


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder' : 'Enter Password',
        'class' : 'form-control',
    }))

    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder' : 'Confirm Password',
        'class' : 'form-control',
    }))
    class Meta:
        model = Account
        fields = ['first_name', 'last_name', 'phone_number', 'email','password','confirm_password']

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs["placeholder"] = 'Enter Your First Name'
        self.fields['last_name'].widget.attrs["placeholder"] = 'Enter Your Last Name'
        self.fields['phone_number'].widget.attrs["placeholder"] = 'Phone Number'
        self.fields['email'].widget.attrs["placeholder"] = 'Email'

        for field in self.fields:
            self.fields[field].widget.attrs["class"] = 'form-control'

    def clean(self):
        cleaned_data = super(RegistrationForm, self).clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise forms.ValidationError(
                "Password does not match"
            )

class ChangePasswordForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder' : 'Enter Password',
        'class' : 'form-control',
    }))

    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder' : 'Confirm Password',
        'class' : 'form-control',
    }))
    class Meta:
        model = Account
        fields = ['password','confirm_password']

    def __init__(self, *args, **kwargs):
        super(ChangePasswordForm, self).__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs["class"] = 'form-control'

    def clean(self):
        cleaned_data = super(ChangePasswordForm, self).clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise forms.ValidationError(
                "Password doesn't match"
            )


class UserForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ('first_name','last_name','phone_number',)

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs["class"] = 'form-control'


class UserProfileForm(forms.ModelForm):
    #rapikan file input
    profile_picture = forms.ImageField(required=False, error_messages={'Invalid':{"Image File  Only"}}, widget=forms.FileInput)

    class Meta:
        model = UserProfile
        fields = ('address_line_1','address_line_2','city','state','city','profile_picture','country')

    def __init__(self, *args, **kwargs):
        super(UserProfileForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs["class"] = 'form-control'
