from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from datetime import datetime
from django.shortcuts import redirect
from .models import B_user
# Create your views here.

def index(request):
    template = get_template('bikapi/index.html')
    buser = B_user.objects.all()
    html = template.render(locals())

    return HttpResponse(html)
