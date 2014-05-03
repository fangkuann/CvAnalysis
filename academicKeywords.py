# coding=utf-8
__author__ = 'fangkuan'
import collections
import jieba
import jieba.analyse

jwords = {}
sjob = {}
count = 0
fin = open(u'F:/人才雷达/yincai_record_30w.txt', 'r')
for line in fin:
    count += 1
    # if count == 10000:
    #     break
    cv = line.strip().replace('null', "'null'")
    cv = eval(cv)
    if cv['education'] == 'null':
        continue

    experience = cv['education']
    #skill = cv['t_pre_skill']
    skill = cv['pro_title']
    #print experience
    for li in experience:
        jname = li['college']
        if jname == 'null' or skill == 'null':
            continue
        if jname not in jwords:
            jwords[jname] = skill
        else:
            jwords[jname] += skill
fin.close()

fout = open('./academic_jobs.txt', 'w')
for job in jwords:
    #print jwords[job]
    c = collections.Counter(jwords[job])
    common = c.most_common(10)
    #print common
    jobs = []
    for j in common:
        jobs.append(j[0])
#    print jobs
    fout.write(job+'\t'+','.join(jobs)+'\n')
fout.flush()
fout.close()

# fout = open('./keywords_job.txt', 'w')
# for skill in sjob:
#     c = collections.Counter(sjob[skill])
#     common = c.most_common(10)
#     jobs = []
#     for j in common:
#         jobs.append(j[0])
#
#     fout.write(skill+'\t'+','.join(jobs)+'\n')
# fout.flush()
# fout.close()