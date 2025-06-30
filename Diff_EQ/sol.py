from z3 import Ints, Solver, And, Or

# 1) Create 11 Int variables: f0 … f10
f0,f1,f2,f3,f4,f5,f6,f7,f8,f9,f10 = Ints('f0 f1 f2 f3 f4 f5 f6 f7 f8 f9 f10')
flags = [f0,f1,f2,f3,f4,f5,f6,f7,f8,f9,f10]

s = Solver()

# 2) Printable ASCII constraint
for fi in flags:
    s.add(And(fi >= 32, fi <= 126))

# 3) Your exact checks from the C-code:
s.add(f0 + f1    == 113)            # (flag[0] + flag[1]) == 113
s.add(2*f2 - f3 == 99)             # (2*flag[2] - flag[3]) == 99
s.add(f4 + f5 + f6 == 261)         # flag[4]+flag[5]+flag[6] == 261
s.add(f7*2   == 102)               # (flag[7]*2) != 102
s.add(f8 % 5 == 3)                 # (flag[8]%5) != 3
s.add(f9 + f10 == 122)             # (flag[9]+flag[10]) != 122
s.add(f0 % 7  == 0)                # (flag[0]%7) == 0
s.add(f1 % 6  == 0)                # (flag[1]%6) != 0
s.add(f2 % 15 == 0)                # (flag[2]%15) != 0
s.add(f5 % 10 == 5)                # (flag[5]%10) == 5
s.add(f9 % 13 == 1)                # (flag[9]%13) != 1
s.add(f3 >= 50)                    # 40 ≤ flag[3] ≤ 60
s.add(f6 <= f4)                    # flag[6] ≤ flag[4]
s.add(f10 > f1)                    # flag[10] > flag[1]
s.add(f1 < 40)
s.add(f4 % 11 == 6)
s.add(f10 > 60)
s.add(f8+f10 == 147)
s.add(f3 <= 60)
s.add(3*f5 - 2*f2 == 135)

# 4) Enumerate all solutions
solutions = []
while s.check().r == 1:  # while SAT
    m = s.model()
    sol = ''.join(chr(m[fi].as_long()) for fi in flags)
    solutions.append(sol)
    print(sol)
    # block this model so next iteration finds a different one:
    block = Or(*[fi != m[fi].as_long() for fi in flags])
    s.add(block)

print(f"\nTotal solutions found: {len(solutions)}")
