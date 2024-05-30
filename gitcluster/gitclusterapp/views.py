from django.shortcuts import redirect
from django.http import JsonResponse, HttpResponse
from django.conf import settings
from .models import Repository
import requests

def github_connect(request):
    if 'code' in request.GET:
        code = request.GET['code']
        access_token_response = requests.post(
            'https://github.com/login/oauth/access_token',
            data={
                'client_id': settings.GITHUB_CLIENT_ID,
                'client_secret': settings.GITHUB_CLIENT_SECRET,
                'code': code
            },
            headers={'Accept': 'application/json'}
        )
        access_token = access_token_response.json().get('access_token')
        if access_token:
            headers = {'Authorization': f'token {access_token}'}
            repos_response = requests.get('https://api.github.com/user/repos', headers=headers)
            repos = repos_response.json()
            for repo in repos:
                Repository.objects.update_or_create(
                    full_name=repo['full_name'],
                    defaults={
                        'name': repo['name'],
                        'private': repo['private'],
                        'html_url': repo['html_url'],
                        'description': repo['description'],
                        'created_at': repo['created_at'],
                        'updated_at': repo['updated_at'],
                    }
                )
            return JsonResponse({'status': 'success', 'repos': [repo['full_name'] for repo in repos]})
        else:
            return HttpResponse("Failed to retrieve access token", status=400)
    else:
        github_auth_url = f'https://github.com/login/oauth/authorize?client_id={settings.GITHUB_CLIENT_ID}&scope=repo'
        return redirect(github_auth_url)
