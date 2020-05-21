from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

from accounts import views as accounts_view
from home import views as home_view
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('signup/', accounts_view.signup, name='signup'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('', home_view.start_page, name='start'),
    path('admin/', admin.site.urls, name='admin'),
    path('view_cv/<int:cv_number>', home_view.view_cv, name='view_cv'),
    path('cv_list/', home_view.cv_list, name='cv_list'),

]
