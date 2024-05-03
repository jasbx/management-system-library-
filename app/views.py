from django.shortcuts import redirect, render

from app.form import Bookform
from .models import *
# Create your views here.
def index(request):

    if request.method=='POST':
        
        title=request.POST.get('title')
        auther=request.POST.get('author')
        desc=request.POST.get('desc')
        price=request.POST.get('price')
        slug=request.POST.get('slug')
        img=request.POST.get('img')
        page=request.POST.get('pages')
        categray=request.POST.get('Categray')
        save=Books(pages=page,slug=slug,title=title,author=auther,description=desc,img=img,price=price,Categray=categray)
        if save is not None:
            save.save()
        else:
            return render(request, 'index.html')
        
        
        
        return render(request, 'index.html')
    book=Books.objects.all()
    mybooks={
            'books':book,
            
        }
    return render(request, 'index.html',context=mybooks)
def blank(request):
    return render(request, 'blank.html')
def table(request):
        
    book=Books.objects.all()
    mybooks={
            'books':book,
        }
      
   
      
    return render(request, 'table.html',context=mybooks)

def tab(request):
       
       book=Books.objects.all()
       mybooks={
            'books':book,
        }
       return render(request, 'tab.html',context=mybooks)
def form(request):
    return render(request, 'form.html')




def home_view(request):
    book=Books.objects.all()
    form=Bookform(book)
    return render(request, "blank.html", context={"form": form})


from .form import *
def update(request,pk):
    book=Books.objects.get(id=pk)
    form=Bookform(instance=book)
    if request.method=='POST':
        form=Bookform(request.POST,instance=book)
        if form.is_valid():
            form.save()
         
    context={
        'form':form
    }
    return render (request,'updateBooks.html',context=context)

def delete(request,pk):
    d=Books.objects.get(id=pk)
    if request.method=='POST':
        d.delete()


        
    contect={
        'delete':d
    }
    return render(request,'deleteBooks.html',context=contect)

def detal_Book(request,slug):
    
     detal_book=Books.objects.get(slug=slug)
     context={
        'detales':detal_book
    }
     return render (request,'detalBooks.html',context=context)



