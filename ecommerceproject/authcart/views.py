from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import auth
from .forms import CustomUserCreationForm
from django.views.generic import View
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_decode,urlsafe_base64_encode
from .utils import TokenGenerator,generate_token
from django.utils.encoding import force_bytes,force_str,DjangoUnicodeDecodeError
from django.core.mail import EmailMessage
from django.conf import settings
# Create your views here.

'''def signup(request):  
    if request.method=='POST':
        
        form = CustomUserCreationForm()  
        print(form)
        if form.is_valid(): 
            print('w2') 
            form.save()  
        else:  
            form = CustomUserCreationForm()  
            print('w3')

    return render(request, 'authtemplates/signup.html', {'form': form})
'''



def signup(request):

   

    if request.method == 'POST':
        username=request.POST['username']
        email=request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        
        
        print(email)
        if password1!=password2:
            
            messages.info(request,'both password not same')
            return redirect('/authcart/signup')

        form = UserCreationForm(request.POST)
        
        if form.is_valid():
            user = User.objects.create_user(username,email,password1)
            user.is_active=False
            print(user)
            user.save()
            email_subject="activate your account"
            print('w1')
            message=render_to_string('activate.html',
                                     {
                'user':user,
                'domain':'127.0.0.1:8000',
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                'token':generate_token.make_token(user),
                                     }
                                     )
            print(message)
            email = form.cleaned_data.get('email')
            email_message= EmailMessage(email_subject,message,settings.EMAIL_HOST_USER,to=[email])
            email_message.send()
            print('w3')
            messages.success(request,"actiavet your account by clicking the link in your email")

            return redirect('/authcart/login')
        
        if form.is_valid()==False:
            messages.warning(request,'may be email already taken \n password should be in special characters')
            return redirect('/authcart/signup')
    else:
        form = UserCreationForm()
    return render(request, 'authtemplates/signup.html', {'form': form})


class ActivateAccountView(View):
    def get(self,request,uidb64,token):
        try:
            uid=force_str(urlsafe_base64_decode(uidb64))
            user=User.objects.get(pk=uid)
        except Exception as identifier:
            user = None
        if user is not None and generate_token.check_token(user,token):
            user.is_active=True
            user.save()
            messages.info(request,"account activated successfully")
            return redirect('/authcart/login')
        return render(request,'authtemplates/activatefail.html')


def login(request):
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        print(username,password)
        form = AuthenticationForm(data=request.POST)
        
        if form.is_valid():
            
            user = form.get_user()
            auth.login(request,user) 
            return redirect('/')
        if form.is_valid()==False:
            messages.info(request,'invaild')
            return redirect('/authcart/login')

    else:
        
        form = AuthenticationForm()
    return render(request, 'authtemplates/login.html', {'form': form})
 
def logout(request):
    auth.logout(request)
    return redirect('/')



"""def handlesignup(request):

    if request.method=='POST':
        #print("post method is running")
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        
        if pass1!=pass2:
            messages.info(request,'both password not same')
            return redirect('/authcart/signup')
            

        try:
            if User.objects.filter(email=email).exists():
                messages.warning(request,'email already taken')
                return redirect('/authcart/signup')
        except Exception as identifier:
            pass
        
        user = User.objects.create_user(email=email,password=pass1,password1=pass2)
        user.save()
        print(user)
        return redirect('/authcart/login')

    else:
        print('get method is running') 
    
    return render(request,'authtemplates/signup.html')

def handlelogin(request):
    if request.method=='POST':

        email = request.POST['email']
        pass1 = request.POST['pass1']

        user = authenticate(email=email,password=pass1)
        print('worked')
        print(user)
        if user is not None:
            login(request,user)
            print('success')
            return redirect('/')
        else:
            messages.info(request,'invaild')
            return redirect('/authcart/login')

        
    return render(request,'authtemplates/login.html')


def handlelogout(request):
    return redirect('/authcart/login')"""

