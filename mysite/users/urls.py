from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy


urlpatterns = [
    path('register',views.register,name='register'),
    path('email_verification/<str:uidb64>/<str:token>',views.email_verification,name='email-verification'),
    path('email_verification_sent',views.email_verification_sent,name='email-verification-sent'),
    path('email_verification_success',views.email_verification_success,name='email-verification-success'),
    path('email_verification_failed',views.email_verification_failed,name='email-verification-failed'),
   
   
   
    path('login',views.user_login,name='login') ,
    path('logout',views.user_logout,name='logout') ,
    path('profile',views.profile,name='profile') ,
    
    
    
    # password reset url paths
    path('password-reset',auth_views.PasswordResetView.as_view(template_name='users/password-reset.html'),name='password_reset'),    
    path('password-reset/done',auth_views.PasswordResetDoneView.as_view(template_name='users/password-reset-sent.html'),name='password_reset_done'),
   
path(
    'reset/<uidb64>/<token>/',
    auth_views.PasswordResetConfirmView.as_view(
        template_name='users/password-reset-form.html',
        success_url=reverse_lazy('login')   
    ),
    name='password_reset_confirm'
),
    path('password_reset_complete',auth_views.PasswordResetCompleteView.as_view(template_name='users/password-reset-complete.html'),name='password_reset_complete'), 
]
