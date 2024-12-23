class InfiniteRange:

    def __init__(self, start):
        self.start = start

    def __next__(self):
        self.start += 1
        return self.start
    
    def __iter__(self):
        return self
