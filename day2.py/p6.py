person = {
    "firstname": "abc",
    "middlename": "aaa",
    "lastname": "xyz",
    "parents": {
        "father":{
            "name": "aaaa"
        },
        "mother":{}
    },
    "qualifications": ["SSC", "HSC", "BCA"],
    "hobbies": {},
    "isAlive": True
}

print(person)
print(person["isAlive"])

person["isAlive"] = False
print(person["isAlive"])

print(type(person))