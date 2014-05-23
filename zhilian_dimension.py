# coding=utf-8
__author__ = 'fangkuan'
import collections
import jieba
import pymongo
import json
from pymongo import MongoClient

dest = "192.168.4.250"
dbname = "yingcai"
client = MongoClient(dest, 27017)
db = client[dbname]
yingcai = db['yingcai_userinfo']
fin = open('e:/zhilian_records.txt', 'r')
user_dimension = db['user_dimension']
college_loc = {}
Allinfo = []

def college_location():
    for line in open('./data/college_location.txt'):
        line = line.strip()
        college, location = line.split('\t')
        college_loc[college] = location


def cal_location(exp_location, living, education):
    if exp_location != 'null':
        return exp_location[0]
    elif living != 'null':
        return living[0]
    elif education != 'null':
        for edu in education:
            college = edu['college']
            if college in college_loc:
                return college_loc[college]
        return 'null'
    else:
        return 'null'


def cal_job(pro_title, work_experience):
    if pro_title != 'null':
        return pro_title[0]
    elif work_experience != 'null':
        for work in work_experience:
            return work['job_name']
        return 'null'
    else:
        return 'null'


def cal_dimensions():
    count = 0

    for cv in fin:
        cv = cv.strip().replace('null', "'null'")
        cv = eval(cv)
        post = {}
        uid = count
        count += 1
        if count % 1000 == 0:
            print count
        pro_title = cv['pro_title']
        exp_location = cv['exp_location']
        living = cv['living']
        education = cv['education']
        work_experience = cv['experience']

        location = cal_location(exp_location, living, education)
        job = cal_job(pro_title, work_experience)
        post['location'] = location
        post['job'] = job
        post['uid'] = str(uid).encode('utf8')
        with open('./data/zhilian_dimension.txt', mode='a') as fout:
            json.dump(post, fout, encoding='utf-8', ensure_ascii=False)
            fout.write('\n')


college_location()
cal_dimensions()
