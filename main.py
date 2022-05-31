import numpy as np
# general idea:
# parts:
# 1.implement AHP
#   find principal evec from comparison matrix
#   recursive implementation of hierarchy
#   check consistency
# 2.ask for input for comparison matrix

# structure: [factor_list] (choice level is at index 0, goal level at len(structure)-1
# factors_list: [comp_matrix for each factor] or [1 for the choice and 0 for other choices at level 0]
# or [comp_matrix for the goal] at the goal level
def ahp(structure):
    # TODO this func should print a formatted version of this program (including the process and result
    pass

def choice_level(num_of_choice):
    identity = np.identity(num_of_choice)
    level = []
    for i in range(num_of_choice):
        choice_vec = identity[i].reshape(-1, 1)
        level.append(choice_vec)
    return level

'''
comparison scale:
9: extremely favor over the other
7: very strongly
5: strongly
3: slightly
1: equal
'''
# params:
# choices be a list of choices ex: ['a', 'b', 'c', 'd']
# comparison should be a list of pair-wise comparison scores in the order like
# [a-b, a-c, a-d, b-c, b-d, c-d]
def construct_comparison_matrix(choices, comparison=None):
    if comparison is None:
        comparison = ask_to_compare()
    num_choices = len(choices)
    comp_matrix = np.identity(num_choices)

    last = 0
    for j in range(num_choices):
        i = j + 1

        num_needed = num_choices - i
        comp_matrix[j, i:] = comparison[last: last + num_needed]

        last = last + num_needed

    comp_matrix = fill_in_reciprocals(comp_matrix)
    print_comp_matrix(choices, comp_matrix)
    return comp_matrix

def fill_in_reciprocals(comp_matrix):
    row, col = comp_matrix.shape
    for i in range(row):
        for j in range(col):
            if comp_matrix[i, j] == 0:
                comp_matrix[i, j] = 1 / comp_matrix[j, i]
    return comp_matrix

# TODO
def ask_to_compare():
    return 1

# TODO
def print_comp_matrix(choices, comp_matrix):
    pass

# returns relative weight of each choice at current factor's subtree in form of list
# current_level and current factor each represents an index
def recursive_ahp(structure, current_level, current_factor):
    # base case:
    if current_level == 0:
        return structure[0][current_factor]

    # recursive case:
    factor_weight = structure[current_level][current_factor]
    factor_weight = priority_vec(factor_weight)

    previous_level = current_level - 1
    weight_matrix = []
    for factor_idx in range(len(structure[previous_level])):
        # the weight between choices for factor
        weight_vec = recursive_ahp(structure, previous_level, factor_idx)
        weight_matrix.append(weight_vec)

    # weight_matrix is a matrix with the shape of
    # (the number of choices, the number of factors in previous level)
    weight_matrix = np.hstack(weight_matrix)
    # dot product to find the weighted average by factors for each choice
    return weight_matrix @ factor_weight

# should return a np.narray with the shape of (n, 1)
def priority_vec(comparison_matrix):
    v = principal_evec(comparison_matrix)

    return v / sum(v)

def principal_evec(matrix):
    w, v = np.linalg.eig(matrix)
    real_w = w[w.imag == 0]
    real_v = v[:, w.imag == 0]

    # method 1 to find the max value's index
    # list(w).index(max(w))

    # method 2 to find the max value's index
    i = np.argmax(real_w)
    e_vec = real_v[:, i]
    e_vec = [num.real for num in e_vec]
    return np.array(e_vec).reshape(-1, 1)


def trail_run():
    print('a trail run by replicating the AHP done on the website:')
    print('https://people.revoledu.com/kardi/tutorial/AHP/AHP-Example.htm')
    level1_factors = [
        construct_comparison_matrix('XYZ', [1, 7, 3]),
        construct_comparison_matrix('xyz', [1 / 5, 1 / 2, 5])
    ]

    goal_level_weight = [
        # remember the first arg is the list of choices not the name of the level!
        construct_comparison_matrix('AB', [2])
    ]
    hierarchy = [choice_level(3),
                 level1_factors,
                 goal_level_weight
                 ]
    result = recursive_ahp(hierarchy, 2, 0)
    print(result)

def college_choice_demo():
    print('colleges are [VU, UCSD, NE] factors are [personal growth, value, atmosphere]')
    colleges = ["VU", "UCSD", "NE"]
    personal_growth_matrix = construct_comparison_matrix(colleges, [10/7, 10/9, 10/11])
    value_matrix = construct_comparison_matrix(colleges, [10/14, 10/13, 10/9])
    atmosphere_matrix = construct_comparison_matrix(colleges, [10/7, 10/7, 1])

    level1_factors = [
        personal_growth_matrix,
        value_matrix,
        atmosphere_matrix
    ]

    goal_level_weight = [
        # remember the first arg is the list of choices not the name of the level!
        construct_comparison_matrix(["personal growth", "value", "atmosphere"], [10/15, 10/7, 2])
    ]
    hierarchy = [choice_level(3),
                 level1_factors,
                 goal_level_weight
                 ]
    result = recursive_ahp(hierarchy, 2, 0)
    print(result)

if __name__ == '__main__':
    college_choice_demo()
