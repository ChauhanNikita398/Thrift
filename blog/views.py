from django.shortcuts import render, redirect
from .models import Blog, Comment
import pandas as pd


# Create your views here.
def home(request):
    return render(request, "homeblog.html")

def browse(request):
    if request.method == 'POST':
        comm=request.POST['comment']
        blog_id=request.POST['blog_id']

        model = pd.read_pickle(r'C:\Users\HP\Project\thrift\review\model_file.pkl')
        s=[]
        s.append(comm)
        result = model.predict(s)
        comment=Comment(blog_id=blog_id, comment=comm, review=result[0])
        comment.save()
        return redirect('browse')
    else:
        blogs = Blog.objects.all()
        comments = Comment.objects.all()
        for blog in blogs:
            temp=0
            count=0
            for comment in comments:
                if(comment.blog_id==blog.id):
                    temp=temp+comment.review
                count+=1
            ans=int((temp/count)*100)
            # ans=ans.slice[0,6]
            blog.recommend=ans
            blog.save()

        return render(request, "browseblog.html", {'blogs': blogs, 'comments':comments})

def add(request):
    if request.method == 'POST':
        name=request.POST['name']
        desc=request.POST['description']
        price=request.POST['price']
        img=request.POST['img']
        recommend=0

        blog = Blog(name=name,desc=desc,price=price,img=img,recommend=recommend)
        blog.save()
        return redirect('browse')
    else:
        return render(request, "addblog.html")

