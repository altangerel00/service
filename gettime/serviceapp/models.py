from django.db import models
import psycopg2 as ps
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

@csrf_exempt
def get_data(request):
    if request.method == 'GET':
        action = request.GET.get('action')

        if action == 'getdata':
            try:
                connection = ps.connect(
                    dbname="your_database_name",
                    user="your_database_user",
                    host="localhost",
                    password="your_database_password",
                    port="5432",
                )

                cursor = connection.cursor()

                # Replace 'your_table_name' with the actual table name
                query = "SELECT * FROM your_table_name;"
                cursor.execute(query)

                data_from_database = cursor.fetchall()

                # Convert the data to a list of dictionaries for JSON serialization
                data_list = [{'column1': row[0], 'column2': row[1], 'column3': row[2]} for row in data_from_database]

                return JsonResponse({'status': 'success', 'data': data_list})

            except Exception as e:
                return JsonResponse({'status': 'error', 'message': f'Error: {str(e)}'}, status=500)

            finally:
                if connection:
                    connection.close()
                    print("Connection closed successfully")  # Indicate that the connection is actually closed

        else:
            return JsonResponse({'status': 'error', 'message': 'Invalid action'}, status=400)

    return JsonResponse({'status': 'error', 'message': 'Invalid method'}, status=400)
# Create your models here.
