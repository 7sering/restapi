from rest_framework.views import APIView #APIView from restframework
from rest_framework.response import Response # Response from restframework
from django.shortcuts import render
from .models import * # Model Improting


# Create your views here.
class TodoView(APIView):
    #GET DATA API CODES
    def get(self , request):
        response = {}
        response['status'] = 500
        response['message'] = 'something went wrong'
        
        try:
            todo_objs = Todo.objects.all()
            payload =[]
            for todo_obj in todo_objs:
                payload.append({
                    'todo_name' : todo_obj.todo_name,
                    'todo_description' : todo_obj.todo_description,
                    'is_completed' : todo_obj.is_completed,
                    })
                
            response['status'] = 200
            response['message'] = 'All Todo'
            response['data'] = payload
            
        except Exception as e:
            print(e)
        return Response(response)

#POST DATA API CODE
    def post(self, request):
        response = {}
        response['status'] = 500
        response['message'] = 'something went wrong'
        
        try:
            data = request.data
            # print(data)
            todo_name = data.get('todo_name')
            todo_description = data.get('todo_description')
            
            if todo_name is None:
                response['message'] = 'Todo name must required'
                raise Exception('Todo name not found')
            
            if todo_description is None:
                response['message'] = 'Todo_Description  must required'
                raise Exception('Todo Description not found')
            
            todo_obj = Todo.objects.create(
                todo_name = todo_name,
                todo_description=todo_description
            )    
            
            payload = {}
            payload = {
                'todo_id' : todo_obj.id,
                'todo_name' : todo_obj.todo_name,
                'todo_description' : todo_obj.todo_description
                
            }
                
            response['status'] = 200
            response['message'] = 'Your Todo is saved'
            response['data'] = payload
            
        except Exception as e:
            print(e)
            
        return Response(response)

# Delete API Codes
    def delete(self, request):
        response = {}
        response['status'] = 500
        response['message'] = 'something went wrong'
        
        try:
            todo_id = request.GET.get('todo_id')
            
            if todo_id is None:
                response['message'] = 'Todo_ID is required'
                raise Exception('Todo ID not found')
            
            try:
                todo_obj = Todo.objects.get(id = todo_id)
                todo_obj.delete()
                
                response['status'] = 200
                response['message'] = 'Todo is deleted successfully'
                
            except Exception as e:
                response['message'] = f'Invalid Todo ID **{todo_id}**'
        
        except Exception as e:
            print(e)
            
        return Response(response)
    
#Update API Codes    
    def put(self, request):
        response = {}
        response['status'] = 500
        response['message'] = 'something went wrong'
        
        try:
            data = request.data
            
            todo_id = data.get('todo_id')
            todo_name = data.get('todo_name')
            todo_description = data.get('todo_description')
            is_completed = data.get('is_completed')
            
            if todo_id is None:
                response['message'] = 'todo_id is required'
                raise Exception('todo id is not found')
            
            try:
                todo_obj = Todo.objects.get(id = todo_id)
                
                todo_obj.todo_name = todo_name
                todo_obj.todo_description = todo_description
                todo_obj.is_completed = is_completed
                todo_obj.save()
                
            except Exception as e:
                response['message'] = f'Invalid Todo ID **{todo_id}**'
                return response(response)
        
            response['status'] = 200
            response['message'] = 'Your TODO is updated'
            
        except Exception as e:
            print(e)
            
        return Response(response)
    
    
    
TodoView = TodoView.as_view()  # View Converted for URL