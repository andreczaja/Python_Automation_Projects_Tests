class A():
    print('a')

    def metodo(self):
        print('classe a')

class B(A):
    print('b')

    def metodo(self):
        print('classe b')
class C(B):

    print('c')

    def metodo(self):
        super(B, self).metodo()

c = C()
c.metodo()
