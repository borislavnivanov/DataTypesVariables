class TestClass:
    def __init__(self, name):
        # self.name: str = name # Passes through setter
        self._name: str = name  # does NOT pass through setter Returns Tom

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if name == 'Tom':
            raise ValueError
        else:
            self._name = name

    def __str__(self):
        return f'{self.name}'

try:
    test = TestClass('Tom')
except ValueError:
    print('No object created (caught)')
else:
    print(test)
