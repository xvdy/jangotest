# Create your views here.
from django.http import HttpResponse
import logging
from raven import Client

client = Client('http://17699bf68b014160becc7482508a9892:01035d8c440a4dd0b508d4942d883a67@localhost/2')
def test_dict(name, age):
    logging.info("name:"+str(name)+"age:"+str(age))
    print("name:"+str(name)+"age:"+str(age))

def index(request):
    d = {"name": "xdy", "age": 22}
    test_dict(**d)

    # record a simple message
    client.captureMessage('hello world!')

    # capture an exception
    try:
        1 / 0
    except ZeroDivisionError:
        client.captureException()

    try:
        int("adsf")
    except Exception as e:
        print(str(e))

    return HttpResponse("hello")