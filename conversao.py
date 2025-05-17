import struct

def float_to_binary(num):
    """Converte um float para sua representação binária IEEE-754."""
    # Obtém a representação em bytes de um float64
    bytes_val = struct.pack('>d', num)
    
    # Converte para um inteiro de 64 bits
    int_val = int.from_bytes(bytes_val, 'big')
    
    # Converte para representação binária
    binary = bin(int_val)[2:].zfill(64)
    
    # Formata para leitura
    sign = binary[0]
    exponent = binary[1:12]
    mantissa = binary[12:]
    
    return {
        "binary": binary,
        "sign": sign,
        "exponent": exponent,
        "mantissa": mantissa,
        "parts": f"S:{sign} E:{exponent} M:{mantissa}"
    }


# Exemplos

print("Exemplos de conversão de float para binário:\n")

print("Números com representação exata\n")
# Números com representação exata   
nums = [0.1, 0.2, 0.3]
for num in nums:
    parts = float_to_binary(num)
    print(f"{num}: {parts['parts']}")
    
# Saída:
# 1.0: S:0 E:01111111111 M:0000000000000000000000000000000000000000000000000000
# -1.0: S:1 E:01111111111 M:0000000000000000000000000000000000000000000000000000
# 2.0: S:0 E:10000000000 M:0000000000000000000000000000000000000000000000000000
# 0.5: S:0 E:01111111110 M:0000000000000000000000000000000000000000000000000000

print("\nNúmeros com representação inexata\n")
# # Números com representação inexata
# nums = [0.1, 1e-10]
# for num in nums:
#     parts = float_to_binary(num)
#     print(f"{num}: {parts['parts']}")
    
# # Saída:
# # 0.1: S:0 E:01111111011 M:1001100110011001100110011001100110011001100110011010
# # 1e-10: S:0 E:01111001101 M:1011111000100101110000110011110111110001100111001100


# import numpy as np

# print("\nNúmeros especiais\n")
# special_nums = [np.inf, -np.inf, np.nan]
# for num in special_nums:
#     parts = float_to_binary(num)
#     print(f"{num}: {parts['parts']}")
    
# # Saída:
# # inf: S:0 E:11111111111 M:0000000000000000000000000000000000000000000000000000
# # -inf: S:1 E:11111111111 M:0000000000000000000000000000000000000000000000000000
# # nan: S:0 E:11111111111 M:1000000000000000000000000000000000000000000000000000