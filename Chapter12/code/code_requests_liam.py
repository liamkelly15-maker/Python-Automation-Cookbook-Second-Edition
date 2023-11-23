import requests
from datetime import datetime, timedelta
import json


RECIPES = {
    'DEFAULT': {
        'size': 'small',
        'topping': ['bacon', 'onion'],
    },
    'SPECIAL': {
        'size': 'large',
        'topping': ['bacon', 'mushroom', 'onion'],
    }
}


def order_pizza(recipe):

    delivery_time = datetime.now() + timedelta(hours=1)
    delivery = delivery_time.strftime('%H:%M')

    data = {
        'custname': "Sean O'Connell2",
        'custtel': '123-456-789',
        'custemail': 'sean@oconnell.ie',
        # Indicate the time
        'delivery': delivery,
        'comments': ''
    }

    extra_info = RECIPES[recipe]
    data.update(extra_info)
    #why was the python data dictionary not encoded by using json=data
    resp = requests.post('https://httpbin.org/post', data)
    print('post complete')
    #apply the json method to the resp object - is it now converted into a python dict ? - i think so..the json() call has converted it
    print(resp.json()['form'])
    #return resp.json()['form']
    pythonobject=resp.json()['form]']
    for form in pythonobject:
        print(form[])

    #if __name__ == '__main__':
    #    order=order_pizza(recipe='DEFAULT')

order_pizza('DEFAULT')


x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

#print(json.dumps(x))



