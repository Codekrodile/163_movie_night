import random

section1 = [
    ["What is 1 + 1?", ["2", "1", "3", "4", "5"]],
    ["What is 1 + 2?", ["3", "2", "1", "4", "5"]],
    ["What is 1 + 3?", ["4", "2", "3", "1", "5"]],
    ["What is 1 + 4?", ["5", "2", "3", "4", "1"]],
    ["What is 1 + 0?", ["1", "2", "3", "4", "5"]]
]

section2 = [
    ["What is 5 - 1?", ["4", "1", "2", "3", "5"]],
    ["What is 5 - 2?", ["3", "1", "2", "4", "5"]],
    ["What is 5 - 3?", ["2", "1", "4", "3", "5"]],
    ["What is 5 - 4?", ["1", "4", "2", "3", "5"]],
    ["What is 5 - 0?", ["5", "1", "2", "3", "4"]]    
]

section3 = [
    ["What is 4 * 1?", ["4", "1", "2", "3", "5"]],
    ["What is 3 * 1?", ["3", "1", "2", "4", "5"]],
    ["What is 2 * 1?", ["2", "1", "4", "3", "5"]],
    ["What is 1 * 1?", ["1", "4", "2", "3", "5"]],
    ["What is 5 * 1?", ["5", "1", "2", "3", "4"]]
]

def quiz(n):
    if n == 1:
        quiz = random.choice(section1)
    elif n == 2:
        quiz = random.choice(section2)
    else:
        quiz = random.choice(section3)

    return quiz[0], quiz[1][0], random.sample(quiz[1], len(quiz[1]))

if __name__ == "__main__":
    for i in range(10):
        print(quiz(1))