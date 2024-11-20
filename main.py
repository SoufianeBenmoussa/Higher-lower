import random
from famous import famous_people
from art import logo, vs

def get_random_person(ppl):
  return random.sample(ppl,2)

def opt_1(prsn):
  option = list(prsn[0].values())
  option.pop(1)
  return " ,".join(option)
  
def opt_2(prsn):
  option = list(prsn[1].values())
  option.pop(1)
  return " ,".join(option)

def compare(a,b):
  if a > b:
    return "A"
  else:
    return "B"

  
choice = input("Do you want to play Higher Loowe? Type 'y' or 'n': ").lower()
people = famous_people

person = get_random_person(people)


if choice == "y":
  print(logo)
  score = 0
  
  while True:

    A = person[0]["followers"]
    B = person[1]["followers"]
    Compare = compare(A,B)
    
    print(f"Option A: {opt_1(person)}")

    print("\n" + vs)

    print(f"Option B: {opt_2(person)}")

    follow = input("\nWho has more followers 'A' or 'B': ").upper()

    if follow != Compare:
      print(f"\nYou lose! Your score is {score}")
      break

    elif follow == Compare:
      
      score += 1
      print(f"""\nYou're right! Your score is {score}
      """)

      if person[0] in people:
        people.remove(person[0])
      if person[1] in people:
        people.remove(person[1])
      if len(people) == 0:
        print("\nYou win!")
        break 
    
      if Compare == "A":
        person.remove(person[1])
      else:
        person.remove(person[0])
      
      person.append(random.choice(people))


    else:
      print("Invalid choice! Try again")

else:
  print("Goodbye!")