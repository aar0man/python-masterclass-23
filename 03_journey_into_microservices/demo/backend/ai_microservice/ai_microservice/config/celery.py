from rep_common.config import get_config, is_beat

CELERY_BROKER_URL = 'redis://' + get_config('REDIS_IP', default='redis') + ':6379/0'


#: Only add pickle to this list if your broker is secured
#: from unwanted access (see userguide/security.html)
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'

CELERY_TASK_CREATE_MISSING_QUEUES = True

if is_beat():
    CELERY_BEAT_SCHEDULE = {
        # add here celery beats
    }

CELERY_TASK_ROUTES = {
    # add here celery tasks routes
}

