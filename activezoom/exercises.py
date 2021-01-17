import os.path
from os import path
import requests
import re
import json
import random

class Exercises():
    muscles = ["Shoulders","Chest","Traps","Biceps","Forearms","Abdominals","Quads","Calves", "Traps_middle", "Triceps", "Lats", "Lowerback", "Glutes", "Hamstrings"]
    ex_types = ['Stretches', 'Bodyweight', 'Barbell', 'Dumbbells', 'Kettlebells']
    human_model = ["Male", "Female"]
    exercise_html_regex = r'<h3>(\n.*){4}<\/h3>(\n.*)+?(?=\n<\/ol>)'
    exercise_site_root = "http://musclewiki.com"
    available_exercises = {}
    

    def __init__(self):
        if(not path.exists("exercises.json")):
            for sex in self.human_model:
                self.available_exercises[sex] = {}
                for muscle in self.muscles:
                    self.available_exercises[sex][muscle] = {}
                    for ex_type in self.ex_types:
                        r = requests.get("{0}/{1}/{2}/{3}".format(self.exercise_site_root, ex_type, sex, muscle))
                        html_exercise_list = [x.group() for x in re.finditer(self.exercise_html_regex, r.text, re.M)]
                        html_exercise_list = [html_exercise.replace('src="', 'src="{0}'.format(self.exercise_site_root)) + '</ol>' for html_exercise in html_exercise_list] 
                        self.available_exercises[sex][muscle][ex_type] = html_exercise_list

            json.dump(self.available_exercises, open("exercises.json", 'w'))

        else:
            self.available_exercises = json.load(open("exercises.json"))

    def recommend_exercise(self):
        muscle = random.choice(self.muscles)
        ex_type = random.choice(self.ex_types)
        idx = random.randrange(len(self.available_exercises["Male"][muscle][ex_type]))
        return self.available_exercises["Male"][muscle][ex_type][idx]