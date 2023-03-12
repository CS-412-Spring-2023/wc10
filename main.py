for i in range(1,62):
    f = open(f"inputs/input{i}.txt","r")
    with open(f"tests/survey_{i}.txt","w") as f1:
        n, q = map(int, f.readline().strip().split())
        f1.write(f"{n} {q}\n")
        for line in f.readlines():
            b, u, v = map(int, line.strip().split())
            if b == 1:
                f1.write(f"A {u} {v}\n")
            else:
                f1.write(f"B {u} {v}\n")
       