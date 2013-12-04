#from django.http import HttpResponse

#def index(request):
#    return HttpResponse("PLZ WORK")


from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from upload.models import Document
from upload.forms import DocumentForm

def handle_uploaded_file(f):
    #subprocess.call(["zip", file + ".zip", file])
    #os.system("cat ~/haha/P1050795.JPG " + file + ".zip > " + file + ".jpg")
    with open('trickr/name.txt', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

def upload_file(request):
    # Handle file upload
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            #return HttpResponseRedirect(reverse('views.list'))
            return HttpResponseRedirect('views.list')
    else:
        form = DocumentForm() # A empty, unbound form

    # Render list page with the documents and the form

    return render_to_response(
        'list.html',
       # {'documents': documents, 'form': form},
       # context_instance=RequestContext(request)
    )
