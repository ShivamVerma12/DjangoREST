from django.http import Http404
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Students
from .serializers import StudentSerializer
from django.shortcuts import get_object_or_404


# Create your views here.

class StudentView(APIView):

    # GET ALL
    def get(self, request, pk=None):

        if pk:
            result = Students.objects.filter(pk=pk)

        else:
            result = Students.objects.all()

        serializers = StudentSerializer(result, many=True)
        return Response({"students": serializers.data}, status=200)

    # CREATE
    def post(self, request):
        data = request.data
        serializer = StudentSerializer(data=data)

        # Check if the data passed is valid
        serializer.is_valid(raise_exception=True)

        # Create Student in the DB
        serializer.save()

        # Return Response to User

        response = Response()

        response.data = {
            'message': 'Student Created Successfully',
            'data': serializer.data
        }

        return response

    # UPDATE
    def put(self, request, pk):
        # import pdb
        # pdb.set_trace()

        # student_to_update = Students.objects.get(pk=pk)
        student_to_update = get_object_or_404(Students, pk=pk)
        # student_to_update:
        serializer = StudentSerializer(instance=student_to_update, data=request.data, partial=True)

        serializer.is_valid(raise_exception=True)

        serializer.save()

        response = Response()

        response.data = {
            'message': 'student Updated Successfully',
            'data': serializer.data
        }

        return response

    # DELETE
    def delete(self, request, pk):
        result = get_object_or_404(Students, pk=pk)

        result.delete()
        return Response({"data": "Record Deleted"})
