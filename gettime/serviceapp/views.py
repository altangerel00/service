from django.shortcuts import render
from django.http import JsonResponse
from datetime import datetime
from django.http import JsonResponse
from datetime import datetime
import json
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt




def showTime(request):
    response = {'datetime': datetime.now()}
    return JsonResponse(response)

# def getInfo(request):
#     data = json.loads(request.body)
#     id = data['id']
#     return JsonResponse({'age': datetime.now().year-id})

@csrf_exempt
def get_time(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({'status': 'error', 'message': 'Invalid JSON payload'}, status=400)

        action = data.get('action')

        if action == 'gettime':
            current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            return JsonResponse({'status': 'success', 'time': current_time})
        else:
            return  JsonResponse({'status': 'error', 'message': 'Invalid action'}, status=400)
        

    return JsonResponse({'status': 'error', 'message': 'Invalid method'}, status=400)