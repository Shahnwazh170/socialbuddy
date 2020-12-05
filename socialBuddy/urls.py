from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LoginView.as_view(template_name="socialBuddy/Login.html",
                               redirect_authenticated_user=True)),
    path('dashboard/logout/', LogoutView.as_view(), name="logout"),
    path('dashboard/', views.dashboard),
    path('dashboard/random-meme', views.post_meme, name="random_meme"),
    path('dashboard/indian-meme', views.post_meme, name="indian_meme"),
    path('dashboard/programming-meme', views.post_meme, name="programming_meme"),
    path('dashboard/post-joke', views.post_joke, name="post_joke"),
]
