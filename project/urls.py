from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from main.views import login_our
from django.contrib.auth import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    #path("login/", views.LoginView.as_view(template_name = "login.html", redirect_authenticated_user=True), name = "login"),
    path('login/', login_our, name='login'),
    #path('logout/', , name='logout'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)