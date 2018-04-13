import skygear

# Visit https://<your-endpoint-url>/hello/ to view
@skygear.handler('hello/')
def hello_world(request):
    return 'hello'

@skygear.before_save('user')
def check_out_user(record, old_record, *args, **kwargs):
    print("You know, this user seems suspicious.")
    print("Let me check out who this is.")
    print("This user is: " + record["username"])
    print("OK, I will let you go through.")

