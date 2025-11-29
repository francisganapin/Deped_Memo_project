from django.shortcuts import render, get_object_or_404,redirect,reverse
from b2_dep_model.models import MemoTable
from django.core.paginator import Paginator
from datetime import datetime

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
            memo_list = MemoTable.objects.filter(title__icontains=title_search).values('id','title','description','reference_data','month','year','file')

    paginator = Paginator(memo_list,3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request,'for_admin/admin-page.html',{"page_obj": page_obj,'memo_list_recent':memo_list_recent})





#fix this later for update 
def memo_update_views(request,id):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        reference_data = request.POST.get('reference_data')
        file = request.FILES.get('file')

        memo = MemoTable.objects.get(id=id)

        memo.title = title
        memo.description = description
        memo.reference_data = reference_data

        if file:
            memo.file = file
            
        memo.save()
        return redirect('memo_views')

    return render(request,'for_admin/page3.html')

from django.db import IntegrityError
from django.contrib import messages
from datetime import datetime

def memo_upload_views(request):
    month = datetime.now().strftime("%B")
    year = datetime.now().strftime("%Y")

    if request.method == 'POST':
        try:
            title = request.POST.get('title')
            description = request.POST.get('description')
            reference_data = request.POST.get('reference')
            file = request.FILES.get('file')


            MemoTable.objects.update(recent=False)

  
            MemoTable.objects.create(
                title=title,
                description=description,
                month=month,
                year=year,
                reference_data=reference_data,
                file=file,
                recent=True
            )

            print(f"data was saved: {title}, {description}, {reference_data}, {file}")
            messages.success(request, 'Memo uploaded successfully')
            return redirect('memo_views')

        except IntegrityError:
            messages.error(request, 'A memo with this reference already exists')
            return redirect('memo_views')

        except Exception as e:
            messages.error(request, f'Error uploading memo: {str(e)}')
            return redirect('memo_upload_views')

    return render(request, 'for_admin/page3.html')



def memo_delete_view(request):
    if request.method == 'POST':
        reference_data = request.POST.get('reference_data')
        
       
        memo = get_object_or_404(MemoTable, reference_data=reference_data)
        memo.delete()


        return redirect('memo_views') 

    return render(request, 'for_admin/page3.html')


def memo_check_view(request,id):

    memo_entry = get_object_or_404(MemoTable,id=id)
    return render(request,'for_admin/memo_content_2.html',{'memo_entry':memo_entry})
