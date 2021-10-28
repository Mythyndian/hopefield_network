import numpy as np
import tkinter as tk
import time as t
from button_box import ButtonBox


def reset(tiles : list):
    for tile in tiles:
        tile.button.configure(bg='white')
        tile.value = 0


def add_as_vector(tiles : list, vectors : list):
    vector = np.zeros(64)
    for tile in tiles:
        vector[tile.id] = tile.value
    vectors.append(vector)


def add_as_test_vector(tiles : list, test_vectors : list):
    vector = np.zeros(64)
    
    for tile in tiles:
        vector[tile.id] = tile.value
    test_vectors.append(vector)
    # print(test_vector[0])


def vector_negative(vector) -> np.array:
    vector_negative = np.zeros(len(vector))
    for i in range(len(vector)):
        if vector[i] == 1:
            vector_negative[i] = 0
        else:
             vector_negative[i] = 1
    return vector_negative


def display_vector(vector, tiles):
    for i in range(len(vector)):
        if vector[i] == 1:
            tiles[i].change_color()


def run(vectors : list, test_vectors : list):
    weight_matrix = calculate_weight_matrix(*vectors)
    for vt in test_vectors:
        pre_activation_vector = np.matmul(weight_matrix, vt)
        post_activation_vector = activation_function(pre_activation_vector, vt)
        reset(buttons)
        display_vector(post_activation_vector, buttons)
        print(post_activation_vector) # for debugging purpose
        t.sleep(3)

def display_ui(buttons, vectors, test_vector):
    root = tk.Tk()
    root.title("Symbol picker")

    button_number = 0
    for i in range(8):
        for j in range(8):
            button = tk.Button(width=2, height=2, text=' ', bg='white')
            button.config(relief='solid', borderwidth=1)
            button.grid(row=i, column=j)
            buttons.append(ButtonBox(button_number, button))
            button.bind('<Button-1>', buttons[button_number].change_color)
            button_number += 1
    frame = tk.Frame(root)
    add_as_vector_button = tk.Button(text='Add as vector', width=8, height=2, command=lambda: add_as_vector(buttons, vectors))
    add_as_test_vector_button = tk.Button(text='Add as test vector', width=11, height=2, command=lambda: add_as_test_vector(buttons, test_vector))
    reset_button = tk.Button(text='Reset', width=4, height=2, command=lambda: reset(buttons))
    run_button = tk.Button(text='Run', width=3, height=2, command=lambda: run(vectors, test_vectors))
    add_as_vector_button.config(relief='solid', borderwidth=1)
    add_as_test_vector_button.config(relief='solid', borderwidth=1)
    reset_button.config(relief='solid', borderwidth=1)
    run_button.config(relief='solid', borderwidth=1)
    add_as_vector_button.grid(row=8, column=0, columnspan=2)
    add_as_test_vector_button.grid(row=8, column=2, columnspan=3 )
    reset_button.grid(row=8, column=5, columnspan=2)
    run_button.grid(row=8, column=7, columnspan=2)
    root.mainloop()


def calculate_weight_matrix(*argv) -> np.array:
    matrix = np.zeros(len(argv[0]) ** 2, dtype=np.int16)
    matrix = matrix.reshape(len(argv[0]), len(argv[0]))
    for i in range(len(argv[0])):
        for j in range(len(argv[0])):
            if i == j:
                matrix[i, j] = 0
            else:
                value = 0
                for vector in argv:
                    value += (2 * vector[i] ** i - 1) * (2 * vector[j] ** i - 1)
                matrix[i, j] = value
                matrix[j, i] = matrix[i, j]
    return matrix


def activation_function(vector: np.array, test_vector : np.array) -> np.array:
    result = []
    for p, t in zip(vector, test_vector):
        if p > 0:
            result.append(1)
        if p == 0:
            result.append(t)
        if p < 0:
            result.append(0)
    result = np.array(result)
    return result


vectors = []
buttons = []
test_vectors = []
display_ui(buttons, vectors, test_vectors)
