from django import views
from rest_framework import viewsets

from .models import BRCA1Breast, BRCA1Ovarine, BRCA2Breast, BRCA2Ovarine, PALB2Ovarine, PALB2Breast
from .serializers import BRCA1BreastSerializer ,BRCA1OvarineSerializer, BRCA2BreastSerializer ,BRCA2OvarineSerializer, PALB2BreastSerializer, PALB2OvarineSerializer


class BRCA1BreastViewSet(viewsets.ModelViewSet):
    serializer_class = BRCA1BreastSerializer
    queryset = BRCA1Breast.objects.all()


class BRCA1OvarineViewSet(viewsets.ModelViewSet):
    serializer_class = BRCA1OvarineSerializer
    queryset = BRCA1Ovarine.objects.all()


class BRCA2BreastViewSet(viewsets.ModelViewSet):
    serializer_class = BRCA2BreastSerializer
    queryset = BRCA2Breast.objects.all()


class BRCA2OvarineViewSet(viewsets.ModelViewSet):
    serializer_class = BRCA2OvarineSerializer
    queryset = BRCA2Ovarine.objects.all()

class PALB2BreastViewSet(viewsets.ModelViewSet):
    serializer_class = PALB2BreastSerializer
    queryset = PALB2Breast.objects.all()


class PALB2OvarineViewSet(viewsets.ModelViewSet):
    serializer_class = PALB2OvarineSerializer
    queryset = PALB2Ovarine.objects.all()