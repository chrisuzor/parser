from celery import shared_task

from api import parse_to_sender


@shared_task(bind=True,autoretry_for=(Exception,), retry_backoff=True, retry_kwargs={"max_retries": 5},
             name='parser_mews:send_mews_object_to_sender')
def send_mews_object_to_sender(self, data: str):
    print('inside send_to_sender')
    parse_to_sender.send_to_mews(data)
    return 'success'
