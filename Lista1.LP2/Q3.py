def imprime_args(*args, **kwargs):
    for arg in reversed(args):
        print(arg)
    for chave in sorted(kwargs):
        print(f"{chave}: {kwargs[chave]}")
 
imprime_args(1, "a", 3.5, z=1, b=2, a=3)
 