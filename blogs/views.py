from django.shortcuts import render

# Create your views here.
def hello(request):
    tags=['น้ำตก','ธรรมชาติ','หน้าฝน','ตากหมอก']
    rating = 4
    return render(request, 'index.html',
        {
            'name':'บทความท่องเที่ยวภาคเหนือ',
            'author':'ภาสกร',
            'tags':tags,
            'rating':rating
        }
    )

def page1(request):
    return render(request, 'page1.html')

def createForm(request):
    return render(request, 'form.html')

def addBlog(request):
    name =          request.GET['name']
    description =   request.GET['description']
    return render(request,'result.html',{
        'name':name,
        'description':description})