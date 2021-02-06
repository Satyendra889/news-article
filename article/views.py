from django.shortcuts import render
from django.shortcuts import get_object_or_404, get_list_or_404
from .models import Article
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages



def list(request):
    article = Article.objects.all()
    context = {
        'data': article
    }
    return render(request, 'list.html', context)


def list_detail(request, pk):
    detail = get_list_or_404(Article, id=pk)
    context = {
        'detail': detail
    }
    return render(request, 'detail.html', context)


@csrf_exempt
def insert(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        image = request.FILES.get('image')
        article = Article.objects.create(title=title, content=content, image=image)
        if article:
            messages.success(request, 'Inserted Successfully')
    return render(request, 'insert.html')