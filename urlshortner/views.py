import random
import string
from django.shortcuts import render, redirect
from django.contrib import messages

from .models import Url
from .forms import UrlForm


# Create your views here.
def url_shortener(request):
    if request.method == 'POST':
        form = UrlForm(request.POST)
        if form.is_valid():
            slug = ''.join(random.choice(string.ascii_letters)for x in range(10))
            url = form.cleaned_data['url']
            new_url = Url(url=url, slug=slug)
            new_url.save()

            return redirect('/')

    else:
        form = Url()

    data = Url.objects.all()
    context = {
        'form': form,
        'data': data
    }

    return render(request, 'url.html', context)


def url_redirect(request, slugs):
    data = Url.objects.get(slug=slugs)
    return redirect(data.url)

