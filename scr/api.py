import requests
from base import Joke
    
class DaddyJokes(Joke):
    def get_random_joke(self):   
        url = "https://daddyjokes.p.rapidapi.com/random"
        headers = {
            "X-RapidAPI-Key": "cec400650fmsh50c7d1124f67214p1bca68jsn7a125fdefc6e",
            "X-RapidAPI-Host": "daddyjokes.p.rapidapi.com"}
        response = requests.get(url, headers=headers)
        result_json = response.json()
        return result_json['joke']

class ChuckNorris(Joke) :
    def get_random_joke(self):   
        url = "https://matchilling-chuck-norris-jokes-v1.p.rapidapi.com/jokes/random"
        headers = {
        "accept": "application/json",
        "X-RapidAPI-Key": "cec400650fmsh50c7d1124f67214p1bca68jsn7a125fdefc6e",
        "X-RapidAPI-Host": "matchilling-chuck-norris-jokes-v1.p.rapidapi.com"
        }

        response = requests.get(url, headers=headers)
        result_json = response.json()
        return result_json['value']


class ManateeJokes(Joke):
    def get_random_joke(self):
        url = "https://manatee-jokes.p.rapidapi.com/manatees/random"
        headers = {
            "X-RapidAPI-Key": "cec400650fmsh50c7d1124f67214p1bca68jsn7a125fdefc6e",
            "X-RapidAPI-Host": "manatee-jokes.p.rapidapi.com"}
        response = requests.get(url, headers=headers)
        result_json = response.json()
        return result_json['setup'], result_json['punchline'] 


# manateejokes_obj = ManateeJokes()
# joke = manateejokes_obj.get_random_joke()
# print(joke)


# chucknorris_obj = ChuckNorris()
# joke = chucknorris_obj.get_random_joke()
# print(joke)



# daddyjokes_obj = DaddyJokes()
# joke = daddyjokes_obj.get_random_joke()
# print(joke)


url = "https://daddyjokes.p.rapidapi.com/random"
headers = {
    "X-RapidAPI-Key": "cec400650fmsh50c7d1124f67214p1bca68jsn7a125fdefc6e",
    "X-RapidAPI-Host": "daddyjokes.p.rapidapi.com"}
response = requests.get(url, headers=headers)
result_json = response.json()
print(result_json)