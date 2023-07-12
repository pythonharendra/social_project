from django.shortcuts import render
from socialapp.models import Post
from django.contrib.auth.decorators import login_required
'''
posts= [
    {
        "author":"Pradeep",
        "date_posted" : "23-06-2023",
        "title" : "core python",
        "content" : " core is very well",
    },
    {
        "author": "Hero",
        "date_posted" : "23-06-2023",
        "title" : "Advanced python",
        "content" : " Advanced is very well",
    },
    {
        "author": "Nanna",
        "date_posted" : "23-06-2023",
        "title" : "Devops",
        "content" : " Devops is very well",
    },
]
'''
def home_view(request):
    context= {
        "posts" : Post.objects.all()
    }
    return render(request,'home.html', context)

@login_required()
def about_view(request):
    return render(request, 'about.html')


