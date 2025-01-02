"""
多重继承
"""
class A:
    def demo(self):
        print("")
class B:
    def demo(self):
        print("")

class C(A,B):
    def test(self):
        print("C teat")
