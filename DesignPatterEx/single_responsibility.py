'''it requires that a class should have only one job.
of if a class has more than one jobs it becomes coupled.
'''

class Jurnal:
    def __init__(self):
        self.entries = []
        self.count = 0
    
    def add_entry(self, text):
        self.count += 1
        self.entries.append(f'{self.count} : {text}')
    
    def remove_entry(self, pos):
        del self.entries[pos]
    
    def __str__(self):
        return "\n".join(self.entries)
    
    def save(self, filename):
        file = open(filename, "w")
        file.write(str(self))
        file.close()
    
    def load(self):
        pass
    
    def load_from_web(self, uri):
        pass

class PersistenceManager:
    @staticmethod
    def save_to_file(journal, filename):
        file = open(filename, "w")
        file.write(str(journal))
        file.close()

j = Jurnal()
j.add_entry("i am amardip")
j.add_entry("i am swati")
print (f"journal entries: \n{j}")

p = PersistenceManager()
file = "single_responsibility.txt"
p.save_to_file(j, file)

with open(file) as fh:
    print (fh.read())
