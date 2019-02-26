#Autoreset and Programming Script for Arduino 2560
#Robert Howie
#March 2015

import serial #python serial module
import subprocess #module to call avrdude
import argparse #command line argument parsing module
import time#for sleep

#autoreset the Arduino mega by establishing a serial connection briefly at a specific baud rate
def auto_reset(com_port_name):
    arduino = serial.Serial("{0}".format(com_port_name), 9600, timeout=0) #establish serial connection to reset arduino
    time.sleep(0.5) #wait a bit before programming
    
#end auto_reset

#run avrdude to program the Arduino
def program_with_avrdude(com_port_name, hex_file):
    #call avrdude
    subprocess.call(["avrdude.exe",
        "-Cavrdude.conf",
        "-F",
        "-v",
        "-p", "atmega2560",
        "-c", "stk500v2",
        "-P",
        r"\\.\{0}".format(com_port_name),
        "-b115200",
        "-D",
        "-Uflash:w:{0}:i".format(hex_file)], shell=True)
#end program_with_avrdude

def main(): #main function
    parser = argparse.ArgumentParser()#create argument parser
    parser.add_argument("com_port_name", type=str, help="The com port that the Arduino 2560 is attached to, eg: COM4") #add com_port_name positional argument
    parser.add_argument("hex_file", type=str, help="hex file to program") #add com_port_name positional argument
    args = parser.parse_args() #parse the command line arguments
    print("Writing {0} to Arduino on {1}".format(args.hex_file, args.com_port_name))
    auto_reset(args.com_port_name) #autoreset the Arduino mega by establishing a serial connection briefly at a specific baud rate
    program_with_avrdude(args.com_port_name, args.hex_file) #run avrdude to program the Arduino
#end main

if __name__ == '__main__': #if running script directly run the main function
    main()
