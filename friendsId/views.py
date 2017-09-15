from django.shortcuts import render

# Create your views here.
def friendsId(request):
    return render(request, 'friendsId/friendsId.html', locals())
