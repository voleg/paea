import time

from celery import task
from celery.utils.log import get_task_logger

from service import settings

log = get_task_logger(__name__)


class Status:
    accepted = 'accepted'
    complete = 'complete'
    error = 'error'


@task(name='calculate_function', bind=True, soft_time_limit=120)
def calculate(self, options=None, on_result=None, *args, **kwargs):
    from algos.interface import AlgoTools

    result_queue = on_result.get('queue')
    result_task = on_result.get('task')

    _id = options['id']
    _func_name = options['func_name']
    params = options['params']

    debug_info = f'Algo: {_func_name} with params: {params}'

    def send(status, result=None):
        kwargs = {
            'id': _id,
            'status': status,
            'result': result
        }

        try:
            if result_queue and result_task:
                log.info(f'Sending "{status}" {result_queue}/{result_task} #{_id}')
                self.app.send_task(result_task, queue=result_queue, kwargs=kwargs)

            else:
                return kwargs

        except Exception as e:
            log.error(
                '{} Calculation Failed to send {} {}'
                .format(debug_info, e.__class__.__name__, e)
            )


    log.info('Started calculation task'.format())
    # send(Status.accepted)

    try:
        log.info('start')
        tools = AlgoTools()
        t0 = time.time()
        result = tools.get_function_by_name(_func_name)(**params)

        send(
            Status.complete,
            result={
                'result': str(result),
                'execution_time': time.time() - t0
            }
        )

    except Exception as e:
        log.error(
            'Failed to proceed {} {}'
            .format(debug_info, e.__class__.__name__, e),
            exc_info=True,
        )
        send(Status.error, result={'error': str(e)})