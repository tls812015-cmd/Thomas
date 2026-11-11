from datetime import date, datetime
import random

OUNCES_PER_POUND = 16
DEFAULT_MOOD = "content"


def introduce_baby(baby_name, bday, current_weight_oz, height_in, baby_mood, feeding, drinks, peed, pooped):
    date_formats = ("%Y-%m-%d", "%m/%d/%Y", "%m-%d-%Y", "%B %d, %Y", "%b %d, %Y")
    birth_date = None
    for date_format in date_formats:
        try:
            birth_date = datetime.strptime(bday, date_format).date()
            break
        except ValueError:
            continue
    if birth_date is None:
        raise ValueError("Enter the baby's birthdate as YYYY-MM-DD, MM/DD/YYYY, or Month D, YYYY.")

    age_in_days = (date.today() - birth_date).days
    weight_lb = current_weight_oz / OUNCES_PER_POUND
    activity = random.choice([
        "playing basketball",
        "swinging on items like a monkey",
        "dancing",
        "singing",
        "sleeping all day",
    ])

    print(
        f"Hello! My name is {baby_name}. My birth day is {bday} and I am "
        f"{age_in_days} days old. I weigh {round(weight_lb, 2)} lbs or "
        f"{current_weight_oz} oz. I am {round(height_in, 2)} inches long and "
        f"{baby_mood}. I have ate {feeding} times, drank {drinks} times, "
        f"peed {peed} times, and pooped {pooped} times. An activity I like "
        f"to do is {activity}."
    )

baby_name = input("What's the baby's name?: ")
bday = input("What's the baby's birthdate?: ")
current_weight_oz = int(input("What is the weight in ounce?: "))
height_in = float(input("What is the babies height in inches?: "))
baby_mood = DEFAULT_MOOD
feeding=0
drinks=0
pooped=0
peed=0
action = ("eat", "drink", "sleep", "cry", "status", "home")
def eat(current_weight_oz, feeding, pooped):
    current_weight_oz += 11
    feeding += 1
    if feeding % 3 == 0:
        pooped += 1
        current_weight_oz = poop(current_weight_oz)
    return current_weight_oz, feeding, pooped
def poop(current_weight_oz):
    current_weight_oz -= 5
    print("Baby pooped. Weight decreased by 5 oz.")
    return current_weight_oz
def drink(current_weight_oz, drinks, peed):
    current_weight_oz += 8
    drinks += 1
    if drinks % 3 == 0:
        peed += 1
        current_weight_oz = pee(current_weight_oz)
    return current_weight_oz, drinks, peed
def pee(current_weight_oz):
    current_weight_oz -= 4
    print("Baby peed. Weight decreased by 4 oz.")
    return current_weight_oz
def cry():
    return "sad"
def sleep():
    return "content"
def display_status(baby_name, current_weight_oz, height_in, baby_mood, feeding, drinks, peed, pooped):
    weight_lb = current_weight_oz / OUNCES_PER_POUND
    print(
        f"{baby_name}'s current status: {baby_mood}, {round(weight_lb, 2)} lbs "
        f"({current_weight_oz} oz), {round(height_in, 2)} inches tall; "
        f"ate {feeding} times, drank {drinks} times, peed {peed} times, "
        f"and pooped {pooped} times."
    )


while action != "home":
    action = input("\nChoose an action: eat, drink, sleep, cry, status, home: ").lower()
    if action == "eat":
        current_weight_oz, feeding , pooped = eat(current_weight_oz, feeding, pooped)
        baby_mood = "happy"
    elif action == "drink":
        current_weight_oz, drinks, peed = drink(current_weight_oz, drinks, peed)
        baby_mood = "content"
    elif action == "sleep":
        baby_mood = sleep()
    elif action == "cry":
        baby_mood = cry()
    elif action == "status":
        baby_mood = input("What's the baby's status (happy, sad, content)?: ").lower()
        display_status(baby_name, current_weight_oz, height_in, baby_mood, feeding, drinks, peed, pooped)
    elif action == "home":
        print()
    else:
        print("Unknown action - try again.")
introduce_baby(baby_name, bday, current_weight_oz, height_in, baby_mood, feeding, drinks, peed, pooped)