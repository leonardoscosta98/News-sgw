from datetime import date
from django.shortcuts import render
from .models import Aviso, Sistema
from django.http import JsonResponse
import requests

def index(request):
    system_name = request.GET.get('sistema', None)

    if not system_name:
        return JsonResponse({'message':'Sistema nao informado'},status=400)

    sistema = Sistema.objects.filter(nome_sistema=system_name).first()

    if not sistema:
        return JsonResponse({'message':'Sistema nao encontrado'},status=404)
    
    avisos = Aviso.objects.filter(data_expiracao__gte=date.today(),sistema=sistema).last()   
    
    # response = requests.get('https://api.unsplash.com/photos/random?client_id=1Fya4rUM_fkNHqS_rx1nRZp9HZjIIDpCrE3qhtLzBys&office')
    response = requests.get('https://source.unsplash.com/1080x600/?office')
                
    background_body = ''
    if response.status_code == 200:
        if response.url:
            background_body = response.url
        else:
            background_body = 'https://images.unsplash.com/photo-1603201667141-5a2d4c673378?crop=entropy&amp;cs=tinysrgb&amp;fit=crop&amp;fm=jpg&amp;h=600&amp;ixid=MnwxfDB8MXxyYW5kb218MHx8b2ZmaWNlfHx8fHx8MTY4MTk5Njk3OQ&amp;ixlib=rb-4.0.3&amp;q=80&amp;utm_campaign=api-credit&amp;utm_medium=referral&amp;utm_source=unsplash_source&amp;w=1080'

    if not avisos:
        avisos  = 'null'

    context = {
        'aviso': avisos,   
        'sistema': sistema,
        'imgfundounsplash' : background_body
    }

    return render(request, 'news/index.html', context)