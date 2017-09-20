from django.shortcuts import render
from .dec import login_deny
from .forms import RegisterForm, LoginForm
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
#User是auth模块中维护用户信息的关系模式(继承了models.Model),数据库中该表被命名为auth_user.
from django.contrib.auth import login,logout

@login_deny
def register_view(request):
    form = RegisterForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse_lazy("home"))
    context = {
        'form':form,
        'title':'Register',
        'subtitle':'register and write',
        'submit' : 'Register'
    }
    return render(request,'generic_form.html', context)

@login_deny
def login_view(request):
    form = LoginForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        username = form.cleaned_data['username'] #到目前为止是合法的数据
        password = form.cleaned_data['password'] #到目前为止是合法的数据
        user = User.objects.filter(username=username).first()
        if user and user.check_password(password):
            login(request,user)#login向session中添加SEESION_KEY，便于对用户进行跟踪
            return HttpResponseRedirect(reverse_lazy('home'))
        messages.add_message(request, message.ERROR,'user or password incorrect')
    context = {
            'form':form,
            'title':'Login',
            'subtitle':'login site',
            'submit': 'Login',
            }
    return render(request, 'generic_form.html', context)

#logout会移除request中的user的信息，并刷新session
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse_lazy('home'))
    
             
        

# Create your views here.
