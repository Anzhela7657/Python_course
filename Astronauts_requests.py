import requests

link = "http://api.open-notify.org/astros.json"
response = requests.get(link)

match response.status_code:
    case 200:
     data = response.json()
     number_of_astronauts = data['number']
     astronauts = data['people']
     print(f'Number of astronauts: {number_of_astronauts}\nThe names of astronauts:')
     for astronaut in astronauts:
        print(astronaut['name'])
    case _:
     print(f"Error {response.status_code}")
