# views.py
import json
from django.shortcuts import render
from django.http import JsonResponse

def update_text(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8'))
            new_text = data.get('newText')
            if new_text:
                request.session['text'] = new_text
                return JsonResponse({'status': 'success'})
        except json.JSONDecodeError:
            pass
    
    return JsonResponse({'status': 'error'})

def get_text(request):
    try:
        return JsonResponse({'text': request.session['text']})
    except:
        return JsonResponse({'text': 'close'})
        

def interface_with_button(request):
    return render(request, 'interface_button.html')

def interface_with_text(request):
    return render(request, 'interface_text.html')

def anim(request):
    return render(request, 'compile.html')