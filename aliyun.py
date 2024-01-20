#!/usr/bin/env python3
# coding=utf-8
# liyongjian5179@163.com
# 需要先安装阿里云的接口
# pip3 install aliyun-python-sdk-core-v3
# pip3 install aliyun-python-sdk-alidns

import sys
import json
import argparse
from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.request import CommonRequest
from aliyunsdkalidns.request.v20150109.DescribeDomainRecordsRequest import DescribeDomainRecordsRequest
from aliyunsdkalidns.request.v20150109.DescribeSubDomainRecordsRequest import DescribeSubDomainRecordsRequest
from aliyunsdkalidns.request.v20150109.UpdateDomainRecordRequest import UpdateDomainRecordRequest
from aliyunsdkalidns.request.v20150109.AddDomainRecordRequest import AddDomainRecordRequest


def help_doc():
    aaa = '''
                  !!!something wrong, plz check it!!!
    usage: alidns.py [-h] [--add | --delete | --update | --get]
                          RR TYPE ADDRESS [RR TYPE ADDRESS ...]

    针对 xxx.com 域名记录进行相关操作

    positional arguments:
        RR TYPE ADDRESS  记录 类型 地址

    optional arguments:
        -h, --help       show this help message and exit
        -a, --add            add domain record. (e.g. --add RR TYPE ADDRESS)
        -d, --delete         delete domain record. (e.g. --delete RR)
        -u, --update         update domain record. (e.g. --update RR TYPE ADDRESS)
        -g, --get            get record ip. (e.g. --get RR)
    '''
    print(aaa)


def add_domain_record(rr, add_type, address):
    request = AddDomainRecordRequest()
    request.set_accept_format('json')
    request.set_Type(add_type)
    request.set_Value(address)
    request.set_Line('default')
    request.set_TTL('600')
    request.set_RR(rr)
    request.set_DomainName(domain_name)


    response = client.do_action_with_exception(request)
    # python2:  print(response)
    print(str(response, encoding='utf-8'))


def get_record_id(rr):
    sub_domain_name = rr + "." + domain_name
    try:
        request = DescribeSubDomainRecordsRequest()
        request.set_accept_format('json')
        request.set_SubDomain(SubDomain=sub_domain_name)
        response = client.do_action_with_exception(request)
        json_data = json.loads(str(response, encoding='utf-8'))
        for RecordId in json_data['DomainRecords']['Record']:
            print(RecordId, rr)
            if rr == RecordId['RR']:
                return RecordId['RecordId'], RecordId['Value']
    except Exception as e:
        print("Get RecordId Fail")
        print(e)
        sys.exit(-1)


def get_ip_address(rr):
    request = CommonRequest()
    request.set_accept_format('json')
    request.set_domain('alidns.aliyuncs.com')
    request.set_method('POST')
    request.set_protocol_type('https')  # https | http
    request.set_version('2015-01-09')
    request.set_action_name('DescribeDomainRecords')
    request.add_query_param('PageSize', '500')

    request.add_query_param('DomainName', domain_name)

    response = client.do_action_with_exception(request)
    # python2:  print(response)
    # print(str(response, encoding = 'utf-8'))
    aaa = str(response, encoding='utf-8')
    bbb = json.loads(aaa)
    # print(bbb['RecordId'])
    rr_name = bbb['DomainRecords']['Record']
    # print(rr_name)

    for item in rr_name:
        if item['RR'] == rr:
            address = item['Value']
            print('The ip address :' + item['Value'])
        else:
            continue


def delete_domain_record(rr):
    request = CommonRequest()
    request.set_accept_format('json')
    request.set_domain('alidns.aliyuncs.com')
    request.set_method('POST')
    request.set_protocol_type('https')  # https | http
    request.set_version('2015-01-09')
    request.set_action_name('DeleteSubDomainRecords')

    request.add_query_param('DomainName', domain_name)
    request.add_query_param('RR', rr)

    response = client.do_action_with_exception(request)
    # python2:  print(response)
    print(str(response, encoding='utf-8'))



def update_domain_record(rr, record_id, update_type, address):
    try:
        request = UpdateDomainRecordRequest()
        request.set_accept_format('json')
        DomainValue = address
        request.set_Value(DomainValue)
        request.set_Type(update_type)
        request.set_RR(rr)
        request.set_RecordId(RecordId=record_id)
        response = client.do_action_with_exception(request)
        print("update domain success!")
    except Exception as e:
        print("update domain fail")
        print(e)




if __name__ == "__main__":
    import csv
    import srun4k
    url = "https://gw.buaa.edu.cn"
    csvFile = csv.DictReader(open("AccessKey.csv", 'r'))
    line = csvFile.__next__()
    AccessKey_ID = line['AccessKey ID']
    Access_Key_Secret = line['AccessKey Secret']

    ret = srun4k.check_online(url)
    if ret['online']:
        ADDRESS = ret['ip']
        try:
            RR = "dyf"
            UPDATE_TYPE = 'A'
            domain_name = 'buaamc2.net'
            client = AcsClient(AccessKey_ID, Access_Key_Secret, 'default')
            response = get_record_id(RR)
            print(response)
            if response is not None:
                RECORD_ID, VALUE = response
                print("do not need to update")
                if VALUE != ADDRESS:
                    update_domain_record(RR, RECORD_ID, UPDATE_TYPE, ADDRESS)
                    print(f"update domain {RR}.{domain_name} success!")
            else:
                add_domain_record(RR, UPDATE_TYPE, ADDRESS)
                print(f"add domain {RR}.{domain_name} success!")
        except:
            print("cannot sync {}".format("dyf"))
    else:
        print("offline, please check your network connection")

