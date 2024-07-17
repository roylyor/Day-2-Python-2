# this command write the file automatically
# has to be the top of the code chunk, thr first line codes to write as follow

class Employee:
    def __init__(self, first_name, last_name, emp_number): # attribute
        self._first_name = first_name # _first_name is a private variable
        self._last_name = last_name
        self._emp_number = emp_number

    # getter
    @property #decorator for getter
    def first_name(self):
        return self._first_name
    @property
    def last_name(self):
        return self._last_name
    @property
    def emp_number(self):
        return self._emp_number
    @property
    def full_name(self):
        return self.first_name + " " + self.last_name

    # remove setter
  
