"""This is the file that contains all the functions for the levels of the game.
For every function the following applies:

Parameters:
already_done: list with the questions that have already been displayed
one_question: bool that is set to True when a question has been made and set to False when a new question needs to be generated
mistakes: list with the questions the user answered incorrectly

Returns: tuple with one_question, already_done, the generated question and the correct answer to the generated question
"""
import random

def level_1(already_done, one_question, mistakes):
    """Creates sum exercises with a maximal sum of 9."""
    first_int, second_int = random.randint(0,9), random.randint(0,9)
    chosen_operator = "+"
    question = (first_int, second_int, chosen_operator)
    if question in already_done or first_int + second_int >= 10:
        return level_1(already_done, one_question, mistakes)
    right_answer = str(first_int + second_int)
    already_done.append(question)
    one_question = True
    return (one_question, already_done, question, right_answer)

def level_2(already_done, one_question, mistakes):
    """Creates difference exercises with a minimal answer of 0 and a maximal answer of 9."""
    first_int, second_int = random.randint(0,9), random.randint(0,9)
    chosen_operator = "-"
    question = (first_int, second_int, chosen_operator)
    if question in already_done or first_int - second_int < 0:
        return level_2(already_done, one_question, mistakes)
    right_answer = str(first_int - second_int)
    already_done.append(question)
    one_question = True
    return (one_question, already_done, question, right_answer)

def level_3(already_done, one_question, mistakes):
    """Creates sum and difference exercises (Mix of level_1 and level_2)."""
    sum_and_diff = random.choice([level_1, level_2])(already_done, one_question, mistakes)
    return sum_and_diff

def level_4(already_done, one_question, mistakes):
    """Creates sum and difference exercises with a maximal sum of 20
        and minimal answer of 0."""
    chosen_operator = random.choice(["+", "-"])
    if chosen_operator == "+":
        first_int, second_int = random.randint(0,9), random.randint(0,9)
        right_answer = str(first_int + second_int)
        if int(right_answer) < 10 or int(right_answer) > 19:
            return level_4(already_done, one_question, mistakes)

    if chosen_operator == "-":
        first_int, second_int = random.randint(10,19), random.randint(0,19)
        right_answer = str(first_int - second_int)
        if int(right_answer) < 0 or int(right_answer) > 9:
            return level_4(already_done, one_question, mistakes)

    question = (first_int, second_int, chosen_operator)
    if question in already_done:
        return level_4(already_done, one_question, mistakes)
    already_done.append(question)
    one_question = True
    return (one_question, already_done, question, right_answer)

def level_5(already_done, one_question, mistakes):
    """Creates sum and difference exercises with multiplications of ten."""
    chosen_operator = random.choice(["+", "-"])
    first_int, second_int = random.randrange(10, 100, 10), random.randrange(10, 100, 10)
    if chosen_operator == "+":
        right_answer = str(first_int + second_int)
        if  first_int + second_int >= 100:
            return level_5(already_done, one_question, mistakes)

    if chosen_operator == "-":
        right_answer = str(first_int - second_int)
        if  first_int - second_int < 0:
            return level_5(already_done, one_question, mistakes)

    question = (first_int, second_int, chosen_operator)
    if question in already_done:
        return level_5(already_done, one_question, mistakes)

    already_done.append(question)
    one_question = True
    return (one_question, already_done, question, right_answer)

def level_6(already_done, one_question, mistakes):
    """Creates sum and difference exercises where sum or difference
        of the units (9 in 19, 1 in 21, 4 in 34) are lower than
        or equal to 10, or greater than 0. (ex. 31+43, 47-35, NOT: 37+45, 43-27).
        The maximal sum is 99 and the answers are always postive integers."""
    chosen_operator = random.choice(["+", "-"])
    first_int, second_int = random.randint(10,99), random.randint(10,99)
    unit_1, unit_2 = str(first_int)[-1], str(second_int)[-1]

    if chosen_operator == "+":
        right_answer = str(first_int + second_int)
        if int(unit_1) + int(unit_2) > 10 or int(right_answer) > 100:
            return level_6(already_done, one_question, mistakes)

    if chosen_operator == "-":
        right_answer = str(first_int - second_int)
        if int(right_answer) < 0 or int(unit_1) - int(unit_2) < 0:
            return level_6(already_done, one_question, mistakes)

    question = (first_int, second_int, chosen_operator)
    if question in already_done:
        return level_6(already_done, one_question, mistakes)
    already_done.append(question)
    one_question = True
    return (one_question, already_done, question, right_answer)

