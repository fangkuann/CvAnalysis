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
    if cv['experience'] == 'null':
        continue

    experience = cv['experience']
    #print experience
    for li in experience:
        jname = li['job_name']

        detail = li['work_desc']
        if jname == 'null' or detail == 'null':
            continue
        words = jieba.analyse.extract_tags(detail, 15)
        if jname not in jwords:
            jwords[jname] = list(words)
        else:
            jwords[jname] += list(words)
fin.close()

fout = open('./job_keywords.txt', 'w')
for job in jwords:
    #print jwords[job]
    c = collections.Counter(jwords[job])
    common = c.most_common(10)
    jobs = []
    for j in common:
        jobs.append(j[0].encode('utf8'))
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