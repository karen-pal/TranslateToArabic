from Translator import Translator
import random

tr = Translator()
to_translate = [
    "my back against the cavern walls, the emptiness results in echoes, the absence of connection, pricking my skin",
    "my back hitting the cavern walls, the echoes that arise from the emptiness, no connection, pricking my skin",
    "i can feel the cavern wall surface upon my skin, i can hear the echoes filling the emptiness, null connection, pricking my skin"
    "the skin feels the cavern wall, the ear is filled with emptiness' echoes, no connection, the skin feels pain",
    "the cavern wall is felt by the skin, the echoes are heard by the ear, connection doesn't exist, pain is felt by the skin",
]


def echo(n, results_file):
    for i in range(n):
        text = random.choice(to_translate)
        translated_to_arab = tr.translate(text)
        english_again = tr.reverse(translated_to_arab)

        print(text)
        print(translated_to_arab)
        print(english_again)
        results_file.write("\n")
        results_file.write(text)
        results_file.write("\n")
        results_file.write(translated_to_arab)
        results_file.write("\n")
        results_file.write(english_again)
        results_file.write("\n")
        print(i, " [finished writting to file]")
        to_translate.append(english_again)


for i in range(2):
    results = open("results_echo" + str(i) + ".txt", "w")
    echo(10, results)
    results.close()
