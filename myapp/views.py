from django.http import HttpResponse # type: ignore

def hello_word(request):

    return HttpResponse("<h1>Assalomu Aleykum Tuxtamurod</h1>")
    
    
