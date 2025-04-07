from django.shortcuts import render, get_object_or_404,redirect,reverse
from .models import MemoTable
from django import forms
from django.core.paginator import Paginator

from django.core.exceptions import ValidationError

# Create your views here.
def memo_views(request):
    memo_list = MemoTable.objects.filter(recent=False).values('title','description','reference_data','date')
    memo_list_recent = MemoTable.objects.filter(recent=True).values('title','description','reference_data','date')
    
    paginator = Paginator(memo_list,3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request,'page2.html',{"page_obj": page_obj,'memo_list_recent':memo_list_recent})





def memo_upload_views(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        reference_data = request.POST.get('reference')
        file = request.FILES.get('file')
        
        MemoTable.objects.update(recent=False)

        MemoTable.objects.create(
            title=title,
            description=description,
           reference_data=reference_data,
            file=file
        )
        print(f'data was save{title},{description},{reference_data},{file}')
        return redirect('memo_views')

    return render(request,'page3.html')