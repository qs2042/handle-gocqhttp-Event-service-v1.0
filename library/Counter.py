class Counter:
    def __init__(self) -> None:
        self.n = 0
    
    def previous(self) -> int: 
        if self.n == 0: return None
        self.n -= 1
        return self.n - 1
    def current(self) -> int: 
        self.n
        return self.n
    def next(self) -> int: 
        self.n += 1
        return self.n + 1
    
    