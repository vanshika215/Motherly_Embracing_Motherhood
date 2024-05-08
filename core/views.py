from django.shortcuts import render,get_object_or_404
from .models import post, comment, query
from django.views.generic import CreateView
from .forms import PostForm
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
import requests
import json

# Create your views here.
def index(request):
    return render(request, "index.html")

def blog(request):
    bpost = post.objects.all()
    return render(request, 'blog.html',{'bpost':bpost})

def posts(request, slug):
    bpost = post.objects.get(slug=slug)
    # comment = Comment.objects.filter(post=bpost)
    return render(request, 'post.html',{'bpost':bpost})

def knowscore(request):
    return render(request, "knowscore.html")

def diet(request):
    return render(request, "Diet.html")

def dietres(request):
    if  request.method == "POST":
        qr = request.POST['query']
        api_url = 'https://api.calorieninjas.com/v1/nutrition?query='
        query = qr
        response = requests.get(api_url + query, headers={'X-Api-Key': '26FIamwdHuBsY8jrYmJbYA==ucOuylZIrx7jlSfZ'})
        if response.status_code == requests.codes.ok:
            res_dict = dict(json.loads(response.text))
            res = res_dict['items'][0]
            print(res.keys())
            
        # else:
        #     print("Error:", response.status_code, response.text)
        return render(request, "Dietres.html", {'res':res})


def pquery(request):
    pq = query.objects.all()
    return render(request,'pquery.html',{'queries':pq})

class AddQueryView(CreateView):
    model = query
    form_class = PostForm
    # fields = ['name','body']
    template_name = 'add_query.html'

def psave(request):
    return render(request, 'psave.html')

def csave(request):
    username = request.POST['username']
    queryn = request.POST['queryn']
    body = request.POST['body']

    new_comment = comment.objects.create(body=body,user=username,queryn=queryn,name=username)
    new_comment.save()
    return HttpResponse("Comment Sent Succesfully")

def LikeView(request, pk):
    p = get_object_or_404(query, id=request.POST.get('queries_id'))
    
    liked = False
    if p.likes.filter(id=request.user.id).exists():
        p.likes.remove(request.user)
        liked = False
    else:
        p.likes.add(request.user)
        liked =True
    return HttpResponseRedirect(reverse('pcomment', args=[str(pk)]))

def pcomment(request, pk):
    username = request.user.username
    pb = query.objects.get(id=pk)
    com = comment.objects.filter(queryn=pk)
    stuff = get_object_or_404(query, id= pk)
    likes_count = stuff.total_likes()

    liked = False
    if stuff.likes.filter(id=request.user.id).exists():
        liked = True
    return render(request, 'comment.html',{'queries':pb,'com':com,'queryn':pk,'username':username,'likes_count':likes_count,'liked':liked})
