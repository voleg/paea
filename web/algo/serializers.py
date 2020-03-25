from rest_framework import serializers


class CalculationParam(serializers.Serializer):
    name = serializers.CharField(max_length=8)
    value = serializers.IntegerField()



class CalculationRequestSerializer(serializers.Serializer):
    func_name = serializers.CharField(max_length=200, required=True)
    # todo: there are culd be many of params ... 
    params = CalculationParam(many=True)