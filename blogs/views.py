from django.shortcuts import render

# Create your views here.
def hello(request):
    tags=['น้ำตก','ธรรมชาติ','หน้าฝน','ตากหมอก']
    return render(request, 'index.html',
        {
            'name':'บทความท่องเที่ยวภาคเหนือ',
            'author':'ภาสกร',
            'tags':tags
        }
    )
