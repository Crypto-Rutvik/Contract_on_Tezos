# Store Value - Example for illustrative purposes only.

import smartpy as sp

class StoreValue(sp.Contract):
    def __init__(self, value):
        self.init(storedValue = value)

    @sp.entry_point
    def replace(self, params):
        self.data.storedValue = params.value

    @sp.entry_point
    def double(self):
        self.data.storedValue *= 2

    @sp.entry_point
    def divide(self, params):
        sp.verify(params.divisor > 5)
        self.data.storedValue /= params.divisor

if "templates" not in __name__:
    @sp.add_test(name = "StoreValue")
    def test():
        c1 = StoreValue(12)
        scenario = sp.test_scenario()
        scenario.h1("Store Value")
        scenario += c1

    sp.add_compilation_target("storeValue", StoreValue(12))
