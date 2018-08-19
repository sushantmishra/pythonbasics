class Flight:

    def __init__(self,number,aircraft):
        self._number = number
        self._aircraft = aircraft
    
    def number(self):
        return self._number # return "SN060" for the first scenario of constant string
        
    def airline(self):
        return self._number[0:2]
        
    def aircraft_model(self):
        return self._aircraft.model()
        
class Aircraft:
    
    def __init__(self,registration,model,num_rows,num_seats_per_row):
        self._registration = registration
        self._model = model
        self._num_rows = num_rows
        self._num_seats_per_row = num_seats_per_row
        
    def registration(self):
        return self._registration
        
    def model(self):
        return self._model
        
    def seating_plan(self):
        return (range(1,self._num_rows + 1),"ABCDEFGHIJK"[:self._num_seats_per_row])