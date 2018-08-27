from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth import authenticate, login
from django.views.generic import View
from django.contrib.auth.models import User
from .forms import LoginForm, RegisterForm

# from .

def about(request):
    mycontext = {
        'data': ''
    }
    return render(request, 'firstapp/about.html',mycontext)

def book(request):
    mycontext = {
        'data': ''
    }
    return render(request, 'firstapp/book.html',mycontext)

def home(request):
    loggedin = request.user.is_authenticated

    mycontext = {
        'data': '',
        'loggedin' : loggedin
    }
    return render(request, 'firstapp/home.html', mycontext)




class RegisterFormView(View):
    form_class = RegisterForm
    template_name = 'firstapp/signup.html'
    print('I am registerForm()')
    def get(self, request):
        print('GET IN REGISTERFROM')
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        print('POST IN REGISTERFROM')
        form = self.form_class(request.POST)
        print('form class variable success '+str(form.is_valid()))
        username = request.POST.get('username', 'Default')
        email = request.POST.get('email', 'Default')
        password = request.POST.get('password', 'Default')
        print('Form valid')
        user = User(username=username, email=email, password=password, is_superuser=0)
        user.save()
        #user = authenticate(username=username, password=password)
        user = User.objects.filter(username=username, password=password)
        if user is not None:
            print('User not none')
            user = user[0]
            if user.is_active:
                print('starting login')
                login(request, user)
                print('Login success')
                return redirect('/firstapp/home')
            else:
                print('The user acccount is disabled')
                return redirect('/firstapp/?login=disabled')
        else:
            print('The username and password is wrong')
            return redirect('/firstapp/?login=failed')


class LoginFormView(View):
    form_class = LoginForm
    template_name = 'firstapp/index.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        print('received an post request for login')
        username = request.POST['username']
        password = request.POST['password']
        user = User.objects.filter(username=username, password=password)

        if user is not None:
            user = user[0]
            if user.is_active:
                login(request, user)
                return redirect('/firstapp/home')
            else:
                print('The user acccount is disabled')
                return redirect('/firstapp/?login=disabled')
        else:
            print('The username and password is wrong')
            return redirect('/firstapp/?login=failure')


from django.contrib.auth import logout

def logoutForm(request):
    logout(request)
    # Redirect to a success page.
    return redirect('/firstapp/')







