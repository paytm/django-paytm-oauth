===========
Paytm Oauth
===========

Paytm Oauth is a django based consumer for paytm oauth.

Quick start
-----------

1. Add "paytmoauth" to your INSTALLED_APPS setting like this::

    ```
    INSTALLED_APPS = (
        ...
        'paytmoauth',
    )
    ```

2. Define the following variables in your settings

    ```
    OAUTH_PROVIDER_URL
    ACCESS_TOKEN_URL_ENDPOINT
    USER_ACCESS_URL_ENDPOINT
    
    CLIENT_SECRET
    CLIENT_ID
    SCOPE
    ```

3. Include urls in root urls like this::

    ```
    url(r'^oauth/', include('paytmoauth.urls')),
    ```