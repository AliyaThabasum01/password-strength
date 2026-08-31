import string


def check_strength(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Use at least 8 characters.")

    if any(char.isupper() for char in password):
        score += 1
    else:
        feedback.append("Add an uppercase letter.")

    if any(char.islower() for char in password):
        score += 1
    else:
        feedback.append("Add a lowercase letter.")

    if any(char.isdigit() for char in password):
        score += 1
    else:
        feedback.append("Add a number.")

    if any(char in string.punctuation for char in password):
        score += 1
    else:
        feedback.append("Add a special character.")

    if not feedback:
        feedback.append("Strong password!")

    return score, feedback
