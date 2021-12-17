#!/bin/python3
from os import system, getlogin, getuid, path, remove, chdir, getcwd
from socket import socket, AF_INET, SOCK_STREAM, SOCK_DGRAM, SOCK_NONBLOCK, getservbyport, gethostbyname, setdefaulttimeout
from sys import exit
from requests import get
from bs4 import BeautifulSoup
from datetime import datetime
from itertools import zip_longest
from core.colors import *
import csv
import json

document_dir = f'/home/{getlogin()}/Documents'
current_date = f'{datetime.now().year}-{datetime.now().month}-{datetime.now().day}'


def check_root():
    if getuid() != 0:
        exit(red('Please run as root.'))


def clear():
    system('clear')


def command(dir='~'):
    return int(input(f'{cyan("[")} {cyan("adwt")} {yellow(dir)} {cyan("]")}{yellow("#")} ').strip().lower())


def check_tor():
    clear()
    try:
        get_ip = get('https://ipinfo.io/json', verify=True)
        system_ip = get_ip.json()['ip']
        tor_ips = get('https://check.torproject.org/exit-addresses').text
        if system_ip in tor_ips:
            adwt = {
                "tor": green('Active'),
                "ip": green(system_ip)
            }

            json_object = json.dumps(adwt, indent=4)
            with open("adwt.json", "w") as outfile:
                outfile.write(json_object)
        else:
            adwt = {
                "tor": red('Inactive'),
                "ip": red(system_ip)
            }

            json_object = json.dumps(adwt, indent=4)
            with open("adwt.json", "w") as outfile:
                outfile.write(json_object)
    except:
        print(red('[-] Please check your internet connection'))
        exit()


def get_info():
    if not path.exists('adwt.json'):
        check_tor()
    else:
        with open('adwt.json', 'r') as openfile:
            json_object = json.load(openfile)

        return json_object['tor'], json_object['ip']


def get_host(host):
    host = host.strip('https://www.')
    host = host.strip('http://www.')
    host = host.rstrip('/')

    try:
        ip = gethostbyname(host)
    except:
        ip = host

    return ip


def nmap(ip, ports, protocol='tcp'):
    ports_status = []

    startTime = datetime.now()
    print(green(f'Start at {datetime.now().strftime("%c")}'))
    print('')

    for port in ports:

        port = int(port)

        if protocol == 'tcp':
            s = socket(AF_INET, SOCK_STREAM)
        # elif protocol == 'udp':
        #     s = socket(AF_INET, SOCK_DGRAM)

        setdefaulttimeout(.3)
        r = s.connect_ex((ip, port))
        if r == 0:
            try:
                service = f'SERVICE: {getservbyport(port)}'
            except:
                service = ''
            try:
                s.connect((ip, port))
                # Protocol Information
                info = f"VERSION: {s.recv(1024).decode('utf-8')}"
            except:
                info = ''
            ports_status.append(
                green(f'[+] PORT: {port}/{protocol}   {service} {info}'))

    for port in ports_status:
        print(port)

    doneTime = float(datetime.now().strftime('%S')) - \
        float(startTime.strftime('%S'))

    print('')
    print(
        green(f'End at {datetime.now().strftime("%c")}  ({doneTime} Seconds)'))

    print('')
    s.close()


def green_input(text):
    return input(green(text))


def yellow_input(text):
    return input(yellow(text))


def final():
    input(yellow('Press Enter To Continue'))


def success(text):
    clear()
    print(green(text))
    final()


def danger(text):
    clear()
    print(red(text))
    final()
