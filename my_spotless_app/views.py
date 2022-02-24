from django.shortcuts import render



def home_page_view(request):
    context = {}
    return render(request, "index.html", context)

def profile_view(request):
    context = {
        'user':request.user
    }
    return render(request, "profile.html", context)

