from Translator import Translator
import random

to_translate = [
    "my back against the cavern walls, the emptiness results in echoes, the absence of connection, pricking my skin",
    "my back hitting the cavern walls, the echoes that arise from the emptiness, no connection, pricking my skin",
    "i can feel the cavern wall surface upon my skin, i can hear the echoes filling the emptiness, null connection, pricking my skin",
    "the skin feels the cavern wall, the ear is filled with emptiness' echoes, no connection, the skin feels pain",
    "the cavern wall is felt by the skin, the echoes are heard by the ear, connection doesn't exist, pain is felt by the skin",
]


class InsideCave:
    def __init__(self, *, resonance):
        self.tr = Translator()
        self.poems = to_translate
        self.resonance = resonance

    def echo(self, out_file):
        for i in range(self.resonance):
            text = random.choice(self.poems)
            translated_to_arab = self.tr.translate(text)
            english_again = self.tr.reverse(translated_to_arab)

            print(text)
            print(translated_to_arab)
            print(english_again)
            out_file.write("\n")
            out_file.write(text)
            out_file.write("\n")
            out_file.write(translated_to_arab)
            out_file.write("\n")
            out_file.write(english_again)
            out_file.write("\n")
            print(i, " [finished writting to file]")
            if english_again not in self.poems:
                self.poems.append(english_again)

    def propagate(self):
        for i in range(2):
            results = open("results_echo" + str(i) + ".txt", "w")
            self.echo(results)
            results.close()
        self.tr.close()
