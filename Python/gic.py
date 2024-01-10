#!/usr/bin/python3
# coding: utf-8

# MIT License
# 
# Copyright (c) 2024 Altair31
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
# 

__all__ = ["loadPrefixes", "checkAddress"]

import urllib.request
import ipaddress
import json

def loadPrefixes(fileUri:str = "https://developers.google.com/search/apis/ipranges/googlebot.json"):
    '''
    Load prefixes from Googlebot JSON list.
    By default, loads the prefixes from the official URL.
    @note Beware of being banned by Google if you abuse their bandwidth by calling this method

    @param fileName The file name to load.
    @returns Loaded prefixes
    '''

    with urllib.request.urlopen(fileUri) as file:
        return [
            ipaddress.ip_network(prefix['ipv4Prefix' if 'ipv4Prefix' in prefix else 'ipv6Prefix'])
            for prefix in json.load(file)['prefixes']
        ]
    
def checkAddress(ipAddress, prefixes):
    """
    Check an IP address

    @param ipAddress The IP address to check
    @param prefixes Prefixes loaded with loadPrefixes
    @returns True if the address is in the prefix list
    """
    ip = ipaddress.ip_address(ipAddress)
    for net in prefixes:
        if ip in net:
            return True
    return False

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print ("Usage:", sys.argv[0], " <ip-or-filename>")
    else:
        try :
            if checkAddress(ipaddress.ip_address(sys.argv[1]), loadPrefixes()):
                print(sys.argv[1], "is a Googlebot")
        except ValueError:
            with open(sys.argv[1], 'rt') as file :
                prefixes = loadPrefixes()
                for line in file:
                    address = line.strip()
                    if checkAddress(address, prefixes):
                        print(address, "is a Googlebot")