def level_7(already_done, one_question, mistakes):
    """Creates sum and difference exercises where sum or difference
        of the units (9 in 19, 1 in 21, 4 in 34) are higher than 9
        or lower than 0. (ex. 37+45, 43-27, NOT: 31+43, 47-35).
        The maximal sum is 99 and the answers are always postive integers."""
    chosen_operator = random.choice(["+", "-"])
    first_int, second_int = random.randint(10,99), random.randint(10,99)
    unit_1, unit_2 = str(first_int)[-1], str(second_int)[-1]

    if chosen_operator == "+":
        right_answer = str(first_int + second_int)
        if int(unit_1) + int(unit_2) <= 10 or int(right_answer) > 100:
            return level_7(already_done, one_question, mistakes)

    if chosen_operator == "-":
        right_answer = str(first_int - second_int)
        if int(right_answer) < 0 or int(unit_1) - int(unit_2) > 0:
            return level_7(already_done, one_question, mistakes)

    question = (first_int, second_int, chosen_operator)
    if question in already_done:
        return level_7(already_done, one_question, mistakes)
    already_done.append(question)
    one_question = True
    return (one_question, already_done, question, right_answer)

def level_8(already_done, one_question, mistakes):
    """Creates multiplication exercises of the tables of 1 and 10."""
    first_int, second_int = random.choice([1, 10]), random.randint(1,10)
    chosen_operator = "×"
    question = (first_int, second_int, chosen_operator)
    if question in already_done:
        return level_8(already_done, one_question, mistakes)
    right_answer = str(first_int * second_int)
    already_done.append(question)
    one_question = True
    return (one_question, already_done, question, right_answer)

def level_9(already_done, one_question, mistakes):
    """Creates multiplication exercises of the tables of 2 and 5."""
    first_int, second_int = random.choice([2, 5]), random.randint(1,10)
    chosen_operator = "×"
    question = (first_int, second_int, chosen_operator)
    if question in already_done:
        return level_9(already_done, one_question, mistakes)
    right_answer = str(first_int * second_int)
    already_done.append(question)
    one_question = True
    return (one_question, already_done, question, right_answer)

def level_10(already_done, one_question, mistakes):
    """Creates multiplication exercises of the tables of
        1, 2, 5 and 10 (Mix of level_8 and level_9)."""
    tables = random.choice([level_8, level_9])(already_done, one_question, mistakes)
    return tables

def level_11(already_done, one_question, mistakes):
    """Creates multiplication exercises of the tables of 3 and 4."""
    first_int, second_int = random.choice([3, 4]), random.randint(1,10)
    chosen_operator = "×"
    question = (first_int, second_int, chosen_operator)
    if question in already_done:
        return level_11(already_done, one_question, mistakes)
    right_answer = str(first_int * second_int)
    already_done.append(question)
    one_question = True
    return (one_question, already_done, question, right_answer)

def level_12(already_done, one_question, mistakes):
    """Creates multiplication exercises of the tables of 6 and 7."""
    first_int, second_int = random.choice([6, 7]), random.randint(1,10)
    chosen_operator = "×"
    question = (first_int, second_int, chosen_operator)
    if question in already_done:
        return level_12(already_done, one_question, mistakes)
    right_answer = str(first_int * second_int)
    already_done.append(question)
    one_question = True
    #returnt de som en het antwoord:
    return (one_question, already_done, question, right_answer)

def level_13(already_done, one_question, mistakes):
    """Creates multiplication exercises of the tables of 8 and 9."""
    first_int, second_int = random.choice([8, 9]), random.randint(1,10)
    chosen_operator = "×"
    question = (first_int, second_int, chosen_operator)
    if question in already_done:
        return level_13(already_done, one_question, mistakes)
    right_answer = str(first_int * second_int)
    already_done.append(question)
    one_question = True
    return (one_question, already_done, question, right_answer)

def level_14(already_done, one_question, mistakes):
    """Creates multiplication exercises of the tables of 1 to 10.
        (Mix of level_8, level_9, level_11, level_12 and level_13)."""
    tables = random.choice([level_8, level_9, level_11,
        level_12, level_13])(already_done, one_question, mistakes)
    return tables

def level_15(already_done, one_question, mistakes):
    """Creates division exercises of 1, 2, 5 and 10."""
    first_int, second_int = random.randint(1,100), random.choice([1, 2, 5, 10])
    chosen_operator = ":"
    question = (first_int, second_int, chosen_operator)
    if question in already_done:
        return level_15(already_done, one_question, mistakes)
    if first_int % second_int != 0 or second_int * 10 < first_int:
        return level_15(already_done, one_question, mistakes)
    right_answer = str(int(first_int / second_int))
    already_done.append(question)
    one_question = True
    return (one_question, already_done, question, right_answer)

