from problem_modeling import compute_similarity
import json 
import random 

with open('csvs_and_jsons\\movie_vectors2.json', 'r') as file:
    data = json.load(file)

with open('csvs_and_jsons\\random_users.json', 'r') as file:
    users= json.load(file)

class Local_search_problem():
    def __init__(self,problem_vector):
        self.problem_vector = problem_vector

def temperature_schedule(iteration, initial_temp=1.0, decay_rate=0.99, min_temp=0.001):
    temp = initial_temp * (decay_rate ** iteration)
    return max(temp, min_temp)

def simulated_annealling(problem):
    max_similarity=0
    best_match_key=None
    for i,(key, value) in enumerate(data.items()):
        current = compute_similarity(problem.problem_vector,value)
        if current> max_similarity:
            max_similarity=current
            best_match_key=key
        else:
            random_number = random.random()
            if temperature_schedule(i)>random_number:
                max_similarity=current
                best_match_key=key
            else:
                return best_match_key
            
user_id  = 'user1'
movie ='A Christmas Carol'
initial_state = users[user_id][movie] 
recommender = Local_search_problem(initial_state)
recommended_movie = simulated_annealling(recommender)
if recommended_movie:
    print("Recommended movie:", recommended_movie)
else:
    print("No similar preference found.")