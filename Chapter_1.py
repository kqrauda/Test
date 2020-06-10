class IllegalCarError(Exception):
    pass
class Car:
    def __init__(self, pax_count, car_mass, gear_count):
        # self._pax_count = pax_count
        self.set_pax_count(pax_count)
        self.set_car_mass(car_mass)
        self.gear_count = gear_count

    def get_pax_count(self):
        return self._pax_count
    def set_pax_count(self,wawa):
        if not 1 <= wawa <= 5:
            raise IllegalCarError('pax_count should be between 1 to 5')
        self._pax_count=wawa

    @property
    def pax_count(self):
        return self._pax_count

    @pax_count.setter
    def pax_count(self,wawa):
        if not 1 <= wawa <= 5:
            raise IllegalCarError('pax_count should be between 1 to 5')
        self._pax_count=wawa
    def get_car_mass(self):
        return self.car_mass
    def set_car_mass(self,wawa2):
        if wawa2>2000:
            raise IllegalCarError('car_mass should be  less  than 2000')
        self.car_mass = wawa2
    def description_name (self):
        """zwracamy opis  samochodu """
        desc = self._pax_count,self.car_mass, self.gear_count
        return desc
    def get_total_mass ( self):
        """Rozważamy całkowitą masę samochodu"""
        pax=70
        a=self.car_mass + self._pax_count * pax
        return a
