__author__ = 'fangkuan'
import collections
import jieba

jskill = {}
fin = open('d:/yincai_record_30w.txt', 'r')
for line in fin:
    cv = line.strip().replace('null', "'null'")
    cv = eval(cv)
    skill = cv['t_pre_skill']
    job = cv['pro_title']
    if job not in jskill:
        jskill.update({job: [skill]})
    else:
        jskill[job].append(skill)
fin.close()

