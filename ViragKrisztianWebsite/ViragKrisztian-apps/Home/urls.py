from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home, name = 'Home'),
    path('home/', views.home, name = 'Home'),
    path('navbar/', views.navbar, name = 'Navbar'),
    #path('register/', views.register, name = 'Registration'),
    path('register/', views.register_request, name = 'Registration'),
    path('login/', views.login_request, name = 'Login'),
    path("logout/", views.logout_request, name= "Logout"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('booking/', views.booking, name = 'Booking'),
    path('confirmation/', views.confirmation, name = 'Confirmation'),
    path('gallery/', views.gallery, name = 'Gallery'),
    path('price/', views.price, name = 'Price'),
    path('living_room/', views.living_room, name = 'Living_room'),
    path('kitchen/', views.kitchen, name = 'Kitchen'),
    path('built_in_wardrobes/', views.built_in_wardrobes, name = 'Built_in_wardrobes'),
    path('test/', views.test, name = 'Test'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='Password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="Password_reset_confirm.html"), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='Password_reset_complete.html'), name='password_reset_complete'),
    path("password_reset", views.password_reset_request, name="password_reset"),
    path("", include("allauth.urls")),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)