def level_16(already_done, one_question, mistakes):
    """Creates division exercises of 3 and 4."""
    first_int, second_int = random.randint(1,40), random.choice([3, 4])
    chosen_operator = ":"
    question = (first_int, second_int, chosen_operator)
    if question in already_done:
        return level_16(already_done, one_question, mistakes)
    if first_int % second_int != 0 or second_int * 10 < first_int:
        return level_16(already_done, one_question, mistakes)
    right_answer = str(int(first_int / second_int))
    already_done.append(question)
    one_question = True
    return (one_question, already_done, question, right_answer)

def level_17(already_done, one_question, mistakes):
    """Creates division exercises of 6 and 7."""
    first_int, second_int = random.randint(1,70), random.choice([6, 7])
    chosen_operator = ":"
    question = (first_int, second_int, chosen_operator)
    if question in already_done:
        return level_17(already_done, one_question, mistakes)
    if first_int % second_int != 0 or second_int * 10 < first_int:
        return level_17(already_done, one_question, mistakes)
    right_answer = str(int(first_int / second_int))
    already_done.append(question)
    one_question = True
    return (one_question, already_done, question, right_answer)

def level_18(already_done, one_question, mistakes):
    """Creates division exercises of 8 and 9."""
    first_int, second_int = random.randint(1,90), random.choice([8, 9])
    chosen_operator = ":"
    question = (first_int, second_int, chosen_operator)
    if question in already_done:
        return level_18(already_done, one_question, mistakes)
    if first_int % second_int != 0 or second_int * 10 < first_int:
        return level_18(already_done, one_question, mistakes)
    right_answer = str(int(first_int / second_int))
    already_done.append(question)
    one_question = True
    return (one_question, already_done, question, right_answer)

def level_19(already_done, one_question, mistakes):
    """Creates division exercises of 1 to 10.
        (Mix of level_15, level_16, level_17, level_18).
        level_15 shows up twice because there are 4 numbers (1, 2, 5, 10)
        as opposed to the other functions (those have 2)."""
    division = random.choice([
        level_15, level_15, level_16, level_17, level_18
        ])(already_done, one_question, mistakes)
    return division

def level_20(already_done, one_question, mistakes):
    """Creates division and multiplication exercises of 1 to 10.
        (Mix of level_14 and level_19)."""
    mul_and_div = random.choice([level_14, level_19])(already_done, one_question, mistakes)
    return mul_and_div

def level_21(already_done, one_question, mistakes):
    """Creates sum and difference exercises with a maximal
        sum of 20 and a minimal answer of 0. Also includes
        the exercises with tens with a maximal sum of 100.
        (Mix of level_3, level_4 and level_5)."""
    mix = random.choice([level_3, level_4, level_5])(already_done, one_question, mistakes)
    return mix

def level_22(already_done, one_question, mistakes):
    """Creates sum and difference exercises with a maximal
        sum of 99 and a minimal answer of 0. (Mix of level_3,
        level_4, level_5, level_6 and level_7)."""
    mix = random.choice([level_3, level_4, level_5, level_6, level_7])(already_done, one_question, mistakes)
    return mix

def level_23(already_done, one_question, mistakes):
    """Creates sum, difference and multiplication exercises with a
        maximal sum of 99 and a minimal answer of 0. The multiplication
        exercises are of the tables of 1 to 10. (Mix of level_4,
        level_5, level_6, level_7 and level_14)."""
    mix = random.choice([level_4, level_5, level_6, level_7, level_14])(already_done, one_question, mistakes)
    return mix

def level_24(already_done, one_question, mistakes):
    """Creates sum, difference and division exercises with a
        maximal sum of 99 and a minimal answer of 0. The division
        exercises are of 1 to 10. (Mix of level_4,
        level_5, level_6, level_7 and level_19)."""
    mix = random.choice([level_4, level_5, level_6, level_7, level_19])(already_done, one_question, mistakes)
    return mix

def level_25(already_done, one_question, mistakes):
    """Ultimate megamix of sum, difference, multiplication and
        division exercises. Maximal sum 99, all answers are
        postive. Tables and division exercises are of 1 to 10.
        (Mix of level_6, level_7, level_14 and level_19)."""
    megamix = random.choice([level_6, level_7, level_14, level_19])(already_done, one_question, mistakes)
    return megamix

levels = [
    level_1, level_2, level_3, level_4, level_5,
    level_6, level_7, level_8, level_9, level_10,
    level_11, level_12, level_13, level_14, level_15,
    level_16, level_17, level_18, level_19, level_20,
    level_21, level_22, level_23, level_24, level_25
        ]
