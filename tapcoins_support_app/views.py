from django.shortcuts import render

# Create your views here.
def support_page(request):
    return render(request, "support_page.html")