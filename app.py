import os
import json

pathh = os.path.join("data","karvand.json")

if not os.path.exists("data"):
    os.mkdir("data")

if not os.path.exists(pathh):
    with open (pathh, "w") as file:
        json.dump({}, file, indent=4)

msg = """
1) Add
2) Show
3) Search by ID
4) Edit
5) Delete
6) Exit
"""

def get_score():
    while True:
        try:
            score = int(input("score: "))
            if 0<= score < 101:
                return score
            else:
                print("score must be between 0 and 100")
        except ValueError:
            print("enter a valid number!")

while True:
    user = int(input(msg))

    if user == 1:
        with open(pathh, "r") as file:
            karvand = json.load(file)
        
        new_id = str(len(karvand) + 1)
        info = {
        "bootKamp" : {
           "title": input("title: "),
           "year": input("year: "),
       },

        "karvands" : {
        "ID": new_id,
        "fullName":input("name: "),
        "email":input("email: "),
        "city":input("city: "),
        "education":{
            "degree":input("degree: "),
            "field":input("field: "),
        },
        "skill":[{
            "name":input("skill name: "),
            "level":input("level: "),
            "score":get_score(),
            }] 
        }
        }
        karvand[new_id] = info

        with open(pathh, "w") as file:
            json.dump(karvand, file, indent=4)

        print("added.")

    elif user == 2:
        with open(pathh, "r") as file:
            karvand = json.load(file)
            
            if not karvand:
                print("Karvand has not been registered")
            else:
                for item in karvand.values():
                    print(f"""
                    ID:{item["karvands"]["ID"]}
                    Name:{item["karvands"]["fullName"]}
                    Email:{item["karvands"]["email"]}
                    City:{item["karvands"]["city"]}
                    Education:{item["karvands"]["education"]}
                    Skill:{item["karvands"]["skill"]}
                """)                  

    elif user == 3:
        with open(pathh , "r") as file:
            karvand = json.load(file)

            user_id = input("ID: ")
            for item in karvand.values():
                if item["karvands"]["ID"] == user_id:
                    print(f"""
                        ID:{item["karvands"]["ID"]}
                        Name:{item["karvands"]["fullName"]}
                        Email:{item["karvands"]["email"]}
                        City:{item["karvands"]["city"]}
                        Education:{item["karvands"]["education"]}
                        Skill:{item["karvands"]["skill"]}
                    """)
                    break
            else:
                print("karvand was not found with this ID")