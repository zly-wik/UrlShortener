from django.shortcuts import render, HttpResponseRedirect

from core.models import ShortUrl


def index(request, code=None):
    if request.method == 'GET':
        if code:
            item = ShortUrl.objects.filter(short_code=code).first()
            if item:
                return HttpResponseRedirect(item.long_url)

        return render(request, 'create_short_url.html', context={})

    elif request.method == 'POST':
        item = ShortUrl.objects.create(long_url=request.POST.get('long_url'))
        item.generate_short_code()
        item.save()
        item.short_code

        return render(request, 'create_short_url.html', context={'item': item})
