# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.decorators.http import require_POST
import json
from django.http import HttpResponse
from .forms import JobsForm
from .models import Jobs
import logic.testLogins as testLogins

# Create your views here.

def testLogin(data):
    if (data['type'] == 'SFTP'):
#         return testLogins.testSFTP('test.rebex.net', 'demo', 'password', 22, '/')
        return testLogins.testSFTP(data['hostname'], data['username'], data['password'], data['port'], data['remotePath'])
        
        

def jobs(request):
    jobs = Jobs.objects.all()
    return render(request, 'backup/jobs.html', {'jobs': jobs});

def addJob(request):
    return render(request, 'backup/add_job.html');

@require_POST
def submitAddJob(request):
    try:
        data = json.loads(request.body)
        
        form = JobsForm(data)

        if form.is_valid():
            loginResult = testLogin(data)
            if (loginResult == True):
                form.save()
                data_ret = {'status': 1, 'error_message': ""}
            else:
                data_ret = {'status': 0, 'error_message': str(loginResult)}
                
        else:
            print form.errors
            data_ret = {'status': 1, 'error_message': str(form.errors)}

    except BaseException, msg:
        print msg
        data_ret = {'status': 0, 'error_message': str(msg)}
        
    json_data = json.dumps(data_ret)
    return HttpResponse(json_data)