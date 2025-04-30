import gp_random_inconsistency
import max_refined
import inconsistency
import gp_max_inconsistency
import qualitonumber
import numpy as np

#import matplotlib.pyplot as plt 
import time

# def process_matrix(matrix):
#     """Dummy function to process a matrix. Replace with your actual function."""
#     print(f"Processing matrix:\n{matrix}\n")


def read_symbolic_matrices_from_file(filename):
    matrices = []
    matrix = []

    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            line = line.strip()
            if line.startswith("Matrix"):
                if matrix:
                    matrices.append(np.array(matrix))  # ⬅️ convert here
                    matrix = []
            elif line:
                matrix.append(line.split())
        if matrix:
            matrices.append(np.array(matrix))  # ⬅️ and here too
    
    return matrices

# Example usage:
filename = "d:/research/code/Qualitative/matrices5.txt"  # Your uploaded file
matrices = read_symbolic_matrices_from_file(filename)
num_generation=[]
all_min_inconsistencies = []
i=0
for matrix in matrices:
    min_inconsistencies, num_generation_each =max_refined.main(matrix)
    #print("min: ",min_inconsistencies)
    all_min_inconsistencies.append(min_inconsistencies)
    num_generation.append(num_generation_each)
    i+=1
    print(i,num_generation_each)#print(i,main_gp.main(matrix)[1])
print(num_generation)


#gp_max
#data=[27, 10, 7, 11, 9, 14, 17, 12, 16, 23, 12, 19, 14, 21, 15, 15, 13, 13, 25, 25, 9, 36, 10, 14, 28, 14, 14, 5, 18, 18, 22, 50, 43, 14, 22, 42, 8, 34, 22, 44, 12, 8, 3, 28, 12, 93, 24, 9, 18, 18, 4, 78, 102, 14, 85, 3, 59, 18, 20, 21, 5, 26, 5, 10, 20, 9, 15, 10, 88, 16, 16, 12, 4, 12, 15, 17, 29, 15, 3, 45, 22, 44, 27, 19, 14, 45, 14, 54, 9, 13, 6, 41, 11, 12, 6, 18, 24, 16, 12, 8]
#data_refined=[25, 10, 7, 8, 8, 10, 22, 16, 12, 21, 11, 15, 16, 22, 11, 14, 12, 11, 24, 22, 10, 36, 8, 14, 22, 11, 10, 5, 16, 13, 19, 28, 35, 14, 18, 22, 7, 55, 17, 41, 13, 9, 3, 21, 9, 58, 24, 8, 16, 14, 4, 53, 64, 12, 47, 3, 52, 18, 20, 10, 6, 16, 5, 10, 11, 8, 15, 10, 58, 13, 21, 10, 3, 11, 14, 13, 32, 11, 3, 29, 18, 37, 20, 14, 15, 33, 14, 44, 9, 10, 5, 23, 11, 13, 7, 10, 14, 17, 11, 8]
#data_withoutcross=[24, 11, 7, 10, 9, 15, 26, 16, 17, 14, 12, 29, 25, 21, 14, 15, 16, 11, 21, 15, 13, 27, 10, 19, 14, 13, 11, 6, 22, 15, 30, 17, 31, 21, 20, 20, 9, 33, 24, 31, 16, 10, 4, 17, 13, 48, 19, 9, 16, 18, 5, 37, 38, 13, 28, 4, 25, 20, 19, 14, 6, 26, 5, 18, 14, 9, 19, 16, 27, 22, 21, 13, 4, 15, 12, 21, 39, 9, 3, 31, 22, 28, 15, 14, 12, 31, 16, 26, 9, 10, 6, 44, 10, 11, 8, 13, 18, 14, 15, 13]
#number of equal=0
#near refined=0
#near to equal=2
#

#gp_random
#data=[55, 25, 27, 18, 32, 28, 25, 41, 28, 38, 60, 31, 131, 94, 20, 30, 37, 67, 60, 54, 21, 63, 23, 46, 21, 35, 23, 8, 31, 16, 58, 66, 59, 33, 73, 75, 12, 175, 54, 122, 35, 14, 3, 73, 43, 93, 37, 21, 50, 27, 6, 124, 200, 194, 81, 4, 98, 84, 46, 18, 11, 64, 8, 22, 45, 29, 52, 30, 200, 47, 56, 39, 9, 30, 32, 35, 200, 35, 2, 42, 41, 155, 64, 61, 25, 40, 89, 127, 20, 16, 14, 65, 33, 27, 11, 35, 36, 48, 20, 26]
#data_refined=[66, 33, 18, 18, 22, 20, 25, 85, 20, 26, 31, 33, 41, 44, 20, 28, 24, 24, 48, 32, 14, 56, 25, 29, 37, 24, 26, 10, 32, 15, 47, 37, 124, 29, 53, 54, 19, 54, 53, 198, 19, 11, 5, 35, 29, 101, 27, 11, 28, 26, 6, 56, 186, 43, 101, 3, 121, 40, 36, 31, 8, 57, 9, 25, 41, 27, 38, 30, 190, 39, 139, 37, 10, 29, 42, 20, 49, 14, 3, 39, 28, 41, 59, 31, 25, 61, 78, 82, 14, 21, 16, 50, 38, 21, 11, 35, 26, 31, 23, 29]
#number of equal= 0
#near refined=6
#near to equal=4


#to number
#data=[23, 16, 16, 19, 19, 18, 21, 17, 20, 20, 22, 20, 24, 22, 23, 16, 19, 21, 22, 21, 16, 27, 25, 21, 17, 18, 18, 14, 22, 18, 26, 20, 24, 22, 20, 21, 15, 26, 23, 30, 17, 10, 8, 23, 21, 31, 19, 18, 21, 18, 12, 30, 24, 16, 27, 10, 26, 25, 23, 18, 12, 23, 13, 18, 21, 17, 21, 19, 25, 23, 23, 20, 11, 17, 18, 24, 27, 17, 11, 25, 23, 24, 19, 20, 14, 24, 22, 24, 14, 19, 15, 26, 20, 15, 18, 17, 17, 18, 20, 17]
#number of equal=0
#near to equal=12


#inconsistency
#data=[16, 24, 16, 12, 12, 17, 17, 15, 16, 17, 19, 19, 19, 14, 22, 17, 12, 15, 18, 20, 20, 22, 26, 22, 17, 20, 16, 7, 17, 13, 27, 16, 21, 21, 24, 18, 10, 22, 23, 27, 21, 8, 15, 17, 16, 23, 15, 14, 18, 15, 14, 23, 17, 12, 24, 14, 21, 15, 22, 13, 17, 24, 7, 17, 24, 14, 22, 14, 17, 14, 20, 16, 6, 23, 14, 21, 23, 11, 11, 18, 14, 23, 21, 17, 11, 18, 25, 18, 8, 12, 8, 24, 21, 21, 8, 11, 14, 17, 17, 12]
#number of equal=0
#near to equal=70



