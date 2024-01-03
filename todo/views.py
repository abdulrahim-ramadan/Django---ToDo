from django.shortcuts import render
from .models import Post



def post_list(request):
    data = Post.objects.all()
    return render(request,'todo_leist.html',{'todo':data})




def post_detali(request,id):
    data =Post.objects.get(id=id)
    return render(request,'tod_detail.html',{'tod': data})