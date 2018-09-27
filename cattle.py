#!/usr/bin/python
# -*- coding: utf-8 -*-

# Import the required modules.
import sys
import requests
import os
import errno
from gevent.pool import Pool

def stress_test(url):
    """
    Gets a request code from a url.
    If there's an error, abort everything!
    """

    try:
        return requests.head(url).status_code
    except:
        return "ERROR"

def parse_log(content, url):
    """
    Parse the content into string, so it can be written into the log file.
    Ugly but it works! :D

    """
    percentage = (float(content.get(200, 0)) / sum(content.values())) * 100.00
    log = \
    "Result\n" + url + "\n\n" + \
    "HTTP Status Code                  Times\n" + \
    "200 OK  ----------------------->  " + str(content.get(200, 0)) + "\n" + \
    "400 Bad Request  -------------->  " + str(content.get(400, 0)) + "\n" + \
    "403 Forbidden  ---------------->  " + str(content.get(403, 0)) + "\n" + \
    "404 Not Found  ---------------->  " + str(content.get(404, 0)) + "\n" + \
    "405 Method Not Allowed  ------->  " + str(content.get(405, 0)) + "\n" + \
    "408 Request Timeout  ---------->  " + str(content.get(408, 0)) + "\n" + \
    "409 Conflict  ----------------->  " + str(content.get(409, 0)) + "\n" + \
    "429 Too Many Requests  -------->  " + str(content.get(429, 0)) + "\n" + \
    "500 Internal Server Error  ---->  " + str(content.get(500, 0)) + "\n" + \
    "502 Bad Gateway  -------------->  " + str(content.get(502, 0)) + "\n" + \
    "503 Service Unavailable  ------>  " + str(content.get(503, 0)) + "\n" + \
    "504 Gateway Time-out  --------->  " + str(content.get(504, 0)) + "\n" + \
    "Other  ------------------------>  " + str(content.get("ERROR", 0)) + \
    "\n\n================================\n" + \
    "Rating: " + str(percentage)+ "%\n"
    return log

url='http://google.com'
pool = Pool(10)
status = pool.map(stress_test, [url] * 10)
result = dict((i, status.count(i)) for i in status)
log = parse_log(result, url)
print ("Benchmark done! Check your log file: " + log)
