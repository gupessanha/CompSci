# "Um menos um" não é sempre zero
x = 1.0
y = x + 1e-16
print(y - x)  # 0.0 (deveria ser 1e-16)

print("----")

# Associatividade perdida
a = 0.1
b = 0.2
c = 0.3
print((a + b) + c)  # Aproximadamente 0.6000000000000001
print(a + (b + c))  # Aproximadamente 0.6