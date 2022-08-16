#!/bin/env python3
import os
from time import sleep
from uptime import uptime

env = '/bin/bash'

def filecheck():
  """writing uptime to a file for comparing with a given time"""
  try:
    if os.path.exists("uptime.txt") :
      print("[!] uptime.txt file exsits.")

    else :
      print("[!] creating uptime.txt file")
      with open("uptime.txt", "w") as time:
        time.write("0")
  except PermissionError:
    print('Permission Error')

import sys
import base64

def encrypt_data(command):
  """Encrypt Given Output for fun :)"""
  global exec
  command = args.exec
  command_bytes = command.encode('ascii')
  base64_bytes = base64.b64encode(command_bytes)
  exec = base64_bytes.decode('ascii')
  return exec

def run(command):
  """Excecute Given Command with base64"""
  global totaltime
  command = str(f"base64 -d <<< {exec} | {env} - ")
  readtime = open('uptime.txt','r')
  systime = uptime()
  sys_time = readtime.read()
  totaltime = int(float(sys_time)) + int(systime)
  print("[!] Current time is: " + str(totaltime))

def compare_time(ostime):
  """Comparing Given Time with os uptime"""
  global totaltime
  while True :

      if not ostime:
        break

      if totaltime > ostime :
      
          print('running app')
          encrypt_data(exec)
          (__import__('os').system(__import__('base64').b64decode(exec)))
          totaltime = 0 # Reset the totaltime
          break

      else :
          print(totaltime)

      sleep(1)
      totaltime += 1
      with open("uptime.txt", "w") as file1: 
          
          # Update uptime.txt file to the new time
          file1.write(str(totaltime))

import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='systime run')
    parser.add_argument(
    "--exec",
    "-e",
    "--e",
    action="store",
    help='\texecute app',
    )
    parser.add_argument(
    "--time",
    "-t",
    "--t",
    action="store",
    type=int,
    default=0,
    help='\tset time',
    )
    
    args = parser.parse_args()
    command = args.exec

    try:
      filecheck()
      run(args.exec)
      compare_time(args.time)

      if args.time == False :
        print('[!] no time vaule enterd')
      else:
        print(f'[!] input time : {args.time}')
    except UnicodeEncodeError:
      print('[!] only ascii Cheracters allowed')
