def mass(n,m):
    a=[k for k in range(1,n+1)]
    q=a
    it=[1]
    while it[-1]!=a[0] or len(it)==1:
        q.extend(q[:m-1])
        q=q[m-1:]
        it.append(q[0])
    print("".join(str(x) for x in it[:-1]))
mass(5,4)