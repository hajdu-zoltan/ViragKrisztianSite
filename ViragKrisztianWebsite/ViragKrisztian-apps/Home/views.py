# Create your views here.
from email import message
from http.client import HTTPResponse
import imp
from pickle import NONE
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Image, Video
from django.contrib.auth.models import User
from .forms import FormWithCaptcha
from django.contrib import messages
from datetime import datetime
from django.core.mail import EmailMessage
from .forms import NewUserForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.contrib.auth.forms import PasswordResetForm
from django.core.mail import send_mail, BadHeaderError
from django.core.mail import EmailMultiAlternatives

images = Image.objects.filter(category__id__in=[1, 2, 3, 4, 5])
videos = Video.objects.filter(category__id=1)
user_id = -1


def test(request):
    return render(request, "Test.html", {'actual_page': 'test', })


def navbar(request):
    actual_page = ''
    return render(request, "Navbar.html", {'actual_page': 'navbar'})


def home(request):
    return render(request, "Home.html",
                  {'actual_page': 'home', 'range': range(12), 'user_id': user_id, 'price_datas': "price_datas",
                   'hairdressers': "hairdressers", 'videos': videos, 'images': images})


def gallery(request):
    images = Image.objects.filter(category__id__in=[1, 2, 3, 4, 5])
    return render(request, "Gallery.html",
                  {'actual_page': 'gallery', 'user_id': user_id, 'range': range(15), 'images': images,
                   'videos': videos})


def price(request):
    if request.method == 'GET':
        price_datas = ""
        return render(request, "Gallery.html",
                      {'actual_page': 'price', 'user_id': user_id, 'price_datas': price_datas})


def living_room(request):
    if request.method == 'GET':
        images = Image.objects.filter(category__id__in=[4])
        return render(request, "Gallery.html",
                      {'actual_page': 'Living_room', 'user_id': user_id, 'range': range(15), 'images': images,
                       'videos': videos})


def kitchen(request):
    if request.method == 'GET':
        images = Image.objects.filter(category__id__in=[1, 2, 3, 4, 5])
        return render(request, "Gallery.html",
                      {'actual_page': 'Kitchen', 'user_id': user_id, 'range': range(15), 'images': images,
                       'videos': videos})


def built_in_wardrobes(request):
    if request.method == 'GET':
        images = Image.objects.filter(category__id__in=[5])
        return render(request, "Gallery.html",
                      {'actual_page': 'Built_in_wardrobes', 'user_id': user_id, 'range': range(15), 'images': images,
                       'videos': videos})


def booking(request):
    _name = None
    _email = None
    _phone = None
    _categori_id = None
    _message = None
    price = ""
    if request.method == 'GET':
        return render(request, "Booking.html", {'actual_page': 'booking', 'user_id': user_id})
    elif request.method == 'POST':
        _name = request.POST.get('name')
        _email = request.POST.get('email')
        _phone = request.POST.get('phone')
        _message = request.POST.get('message')
        form = FormWithCaptcha(request.POST)
        errors = 0
        if form.is_valid():
            if _name == '' or _email == '' or _phone == '' or _message == '':
                errors += 1
                messages.success(request, "Tölsd ki az összes mezőt!")
                return render(request, "Booking.html",
                              {'actual_page': 'booking', 'user_id': user_id, 'number': range(9, 20), 'email': _email,
                               'name': _name, 'message': _message})

            if errors == 0:
                c = {
                    "name": _name,
                    "email": _email,
                    "phone": _phone,
                    "message": _message,
                    "date_time": datetime.now(),
                }

                email_subject = 'Árajánlat kérés'
                email_body = render_to_string("booking_mail.html", c)

                email = EmailMessage(
                    subject=email_subject,
                    body=email_body,
                    to=[_email],
                )

                # itt állítjuk be az email tartalom típusát html-re
                email.content_subtype = 'html'

                email.send()
                return render(request, "Successful_booking.html",
                              {'actual_page': 'booking', 'user_id': user_id, 'email': _email, 'name': _name,
                               'date': "", 'time': "", 'hairdresser': "_hairdresser",
                               'categori': ""})
        else:
            messages.success(request, "Nem megfelelően töltötte ki az adatokat!")
            return render(request, "Booking.html", {'actual_page': 'booking', 'user_id': user_id, 'price': price,
                                                    'booked_appointments': "booked_appointments", 'number': range(9, 20),
                                                    'email': _email, 'name': _name, 'hairdressers': 'test',
                                                    'hairdresser_id': 2,
                                                    'categori_id': _categori_id})

        return render(request, "Registration.html", {'actual_page': 'conformation', 'code': code})


def confirmation(request):
    if request.method == 'GET':
        code = '1234'
        return render(request, "Confirmation.html", {'actual_page': 'conformation', 'code': code})
    elif request.method == 'POST':
        _code = request.POST.get('code')


