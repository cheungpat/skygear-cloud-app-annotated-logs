import skygear

# Visit https://<your-endpoint-url>/hello/ to view
@skygear.handler('hello/')
def hello_world(request):
    return 'hello'

@skygear.before_save('user')
def reject_user(record, old_record, *args, **kwargs):
    raise Exception('i refuse to do work')


