import matplotlib.pyplot as plt

def process_data(data):
    bytes = []
    for i in range(int(len(hex(data))/2)):
        bytes.append(data & 0xFF)
        data = data >> 8

    return bytes

if __name__ == '__main__':
    logfile = open("peter_pegging.log")
    #cansend can0
    
    times = []

    #001
    bms_times = []
    pack_current = []
    pack_inst_V = []
    failsafe_status = []
    high_temp = []
    low_temp = []

    #002
    high_cell_V = []
    low_cell_V = []
    pack_DCL = []
    contactor_op = []
    flags_DTC_1 = []

    #181
    mc181_times = []
    statusword = []
    velocity = []
    
    #281
    mc281_times = []
    motor_temps = []
    mc_temps = []
    warnings = []
    DCL_cir_volts = []

    #381
    mc381_times = []
    throttle_voltage = []

    #581
    mc581_times = []
    rpm = []
    rpm_scaled = []
    rpm_max_scaled = []

    for message in logfile:

        if "can0" in message and "#" in message:
            time = float(message[1:message.index(')')])
            times.append(time)

            id_start = message.index("can0") + 5
            can_id = message[id_start:id_start+3]

            data_start = message.index("#")
            data = int(message[data_start+1:], base=16)
            bytes = process_data(data)

            if can_id == '001':
                print(message)
                print(bytes)
                bms_times.append(time-times[0])

                pack_current.append(((bytes[0] << 8) + bytes[1]))
                pack_inst_V.append(((bytes[2] << 8) + bytes[3]))
                # failsafe_status.append(((bytes[4] << 8) + bytes[5]))
                # high_temp.append(bytes[6])
                # low_temp.append(bytes[7])


            
            if can_id == '002':
                print(message)
                print(bytes)
                high_cell_V.append(((bytes[0] << 8) + bytes[1]))
                low_cell_V.append(((bytes[2] << 8) + bytes[3]))
                pack_DCL.append(bytes[4])
                contactor_op.append(bytes[5])
                flags_DTC_1.append(((bytes[6] << 8) + bytes[7]))

            if can_id == '181':
                #print(message)
                #print(bytes)
                mc181_times.append(time - times[0])
                statusword.append(((bytes[4] << 8) + bytes[5]))
                #print(((bytes[0] << 32) + (bytes[1] << 16) + (bytes[2] << 8) + bytes[3]))
                velocity.append(((bytes[0] << 32) + (bytes[1] << 16) + (bytes[2] << 8) + bytes[3]))


            if can_id == '281':
                #print(message)
                #print(bytes)
                mc281_times.append(time - times[0])

                #print(bytes)

                motor_temps.append(bytes[5])
                mc_temps.append(bytes[4])
                warnings.append(((bytes[0] << 8) + bytes[1]))
                DCL_cir_volts.append((((bytes[2] << 8) + bytes[3]))*0.1)


            if can_id == '381':

                #print(message)
                #print(bytes)
                if len(bytes) > 5:
                    mc381_times.append(time - times[0])
                    throttle_voltage.append(((bytes[4] << 8) + bytes[5]) * 0.05)


            if can_id == '581':
                mc581_times.append(time - times[1])

                #print(message)
                #print(bytes)

                inst_rpm = ((bytes[0] << 32) + (bytes[1] << 16) + (bytes[2] << 8) + bytes[3])
                rpm.append(inst_rpm)

                scale = 0.05
                rpm_scaled.append(inst_rpm * scale)



    #plt.plot(bms_times, pack_inst, label='BMS Pack Inst. V')

    plt.title(logfile.name)
    plt.plot(mc581_times, rpm)
    plt.show()

    #plt.axhline(y=6000*0.05)
    #plt.plot(mc581_times, rpm_scaled, label='Scaled RPM', color='y')

    plt.plot(mc381_times, throttle_voltage, label='Throttle Voltage', color='b')
    plt.plot(mc281_times, mc_temps, label='MC Temp', color='orange')
    plt.plot(mc181_times, statusword, label='Statusword', color='g')
    plt.plot(mc281_times, warnings, label='Warnings', color='r')
    plt.plot(mc281_times, motor_temps, label='Motor Temp', color='purple')
    plt.plot(mc281_times, DCL_cir_volts, label='DC Link Circuit Voltage', color='pink')
    plt.plot(bms_times, pack_inst_V, label='Pack Inst Voltage')
    #plt.plot(mc181_times, velocity, label='Velocity', color='r')


  



    print('Warnings: ' + str(set(warnings)))
    print('Statuswords: ' + str(set(statusword)))

    print(max(mc_temps))

    plt.legend()
    plt.show()
    print(len(times))



    #new additions test graph
    plt.title('new additions test')
    plt.plot(pack_current, bms_times)
    plt.plot(pack_inst_V, bms_times)
    plt.plot(failsafe_status, bms_times)
    plt.plot(high_temp, bms_times)
    plt.plot(low_temp, bms_times)
    plt.plot(high_cell_V, bms_times)
    plt.plot(low_cell_V, bms_times)
    plt.plot(pack_DCL, bms_times)
    plt.plot(contactor_op, bms_times)
    plt.plot(flags_DTC_1, bms_times)
    plt.show()

