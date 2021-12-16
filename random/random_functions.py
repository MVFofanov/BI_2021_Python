import numpy as np
import random
import time
import matplotlib.pyplot as plt
from collections import defaultdict
import re


def compare_random_and_numpy():
    random_times = dict()
    np_times = dict()

    for i in range(1, 1001):
        start = time.time()
        for _ in range(i):
            random.uniform(0, 1)
        stop = time.time()
        random_times[i] = stop - start

    for j in range(1, 1001):
        start = time.time()
        np.random.uniform(size=j)
        stop = time.time()
        np_times[j] = stop - start

    x_random = random_times.keys()
    y_random = np.array(list(random_times.values())) * (10 ** 6)
    x_np = np_times.keys()
    y_np = np.array(list(np_times.values())) * (10 ** 6)

    plt.plot(x_random, y_random, color='red', label='random')
    plt.plot(x_np, y_np, color='blue', label='numpy')
    plt.title('Random and numpy time calculation comparison')
    plt.xlabel('Times')
    plt.ylabel('Time (microseconds)')
    plt.legend()
    plt.grid()
    plt.show()


def is_sorted(mylist):
    return all(mylist[i] <= mylist[i + 1] for i in range(len(mylist) - 1))


def monkey_sort(mylist):
    while (is_sorted(mylist) is False):
        np.random.shuffle(mylist)


def monkey_sort_visualization():
    mylist = [1, 2, 45, 16, 2024, 78, 34, 99, 12, 0, 617, 3]
    time_dic = defaultdict(list)

    for length in range(2, 10):
        for _ in range(5):
            mylist = np.random.normal(size=length)
            start = time.time()
            monkey_sort(mylist)
            stop = time.time()
            time_dic[length].append(stop - start)

    time_list = time_dic.keys()
    y_means = np.array(list(np.array(time_dic[i]).mean() for i in time_list))
    y_sd = np.array(list(np.array(time_dic[i]).std() for i in time_list))

    plt.errorbar(time_list, y_means, y_sd, marker='^', linestyle='None')
    plt.title('Monkey sort comparison results')
    plt.xlabel('List length')
    plt.ylabel('Time (seconds)')
    plt.show()
    plt.close()


def generate_random_walk(n):
    x = y = 0
    X_list, Y_list = list(), list()
    step = (-1, 1)
    for _ in range(n):
        x += np.random.choice(step)
        y += np.random.choice(step)
        X_list.append(x)
        Y_list.append(y)
    return X_list, Y_list


def make_random_walk_plot():
    x, y = generate_random_walk(100000)
    plt.figure(figsize=(10, 10))
    plt.scatter(x, y, s=0.1)
    plt.ylabel('y', fontsize=14)
    plt.xlabel('x', fontsize=14)
    plt.title('Random walk plot', fontsize=20)
    plt.show()


def make_sierpinski_triangle_plot():
    steps = 10000
    x = (0, 50, 100)
    y = (0, 100, 0)
    points_index = (0, 1, 2)
    x_point = [0]
    y_point = [0]
    for _ in range(steps):
        ind = random.choice(points_index)
        x_point.append((x[ind] + x_point[-1]) / 2)
        y_point.append((y[ind] + y_point[-1]) / 2)
    fig, ax = plt.subplots()
    ax.scatter(x_point, y_point)
    ax.set_title("Sierpinski's Triangle")
    plt.show()


def shuffle(letters, last_char):
    result = letters[1: last_char]
    random.shuffle(result)
    return ''.join(result)


def make_words_shuffle(word):
    letters = list(word)
    if len(letters) <= 3:
        return word
    if re.match(r"\w", letters[-1]):
        return f"{letters[0]}{shuffle(letters, -1)}{letters[-1]}"
    else:
        return f"{letters[0]}{shuffle(letters, -2)}{''.join(letters[-2:])}"


def make_text_shuffle(text):
    words = text.split()
    print(*list(map(make_words_shuffle, words)))


if __name__ == "__main__":
    compare_random_and_numpy()
    monkey_sort_visualization()
    make_random_walk_plot()
    make_sierpinski_triangle_plot()
    make_text_shuffle('''
    По рзеузльаттам илссоевадний одонго анлигсйокго унвиертисета, не иеемт занчнеия,
    в каокм проякде рсапжоолены бкувы в солве.
    Галовне, чотбы преавя и пслонедяя бквуы блыи на мсете.
    осатьлыне бкувы мгоут селдовтаь в плоонм бсепордяке, все-рвано ткест чтаитсея без побрелм.
    Пичрионй эгото ялвятеся то, что мы не чиаетм кдаужю бкуву по отдльенотси, а все солво цлиеком.
    ''')
