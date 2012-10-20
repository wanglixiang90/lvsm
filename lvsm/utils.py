"""Common utility functions used by lvsm"""
import socket
import subprocess
import sys

DEBUG = False


def log(msg):
    if DEBUG:
        print "[DEBUG] " + msg


def parse_config(filename):
    #open config file and read it
    lines = print_file(filename)
    # list of valid config keys
    config_items = {'ipvsadm': 'ipvsadm',
                    'iptables': 'iptables',
                    'director_config': '',
                    'firewall_config': '',
                    'dsh_group': '',
                    'director': '',
                    'maintenance_dir': ''
                    }
    linenum = 0
    for line in lines:
        linenum += 1
        if line[0] == '#':
            continue
        k, sep, v = line.rstrip().partition('=')
        key = k.lstrip().rstrip()
        value = v.lstrip().rstrip()
        if config_items.get(key) is None:
            print "[ERROR] configuration file line " + str(linenum) +\
                  ": invalid variable '" + key + "'"
            sys.exit(1)
        else:
            config_items[key] = value
            # if the item is a config file, verify that the file exists
            if key.endswith('_config'):
                try:
                    file = open(value)
                    file.close()
                except IOError as e:
                    print "[ERROR] in lvsm configuration file line " +\
                          str(linenum)
                    print "[ERROR] " + e.strerror + ": '" + e.filename +\
                          "'"
                    sys.exit(1)
    return config_items


def print_file(filename):
    """opens a file and returns its contents as list"""
    lines = list()
    try:
        file = open(filename)
        lines = file.readlines()
        file.close()
    except IOError as e:
        print "[ERROR] Unable to read '" + e.filename + "'"
        print "[ERROR] " + e.strerror + ": '" + e.filename + "'"
    return lines


def getportnum(port):
    """accepts a port name or number and returns the port number as an int.
    returns -1 in case of invalid port name"""
    try:
        portnum = int(port)
        if portnum < 0 or portnum > 65535:
            print "[ERROR] invalid port number"
            portnum = -1
    except:
        try:
            p = socket.getservbyname(port)
            portnum = int(p)
        except socket.error, e:
            print "[ERROR] " + str(e)
            portnum = -1
    return portnum


def gethostname(host):
    try:
        hostip = socket.gethostbyname(host)
    except socket.gaierror as e:
        print "[ERROR] " + e.strerror
        return ''
    else:
        return hostip