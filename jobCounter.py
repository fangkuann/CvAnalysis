# coding=utf-8
__author__ = 'fangkuan'
import collections
import jieba

jskill = {}
count = 0
fin = open(u'F:/人才雷达/yincai_record_30w.txt', 'r')
for line in fin:
    count += 1
    # if count == 1000:
    #     break
    cv = line.strip().replace('null', "'null'")
    cv = eval(cv)
    skill = cv['t_pre_skill']
    job = cv['pro_title']
    if job != 'null' and len(job) > 0 and skill != 'null':
        job = job[0]
    else:
        continue
    if job not in jskill:
        jskill.update({job: [skill]})
    else:
        jskill[job].append(skill)

fin.close()

fout = open('./job_skill.txt', 'w')
for job in jskill:
    c = collections.Counter(jskill[job])
    common = c.most_common(10)
    jobs = []
    for j in common:
        jobs.append(j[0])

    fout.write(job+'\t'+','.join(jobs)+'\n')
fout.flush()
fout.close()
