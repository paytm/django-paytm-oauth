# django-paytm-oauth

django-paytm-oauth is a Django based consumer for Paytm Oauth 2.

##Installation

django-paytm-oauth is available as a git repository. It can be installed by

```
git clone https://github.com/paytm/django-paytm-oauth.git
cd django-paytm-oauth
python setup.py install
```

##Requirements

* Python 3.4
* Django 1.8


##Configuration

* After installing, you need to add `paytmoauth` in your `INSTALLED_APPS` like

```
# settings.py
INSTALLED_APPS = (
    ...
    'paytmoauth',
)

```

* Include urls in your root urls `urlpatterns` like

```
# urls.py
urlpatterns = [
    ...
    url(r'^oauth/', include('paytmoauth.urls')),
]

```

This url should be whitelisted. In the above case `oauth/callback` needs to be whitelisted.

##Settings

The following variables needs to be defined in the settings

* OAUTH_PROVIDER_URL
* ACCESS_TOKEN_URL_ENDPOINT
* USER_ACCESS_URL_ENDPOINT
* CLIENT_SECRET
* CLIENT_ID
* SCOPE