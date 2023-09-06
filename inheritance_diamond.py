class A(object):
    def ping(self):
        print ("ping", self)

class B(A):
    def pong(self):
        print("pong B", self)
    
class C(A):
    def pong(self):
        print ("PONG C", self)

class D(B, C):
    def ping(self):
        super(D, self).pong()
        print('post-ping:', self)

    def pingpong(self):
        self.ping()
        super(D, self).ping()
        self.pong()
        super(D, self).pong()
        C.pong(self)

obj = D()
print (obj.ping())
print ("----")
print (obj.pingpong())
