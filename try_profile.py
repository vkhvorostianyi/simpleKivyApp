import cProfile, pstats, io

def a():
    for i in range(100000):
        i +=i

pr = cProfile.Profile()
pr.enable()
# ... do something ...

a()
pr.disable()
s = io.StringIO()
sortby = 'cumulative'
ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
ps.print_stats()
print(s.getvalue())

