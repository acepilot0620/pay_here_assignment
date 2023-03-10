from django.contrib import admin
from django.conf import settings
from django.urls import path, include, re_path
from dj_rest_auth.views import LoginView, LogoutView
from dj_rest_auth.registration.views import RegisterView


urlpatterns = [
    path('admin/', admin.site.urls),
    
    # 로그인/회원가입
    path('login/', LoginView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('signup/', RegisterView.as_view()),

    # 하위 앱
    path('', include('user.urls')),
    path('', include('ledger.urls')),
]