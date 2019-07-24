# -*- coding: utf-8 -*-
"""
Created on Fri Jul 20 21:41:43 2018

@author: DELL
"""
import socket

def get_host_ip():
    # try:
    #     s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    #     s.connect(('8.8.8.8', 80))
    #     #ip = s.getsockname()[0]
    #     ip="127.0.0.1"
    # finally:
    #     s.close()
    ip = "127.0.0.1"
    return ip  

if __name__ == "__main__":
    ip = get_host_ip()
    print(ip)