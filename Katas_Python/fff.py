class Dictionary():
    def __init__(self):
        # Your code
        self.fruits = []
        
    def newentry(self, word, definition):
        # Your code
        print(word, definition)
        
        self.fruits.append([word,definition])
        
    def look(self, key):
        keys = [a for a in self.fruits if a[0] == key]
        if len(keys) > 0:
            return keys[0][1]
        else:
            return f"Can't find entry for {key}"
        
a = Dictionary()
a.newentry("Apple", "A fruit")
a.newentry("Soccer", "A sport")

print(a.fruits)
print(a.look("Soccer"))
