#!/bin/python3
from core.functions import clear, red, green

logo = red('Anonymous Dark Web Tool')


def banner(tor):
    clear()
    print(green(f''' 
          {logo}
          
          Tor Service: {tor} 
          
          [1] - Anonymous Mode
          [2] - Darkweb Search Engines
          [3] - Check Onion Url/s
          [4] - Scanning Host/IP
          [5] - Update
          [6] - About
          
          [0] - Exit
          '''))
    # [4] - Capture Url/s


def anonymous_banner():
    clear()
    print(green(f''' 
          {logo}
          
          [1] - Start       # start tor and redirect all traffic through tor
          [2] - Stop        # stop tor and redirect all traffic through clearnet
          [3] - Restart     # restart tor and traffic rules
          [4] - IP          # get remote ip address
          [5] - Change ID   # change tor identity
          [6] - Change Mac  # change mac addresses of all interfaces
          [7] - Revert Mac  # revert mac addresses of all interfaces
          
          [0] - Back
          '''))


def search_banner():
    clear()
    print(green(f''' 
          {logo}
          
          [1] - Ahmia
          
          [0] - Back
          '''))


def check_banner():
    clear()
    print(green(f''' 
          {logo}
          
          [1] - Single Url
          [2] - Multi Urls
          
          [0] - Back
          '''))


# def capture_banner():
#     clear()
#     print(f'''
#           {logo}

#           [ Capture ]

#           [1] - Single Url
#           [2] - Multi Urls

#           [0] - Back
#           ''')


def scan_banner():
    clear()
    print(green(f''' 
          {logo}
          
          [1] - Default (Max 65535)
          [2] - Top 1,000 TCP Ports
          
          [0] - Back
          '''))
    # [3] - Top 1,000 UDP Ports
