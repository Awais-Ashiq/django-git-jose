from django import forms
from django.contrib.auth.models import User
from final_app.models import UserModel, UserModal

#Create yours forms here

class UserForm(forms.ModelForm):
    class Meta():
        model = UserModel
        fields = '__all__'
class UserRegForm(forms.Form):
    fname = forms.CharField(label='First Name')
    lname = forms.CharField(label='Last Name')
    email = forms.CharField(label='Email')

class UserModalForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta():
        model = User
        fields = ('username', 'email', 'password')

class ProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserModal
        fields = ('portfolio_url','profile_pic')
