from django.shortcuts import render, get_object_or_404,redirect,reverse
from b2_dep_model.models import MemoTable
from django.core.paginator import Paginator


# for regular user
def memo_page1_view(request):
    memo_list = MemoTable.objects.filter(recent=False).values('id','title','description','reference_data','month','year','file')

    title_search = None
    month_search = None
    year_search = None
    page_number = request.GET.get('page') or request.POST.get('page')

    if request.method == 'POST':
        title_search = request.POST.get('title')
        month_search = request.POST.get('month')
        year_search = request.POST.get('year')
        
        filters = {'recent':False}

        #apply filter if provided

        if title_search:
            print(title_search)
            filters['title__contains'] = title_search

        if month_search:
            print(month_search)
            filters['month'] = month_search

        if year_search:
            print(year_search)
            filters['year'] = year_search

        memo_list = (
            MemoTable.objects.filter(**filters).values('id','title','description','reference_data','month','year','file')
        )


    paginator = Paginator(memo_list,4)
    page_obj = paginator.get_page(page_number)
    
    return render(request,'for_user/1_memo_list.html',{
        "page_obj": page_obj,
        'title_search':title_search or '',
        'month_search':month_search or '',
        'year_search':year_search or '',
                                                       
            })



    
def memo_views_content(request,page_number,id,):

    memo_entry = get_object_or_404(MemoTable,id=id)
   
    # add page number to memo_views_content so that they know what page they are
    return render(request,'for_user/2_memo_content.html',{'memo_entry':memo_entry,'page_number':page_number})
