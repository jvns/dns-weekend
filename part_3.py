from part_1 import header_to_bytes, question_to_bytes, encode_dns_name
from part_2 import DNSHeader, DNSQuestion, DNSRecord, DNSPacket
from part_2 import decode_name, parse_header, parse_question, parse_dns_packet
from part_2 import ip_to_string
TYPE_A = 1
CLASS_IN = 1
import random


def build_query(domain_name, record_type):
    name = encode_dns_name(domain_name)
    id = random.randint(0, 65535)
    header = DNSHeader(id=id, num_questions=1, flags=0)
    question = DNSQuestion(name=name, type_=record_type, class_=CLASS_IN)
    return header_to_bytes(header) + question_to_bytes(question)


import socket


def send_query(ip_address, domain_name, record_type):
    query = build_query(domain_name, record_type)
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(query, (ip_address, 53))
    data, _ = sock.recvfrom(1024)
    return parse_dns_packet(data)


TYPE_TXT = 16
TYPE_A = 1
TYPE_NS = 2
import struct


def parse_record(reader):
    name = decode_name(reader)
    data = reader.read(10)
    type_, class_, ttl, data_len = struct.unpack('!HHIH', data)
    if type_ == TYPE_NS:
        data = decode_name(reader)
    elif type_ == TYPE_A:
        data = ip_to_string(reader.read(data_len))
    else:
        data = reader.read(data_len)
    return DNSRecord(name, type_, class_, ttl, data)


from io import BytesIO
from part_2 import parse_header, parse_question, decode_name


def parse_dns_packet(data):
    reader = BytesIO(data)
    header = parse_header(reader)
    questions = [parse_question(reader) for _ in range(header.num_questions)]
    answers = [parse_record(reader) for _ in range(header.num_answers)]
    authorities = [parse_record(reader) for _ in range(header.num_authorities)]
    additionals = [parse_record(reader) for _ in range(header.num_additionals)]
    return DNSPacket(header, questions, answers, authorities, additionals)


def get_answer(packet):
    for x in packet.answers:
        if x.type_ == TYPE_A:
            return x.data


def get_nameserver_ip(packet):
    for x in packet.additionals:
        if x.type_ == TYPE_A:
            return x.data


def resolve_wrong(domain_name, record_type):
    nameserver = '198.41.0.4'
    while True:
        print(f'Querying {nameserver} for {domain_name}')
        response = send_query(nameserver, domain_name, record_type)
        if (ip := get_answer(response)):
            return ip
        elif (nsIP := get_nameserver_ip(response)):
            nameserver = nsIP
        else:
            raise Exception('something went wrong')


def get_nameserver(packet):
    for x in packet.authorities:
        if x.type_ == TYPE_NS:
            return x.data.decode('utf-8')


def resolve(domain_name, record_type):
    nameserver = '198.41.0.4'
    while True:
        print(f'Querying {nameserver} for {domain_name}')
        response = send_query(nameserver, domain_name, record_type)
        if (ip := get_answer(response)):
            return ip
        elif (nsIP := get_nameserver_ip(response)):
            nameserver = nsIP
        elif (ns_domain := get_nameserver(response)):
            nameserver = resolve(ns_domain, TYPE_A)
        else:
            raise Exception('something went wrong')
