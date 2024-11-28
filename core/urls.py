from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views  

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.login_view, name='login'), 
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    path('', include('client.urls')),
    path('proveedores/', include('provider.urls')),
    path('papelera/', include('bin.urls')),
]