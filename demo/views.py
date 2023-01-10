from django.http import Http404, HttpResponseBadRequest, JsonResponse
from django.shortcuts import render
from rest_framework.exceptions import NotFound
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Students
from .serializers import StudentSerializer
from django.shortcuts import get_object_or_404


# Create your views here.
def validate(data):
    if data.get('first_name'):
        first = data.get('first_name')
        if not isinstance(first, str):
            return False, "First name should be String"

    if data.get('last_name'):
        last = data.get('last_name')
        if not isinstance(last, str) :
            return False, "Last name should be String"

    if data.get('class_name'):
        clss = data.get('class_name')
        if not isinstance(clss, str):
            return False, "Class name should be String"

    if data.get('age'):
        age = data.get('age')
        if not isinstance(age, int):
            return False, "Age should be int"

    return True, "Success"


class StudentView(APIView):

    def get(self, request, id=None):

        if id:

            result = Students.objects.filter(id=id)

        else:
            result = Students.objects.all()

        serializers = StudentSerializer(result, many=True)
        return Response({"students": serializers.data})

    # CREATE
    def post(self, request):

        data = request.data
        flag, msg = validate(data)
        if not flag:
            return Response({'Message': msg}, status=400)

        # validate(data)
        serializer = StudentSerializer(data=data)

        serializer.is_valid(raise_exception=True)

        serializer.save()

        response = Response()

        response.data = {
            'message': 'Student Created Successfully',
            'data': serializer.data
        }

        return response

    # UPDATE
    def patch(self, request, id):
        # # import pdb
        # # pdb.set_trace()
        #
        # # student_to_update = get_object_or_404(Students, id=id)
        # student_update = Students.objects.filter(id=id)
        #
        # # student_to_update = Students.objects.get(pk=pk)
        #
        # # student_to_update:
        update = Students.objects.get(id=id)

        data = request.data
        flag, msg = validate(data)
        if not flag:
            return Response({'Message': msg}, status=400)

        serializer = StudentSerializer(instance=update, data=request.data, partial=True)

        serializer.is_valid(raise_exception=True)

        serializer.save()

        response = Response()

        response.data = {
            'message': 'student Updated Successfully',
            'data': serializer.data
        }

        return response

    def put(self, request, id):
        data = request.data
        print(data)
        flag, msg = validate(data)
        if not flag:
            return Response({'Message': msg}, status=400)

        update = Students.objects.get(id=id)
        print(update)
        serializer = StudentSerializer(instance=update, data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'Message': "Student updated Successfully", "data": serializer.data})

        # DELETE

    def delete(self, request, id):

        result = get_object_or_404(Students, id=id)

        result.delete()
        return Response({"data": "Record Deleted"})
