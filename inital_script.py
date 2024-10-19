from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from collections import deque

preferences = [
    [[0, 0, 0, 1, 1, 1], [1, 0, 1, 0, 1, 0]],
    [[0, 0, 0, 1, 1, 1], [0, 0, 1, 1, 1, 1]]
]
movies = [
    [['inception'], ['avatar']],
    [['The platform'], ['12 angry men']]
]

class Node:
    def __init__(self, state, parent, action, path_cost):
        self.state = state
        self.parent = parent
        self.action = action
        self.path_cost = path_cost
    
    @classmethod
    def root(cls, init_state):
        return cls(init_state, None, None, 0)

    @classmethod
    def child(cls, problem, parent, action):
        return cls(
            problem.result(parent.state, action),
            parent,
            action,
            parent.path_cost + 1
        )

class movieRecommender:
    def __init__(self, initial_state, initial_index):
        self.initial_state = initial_state
        self.initial_index = initial_index
        self.visited = set()  

    def actions(self, vector, index):
        vector_copy = vector[:]
        if vector_copy[index] == 0:
            vector_copy[index] = 1
        else:
            vector_copy[index] = 0
        return vector_copy

    def goal_test(self, original_vector):
        for group in range(len(preferences)):
            for i, preference in enumerate(preferences[group]):
                if preference != self.initial_state:
                    if self.computeSimilarity(original_vector, preference) ==1:
                        return (group, i) 
        return False

    def computeSimilarity(self, vector1, vector2):
        vector1 = np.array(vector1).reshape(1, -1)
        vector2 = np.array(vector2).reshape(1, -1)
        similarity = cosine_similarity(vector1, vector2)
        return similarity[0][0]
    
    def result(self, state, action):
        return action

def breadth_first_tree_search(problem, user_index, movie_index):
    frontier = deque([Node.root(problem.initial_state)])
    while frontier:
        node = frontier.popleft()
        state_tuple = tuple(node.state)
        print(state_tuple)
        if state_tuple in problem.visited:
            continue
        problem.visited.add(state_tuple)
        goal_result = problem.goal_test(node.state)
        if goal_result:
            group, preference_index = goal_result
            return movies[group][preference_index][0]
        for i in range(len(preferences[user_index][movie_index])):
            new_state = problem.actions(node.state, i)
            child_node = Node.child(problem, node, new_state)

            frontier.append(child_node)
    return None

initial_state = preferences[0][0]
recommender = movieRecommender(initial_state, 0)
recommended_movie = breadth_first_tree_search(recommender, user_index=0, movie_index=0)
if recommended_movie:
    print("Recommended movie:", recommended_movie)
else:
    print("No similar preference found.")



