from math10 import *


factorial = factorial(10, coma=True)

print("f = ", factorial)

combination = combination(10, 3, coma=True)

print("nCr = ", combination)

permutation_with_repetition = permutationword("Tallahassee", coma=True)

print("nPr = ", permutation_with_repetition)

permutation_with_repetition_int = permutationint(11, 3, 2, 2, 2, coma=True)

print("nPr = ", permutation_with_repetition_int )

print("\n False Comma\n") #coma default value is false

circle_permutation_counter_clockwise = circle(10, counterc=True, coma=False)

print("P = ", circle_permutation_counter_clockwise, "--> Counter Clockwise")

circle_permutation_clockwise = circle(10, coma=False)

print("P = ", circle_permutation_clockwise, "--> Clockwise")

permutation_without_repetition = permutationwo(12, 6, coma=False)

print("nPr = ",permutation_without_repetition)

