import parts

#1. Get names of suppliers that supply bolts.
boltsupps = {supp[1] for supp in parts.suppliers
                       for r in parts.spj
                       for proj in parts.parts 
                       if r[0]==supp[0] if proj[0]==r[1] if proj[1]=='Bolt'}
print(boltsupps)

#2. Get names of suppliers that supply red parts.
redsupps = {supp[1] for supp in parts.suppliers
                       for r in parts.spj
                       for proj in parts.parts 
                       if r[0]==supp[0] if proj[0]==r[1] if proj[2]=='Red'}
print(redsupps)

#3. Get pairs of names of suppliers that are located in the same city.
suppssamecity = {(x[1], y[1]) for x in parts.suppliers
                                    for y in parts.suppliers
                                    if x[1]!=y[1] if x[3]==y[3]}
removedoubles = set(tuple(sorted(t)) for t in suppssamecity)
print(removedoubles)

#4. Print the suppliers out by city
cityname = {x[3] for x in parts.suppliers}
dict = {k: list(((d[1] for d in parts.suppliers if d[3] == k)))  for k in cityname}
print(dict)


