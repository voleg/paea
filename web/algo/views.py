from rest_framework import viewsets, status
from rest_framework.response import Response

from algo.indicies import Calculation, CalculationSearch
from algo.serializers import CalculationRequestSerializer


class CalculationViewSet(viewsets.ViewSet):
    serializer_class = CalculationRequestSerializer

    def list(self, request):
        hits = (
            CalculationSearch(1000)
            .query()
        )

        def format_hits(hit):
            doc = hit.to_dict()
            doc['id'] = hit.meta.id
            return doc

        return Response({
            'total': hits.total,
            'items': [format_hits(i) for i in hits.scroll]
        })

    def create(self, request):
        serializer = self.serializer_class(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

        data = serializer.validated_data
        obj = Calculation(
            func_name=data['func_name'],
            params=data['params']
        )
        obj.save()
        obj.run()
        return Response({'detail': obj.meta.id})

    def retrieve(self, request, pk=None):
        return Response({})

    def update(self, request, pk=None):
        return Response({})

    def partial_update(self, request, pk=None):
        return Response({})

    def destroy(self, request, pk=None):
        return Response({})
