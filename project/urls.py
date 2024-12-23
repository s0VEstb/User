from posts.views import hello_view, html_view, list_view, main_view, detail_view, create_post
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from user.views import register_view, login_view, logout_view
urlpatterns = [
    path('admin/', admin.site.urls),
    path("hello/", hello_view),
    path("tea/", html_view),
    path("list_view/", list_view),
    path("", main_view, name="main-page"),
    path('post_detail/<int:id>/', detail_view),
    path("create_post/", create_post),
    path("register/", register_view),
    path("login/", login_view, name="login-view"),
    path("logout/", logout_view, name="logout-view"),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)