from django.http import request
from django.shortcuts import render,redirect
from .models import BookList
from  django.http import HttpResponse

# Create your views here.

def create(request):

 if (request.method=='POST'):
    p =request.POST.get('name')
    u=request.POST.get('price')
    v=request.POST.get('author')


    book_details=BookList(name=p,price=u,author=v)
    book_details.save()

    return redirect('/')
 else:
     return  HttpResponse("")








def add_book(request ):

    return  render(request,'add_book.html')

def index(request):
    books=BookList.objects.all()
    return  render(request,'index.html',{'books':books})
def delete(request , id):
    books=BookList.objects.get(pk=id)
    books.delete()
    return  redirect('/')
def update(request , id):
    books=BookList.objects.get(pk=id)
    books.name=request.POST.get('name')
    books.price=request.POST.get('price')
    books.author=request.POST.get('author')
    books.save()
    return  redirect('/')
def edit(request ,id):
    books = BookList.objects.get(pk=id)
    books.id=id
    return  render(request,'edit.html',{'books':books})