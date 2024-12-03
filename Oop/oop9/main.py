class Hendler:

    def __init__(self,methods=("GET",)):
        self.methods = methods

    def __call__(self, func, *args, **kwargs):
        type_methods = {
            "GET": self.get,
            "POST": self.post,
        }

        def wrapper(request, *args, **kwargs):
            if request["methods"] not in self.methods:
                raise f'Данная страница не принимает тип запросов {request["methods"]}'
            return type_methods[request["methods"]](func, request, *args, **kwargs)
        
    def get(self, func, request, *args, **kwargs):
        return func(request, *args, **kwargs)
    
    def post(self, func, request, *args, **kwargs):
        return func(request, *args, **kwargs)
    
@Hendler(methods=("POST",))
def get_page(request):
    return "Привет мир"

# print(get_page({"methods": "POST",}))

class Power:

    def __init__(self, n):
        self.n = n
    
    def __call__(self, func, *args, **kwargs):
        print(func(self) ** self.n)
        
    
@Power(2)
def degree(a):
    return 3

class Repeat:
    def __init__(self, n):
        self.n = n

    def __call__(self, func, *args, **kwargs):
        i = 0
        while(i < self.n):
            i += 1
            print(func(self))

@Repeat(3)
def function(a):
    return "asda"

