import json 
import requests
from flask import Flask, render_template, request

app = Flask(__name__)

API_URL= 'https://swapi.py4e.com/api'

# Main page (homepage)
@app.route('/')
def homepage(): 
    return render_template('base.html')

# shows the results for the character the user searched 
@app.route('/results')
def results(): 
    id_character = request.args.get('id_character')
    character_result = requests.get(f"{API_URL}/people/{id_character}")
    person = json.loads(character_result.content)

    if character_result.status_code == 404:
        return render_template('results.html')
    else: 

   

        # get results for homeword 
        homeworld_response = requests.get(person["homeworld"])
        homeworld = json.loads(homeworld_response.content)

        # get films 
        films = person["films"]
        film_list= []
        for film in films:
            film_list.append(json.loads(requests.get(film).content))



        context = { 
            "person": person,
            'homeworld': homeworld,
            "films": film_list
        }

        return render_template('results.html', **context)






if __name__ == '__main__':
    app.config['ENV'] = 'development'
    app.run(debug=True, port=3000)

