from django import forms
from django.contrib.auth import password_validation
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from article.tools import get_field_attrs

class RegisterForm(UserCreationForm):
    password1 = forms.CharField(
        label = 'Paddword',
        strip=False,#是否移除用户输入空白 
        widget=forms.PasswordInput(get_field_attrs('Password')),
        #help_text=password_validation.password_validations_help_text_html(),
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        label = "Confirm Password",
        strip = False,
        widget = forms.PasswordInput(get_field_attrs("Confirm Password")),
        help_text = "enter the same password",
    )

    class Meta:
        model = User
        fields = ['username','email']#该表单包含的字段
        widgets = {
            'username':forms.TextInput(get_field_attrs('Username')),
            'email' : forms.EmailInput(get_field_attrs('Email')),
    }

    def clean_email(self):
        email = self.cleaned_data['email']#目前为止已经合法的数据
        user = User.objects.filter(email=email).first() #根据email的地址查找用户 select * from user where email = 'summer.zhang@gmail.com' limit 1 limit 1表示避免全表扫描
        if user:
            raise forms.ValidationError("the email is already exist")
        self.instance.email = email
        return email

class LoginForm(forms.Form):
    username = forms.CharField(
    label = "Username",
    widget = forms.TextInput(get_field_attrs("Username")),
    )
    password = forms.CharField(
    label = "Password",
    widget = forms.TextInput(get_field_attrs("Password")),
    )        
