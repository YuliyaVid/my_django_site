from django.shortcuts import render
from .models import Client
from django.http import HttpResponse
from .forms import PostForm
from django.utils import timezone
from django.shortcuts import redirect


def Client_list (request):
    clients = Client.objects.order_by('Name')
    return render(request, 'my_app/Client_list.html', {'clients': clients})


def Client_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)

        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.created_date = timezone.now()
            post.save()
            return redirect('../../')
    else:
        form = PostForm()
        return render(request, 'blog/post_edit.html', {'form': form})


#def Contract_list (request):
    #html = "<html><body><H1>Второе представление на джанго выполнилось</H1></body></html>"
    #return HttpResponse(html)

#def Imychestvo_list (request):
    #html = "<html><body><H1>Третье представление на джанго выполнилось</H1></body></html>"
    #return HttpResponse(html)