def register(request):
    form = FormWithCaptcha(request.POST)
    form = FormWithCaptcha()
    _name = ''
    _email = ''
    _password = ''
    _forget_password = ''
    _phone = ''

    if request.method == 'POST':
        form = FormWithCaptcha(request.POST)
        _name = request.POST.get('name')
        _email = request.POST.get('email')
        _password = request.POST.get('password')
        _forget_password = request.POST.get('forget_password')
        _phone = request.POST.get('phone')
        if form.is_valid():
            errors = 0
            users = User.objects.all()

            if _name == '' or _email == '' or _password == '' or _forget_password == '':
                errors += 1
                messages.success(request, "Tölsd ki az összes mezőt!")
            else:
                for user in users:
                    if user.email == _email:
                        messages.success(request, "Ezzel az email címmel már regisztráltak")
                        return render(request, "Registration.html",
                                      {'actual_page': 'registration', 'form': form, 'email': _email, 'name': _name,
                                       'password': _password, 'forget_password': _forget_password, 'phone': _phone})

                if _password != _forget_password:
                    messages.success(request, "A megadot jelszavak nem egyeznek!")
                    errors += 1
                if errors == 0:
                    user = User(name=_name, email=_email, password=_password)
                    user.save()
                    return render(request, "Login.html", {'actual_page': 'login', 'form': form})
                else:
                    form = FormWithCaptcha()
                    return render(request, "Registration.html",
                                  {'actual_page': 'registration', 'form': form, 'email': _email, 'name': _name,
                                   'password': _password, 'forget_password': _forget_password, 'phone': _phone})
        else:
            messages.success(request, "Nem megfelelően töltötte ki az adatokat!")
    else:
        form = FormWithCaptcha()
    return render(request, "Registration.html",
                  {'actual_page': 'registration', 'form': form, 'email': _email, 'name': _name, 'password': _password,
                   'forget_password': _forget_password, 'phone': _phone})


def _login(request):
    if request.method == 'GET':
        return render(request, "Login.html", {'actual_page': 'login'})
    elif request.method == 'POST':
        users = User.objects.all()
        _email = request.POST.get('email')
        _password = request.POST.get('password')
        login = False
        user_id = -1
        for user in users:
            if user.email == _email:
                if user.password == _password:
                    login = True
                    user_id = user.id
        if login:
            return render(request, "Home.html",
                          {'actual_page': 'home', 'prices': price_datas, 'hairdressers': hairdressers,
                           'user_id': user_id})
            # return render(request, "Registration.html", {'actual_page': 'registration'})
        else:
            return render(request, "Login.html", {'actual_page': 'login'})

        # user = User(email=email, password=password)
        # user.save()


def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            _users = User.objects.all()
            _email = request.POST.get('email')
            _password = request.POST.get('password')
            _forget_password = request.POST.get('forget_password')
            _error = 0
            for user in _users:
                if user.email == _email:
                    messages.error(request, "Ezzel az email címmel már regisztráltak.")
                    _error = 1
                    break
            if _password != _forget_password:
                messages.error(request, "A megadot jelszavak nem egyeznek!")
                _error = 1
            if _error != 1:
                user = form.save()
                login(request, user)
                messages.success(request, "Registration successful.")
                return redirect("/home/")
        else:
            messages.error(request, "Nem megfelelően töltötte ki az adatokat.")
    else:
        form = NewUserForm()
    return render(request=request, template_name="Registration.html", context={"form": form})


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                # messages.info(request, f"You are now logged in as {username}.")
                return redirect("/home/")
            else:
                messages.error(request, "Hibás jelszó vagy felhasználónév.")
        else:
            messages.error(request, "Hibás jelszó vagy felhasználónév.")
    form = AuthenticationForm()
    return render(request=request, template_name="Login.html", context={"form": form})


def logout_request(request):
    logout(request)
    messages.info(request, "Sikeres kijelentkezés.")
    return redirect("/home/")


def password_reset_request(request):
    if request.method == "POST":
        password_reset_form = PasswordResetForm(request.POST)
        if password_reset_form.is_valid():
            data = password_reset_form.cleaned_data['email']
            associated_users = User.objects.filter(Q(email=data))
            if associated_users.exists():
                for user in associated_users:
                    subject = "Password Reset Requested"
                    email_template_name = "password_reset_email.txt"
                    c = {
                        "email": user.email,
                        'domain': '192.168.1.69',
                        'site_name': 'Website',
                        "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                        "user": user,
                        'token': default_token_generator.make_token(user),
                        'protocol': 'http',
                    }
                    email = render_to_string(email_template_name, c)
                    try:
                        send_mail(subject, email, 'figaroszeged@gmail.com', [user.email], fail_silently=False)
                    except BadHeaderError:
                        return HttpResponse('Invalid header found.')
                    return redirect("/password_reset/done/")
    password_reset_form = PasswordResetForm()
    return render(request=request, template_name="Password_reset.html",
                  context={"password_reset_form": password_reset_form})
