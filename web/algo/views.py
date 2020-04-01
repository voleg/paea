from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action

from algo.indicies import Calculation, CalculationSearch, Status as CalcStatus
from algo.serializers import CalculationRequestSerializer


class CalculationViewSet(viewsets.ViewSet):
    serializer_class = CalculationRequestSerializer

    @action(methods=['GET'], detail=False, name='features')
    def features(self, request):
        data = {
            'implementations': [
                {
                    'name': 'factorial',
                    'params': [
                        {
                            'name': 'n',
                            'type': 'number'
                        }
                    ]
                },
                {
                    'name': 'fibonacci',
                    'params': [
                        {
                            'name': 'n',
                            'type': 'number'
                        }
                    ]
                },
                {
                    'name': 'ackermann',
                    'params': [
                        {
                            'name': 'm',
                            'type': 'number'
                        },
                        {
                            'name': 'n',
                            'type': 'number'
                        }
                    ]
                },
            ]
        }
        return Response(data)

    def _get_position(self, limit=10, offset=0):
        try:
            limit = int(self.request.query_params.get('limit', limit))
            offset = int(self.request.query_params.get('offset', offset))

        except Exception:
            pass

        return limit, offset


    def list(self, request, *args, **kwargs):
        columns = [
            {'id': 'status', 'name': 'Status'},
            {'id': 'id', 'name': 'ID', 'hidden': True },
            {'id': 'created_at', 'name': 'Created at'},
            {'id': 'func_name', 'name': 'Function'},
            {'id': 'params_display' , 'name': 'Params'},
            {'id': 'exec_time', 'name': 'time', 'type': 'numeric'},
            {'id': 'result', 'name': 'Result', 'type': 'numeric'}
        ]
        hits = CalculationSearch().query()
        limit, offset = self._get_position()
        return Response({
            'total': hits.total,
            'columns': columns,
            'items': [h.to_display() for h in hits.search[offset:limit]]
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
        return Response(obj.to_display())

    @action(methods=['POST'], detail=True, name='restart')
    def restart(self, request, pk=None):
        obj = Calculation.get(id=pk)
        obj.update(status=CalcStatus.new)
        obj.run()
        return Response(obj.to_display())
 
    def retrieve(self, request, pk=None):
        return Response({})

    def update(self, request, pk=None):
        return Response({})

    def partial_update(self, request, pk=None):
        return Response({})

    def destroy(self, request, pk=None):
        return Response({})
