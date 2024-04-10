'''
The Observer Design Pattern is a behavioral design pattern that defines 
a one-to-many dependency between objects so that when one object changes state, 
all its dependents are notified and updated automatically. It is useful in scenarios
 where objects need to be notified of changes in another object's state without coupling them tightly.
'''

class Subject:
    def __init__(self):
        self._observer = []
    
    def attach(self, observer):
        if observer not in self._observer:
            self._observer.append(observer)
    
    def detach(self, observer):
        try:
            self._observer.remove(observer)
        except:
            pass
    
    def notify(self):
        for observer in self._observer:
            observer.update(self)

class Observer:
    def update(self, subject):
        pass

class ConcreateSubject(Subject):
    def __init__(self, state = None):
        super().__init__()
        self._state = state
    
    @property
    def state(self):
        return self._state
    
    @state.setter
    def state(self, state):
        self._state = state
        self.notify()

class ConcreateObserver(Observer):
    def update(self, subject):
        print("Observer: Subject's state has changed to {}".format(subject.state))


if __name__ == "__main__":
    subject = ConcreateSubject()
    observer1 = ConcreateObserver()
    observer2 = ConcreateObserver()
    subject.attach(observer1)
    subject.attach(observer2)
    subject.state = 1
