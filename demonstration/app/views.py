from django.shortcuts import render, HttpResponse
import requests
import json

# Create your views here.
def index(request):
	return render(request, 'app/index.html')
	#return HttpResponse('Hello World!')
def test(request):
	return HttpResponse('My second view!')
def profile(request):
	parsedData = []
	if request.method == 'POST':
		try:
			username = request.POST.get('user')
			req = requests.get('https://api.github.com/users/' + username)
			jsonList = []
			jsonList.append(json.loads(req.content.decode('utf-8')))
			userData = {}
			for data in jsonList:
				userData['name'] = data['name']
				userData['blog'] = data['blog']
				userData['email'] = data['email']
				userData['public_gists'] = data['public_gists']
				userData['public_repos'] = data['public_repos']
				userData['avatar_url'] = data['avatar_url']
				userData['followers'] = data['followers']
				userData['following'] = data['following']
				parsedData.append(userData)
		except:
			userData['name'] = 'n/a'
			userData['blog'] = 'n/a'
			userData['email'] = 'n/a'
			userData['public_gists'] = 'n/a'
			userData['public_repos'] = 'n/a'
			userData['avatar_url'] = 'n/a'
			userData['followers'] = 'n/a'
			userData['following'] = 'n/a'
			parsedData.append(userData)
	return render(request, 'app/profile.html', {'data': parsedData})
