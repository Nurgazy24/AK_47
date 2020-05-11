class Soldier:
    def __init__(self, name):
        self.name = name

class Gun:
    def __init__(self, model, max_bullets):
        self.model = model
        self.max_bullets = max_bullets
        self.bullets_count = max_bullets

    def reload(self):
        self.bullets_count = self.max_bullets
        print('Your gun reloaded')


class Act_of_Shooting(Soldier, Gun):
    def __init__(self, name, model, max_bullets):
        Soldier. __init__(self, name)
        Gun.__init__(self, model, max_bullets)

    def fire(self):
        if self.bullets_count:
            print("tigi-tish")
            self.bullets_count -= 1
        else:
            self.reload()
    
a = Act_of_Shooting('Ryan', 'AK47', 30)
a.fire()