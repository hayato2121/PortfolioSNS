from django.urls import path
from accounts import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('login/', views.LoginView.as_view(), name='account_login'),
    path('signup/', views.SignupView.as_view(), name='account_signup'),
    path('logout/', views.LogoutView.as_view(), name='account_logout'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)