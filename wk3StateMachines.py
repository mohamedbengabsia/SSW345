from abc import ABC, abstractmethod

class SM(ABC):
    state = 0
    startState = 0

    def start(self):
        self.state = self.startState

    # step returns the next output.
    # getNextValues returns (nextState, nextOutput)
    def step(self, inp):
        (s, o) = self.getNextValues(self.state, inp)
        self.state = s
        return o

    def transduce(self, inputs):
        self.start()
        return [self.step(inp) for inp in inputs]

    def run(self, n=10):
        return self.transduce([None] * n)

    # by default getNextValues assumes that
    # the output is the next state.
    def getNextValues(self, state, inp):
        nextState = self.getNextState(state, inp)
        return (nextState, nextState)

    @abstractmethod
    def getNextState(self, state, inp):
        pass

class Accumulator(SM):
    # predefine the startState to follow UML
    startState = 0

    def __init__(self, initialValue=0):
        self.startState = initialValue

#    state = 0
#    def getNextValues(self, state, inp):
#        return (state + inp,state + inp)

    def getNextState(self, state, inp):
        return state + inp


a = Accumulator()
print(f"{a.transduce([100,-3,4,-123,10])}")

class Gain(SM):
    def __init__(self, k):
      self.k = k

    def getNextState(self, state, inp):
        return inp * self.k


g = Gain(3)
print(f"{g.transduce([1.1, -2, 100, 5])}")

class UpDown(SM):
    startState = 0
    def getNextState(self, state, inp):
        if inp == 'u':
            return state + 1
        else:
            return state - 1

class Delay(SM):
    def __init__(self, v0):
        self.startState = v0

    def getNextState(self, state, inp):
        return 0

    def getNextValues(self, state, inp):
        return (inp, state)

d = Delay(7)
print(f"{d.transduce([3,1,2,5,9])}")

class Average2(SM):
    startState = 0
    def getNextValues(self, state, inp):
        return (inp, (inp + state) / 2.0)

    def getNextState(self, state, inp):
        return state + inp

a2 = Average2()
print(f"{a2.transduce([10,5,2,10])}")

class SimpleParkingGate(SM):
    startState = 'waiting'

    def generateOutput(self, state):
        if state == 'raising':
            return 'raise'
        elif state == 'lowering':
            return 'lower'
        else:
            return 'nop'

    def getNextValues(self, state, inp):
        (gatePosition, carAtGate, carJustExited) = inp
        if state == 'waiting' and carAtGate:
            nextState = 'raising'
        elif state == 'raising' and gatePosition == 'top':
            nextState = 'raised'
        elif state == 'raised' and carJustExited:
            nextState = 'lowering'
        elif state == 'lowering' and gatePosition == 'bottom':
            nextState = 'waiting'
        else:
            nextState = state
        return (nextState, self.generateOutput(nextState))

    def getNextState(self, state, inp):
        return state
    
# --------------- Vending machine class -------------------
class VendingMachine:
    def __init__(self):
        self.total = 0
        self.drink_cost = 75
        self.values = {
            'dollar': 100,
            'quarter': 25,
            'dime': 10,
            'nickel': 5
        }

    def receive_money(self, money):
        for coin, count in money.items():
            if coin in self.values:
                self.total += self.values[coin] * count
            else:
                print(f"Invalid currency: {coin}")
            print(f"Total money inserted {self.total} cents")
    
    def dispense(self):
        if self.total >= self.drink_cost:
            change = self.total - self.drink_cost
            self.total = 0
            if change > 0:
                return f"Drink has been served, your change is {change} cents"
            return "Drink dispensed"
        else:
            needed = self.drink_cost - self.total
            return f"Please insert {needed} cents to get your drink"
        
    def cancelled(self):
        moneyReturned = self.total
        self.total = 0
        return f"Here is your money back, {moneyReturned} cents"
    

#Testing VendingMachine class ---------
vending = VendingMachine()
vending.receive_money({'dollar': 1, 'quarter': 1})
print(vending.dispense())



gate = SimpleParkingGate()
# (gatePosition, carAtGate, carJustExited)
gateInput = [
    ('bottom', False, False),
    ('bottom', True, False),
    ('bottom', True, False),
    ('middle', True, False),
    ('middle', True, False),
    ('middle', True, False),
    ('middle', True, False),
    ('top', True, False),
    ('top', True, False),
    ('top', True, False),
    ('top', True, True),
    ('top', True, True),
    ('middle', True, False),
    ('middle', True, False),
    ('bottom', True, False),
    ('bottom', True, False)
]
print(f"{gate.transduce(gateInput)}")