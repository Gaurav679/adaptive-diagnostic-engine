def update_ability(current_ability, difficulty, correct):

    learning_rate = 0.1

    if correct:
        current_ability = current_ability + learning_rate * (1 - difficulty)
    else:
        current_ability = current_ability - learning_rate * difficulty

    current_ability = max(0.1, min(1.0, current_ability))

    return current_ability