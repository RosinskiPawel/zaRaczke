# a, b, c, d, e, f, g, h = [], [], [], [], [], [], [], []


# for x in range(9):
#     d.append(0)
#     e.append(0)
#     if x % 2:
#         a.append(0)
#         b.append(1)
#         c.append(0)
#         f.append(1)
#         g.append(0)
#         h.append(1)
#     else:
#         a.append(1)
#         b.append(0)
#         c.append(1)
#         f.append(0)
#         g.append(1)
#         h.append(0)
# z = [a, b, c, d, e, f, g, h]
# for row in z:
#     print(row)
class Warcaby:
    def __init__(self):
        pass

    def crator(self):
        a, b, c = [[0 if (i + j) % 2 else 1 for i in range(8)] for j in range(3)]
        f, g, h = [[2 if (i + j) % 2 else 0 for i in range(8)] for j in range(3)]
        d, e = [[0 for x in range(8)] for x in range(2)]
        k = ["1", "2", "3", "4", "5", "6", "7", "8"]
        print("   " + "  ".join(k))
        print("   " + "-----------------------")
        z = [
            ("A", a),
            ("B", b),
            ("C", c),
            ("D", d),
            ("E", e),
            ("F", f),
            ("G", g),
            ("H", h),
        ]
        for variable, value in z:
            print(variable, value)

        # z = [a, b, c, d, e, f, g, h]
        # for row in z:
        #     print("a", row)
