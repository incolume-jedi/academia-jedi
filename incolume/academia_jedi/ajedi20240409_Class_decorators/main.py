from decorator import Accolade
from propertly import Pencil, Pen



@Accolade
def simple_function(name):
  print(name)




def run():
    """Run it."""
    simple_function('John McKinsey')
    
    HB = Pencil(100)
    print (HB.counter)
    HB.counter = 20
    print (HB.counter)


if __name__ == '__main__':
   run()