# from django.shortcuts import render
# from django.http import JsonResponse
# from datetime import datetime
# from django.http import JsonResponse
# from datetime import datetime
# import json
# from django.views.decorators.http import require_http_methods
# from django.views.decorators.csrf import csrf_exempt
# from gettime.settings import *




# def showTime(request):
#     response = {'datetime': datetime.now()}
#     return JsonResponse(response)

# # def getInfo(request):
# #     data = json.loads(request.body)
# #     id = data['id']
# #     return JsonResponse({'age': datetime.now().year-id})

# @csrf_exempt
# def get_time(request):
#     if request.method == 'POST':
#         try:
#             data = json.loads(request.body)
#         except json.JSONDecodeError:
#             return JsonResponse({'status': 'error', 'message': 'Invalid JSON payload'}, status=400)

#         action = data.get('action')

#         if action == 'gettime':
#             current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
#             return JsonResponse({'status': 'success', 'time': current_time})
#         else:
#             return  JsonResponse({'status': 'error', 'message': 'Invalid action'}, status=400)
        

#     return JsonResponse({'status': 'error', 'message': 'Invalid method'}, status=400)




from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.db import connection
from datetime import datetime
from gettime.settings import *
import json

@csrf_exempt
def get_data(request):
    if request.method == 'POST':
        try:
            request_data = json.loads(request.body)
            if "action" not in request_data:
                message = {"message": "json error"}
                return JsonResponse(message)
            else:
                action = request_data.get("action")
                if action == "gettime":
                    current_time = datetime.now()
                    return JsonResponse({'message': 'Current Time', 'time': current_time})
                elif action == "alldata":
                    return all_data(request_data)
                else:
                    message = {"message": "json error"}
                    return JsonResponse(message)

        except json.JSONDecodeError:
            message = {"message": "json error"}
            return JsonResponse(message)

def all_data(request):
    con = connectDB()
    try:
        
      
        cur = con.cursor()
        cur.execute("SELECT * FROM cus.customer")

        cols = cur.description
        rows = cur.fetchall()
        data = [dict(zip[cols, row]) for row in cur.fetchall()]
        respRow = [{cols[index][0]: column for index, column in enumerate(value)} for value in rows]

        cur.close()
        return JsonResponse(respRow, safe=False)
    except Exception as e:
        print(e)
        message = {"message": f"DB error: {str(e)}"}
        return JsonResponse(message)
    finally:
        disconnectDB(con)

       

    