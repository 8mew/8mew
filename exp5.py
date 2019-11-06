import numpy as np
key = input("Enter a 64 bit key =")
x_len = 19
y_len = 22
z_len = 23
x = key[:x_len]
y = key[x_len:x_len + y_len]
z = key[x_len + y_len:]
x = [int(bit) for bit in x]
y = [int(bit) for bit in y]
z = [int(bit) for bit in z]

pt = input("Enter PT = ")
binary_pt = ""
for letter in pt :
    binary_pt = binary_pt + str(format(ord(letter),'08b'))
binary_pt = [int(bit) for bit in binary_pt]
print(binary_pt)
    
def get_majority(x,y,z):
    if( x+y+z > 1 ):
        return 1
    else:
        return 0

x_reg = np.array(x)
y_reg = np.array(y)
z_reg = np.array(z)
print(x_reg)
stream = []
for i in range(len(binary_pt)):
    majority = get_majority(x_reg [8], y_reg[10], z_reg[10])
    if(x_reg[8] == majority):
        new_x = x_reg[13] ^ x_reg[16] ^ x_reg[17] ^ x_reg[18]
        x_reg = np.roll(x_reg,1)
        x_reg[0] = new_x
    if(y_reg[10] == majority):
        new_y = y_reg[20] ^ y_reg[21]
        y_reg = np.roll(y_reg,1)
        y_reg[0] = new_y
    if(z_reg[10] == majority):
        new_z = z_reg[7] ^ z_reg[20] ^ z_reg[21] ^ z_reg[22]
        z_reg = np.roll(z_reg,1)
        z_reg[0] = new_z
        stream.append(x_reg[18] ^ y_reg[21] ^ z_reg[22])
print(stream)
ans = [a^b for (a,b) in zip(binary_pt,stream)]
output = ''.join(str(i) for i in ans)
print("Encrypted Key is :",output)