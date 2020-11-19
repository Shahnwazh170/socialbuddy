from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LoginView.as_view(template_name="socialBuddy/Login.html",
                               redirect_authenticated_user=True)),
    path('dashboard/logout/', LogoutView.as_view()),
    path('dashboard/', views.dashboard),
    path('dashboard/post-meme', views.post_meme, name="post_meme"),
]
