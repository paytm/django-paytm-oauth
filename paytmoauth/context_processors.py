from django.conf import settings

def login_url(request):

    ''' 
    adds a variable `paytmoauth_login_url`
    in the context which is the login url for Paytm Oauth
    '''

    url = settings.PAYTMOAUTH_PROVIDER_URL + settings.PAYTMOAUTH_AUTHORIZATION_ENDPOINT
    url += '?response_type=code&client_id={}&scope=paytm&redirect_uri={}&theme-web'.format(
        settings.PAYTMOAUTH_CLIENT_ID, settings.PAYTMOAUTH_REDIRECT_URL)

    return {
            'paytmoauth_login_url': url
        }
