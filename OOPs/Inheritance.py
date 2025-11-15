
'''

Inheritance--> transfering the properties from one class to another class
by using relationship

5 different inheritance
1. single
2. multiple
3. multilevel
4. hierarchical
5. hybrid

Single
-----
parent--> child

multilevel
------------
parent -> child--> grand child

hierarchical
-------------
parent
    child1
    child2

multiple
--------
parent1  parent2
    child

hybrid
-------
combination of two or more inheritance concepts

grandparent
    |
    parent1   parent2
        |   /
    child




Why Inheritance
---------------
it will reduce the object creations
it will increase the reusablity of the method

'''
# parent
class Venkatachalam():

    def hose(self):
        print("Chennai house")

    def land(self):
        print("ECR land")

class Radha():
    def gold(self):
        print("1KG of gold")

# child
class Karthic(Venkatachalam, Radha):

    def laptop(self):
        print("HP laptop")

    def Bike(self):
        print("FZ")

class Vijay(Venkatachalam, Radha):
    pass





venki = Venkatachalam()
venki.hose()
venki.land()


kt = Karthic()
kt.Bike()
kt.laptop()
kt.land()
kt.hose()
kt.gold()

vj = Vijay()
vj.hose()
vj.land()
vj.gold()





