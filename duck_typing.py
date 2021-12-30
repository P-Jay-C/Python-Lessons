class Duck:

    def quack(self):
        print('Quack, quack')
    
    def fly(self):
        print('Flap, flap.')

class Person:
    def quack(self):
        print("I'm quacking like a Duck!")

    def fly(self):
        print("I'am flapping my arms")


def quack_and_fly(thing):

    try:
        thing.quack()
        thing.fly()
        thing.bark()
    except AttributeError as e:
        print(e)

    print()
#nonpythonic way
'''
    if hasattr(thing,'quack'):
        if callable(thing.quack):
            thing.quack()

    if hasattr(thing,'fly'):
        if callable(thing.fly):
            thing.fly()
'''
    
'''
    if isinstance(thing,Duck):
        thing.quack()
        thing.fly()
    else:
        print("This must be a Duck")
'''
    

d = Duck()

quack_and_fly(d)

p = Person()
quack_and_fly(p)