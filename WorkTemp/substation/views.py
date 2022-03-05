from django.shortcuts import (
        render, 
        redirect, 
        get_object_or_404
        )
from .models import *
# Create your views here.


def redirect_in_all(request):
    return redirect('substation:all_url')
'''

'accepted_types', 'accepts', 'body', 
'build_absolute_uri', 'close', 'content_params', 
'content_type', 'csrf_processing_done', 'encoding', 
'environ', 'get_full_path', 'get_full_path_info', 
'get_host', 'get_port', 'get_signed_cookie',
'headers', 'is_secure', 'method', 'parse_file_upload', 
'path', 'path_info', 'read', 'readline', 'readlines', 
'resolver_match', 'scheme', 'session', 
'upload_handlers', 

'''

def get_all(request):
    r = request
    print(r.content_params)
    import random
    rc = random.choice
    tp = [rc(Substation.objects.all()) for _ in range(3)]
    context = {'substation': tp}
    return render(request, 'substation/all.html', context)




def get_one(request, tp):
    try:
        tp = Substation.objects.get(pk=tp)
    except Substation.DoesNotExist:
        return redirect('substation:all_url')
    context = {'substation': tp}
    return render(request, 'substation/get_one.html', context)

















def search_by_args(request, city, view=None, number=None):
    print(city, view, number)
    w =Substation.objects.all()[1]
    print(w.city.name_transle)
    if number:
        try:
            tp = Substation.objects.get(city=city, view=view, number=number)
            print(True)
        except Substation.DoesNotExist:
            return redirect('substation:all_url')
        return render(request, 'substation/get_one.html', {'substation':tp})



    try:
        tp = Substation.objects.get(pk=1)
    except Substation.DoesNotExist:
        return redirect('substation:all_url')
    context = {'substation': tp}
    return render(request, 'substation/get_one.html', context)
