import re
import datetime
import json


class IpAddress:
    def __init__(self, ip_address: str):
        self.ip_address = ip_address

    def __str__(self):
        return self.ip_address


class Request:
    def __init__(self, req_text):
        self.method = " ".split(req_text)[0]
        self.path = " ".split(req_text)[1]
        self.protocol = " ".split(req_text)[2]


class Status:
    def __init__(self, req_text):
        self.status = req_text



class Log:
    def __init__(self, ip_addr, access_datetime, request, status, bytes: int, file, referer):
        self.ip_addr = ip_addr
        self.access_datetime = access_datetime
        self.request = request
        self.starus = status
        self.bytes = bytes
        self.file = file
        self.referer = referer


class LogParser:
    def __init__(self, log_text):
        self.raw_text = log_text

        ip_addr_pattern = re.compile(r"^(\d{1,3}\.){3}\d{1,3}")
        self.ip_addr = ip_addr_pattern.search(log_text).group(0)  # type: str
        log_text = ip_addr_pattern.sub("", log_text)

        access_datetime_pattern = re.compile(r"^\s\S+\s\S+\s\[(\d{2}/\w{3}/\d{4}:\d{2}:\d{2}:\d{2}\s[+-]\d{4})\]")
        self.access_datetime = datetime.datetime.strptime(access_datetime_pattern.search(log_text).group(1), "%d/%b/%Y:%H:%M:%S %z")
        log_text = access_datetime_pattern.sub("", log_text)

        request_pattern = re.compile(r"^\s\"([A-Z]{3,7}\s\S+\s\S+)\"")
        self.request = request_pattern.search(log_text).group(1)
        log_text = request_pattern.sub("", log_text)

        status_pattern = re.compile(r"^\s(\d+)")
        self.status = int(status_pattern.search(log_text).group(1))
        log_text = status_pattern.sub("", log_text)
        # self.bytes = bytes
        # self.file = file
        # self.referer = referer


file_path = "./log_tiny.log"
with open(file_path, "r") as log_file:
    parsed_list = [LogParser(line) for line in log_file]

for parser in parsed_list:
    if parser.status == 404:
        print("Detected 404 at:", parser.access_datetime, "\nRaw data:", parser.raw_text)




