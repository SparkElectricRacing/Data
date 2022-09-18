import matplotlib.pyplot as plt

def process_data(data):
    bytes = []
    for i in range(int(len(hex(data))/2)):
        bytes.append(data & 0xFF)
        data = data >> 8
        print(bytes)
        print(hex(data))

    return bytes


message = '(1662126576.477670) can0 002#910C90A55F000000'



id_start = message.index("can0") + 5
can_id = message[id_start:id_start+3]

data_start = message.index("#")
data = int(message[data_start+1:], base=16)
print('1')
print(data)
bytes = process_data(data)

print(bytes)