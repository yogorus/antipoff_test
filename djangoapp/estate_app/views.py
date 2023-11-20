import json
import requests
from django.shortcuts import redirect
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import RetrieveAPIView, CreateAPIView, ListAPIView

from .serializers import CadastralInputSerializer, CadastralResultSerializer
from .models import CadastralRequest


class QueryView(CreateAPIView):
    serializer_class = CadastralInputSerializer

    def post(self, request):
        input_serializer = self.get_serializer(data=request.data)
        if input_serializer.is_valid():
            data = input_serializer.validated_data
            data_to_send = data
            data_to_send["longitude"] = float(data["longitude"])
            data_to_send["latitude"] = float(data["latitude"])

            # Send request to external API
            response: dict = requests.post(
                "http://127.0.0.1:8080/", json.dumps(data)
            ).json()

            status = response.get("status")
            data["status"] = status

            result_serializer = CadastralResultSerializer(data=data)
            result_serializer.is_valid(raise_exception=True)
            result_serializer.save()

            return redirect("result", pk=result_serializer.instance.pk)

        return Response({"message": input_serializer.errors})


class ResultView(RetrieveAPIView):
    queryset = CadastralRequest.objects.all()
    serializer_class = CadastralResultSerializer


class CadastralHistoryView(ListAPIView):
    serializer_class = CadastralResultSerializer

    def get_queryset(self):
        cadastral_number = self.kwargs["cadastral_number"]
        return CadastralRequest.objects.filter(cadastral_number=cadastral_number)


class PingView(APIView):
    def get(self, request):
        return Response({"status": "OK"})
