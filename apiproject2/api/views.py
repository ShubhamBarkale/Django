
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import student as Student
from .serializers import StudentSerializer


class StudentAPI(APIView):

    # =========================
    # GET - Read Student
    # =========================
    def get(self, request, pk=None):

        # Get single student
        if pk:
            try:
                student = Student.objects.get(id=pk)
                serializer = StudentSerializer(student)

                return Response(
                    serializer.data,
                    status=status.HTTP_200_OK
                )

            except Student.DoesNotExist:
                return Response(
                    {"error": "Student not found"},
                    status=status.HTTP_404_NOT_FOUND
                )

        # Get all students
        else:
            students = Student.objects.all()
            serializer = StudentSerializer(
                students,
                many=True
            )

            return Response(
                serializer.data,
                status=status.HTTP_200_OK
            )


    # =========================
    # POST - Create Student
    # =========================
    def post(self, request):

        serializer = StudentSerializer(
            data=request.data
        )

        if serializer.is_valid():
            serializer.save()

            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


    # =========================
    # PUT - Update Student
    # =========================
    def put(self, request, pk=None):

        try:
            student = Student.objects.get(id=pk)

        except Student.DoesNotExist:
            return Response(
                {"error": "Student not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = StudentSerializer(
            student,
            data=request.data
        )

        if serializer.is_valid():
            serializer.save()

            return Response(
                serializer.data,
                status=status.HTTP_200_OK
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


    # =========================
    # DELETE - Delete Student
    # =========================
    def delete(self, request, pk=None):

        try:
            student = Student.objects.get(id=pk)

        except Student.DoesNotExist:
            return Response(
                {"error": "Student not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        student.delete()

        return Response(
            {"message": "Student deleted successfully"},
            status=status.HTTP_204_NO_CONTENT
        )

