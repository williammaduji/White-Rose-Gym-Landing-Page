from django.shortcuts import render
from .forms import Form

# Create your views here.


def index(request):
    form = Form
    if request.method == 'POST':
        form = Form(request.POST)
        if form.is_valid():
            form.save()

    return render(request, 'Index/site.html', {'forms': form
    })
