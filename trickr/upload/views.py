#from django.http import HttpResponse

#def index(request):
#    return HttpResponse("PLZ WORK")


from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from trickr.settings import BASE_DIR
from upload.models import Document
from upload.forms import DocumentForm
import os
import subprocess
import zipfile

def handle_uploaded_file(f):
    os.chdir(os.path.join(BASE_DIR, 'uploads'))
    with open(str(f), 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    os.system("zip " + str(f) + ".zip " + str(f))
    os.system("cat photo.jpg " + str(f) + ".zip > " + str(f) + ".jpg") 
    os.system("rm {0} {0}.zip".format(f))

def upload_file(request):
    # Handle file upload
    if request.method == 'POST':
        #form = DocumentForm(request.POST, request.FILES)
        #if form.is_valid():
        handle_uploaded_file(request.FILES['josh'])
    else:
        print "Form not valid"
        form = DocumentForm() # A empty, unbound form

    # Render list page with the documents and the form

    return render_to_response(
        'list.html', {}, context_instance=RequestContext(request)
    )
