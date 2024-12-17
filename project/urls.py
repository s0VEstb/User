from posts.views import hello_view, html_view, list_view, main_view, detail_view
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path("hello/", hello_view),
    path("tea/", html_view),
    path("list_view/", list_view),
    path("", main_view),
    path('post_detail/<int:id>/', detail_view)
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)