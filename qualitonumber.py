import numpy as np
import random
import tkinter as tk



def qualitative_to_quantitative(value):
    mapping = {
        "≈": 1.0,  # ≈
        "⊐": 1.6,  # ⊐
        "⊃": 2.6,  # ⊃
        ">": 4.7,
        "≻": 7.0,  # ≻
        "⊏": 1 / 1.6,  # ⊏
        "⊂": 1 / 2.6,  # ⊂
        "<": 1 / 4.7,
        "≺": 1 / 7  # ≺
    }
    reverse_mapping = {
        "≈":"≈",
        "⊐": "⊏",
        "⊃": "⊂",
        ">": "<",
        "≻": "≺",
        "⊏": "⊐",
        "⊂": "⊃",
        "<": ">",
        "≺": "≻"
    }
    return mapping.get(value, None), reverse_mapping

def numeric_to_qualitative(value):
    """
    Converts a numeric value to its corresponding qualitative symbol based on the given ranges.
    """
    if 0.79 <= value <= 1.27:
        return "≈"  # Indifferent
    elif 1.27 < value <= 1.94:
        return "⊐"  # Slightly in favour
    elif 1.94 < value <= 3.17:
        return "⊃"  # In favour
    elif 3.17 < value <= 6.14:
        return ">"  # Strongly better
    elif value > 6.14:
        return "≻"  # Extremely better
    elif 1 / 7 <= value < 1 / 6.14:
        return "≺"  # Extremely worse
    elif 1 / 6.14 <= value < 1 / 3.17:
        return "<"  # Strongly worse
    elif 1 / 3.17 <= value < 1 / 1.94:
        return "⊂"  # Slightly worse
    elif 1 / 1.94 <= value < 1.27:
        return "⊏"  # Indifferent
    else:
        return "?"  # Unknown range

def convert_best_matrix_to_qualitative(best_matrix):
    """
    Converts the numeric values in the best matrix to qualitative symbols.
    """
    qualitative_matrix = []
    for row in best_matrix:
        qualitative_row = [numeric_to_qualitative(value) for value in row]
        qualitative_matrix.append(qualitative_row)
    return qualitative_matrix

def convert_matrix_to_numbers(matrix, size):
    num_matrix = []
    for i in range(size):
        row = []
        for j in range(size):
            value = matrix[i, j]  # Directly access the NumPy array element
            numerical_value, _ = qualitative_to_quantitative(value)
            row.append(numerical_value if numerical_value is not None else 0)
        num_matrix.append(row)
    return np.array(num_matrix)

# def convert_matrix_to_numbers(dropdown_vars, size):
#     matrix = []
#     for i in range(1, size + 1):
#         row = []
#         for j in range(1, size + 1):
#             value = dropdown_vars.get((i, j), tk.StringVar()).get()
#             numerical_value, _ = qualitative_to_quantitative(value)
#             row.append(numerical_value if numerical_value is not None else 0)
#         matrix.append(row)
#     return matrix


def create_child(matrix,n):
    
    size = matrix.shape[0]
    child = np.copy(matrix)
    population=[matrix]
    count= 0
    while count < n-1:
        i, j = np.random.choice(size, 2, replace=False)
        while i == j and (child[i,j]<1):  
            i, j = np.random.choice(size, 2, replace=False)
        new_value = child[i, j] + random.uniform(-0.5, 0.5)
        if (7>=new_value >= 1/7) and (7>=(1 / new_value) >= 1/7):
            child[i, j] = new_value
            child[j, i] = 1 / new_value 
        population.append(child)
        child = np.copy(matrix)
        count+=1
    return population

def compute_inconsistency_formula(A):
    n = A.shape[0]
    cm_A = 0
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if i != j and j != k and i != k:
                    term1 = abs(1 - A[i, j] / (A[i, k] * A[k, j]))
                    term2 = abs(1 - (A[i, k] * A[k, j]) / A[i, j])
                    min_inconsistency = min(term1, term2)
                    cm_A = max(cm_A, min_inconsistency)
    return cm_A

def select_top_population(population,inconsitency,n=0.5):
    inconsistency1= inconsitency
    population1=population
    new_pop=[]
    i=0
    count=n*len(population)
    while i <count:
        b=np.argmin(inconsistency1)
        new_pop.append(population1[b])
        inconsistency1.pop(b)
        population1.pop(b)
        i+=1
    return (new_pop)

def select_intact_generation(population,n=0.2):
    size=len(population)
    count=int(n*size)
    i= np.random.choice(size, count, replace=False) 
    new_pop=[] 
    for  a in i:
        new_pop.append(population[a])
    return new_pop

