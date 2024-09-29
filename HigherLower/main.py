import random
from data import celeb_data

def information(account):
    data_name = account["name"]
    data_description = account["description"]
    data_country = account["country"]
    return f"{data_name}, a {data_description}, from {data_country}"


def check_answer(a_count, b_count, user_guess):
    if a_count > b_count:
        return user_guess == "a"
    else:
        return user_guess == "b"

cont = True
score = 0
data_b = random.choice(celeb_data)

while cont:
    data_a = data_b
    data_b = random.choice(celeb_data)
    if data_a == data_b:
        data_b = random.choice(celeb_data)


    print(f" Compare A : {information(data_a)}.")
    print(f" Against B : {information(data_b)}.")


    guess = input("Make a Guess, Type 'A' or 'B' ").lower()
    a_follower_count = data_a["follower_count"]
    b_follower_count = data_b["follower_count"]


    res = check_answer(a_follower_count,b_follower_count,guess)
    if res:
        score += 1
        print(f" Yes, That's right!. Current score: {score} ")
    else:
        print(f" Nope, You've got it wrong!. Your Final score is: {score} ")
        cont = False
