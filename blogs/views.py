from django.shortcuts import render

# Create your views here.
def hello(request):
    return render(request, 'index.html',
        {
            'name':'บทความท่องเที่ยวภาคเหนือ',
            'author':'ภาสกร'
        }
    )
