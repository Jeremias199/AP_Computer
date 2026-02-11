from math import degrees
from multiprocessing.connection import answer_challenge


def calc_Average(num1, num2):
    answer = 0
    answer = (num1 + num2) / 2
    return answer

print(calc_Average(1 , 2))
print(calc_Average(6 , 7))
print(calc_Average(2 , 84))
print(calc_Average(12 , 8))

def Add_Three(Ad1, Ad2, Ad3):
    sum = Ad1 + Ad2 + Ad3
    return sum
print(Add_Three(9,9,9))