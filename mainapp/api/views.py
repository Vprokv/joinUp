from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# from snippets.


class ProgramTestAPIView(APIView):

    def get(self, request, *args, **kwargs):
        data = [{"id": 1, "name": "John"}, {"id": 2, "name": "John"}]
        return Response(data)

    def post(self, request, *args, **kwargs):
        return Response({"id": 3, "name": "axaxa"}, status=status.HTTP_201_CREATED)

    # def put(self, request, *args, **kwargs):
    #     return Response(status=status.HTTP_200_OK)

    def delete(self, request, *args, **kwargs):
        return Response(status=status.HTTP_204_NO_CONTENT)
