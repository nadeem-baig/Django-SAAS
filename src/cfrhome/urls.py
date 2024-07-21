from django.contrib import admin
from django.urls import path,include

from .views import home_page_view
from auth import views as auth_views
urlpatterns = [
    path('', home_page_view,name='home'),
    path('login/', auth_views.login_view),
    path("register/", auth_views.register_view),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
]
