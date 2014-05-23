# coding=utf-8
__author__ = 'fangkuan'
import collections
import jieba
import pymongo
from pymongo import MongoClient

dest = "192.168.4.250"
dbname = "yingcai"
jskill = {}
sjob = {}
count = 0
#fin = open(u'F:/人才雷达/yincai_record_30w.txt', 'r')

client = MongoClient(dest, 27017)
db = client[dbname]
yingcai = db['yingcai_userinfo']
fin = yingcai.find()

for cv in fin:
    count += 1
    if count % 1000 == 0:
        print count
    #cv = line.strip().replace('null', "'null'")
    #cv = eval(cv)
    skill = cv['t_pre_skill']
    job = cv['pro_title']
    if job and len(job) > 0 and skill:
        job = job[0]
    else:
        continue
    if job not in jskill:
        jskill.update({job: [skill]})
    else:
        jskill[job].append(skill)

    if skill not in sjob:
        sjob.update({skill: [job]})
    else:
        sjob[skill].append(job)
fin.close()

fout = open('./job_skill2.txt', 'w+')
for job in jskill:
    c = collections.Counter(jskill[job])
    common = c.most_common(10)
    jobs = []
    for j in common:
        jobs.append(j[0].encode('utf8'))
    fout.write(job.encode('utf8')+'\t'+','.join(jobs)+'\n')
fout.flush()
fout.close()

fout = open('./skill_job2.txt', 'w')
for skill in sjob:
    c = collections.Counter(sjob[skill])
    common = c.most_common(10)
    jobs = []
    for j in common:
        jobs.append(j[0].encode('utf8'))

    fout.write(skill.encode('utf8')+'\t'+','.join(jobs)+'\n')
fout.flush()
fout.close()