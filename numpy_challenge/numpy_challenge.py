import numpy as np


def type_your_input_array(INPUT_ARRAY_TEXT):
    return np.array([(row.split(",")) for row in input(INPUT_ARRAY_TEXT).split(";")], dtype=int)


def make_my_favorite_arrays():
    arrays_list = [np.zeros(9), np.arange(3, 28, 3).reshape(3, 3), np.eye(4)]
    for i in range(3):
        print(f'My favorite array {i + 1} is \n{arrays_list[i]}\n')


def matrix_multiplication(matrix_1, matrix_2):
    return np.matmul(matrix_1, matrix_2)


def multiplication_check(array_list):
    if multiply_matrices(array_list) is None:
        return False
    else:
        return True


def multiply_matrices(array_list):
    product_matrix = array_list[0]
    for i in range(1, len(array_list)):
        columns_1 = product_matrix.shape[1]
        rows_2 = array_list[i].shape[0]
        if columns_1 == rows_2:
            product_matrix = matrix_multiplication(product_matrix, array_list[i])
        else:
            return None
    return product_matrix


def compute_2d_distance(array_1, array_2):
    if array_1.size == array_2.size == 2:
        return np.sqrt(np.sum((array_1 - array_2) ** 2))
    else:
        return 'This arrays are not 2d!'


def compute_multidimensional_distance(array_1, array_2):
    return np.sqrt(np.sum((array_1 - array_2) ** 2))


def compute_pair_distances(array):
    n = array.shape[0]
    distance_matrix = np.zeros((n, n))
    for i in range(n - 1):
        distance = np.sqrt(np.sum((array[i, ] - array[i + 1:, ]) ** 2))
        distance_matrix[i, i + 1:] = distance
        distance_matrix[i + 1:, i] = distance
    return distance_matrix


def greeting_message():
    text = '''
    Welcome to the NumPy universe!
    Here, you can find some useful functions which can be called via following commands:

    Available commands:                      Input:                          Output:

    matrix multiplication (mmul)             two matrices                    producat matrix
    multiplication check (mc)                matrix list                     boolean test result of matrices possibility
                                                                             to be multiplied
    multiply matrices (mmat)                 matrix list                     multiplication matrices product
    compute 2d distance (c2dd)               two arrays (1 dimension)        calculated distance between these points
                                                                             coordinates
    compute multidimensional distance (cmd)  two arrays (1 dimension)        calculated distance between these arrays
    compute pair distances (cpd)             one array (2 dimension)         paired distance matrix

    Functions have the same names as commands above with only space (' ') replaced with the underscore character ('_')
    Commands can be used via its short forms indicated in the brackets in the first column

    Type "exit", "quit", "e" or "q" to quit the program
    '''
    return text


def input_data_processing():
    AVAILABLE_FUNCTIONS = {
        "matrix multiplication": matrix_multiplication,
        "mmul": matrix_multiplication,
        "multiplication check": multiplication_check,
        "mc": multiplication_check,
        "multiply matrices": multiply_matrices,
        "mmat": multiply_matrices,
        "compute 2d distance": compute_2d_distance,
        "c2dd": compute_2d_distance,
        "compute multidimensional distance": compute_multidimensional_distance,
        "cmd": compute_multidimensional_distance,
        "compute pair distances": compute_pair_distances,
        "cpd": compute_pair_distances
                    }
    INPUT_ARRAY_TEXT = "Type your array, columns should be separated with commas while rows with semicolons: "

    print(greeting_message())
    make_my_favorite_arrays()
    try:
        while True:
            command = input("Type your command: ").lower()
            if command in {"exit", "quit", "e", "q"}:
                print("It is enough numpy magic for today. Have a nice day without any arrays and matrices!")
                break
            elif command in {"multiplication check", "multiply matrices", "mc", "mmat"}:
                array_list = []
                text_mes = f'Type your matrix list, matrices should be separated with spaces, {INPUT_ARRAY_TEXT[17:]}'
                array_list_input = input(text_mes).split()
                for matrix in array_list_input:
                    input_array = np.array([(row.split(",")) for row in matrix.split(";")], dtype=int)
                    array_list.append(input_array)
                print(AVAILABLE_FUNCTIONS[command](array_list))
            elif command in {"matrix multiplication", "compute 2d distance", "compute multidimensional distance",
                             "mmul", "c2dd", "cmd"}:
                print('Type your two arrays ')
                input_array = type_your_input_array(INPUT_ARRAY_TEXT)
                second_array = type_your_input_array(INPUT_ARRAY_TEXT)
                print(AVAILABLE_FUNCTIONS[command](input_array, second_array))
            elif command in {"compute pair distances", "cpd"}:
                input_array = type_your_input_array(INPUT_ARRAY_TEXT)
                print(AVAILABLE_FUNCTIONS[command](input_array))
            else:
                print('Invalid command. Try again!')
    except ValueError:
        print("Invalid input array format!")


if __name__ == "__main__":
    input_data_processing()
