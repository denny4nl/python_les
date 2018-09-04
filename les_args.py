def f2(arg1, arg2, *args, **kwargs):
    print(arg1, arg2, args, kwargs)

f2(1, 2, 3)
f2(1, 2, 3, 'groovy')
f2(arg1=1, arg2=2, c=3)
f2(arg1=1, arg2=2, c=3, zzz='hi')
