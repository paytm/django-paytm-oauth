# django-paytm-oauth

django-paytm-oauth is a Django based application for consuming Oauth 2 implementation of Paytm.

##Flow

Paytm oauth is consumer side implementation of Oauth 2.0. The steps involved in the flow are explained are below.

 * __Authentication Request__ : User clicks on the `Login with Paytm` button which redirects to `PAYTMOAUTH_PROVIDER_URL + PAYTMOAUTH_AUTHORIZATION_ENDPOINT` and the following parameters are passed
    - response_type
    - client_id
    - scope
    - redirect_uri

* __Authentication Grant__ : User enters his credentials and then the server authenticates the user. As a result of this authorization, an authorization token is passed. This is authorization grant which is passed to the application. The `PAYTMOAUTH_REDIRECT_URL` receives this response.

* __Authorization Request__ : Now after the application has received user's authorization grant, it authorizes itself by passing its id(CLIENT_ID) and secret(CLIENT_SECRET). The url endpoint here will be `PAYTMOAUTH_AUTHENTICATION_ENDPOINT`. This is a server to server call where in authorization header is passed which contains the credentials of the client. Along with the header, following parameters are passed in the body of the post request
    - grant_type
    - code
    - client_id
    - scope

    Here __grant_type__ is generally `authorization_code` and the value of __code__ is the authorization token received from the previous step. This way the authorization server knows that the application is currently talking about which user. This is a server to server call where in no user is involved.

* __Authorization Grant__ : The authorization server authorizes the request by the application. It authenticates whether the app is genuine or not by validating given client id and client secret. The server passes an access_token in the response. This response is received at `PAYTMOAUTH_REDIRECT_URL`.

* __Protected Resource Access__ : This is again a server to server call where the application uses the __access_token__ received in the previous step as a header. Here the url endpoint will be `PAYTMOUATH_RESOURCE_ACCESS_ENDPOINT`. 

* __Grant Protected Resource__ : The server replies in response to the previous step with the protected resource being requested.

##Installation

django-paytm-oauth is available as a git repository. It can be installed by

```
git clone https://github.com/paytm/django-paytm-oauth.git
cd django-paytm-oauth
python setup.py install
```

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

This url should be white-listed. In the above case `oauth/callback` needs to be white-listed.

* Update your context_processors to include one provided by `paytmoauth` like

```
    TEMPLATES = [
        ...
        'OPTIONS': {
            'context_processors': [
                ...
                'paytmoauth.context_processors.login_url',
            ]
        }
    ]
```

Through this a context variable namely `paytmoauth_login_url` will be available in the templates.

##Settings

The following variables needs to be defined in the settings

* PAYTMOAUTH_PROVIDER_URL
* PAYTMOAUTH_AUTHORIZATION_ENDPOINT
* PAYTMOAUTH_AUTHENTICATION_ENDPOINT
* PAYTMOUATH_RESOURCE_ACCESS_ENDPOINT
* PAYTMOAUTH_CLIENT_ID
* PAYTMOAUTH_CLIENT_SECRET
* PAYTMOAUTH_SCOPE
* PAYTMOAUTH_REDIRECT_URL
