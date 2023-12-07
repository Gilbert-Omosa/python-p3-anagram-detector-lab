# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, word_list):
        return [w for w in word_list if sorted(w) == sorted(self.word)]
    
# Examples

print(Anagram("listen").match(["enlist", "silent", "inlets", "tinsel", "eternal"]))
print(Anagram("restrain").match(["strainer", "terrains", "trainers", "retrains"]))
print(Anagram("medical").match(["declaim", "decimal", "claimed", "melodic", "melancholy"]))
print(Anagram("ranged").match(["garden", "danger", "gander", "grander", "grandar"]))
