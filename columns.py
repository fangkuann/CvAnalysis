# coding=utf-8
# coding=utf-8
import collections
import jieba

jskill = {}
fin = open(u'F:/人才雷达/yincai_record_30w.txt', 'r')
for line in fin:
    cv = line.strip().replace('null', "'null'")
    if cv.find('skill') != -1:
        cv = eval(cv)

        print '\n'.join(cv.keys())
        break
        if cv['last_refresh'] != 'null':
           #print len(cv.keys()),'\t',cv['experience'][0],'\t',cv['projects'][0],'\t',cv['work_status'],'\t',cv['pro_title'][0]#,'\t',cv['f_lang'] ,
            try:
                print cv['experience'][0]['work_desc']#,'\t',cv['experience'][0]['job_name'],'\t',cv['experience'][0]['com_name'],'\t',cv['experience'][0]['com_type']
            except TypeError:
                continue
        continue
    # print '\n'.join(cv.keys())
    #break