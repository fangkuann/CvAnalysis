import collections
import jieba

jskill = {}
fin = open('d:/yincai_record_30w.txt', 'r')
# for line in fin:
#     cv = line.strip().replace('null', "'null'")
#     if cv.find('php') != -1:
#         cv = eval(cv)
#         if cv['last_refresh'] != 'null':
#            #print len(cv.keys()),'\t',cv['experience'][0],'\t',cv['projects'][0],'\t',cv['work_status'],'\t',cv['pro_title'][0]#,'\t',cv['f_lang'] ,
#             try:
#                 print cv['experience'][0]['work_desc']#,'\t',cv['experience'][0]['job_name'],'\t',cv['experience'][0]['com_name'],'\t',cv['experience'][0]['com_type']
#             except TypeError:
#                 continue
#         continue
#     # print '\n'.join(cv.keys())
#     # break