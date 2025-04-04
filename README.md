Movie Recommendation System using AI Search & Q-Learning


Movie Recommendation System uses **Graph Search Algorithms**, **Q-Learning**, and **Genetic Algorithms** to recommend movies based on user preferences 



---


##  Algorithms Used

### Search Algorithms:
- **Breadth-First Search (BFS)**
- **Depth-First Search (DFS)**
- **Uniform Cost Search (UCS)**
- **Greedy Best-First Search (GBFS)**
- **A\* Search**
- **Iterative Deepening Search (IDS)**

All of these search methods work by navigating through the connections between movie similarities and genres to uncover the best recommendations.

###  Q-Learning (Reinforcement Learning):
- **States**: Binary movie vectors (representing features)
- **Actions**: flip Bit to change features
- **Rewards**: Cosine similarity improvement
- **Training**: Over 1000 episodes with a trained Q-table
- **Output**: A sequence of recommended movies using learned policy

### Genetic Algorithm:
- Generate user preferences 
- Develop movie recommendations based on crossover and mutation
- Score users on similarity to user profile

---

## Files

- `movie_dataset.csv`, `cleaned_movie_dataset.csv`: Instead making vectors manually a dataset used to build vactors of films 
- `movie_vectors.json`: Binary vector for each movie
- `q_table_trained.json`: Q-values after learning optimal policy
- `random_users.json`: user preferences profiles
- `random_connections_graph.json`: Graph used in search algorithms

---

## Results (Q-Learning)

- Cosine similarity improved with iteration
- Most effective actions were stored in Q-table
- End policy can successfully recommend movies of the same genre
- Step-by-step explanation in `Qlearning.pdf`


---

## Visualization

All graph-based algorithm visualizations can be seen in your browser:

- `html_files/astar_movie_recommendation.html`
- `html_files/bfs_tree.html`
- `html_files/dfs_tree.html`
- `html_files/weighted_graph_visualization.html`

These show how each algorithm traverses the movie network to provide recommendations.

---

## How to Run

### 1. Install Dependencies

```bash
pip install numpy pandas scikit-learn matplotlib
```

### 2. Preprocess Data

```bash
python cleaning_and_generation_files/dataCleaning.py
```

### 3. Train Q-Learning

```bash
python searching/qlearning.py
```

### 4. Generate Recommendations

```bash
python searching/qlearning_test.py
```

### 5. Visualize Graph Searches

Open any file in `html_files/` in your browser to see traversal paths.


## License

This project is under the MIT License.
