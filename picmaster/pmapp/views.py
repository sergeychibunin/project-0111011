from rest_framework.decorators import api_view

@api_view(['POST'])
def upload(request):
    return Response({"message": "Got some data!"})
