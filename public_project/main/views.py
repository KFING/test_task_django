from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.contrib.auth.models import auth, User
from .models import UserInfo
from django.contrib import messages
# Create your views here.



def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        print('1')
        user = auth.authenticate(username=email, password=password)
        user_email = User.objects.filter(username=email)
        if user_email.exists():
            info_user_auth = UserInfo.objects.filter(user=user_email[0])[0]
            if user is not None:
                if info_user_auth is not None:
                    info_user_auth.true_auth = int(info_user_auth.true_auth) + 1;
                    info_user_auth.save(update_fields=['true_auth'])
                auth.login(request, user)
                return redirect('home')
            else:
                if info_user_auth is not None:
                    info_user_auth.face_auth = int(info_user_auth.face_auth) + 1;
                    info_user_auth.save(update_fields=['face_auth'])
                return redirect('login')
    return render(request, 'login.html')



def register(request):

    if request.method == 'POST':
        email1 = request.POST['email']
        password = request.POST['password']
        password1 = request.POST['password1']

        if password == password1:
            if User.objects.filter(username=email1).exists():
                return redirect('register')
            else:
                user = UserInfo.objects.create(user=User.objects.create_user(username=email1, password=password), face_auth=0, true_auth=0)
                user.save()
                return redirect('login')
        else:
            return redirect('register')
    return render(request, 'register.html')
def success(request):
    return render(request, 'success.html')


def home(request):
    content = UserInfo.objects.filter(user=request.user)[0]
    color = 'red'

    if content is not None:
        result = int(int(content.true_auth)/(int(content.true_auth)+int(content.face_auth))*100)
        if result >= 50:
            color = 'green'
        return render(request, 'home.html', context={
            'email': str(request.user),
            'false_num': str(content.face_auth),
            'true_num': str(content.true_auth),
            'false_result': str(100-result),
            'true_result': str(result),
            'bg_color' : color
        })
    return render(request, 'home.html', context={
        'email': 'fail',
        'false_num': 'fail',
        'true_num': 'fail',
        'true_false': 'fail',
        'bg_color': color
    })

def logout(request):
    return render(request, 'logout.html')
def main_page(request):
    if not User.objects.filter(username='4elovekconstanta@vought.com').exists():
        user = UserInfo.objects.create(user=User.objects.create_user(username='4elovekconstanta@vought.com', password='5uperP@sw00rd'), face_auth=0,
                                       true_auth=0)
        user.save()
    return render(request, 'main.html')