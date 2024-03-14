from django.shortcuts import render
from django.http import JsonResponse
from .models import eightBallResponse

def index(request):
    return render(request, 'eightVue/main.html')

def get_eight_ball_responses(request):
    responses = eightBallResponse.objects.values_list('text', flat=True)
    return JsonResponse(list(responses), safe=False)