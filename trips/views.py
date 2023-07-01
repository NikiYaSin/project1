from datetime import datetime
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

#宣告 hello_world 這個 view
#當 hello_world 被呼叫時，回傳包含字串 Hello World! 的 HttpResponse 物件。
def hello_world(request): 
    return render(request, 'hello_world.html',{
        'current_time': str(datetime.now()),
    })