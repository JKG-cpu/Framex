import inspect

def my_func(a):
    pass

sig = inspect.signature(my_func)
has_one_param = len(sig.parameters) == 1
print(has_one_param)