# write your code here
person = {
    "name": "mai",
    "age": 16,
    "hobbies": ["drawing", "cooking", "complaining"],
    }
print(person["name"])
print(person["age"])
person["age"] = 30
person["country"] = "spain"
print(person)
print(f"number of objects in dictionary: {len((person))}")
person["hobbies"].append("coding")
def check_hobbies(person):
    if len(person["hobbies"]) >= 3:
        return print("WOW YOU ARE AMAZING!")
    else:
        return print("keep exploring your hobbies!")
check_hobbies(person)