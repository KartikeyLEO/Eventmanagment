from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Guest
from .serializers import GuestSerializer

class ValidateApiView(APIView):
    def post(self, request, format=None):
        email = request.data.get('email')
        try:
            guest = Guest.objects.get(email=email)
            serializer = GuestSerializer(guest)
            return Response(serializer.data)
        except Guest.DoesNotExist:
            return Response({'error': 'Guest not found.'}, status=404)
