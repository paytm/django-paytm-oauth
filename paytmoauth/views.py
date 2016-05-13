import base64
import json
import requests

from django.conf import settings
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect


def paytm_oauth(request):
    code = request.GET.get('code', None)
    url = settings.PAYTMOAUTH_PROVIDER_URL + settings.PAYTMOAUTH_AUTHENTICATION_ENDPOINT
    header_value = settings.PAYTMOAUTH_CLIENT_ID + ':' + settings.PAYTMOAUTH_CLIENT_SECRET
    authorization_header = base64.b64encode(header_value.encode('ascii'))
    authorization_header = str(authorization_header,  'ascii')
    if code:
        headers = {
                    "Authorization":  "Basic " + authorization_header,
                    "Content-Type": "application/x-www-form-urlencoded"
                }
        payload = {
            "grant_type":"authorization_code",
            "code": code,
            "client_id":settings.PAYTMOAUTH_CLIENT_ID,
            "scope": settings.PAYTMOAUTH_SCOPE
        }
        try:
            response = requests.post(url, headers=headers, data=payload)
        except Exception as e:
            print ('Error : Request for retriving access token failed', e)
            response = None
        
        if response and response.status_code == 200:
            partial_response = json.loads(response.text)
            url = settings.PAYTMOAUTH_PROVIDER_URL + settings.PAYTMOUATH_RESOURCE_ACCESS_ENDPOINT
            headers = {
                'session_token': partial_response.get('access_token')
            }
            try:
                authentication_response = requests.get(url, headers=headers)
            except Exception as e:
                print('Error : Request for retriving authentication response failed', e)
                authentication_response = None
            else:
                user_detail = json.loads(authentication_response.text)
                username = user_detail.get('id')
                email = user_detail.get('email')
                first_name = user_detail.get('firstName', None)
                last_name = user_detail.get('lastName', None)
                if User.objects.filter(username=username).exists():
                    user = User.objects.get(username=username)
                    user.email = email
                    # first and last name may change
                    if first_name:
                        user.first_name = first_name
                    if last_name:
                        user.last_name = last_name
                    # hack : the proper django way is to use an
                    # authentication backend
                    if not hasattr(user, 'backend'):
                        user.backend = 'django.contrib.auth.backends.ModelBackend'
                    user.save()
                    login(request, user)
                else:
                    new_user = User(username=username, email=email, 
                                    first_name=first_name, last_name=last_name)
                    # hack : the proper django way is to use an
                    # authentication backend
                    if not hasattr(new_user, 'backend'):
                        new_user.backend = 'django.contrib.auth.backends.ModelBackend'
                    new_user.save()
                    login(request, new_user)
                return HttpResponseRedirect(settings.LOGIN_REDIRECT_URL)
    return HttpResponseRedirect('/')