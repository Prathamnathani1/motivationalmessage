from django.shortcuts import render
from requests import *

def home(request):
    if request.GET.get("btn"):
        url1 = "http://api.quotable.io/random"
        url2= "https://pixabay.com/images/search/inspiration/"
        res = get(url1,url2)
        data = res.json()
        msg = data["content"]
        return render(request,"home.html", {"msg":msg})
    else:
        return render(request,"home.html")
