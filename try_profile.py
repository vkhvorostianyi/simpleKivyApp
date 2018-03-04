def custom_profiler(func):
    def wrapper():
        import cProfile, pstats, io
        pr = cProfile.Profile()
        pr.enable()
        #...do sth...
        func()
        pr.disable()
        s = io.StringIO()
        sortby = 'cumulative'
        ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
        ps.print_stats()
        print(s.getvalue())
    return wrapper


@custom_profiler
def g():
    for i in range(10000):
        i+=i**i
# print(custom_profiler)
g()