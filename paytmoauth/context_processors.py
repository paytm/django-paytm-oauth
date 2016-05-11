from django.conf import settings


def login_url(request):

    ''' 
    adds a variable `paytm_oauth_login_url` 
    in the context which is the login url for Paytm Oauth
    '''

    url = settings.PAYTM_OAUTH_PROVIDER_URL + settings.PAYTM_OAUTH_AUTHORIZE_URL_ENDPOINT
    url += '?response_type=code&client_id={}&scope=paytm&redirect_uri={}&theme-web'.format(
        settings.PAYTM_OAUTH_CLIENT_ID, settings.PAYTM_OAUTH_CALLBACK_URL)

    return {
            'paytm_oauth_login_url': url
        }
