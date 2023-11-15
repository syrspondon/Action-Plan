from rest_framework import serializers


from .models import BRCA1Breast ,BRCA1Ovarine, BRCA2Breast ,BRCA2Ovarine, PALB2Breast ,PALB2Ovarine


class BRCA1BreastSerializer(serializers.ModelSerializer):
    class Meta:
        model = BRCA1Breast
        fields = '__all__'


class BRCA1OvarineSerializer(serializers.ModelSerializer):
    class Meta:
        model = BRCA1Ovarine
        fields = '__all__'


class BRCA2BreastSerializer(serializers.ModelSerializer):
    class Meta:
        model = BRCA2Breast
        fields = '__all__'


class BRCA2OvarineSerializer(serializers.ModelSerializer):
    class Meta:
        model = BRCA2Ovarine
        fields = '__all__'


class PALB2BreastSerializer(serializers.ModelSerializer):
    class Meta:
        model = PALB2Breast
        fields = '__all__'


class PALB2OvarineSerializer(serializers.ModelSerializer):
    class Meta:
        model = PALB2Ovarine
        fields = '__all__'