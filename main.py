print("Welcome to Voter Eligibility Checker ")
print("You will be asked a number of questions to see if you can vote or not...")

print()

age = int(input("How old are you? "))

def yes_no(prompt):
    answer = "\0"
    while answer.lower() not in ["y", "n"]:
        answer = input(f'{prompt} (y/n): ')
    return answer == "y"

citizen = yes_no("Are you a legal citizen of the United States?")
registered = yes_no("Are you registered to vote?")
incarcerated = yes_no("Are you currently serving a sentence or being incarcerated for a crime?")

print()

if age >= 18 and citizen and registered and not incarcerated:
    print("You are eligible to vote")
else:
    print("Sorry, you are not eligible to vote")
