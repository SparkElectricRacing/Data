import matplotlib.pyplot as plt

def process_data(data):
    bytes = []
    # for i in range(int(len(hex(data))/2)):
    for i in range(int(len(hex(data))/2)):
        bytes.append(data & 0xFF)
        data = data >> 8
        

    return bytes

if __name__ == '__main__':
    logfile = open("bms_road_2_500A.log")
    #cansend can0
    
    times = []
    
    

    
    test_arr = set({})

    for message in logfile:

        if "can0" in message and "#" in message:
            time = float(message[1:message.index(')')])
            times.append(time)

            id_start = message.index("can0") + 5
            can_id = message[id_start:id_start+3]

            data_start = message.index("#")
            data = int(message[data_start+1:], base=16)
            bytes = process_data(data)
            
            

            if can_id == '036':
                x = len(bytes)
                print(x)
                test_arr.add(bytes[7])
                # print(message)
                # print(bytes)

print(test_arr)
print(len(test_arr))

               

            