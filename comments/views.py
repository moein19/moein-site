from django.shortcuts import render

def comments(request):
    return render(request,"comments/comments.html")

def comment(request):
    return render(request,"comments/comment.html")