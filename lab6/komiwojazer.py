import numpy as np
import matplotlib.pyplot as plt

# odlewgłośc pomiędzy dwoma punktami
def calculate_distance(point1, point2):
    return np.linalg.norm(np.array(point1) - np.array(point2))

#obliczenie długości ścieżki
def calculate_path_distance(points, path):
    distance = 0
    for i in range(len(path) - 1):
        distance += calculate_distance(points[path[i]], points[path[i + 1]])
    distance += calculate_distance(points[path[-1]], points[path[0]])
    return distance

#początkowa ścieżka
def generate_initial_path(num_points):
    return list(range(num_points))

#nowa ścieżka na podstwaie 2-opt
def get_neighboring_path(path):

    i = np.random.randint(0, len(path) - 1)
    j = np.random.randint(i + 1, len(path))
    new_path = path[:i] + path[i:j][::-1] + path[j:]
    return new_path

#akceptacja metropolis-hastings
def metropolis_hastings_acceptance(distance_current, distance_new, temperature):
    if distance_new < distance_current:
        return True
    acceptance_probability = np.exp((distance_current - distance_new) / temperature)
    return np.random.rand() < acceptance_probability

#algorytm symulowanego wyżarzania
def simulated_annealing(points, initial_temperature=100, cooling_factor=0.99, num_iterations=100000):
 
    num_points = len(points)
    current_path = generate_initial_path(num_points)
    best_path = current_path.copy()
    current_distance = calculate_path_distance(points, current_path)
    first_path = current_distance
    best_distance = current_distance
    temperature = initial_temperature

    for iteration in range(num_iterations):
        new_path = get_neighboring_path(current_path)
        new_distance = calculate_path_distance(points, new_path)

        if metropolis_hastings_acceptance(current_distance, new_distance, temperature):
            current_path = new_path
            current_distance = new_distance

        if current_distance < best_distance:
            best_path = current_path.copy()
            best_distance = current_distance

        temperature *= cooling_factor

    return best_path, best_distance, first_path

#rysowanie punktów na wykresie
def plot_path(points, path):
    
    x = [point[0] for point in points]
    y = [point[1] for point in points]

    plt.figure(figsize=(6, 6))
    plt.plot(x, y, 'bo')  # punkty
    plt.plot([points[path[i % len(path)]][0] for i in range(len(path) + 1)],
             [points[path[i % len(path)]][1] for i in range(len(path) + 1)], 'r-')  # ścieżka
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Najkrótsza ścieżka')
    plt.grid(True)
    plt.show()