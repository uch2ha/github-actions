# Esimerkkisuoritus:
#
# Kirjoita postitoimipaikka: Porvoo
# Postinumerot: 06100, 06101, 06150, 06151, 06200, 06400, 06401, 06450, 06500


import json
from typing import Optional


def get_postalcode_by_post_name(code: str)-> Optional[str]:

    f = open("postcode_map_light.json")
    data = json.load(f)

    answer = []
    answerStr = ""


    for key, value in data.items():
        if (code.upper().replace(" ","") == value) | (code.upper() == value):
            answer.append(key)



    answer.sort()

    for i in answer:
        answerStr += i+", "

    return answerStr[:-2]

    f.close()

if __name__ == "__main__":

    post_place = (input("Kirjoita postitoimipaikka:"))


    answer = get_postalcode_by_post_name(post_place)

    if answer:
        print("Postinumerot: ", end="")
        print(answer)
    else:
        print("Tuntematon postitoimipaikka")  



