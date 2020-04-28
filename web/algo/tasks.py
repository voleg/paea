from celery.decorators import task
from celery.utils.log import get_task_logger

from algo.indicies import Calculation, CalculationSearch

log = get_task_logger(__name__)


@task(name='store_calculation_result')
def store_calculation_result(**kwargs):
    log.info(f'Calculation results recieved {kwargs}')
    calc_id = kwargs.get('id')
    status_message = kwargs.get('status')
    result = kwargs.get('result')
    doc = Calculation.get(id=calc_id)
    doc.meta.version=None
    doc.update(
        status=status_message,
        result = result,
        retry_on_conflict=10
    )
    log.info('Calculation #{} result saved'.format(calc_id))
