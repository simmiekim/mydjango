from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User
from django.contrib import auth
from django.shortcuts import redirect

#------------ 회원가입
def signup(request):
    if request.method == 'POST':
        # 두 패스워드가 동일하다면
        if request.POST["password"] == request.POST["password2"]:
            # username와 password 값을 가져와서 user 객체를 생성
            user = User.objects.create_user(
                username=request.POST['username'],
                password=request.POST['password']
            )
            auth.login(request, user)
            # 로그인페이지로 이동
            return redirect('/accounts/login')

        # 두 패스워드가 동일하지 않다면 다시 화면 출력
        return render(request, 'signup.html')
    else:
        # post 방식이라 아니라면 화면만 출력
        return render(request, 'signup.html')

# ---------------------- 로그인
def login(request):
    # POST 방식인경우
    if request.method == 'POST':
        # username와 password를 가져와서 인증확인
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        # 해당하는 user 가 있다면
        if user is not None:
            auth.login(request, user)
            return redirect('/polls') # polls 페이지로 이동
        else:
            return render(request, 'login.html',  {'error':'잘못 입력'})

    # GET 방식인 경우에는 화면만 출력
    else:
        return render(request, 'login.html')


# ---------------------- 로그아웃
def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('/')
    return render(request,'login.html')