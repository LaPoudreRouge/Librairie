from authlib.integrations.django_client import OAuth
from django.conf import settings
from django.shortcuts import render, redirect
from django.urls import reverse
from urllib.parse import quote_plus, urlencode
from django.contrib.auth.models import User
import django.contrib.auth as auth

oauth = OAuth()

oauth.register(
    "auth0",
    client_id=settings.AUTH0_CLIENT_ID,
    client_secret=settings.AUTH0_CLIENT_SECRET,
    client_kwargs={
        "scope": "openid profile email",
    },
    server_metadata_url=f"https://{settings.AUTH0_DOMAIN}/.well-known/openid-configuration",
)


def index(request):

    return render(
        request,
        "index.html",
        context={
            "connected": request.user.is_authenticated,
            "session": request.user.username,
            "pretty":request.user.id,
        },
    )


def callback(request):
    token = oauth.auth0.authorize_access_token(request)
    user_info = token['userinfo']

    email = user_info['email']
    username = user_info.get('nickname', email.split('@')[0])

    user, _ = User.objects.get_or_create(username=username, defaults={'email': email})
    if user is not None:
        auth.login(request, user)

    redirect_url = request.session.pop('redirect_url', 'auth0.index')
    return redirect(request.build_absolute_uri(reverse(redirect_url)))


def login(request):
    if request.method == 'POST':
        request.session['redirect_url'] = request.POST.get('redirect_url')
    return oauth.auth0.authorize_redirect(
        request, request.build_absolute_uri(reverse("callback"))
    )


def logout(request):
    request.session.clear()
    auth.logout(request)
    return redirect(
        f"https://{settings.AUTH0_DOMAIN}/v2/logout?"
        + urlencode(
            {
                "returnTo": request.build_absolute_uri(reverse("auth0.index")),
                "client_id": settings.AUTH0_CLIENT_ID,
            },
            quote_via=quote_plus,
        ),
    )
