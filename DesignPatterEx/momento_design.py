# Memento is a behavioral design pattern that lets you save and restore the previous state of an object without revealing the details of its implementation.

class Momento:
    def __init__(self, state):
        self._state = state
    
    def get_state(self):
        return self._state


class Originator:
    def __init__(self):
        self._state = None

    def set_state(self, state):
        self._state = state
    
    def save_to_momento(self):
        return Momento(self._state)

    def restore_from_momento(self, momento):
        self._state = momento.get_state()
        return self._state
    
class Caretaker:
    def __init__(self):
        self._momento = []
    
    def add_momento(self, momento):
        self._momento.append(momento)
    
    def get_momento(self,index):
        return self._momento[index]


originator = Originator()
caretaker = Caretaker()

originator.set_state("First State")
caretaker.add_momento(originator.save_to_momento())

originator.set_state("Second State")
caretaker.add_momento(originator.save_to_momento())


originator.set_state("Third State")
caretaker.add_momento(originator.save_to_momento())


print ("\n restoring the previous state")
print (originator.restore_from_momento(caretaker.get_momento(0)))

