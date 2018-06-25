from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.views import login, logout
from django.shortcuts import render, redirect


# User클래스 자체를 가져올때는 get_user_model()
# ForeignKey에 User모델을 지정할때는 settings.AUTH_USER_MODEL
User = get_user_model()

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # 받은 username과 password에 해당하는 User가 있는지 인증
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # 세션값을 만들어 DB에 저장하고, HTTP response의 Cookie에 해당값을 담아보내도록 하는
            # login()함수를 실행한다
            login(request, user)
            return redirect('posts:post-list')
        # 인증에 실패한 경우 (username또는 password가 틀린경우)
        else:
            # 다시 로그인 페이지로 redirect
            return redirect('members:login')
    else:
        # form이 있는 template을 보여준다
        return render(request, 'members/login.html')


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('posts:post-list')
    return redirect('posts:post-list')


def signup(request):
    context = {
        'errors':[],
    }
    if request.method == 'POST':

        # 존재하지 않는 경우에만 아래 로직 실
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        # 입력데이터 채워넣기
        context['username'] = username
        context['email'] = email

        # form에서 전송된 데이터들이 올바른지 검사
        if User.objects.filter(username=username).exists():
            context['errors'].append('유저가 이미 존재함')
        if password != password2:
            context['errors'].append('패스워드가 일치하지 않음')

        # errors가 존재하면 render
        if not context['errors']:
            # errors가 없으면 유저 생성 루틴 실행
            user = User.objects.create_user(
                username=username,
                password=password,
                email=email,
            )
            login(request, user)
            return redirect('index')
    return render(request, 'members/signup.html', context)