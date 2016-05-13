===========
Paytm Oauth
===========

Paytm Oauth is a django based consumer for paytm oauth.

Quick start
-----------

1. Add "paytmoauth" to your INSTALLED_APPS in settings like this::

    ```
    INSTALLED_APPS = (
        ...
        'paytmoauth',
    )
    ```

2. Update your context_processors to include one provided by `paytmoauth` like

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

3. Define the following variables in your settings

    ```
        PAYTMOAUTH_PROVIDER_URL
        PAYTMOAUTH_AUTHORIZATION_ENDPOINT
        PAYTMOAUTH_AUTHENTICATION_ENDPOINT
        PAYTMOUATH_RESOURCE_ACCESS_ENDPOINT
        PAYTMOAUTH_CLIENT_ID
        PAYTMOAUTH_CLIENT_SECRET
        PAYTMOAUTH_SCOPE
        PAYTMOAUTH_REDIRECT_URL
    ```

4. Include urls in root urls like this::

    ```
    url(r'^oauth/', include('paytmoauth.urls')),
    ```