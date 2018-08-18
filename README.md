# Celery talk

# Repo para mostrar lo basico de celery con django.

Voy a usar python 2.7 y celery 3 porque es lo que maneja mas. Si queres comenzar un proyecto te sugiero python 3.6 y celery 4.


## Testing
```
In [1]: from core.tasks import test_task_2

# Encola en default
In [2]: test_task_2.delay()
Out[2]: <AsyncResult: 2a2c7cfe-4b79-4845-8238-91bca66dd146>

# No encola en ningun lado
In [3]: test_task_2.apply_async((), routing_key='brasil.rio')
Out[3]: <AsyncResult: e55887b7-f748-46eb-9436-6a6766ec750b>

# Encola en brasil por direct
In [4]: test_task_2.apply_async((), queue='brasil', routing_key='brasil.rio')
Out[4]: <AsyncResult: c5a5dcd5-5099-48b0-90c5-a22e883a197b>

# Encola en brasil por direct
In [5]: test_task_2.apply_async((), queue='brasil')
Out[5]: <AsyncResult: 63003420-f6cf-4b28-ba9e-d8150c0a16ed>

# Encola en argentina por direct
In [6]: test_task_2.apply_async((), queue='argentina')
Out[6]: <AsyncResult: 307bf6fe-1524-48f5-b178-505a4e720b15>

# encola en brasil por topic
In [7]: test_task_2.apply_async((), exchange='por_topico', routing_key='brasil.rio')
Out[7]: <AsyncResult: 2e342de3-429f-4dfe-84a7-068bc3b95d9c>

# encola en argentina por topic
In [8]: test_task_2.apply_async((), exchange='por_topico', routing_key='argentina.chaco')
Out[8]: <AsyncResult: 50b3551a-4734-423d-a279-f9ded439b8cd>

# encola en australia y en nueva zelanda
In [17]: test_task_2.apply_async((), exchange='a_todas_las_q_conectadas')
Out[17]: <AsyncResult: d708b68e-8a17-4776-8aac-27cd5a907834>

# encola en another_direct_queue
In [2]: test_task_2.apply_async((), routing_key='another_direct_queue')
Out[2]: <AsyncResult: d305e0d0-3581-47e6-a971-c7caed7a19c8>

# encola en default
In [3]: test_task_2.apply_async(())
Out[3]: <AsyncResult: 7c5612fe-4daa-4e7d-a2c4-9a010c7b5cdf>
```