from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
import random
# Create your views here.

class RandomView(View):
    def get(self, request):
        html = f'{random.randint(1,100)}'
        return HttpResponse(html)