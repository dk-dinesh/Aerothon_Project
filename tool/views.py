
import subprocess
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import os

# Create your views here.
@csrf_exempt
def Tool(request):
    if request.method == "POST":
        frontend = request.POST.get("frontend framework")
        backend = request.POST.get("backend framework")
        print(frontend,backend)
        if frontend=="React" and backend=="Flask":
            subprocess.call(['sh', os.getcwd()+'/tool/flask.sh'])
            
        # return render(request,'tool.html')
        zip_file = open(os.getcwd()+'/tool/React_Flask.zip', 'rb')
        response = HttpResponse(zip_file, content_type='application/force-download')
        response['Content-Disposition'] = 'attachment; filename="%s"' % 'project.zip'
        return response

    return render(request,'tool.html')

def home(request):
    return render(request,'index.html')

def Team(request):
    return render(request,'team.html')

def Generate(request):
    return render(request,'team.html')

def Download(request):
    print(os.getcwd()+'/tool/React_Flask.zip')
    zip_file = open(os.getcwd()+'/tool/React_Flask.zip', 'rb')
    response = HttpResponse(zip_file, content_type='application/force-download')
    response['Content-Disposition'] = 'attachment; filename="%s"' % 'project.zip'
    return response
