from django.contrib import admin
from django.urls import path

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
    path('add_new_cv', home_view.add_new_cv, name='add_new_cv'),
    path('add_cv_inf/<int:cv_number>', home_view.add_cv_inf, name='add_cv_inf'),
    path('add_data/<int:cv_number>/<int:forms_number>', home_view.add_data, name='add_data'),
    path('cv1/<int:cv_number>', home_view.cv_pattern1, name='cv_pattern1'),
    path('cv2/<int:cv_number>', home_view.cv_pattern2, name='cv_pattern2'),
]
