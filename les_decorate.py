import time
from functools import wraps
# from inspect import Signature, Parameter

def check_param(func):

    @wraps(func)
    def wrapper(*args, **kwargv):
        start_time = time.time()
        print(args)
        print(kwargv)
        # params = [ Parameter('debug', Parameter.POSITIONAL_OR_KEYWORD)]
        # sig = Signature(params)
        # bound_values = sig.bind(*args, **kwargv)
        # for name, value in bound_values:
        #     print(name, value)
        if kwargv.get('debug'):
            print('test')
            print(dir(kwargv))
            print("This is debug")
        result = func(*args, **kwargv)
        end_time = time.time()
        print("consume time:", end_time - start_time)
        return result

    return wrapper


@check_param
def add(x, y, debug=False):
    print(debug)
    return x + y

add(2,3, debug=True)
