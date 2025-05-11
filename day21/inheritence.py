class Animal:
    def __init__(self):
        self.num_eyes=2

    def breathe(self):
        print("inhale, exhale.")

class Fish(Animal):
        def __init__(self):
            super().__init__()

        def breathe(self):
            super().breathe()
            print("doning this underwater")

        def swim(self):
            print("moving in water")

# neno=Fish()
# neno.swim()
memo=Animal()
memo.num_eyes()