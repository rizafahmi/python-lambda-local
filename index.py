import json
from random import randint

print('Loading function')

def lambda_handler(event, context):
    print('Received event: ' + json.dumps(event, indent=2))
    
    if 'name' in event:
        name = event['name']
    else:
        name = 'World'

    randomizer = randint(0, 9)
    greetings = 'Hello ' + name + '!' * randomizer
    print(greetings)
    return greetings
