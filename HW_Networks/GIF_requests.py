#1.Create a program that will ask user to search a word. Search this word in Giphy (use their API). Return links to these GIFs as a result

import requests

word = input("Please enter your word: ")
api_ = f'https://api.giphy.com/v1/gifs/search?api_key=LLuS1SeSYASz09GMVTTWYQchdwBul8zg&q={word}&limit=25&offset=0&rating=g&lang=en'
req = requests.get(api_)
match req.status_code:
    case 200:
     giphy = req.json()
     link_gif = []
     for obj in giphy['data']:
         url_of_gif = obj["images"]["original"]["url"]
         link_gif.append(url_of_gif)
         for link in link_gif:
             print(f'Link to this GIF: {link}')
    case _:
        print('GIF not found')
