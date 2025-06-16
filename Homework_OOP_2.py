class Matrix:
    def __init__(self, data):
        if not all(isinstance(row, list) for row in data):
            raise ValueError("Все строки должны быть списками.")
        if len(set(len(row) for row in data)) != 1:
            raise ValueError("Все строки должны иметь одинаковую длину.")
        self.data = data
        self.rows = len(data)

    def __str__(self):
        lines = []
        for row in self.data:
            line = '\t'.join(str(x) for x in row)
            lines.append(line)
        return '\n'.join(lines)



m1 = Matrix([[1, 2], [3, 4]])
m2 = Matrix([[5, 6], [7, 8]])

print(m1)
print(m2)


