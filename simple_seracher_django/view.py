from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render_to_response
import urllib
import math

from .search import get_search_result
from .cache import get_cache
from .config import entities_per_page
from .config import cache_dir

def index(request):
    return render(request, 'index.html')


def search(request):
    request.encoding='utf-8'
    res = []
    res_count = 0
    search_time = 0
    page = 1
    if 'p' in request.GET:
        page = int(request.GET['p'])
    if 'q' in request.GET:
        res, res_count, search_time = get_search_result(request.GET['q'], page)
    else:
        return HttpResponse("No keyword.")

    res = [(r[0], urllib.parse.quote(r[0], safe=""), r[1]) for r in res]

    context = {}
    context['key'] = request.GET['q']
    context['page'] = page
    context['max_page'] = math.ceil(res_count/entities_per_page)
    context['res_list'] = res
    context['res_count'] = res_count
    context['search_time'] = search_time

    return render(request, 'search.html', context)


def cache(request):
    if 'u' in request.GET:
        filename = request.GET['u']
        cont = ''
        with open(cache_dir+filename, "r", encoding="utf-8") as f:
            cont = f.read()
        return HttpResponse(cont)
    return HttpResponse("Cache not found.")


def about(request):
    return render(request, 'about.html')