def crossover(parent1, parent2):
    size = parent1.shape[0]
    child = np.copy(parent1)
    crossover_point = np.random.randint(size)
    for i in range(crossover_point):
        for j in range(crossover_point):
            child[i, j] = parent2[i, j]
            if j != i:  
                child[j, i] = 1 / child[i, j] 
    return child
def select_crossover(cross,n=0.1):
    size=len(cross)
    count=int(n*size)
    i= np.random.choice(size, count, replace=False) 
    new_pop=[] 
    for  a in i:
        new_pop.append(cross[a])
    return new_pop

def select_mutate(cross,n=0.9):
    size=len(cross)
    count=int(n*size)
    i= np.random.choice(size, count, replace=False)  
    new_pop=[] 
    for  a in i:
        new_pop.append(mutation(cross[a]))
    return new_pop

def mutation(cross):
    size = cross.shape[0]
    child = np.copy(cross)
    i, j = np.random.choice(size, 2, replace=False)
    while i == j and (child[i,j]<1):  
        i, j = np.random.choice(size, 2, replace=False)
    new_value = child[i, j] + random.uniform(-0.5, 0.5)
    if (7>=new_value >= 1/7) and (7>=1 / new_value >= 1/7):
        child[i, j] = new_value
        child[j, i] = 1 / new_value
    return child

def main(matrix1):
    a=matrix1.shape[0]
    matrix=convert_matrix_to_numbers(matrix1, a)
    population_size=1000
    current_generation= create_child(matrix,population_size)
    number_generaration=0
    min_inconsistency= float('inf')
    best_min=[]
    best_matrix=[]
    all_inconsistency= []
    while number_generaration<100 and min_inconsistency> 0.3:
        k= 0
        inconsistency= []
        while k < population_size:
            inconsistency.append(compute_inconsistency_formula(current_generation[k]))
            all_inconsistency.append(compute_inconsistency_formula(current_generation[k]))
            k += 1
        min_inconsistency= min(inconsistency)
        best_matrix= current_generation[np.argmin(inconsistency)]
        best_min.append(float(min_inconsistency))
        top= select_top_population(current_generation,inconsistency)
        next_generation= select_intact_generation(top)
        k=0
        cross_child=[]
        while k< population_size*0.9:
            numbers = random.sample(range(len(top)), 2)
            parent1 = top[numbers[0]]
            parent2 = top[numbers[1]]
            cross_child.append(crossover(parent1,parent2))
            k +=1
        next_generation=next_generation+select_crossover(cross_child)+select_mutate(cross_child)
        current_generation=next_generation
        number_generaration+=1
        #print(best_min)

    # print(matrix,best_matrix,min_inconsistency,number_generaration)
    #print(best_matrix,number_generaration,min_inconsistency)
    # print(best_min)
    # print(len(all_inconsistency))
    # best_matrix=convert_best_matrix_to_qualitative(best_matrix)
    # print(best_min)
    # print(number_generaration)
    print(best_matrix)
    print(convert_best_matrix_to_qualitative(best_matrix))
    return best_min,number_generaration

# matrix =np.array( [
#     ["≈", "⊏", "≻"],
#     ["⊐", "≈", "⊂"],
#     ["≺", "⊃", "≈"]
# ])

# matrix1 =np.array( [
#     ["≈", "⊏", ">"],
#     ["⊐", "≈", "⊂"],
#     ["<", "⊃", "≈"]
# ])
Q_example = np.array([
    ["≈", "⊂", "≈", "⊏", "⊃", "≈", "<", "⊐"],
    ["⊃", "≈", ">", "≈", "≻", "⊐", "≈", ">"],
    ["≈", "<", "≈", "⊂", "⊐", "⊏", "<", "⊏"],
    ["⊐", "≈", "⊃", "≈", "≻", "≈", "⊏", ">"],
    ["⊂", "≺", "⊏", "≺", "≈", "<", "≺", "≈"],
    ["≈", "⊏", "⊐", "≈", ">", "≈", "⊂", "⊃"],
    [">", "≈", ">", "⊐", "≻", "⊃", "≈", "≻"],
    ["⊏", "<", "⊐", "<", "≈", "⊂", "≺", "≈"]
])
# matrix =np.array( [
#     ["≈", "≻", "≺", "⊂", "⊐"],
#     ["≺", "≈", "≺", "⊃", ">"],
#     ["≻", "≻", "≈", "≻", "⊏"],
#     ["⊃", "⊂", "≺", "≈", "≺"],
#     ["⊏", "<", "⊐", "≻", "≈"]
# ])

print(main(Q_example))
