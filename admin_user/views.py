from django.shortcuts import render, get_object_or_404,redirect,reverse
from .models import MemoTable
from django import forms
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.core.exceptions import ValidationError

from datetime import datetime


# Create your views here.
def memo_page1_view(request):
    memo_list = MemoTable.objects.filter(recent=False).values('id','title','description','reference_data','month','year','file')

    if request.method == 'POST':
        title_search = request.POST.get('title')
        month_search = request.POST.get('month')
        year_search = request.POST.get('year')

        if title_search:
            print(title_search)
            memo_list = MemoTable.objects.filter(title=title_search).values('id','title','description','reference_data','month','year','file')

        if month_search:
            print(month_search)
            memo_list = MemoTable.objects.filter(month=month_search).values('id','title','description','reference_data','month','year','file')
        if year_search:
            print(year_search)
            memo_list = MemoTable.objects.filter(year=year_search).values('id','title','description','reference_data','month','year','file')


    paginator = Paginator(memo_list,3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request,'page1.html',{"page_obj": page_obj})

def memo_views_content(request,id):

    memo_entry = get_object_or_404(MemoTable,id=id)

    return render(request,'memo_content.html',{'memo_entry':memo_entry})

#def memo_views_content_download(request,id):

    #response = HttpResponse(request,id)={
        #'Content-Typer':'application/pdf',
        #'Content-Disposition':f'attachment'; filename="{filename}"
    #}

    #return response

# Create your views here.


def memo_views(request):
    memo_list = MemoTable.objects.filter(recent=False).values('id','title','description','reference_data','month','year','file')
    memo_list_recent = MemoTable.objects.filter(recent=True).values('id','title','description','reference_data','month','year','file')
    

    if request.method == 'POST':
        title_search = request.POST.get('title')

        if title_search:
            memo_list = MemoTable.objects.filter(title=title_search).values('id','title','description','reference_data','month','year','file')

    paginator = Paginator(memo_list,3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request,'page2.html',{"page_obj": page_obj,'memo_list_recent':memo_list_recent})




#fix this later for update 
def memo_update_views(request,id):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        reference_data = request.POST.get('reference_data')
        file = request.FILES.get('file')

        memo = MemoTable.objects.get(id=id)

        memo.title = title,
        memo.description = description,
        reference_data = reference_data,

        if file:
            memo.file = file
            
        memo.save()
        return redirect('memo_views')

    return render(request,'page3.html')

def memo_upload_views(request):
    month = datetime.now().strftime("%m-%d")
    year = datetime.now().strftime("%y")
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        reference_data = request.POST.get('reference')
        file = request.FILES.get('file')
        
        MemoTable.objects.update(recent=False)

        MemoTable.objects.create(
            title=title,
            description=description,
            month = month,
            year = year,
           reference_data=reference_data,
            file=file
        )
        print(f'data was save{title},{description},{reference_data},{file}')
        return redirect('memo_views')

    return render(request,'page3.html')


def memo_delete_view(request):
    if request.method == 'POST':
        reference_data = request.POST.get('reference_data')
        
       
        memo = get_object_or_404(MemoTable, reference_data=reference_data)
        memo.delete()


        return redirect('memo_views') 

    return render(request, 'page3.html')


def memo_check_view(request,id):

    memo_entry = get_object_or_404(MemoTable,id=id)
    return render(request,'memo_content_2.html',{'memo_entry':memo_entry})
