from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import render
import requests


class NewsView(APIView):
    def get(self, request):
        url = "https://api.nytimes.com/svc/topstories/v2/home.json"
        params = {
            'api-key': 'U5sciyZvZ74c6RHW5Ui51bhbQYygj20g'
        }

        response = requests.get(url, params=params)

        if response.status_code == 200:
            data = response.json()
            results = data['results']
            last_update = data['last_updated']
            context = {
                'results': results,
                'last_update': last_update,
            }
            if 'format' in request.GET and request.GET['format'] == 'json':
                return Response({'results': results, 'last_update': last_update})
            else:
                return render(request, template_name='news.html', context=context)
