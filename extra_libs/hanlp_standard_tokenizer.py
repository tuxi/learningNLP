# -*- coding: utf-8 -*-
# @Time    : 2019/5/16 9:06 PM
# @Author  : alpface
# @Email   : xiaoyuan1314@me.com
# @File    : hanlp_standard_tokenizer.py
# @Software: PyCharm

import os, platform, re
import jpype

# 通过hanlp进行分词，配置

def start_jvm_for_hanlp():

    if jpype.isJVMStarted() == True:
        return

    from extra_libs import extra_libs_dir

    root_path = os.path.join(extra_libs_dir, 'hanlp_source')
    hanlp_jar_path = os.path.join(root_path, 'hanlp-1.7.3.jar')

    if os.path.exists(hanlp_jar_path) == False:
        raise FileNotFoundError(
            '{path} is not found, download link: https://pan.baidu.com/s/1JYpHqOO4qDGtEytH8J_0Pw'.format(
                path=hanlp_jar_path))

    if (platform.system() == 'Windows'):
        djclass_path = "-Djava.class.path={hanlp_jar_path};{root_path}".format(hanlp_jar_path=hanlp_jar_path,root_path=root_path)
    else:
        djclass_path = "-Djava.class.path={hanlp_jar_path}:{root_path}".format(hanlp_jar_path=hanlp_jar_path,
                                                                               root_path=root_path)

        jpype.startJVM(jpype.getDefaultJVMPath(), djclass_path, "-Xms1g", "-Xmx1g")


# def to_string(sentence, return_generator=False):
#     start_jvm_for_hanlp()
#     Tokenizer = jpype.JClass('com.hankcs.hanlp.tokenizer.StandardTokenizer')
#     if return_generator:
#         return (word_pos_item.toString().split('/') for word_pos_item in Tokenizer.segment(sentence))
#     else:
#         # for word_pos_item in Tokenizer.segment(sentence):
#         #     a = word_pos_item.toString().split('/')[0]
#         #     print(a)
#         return " ".join([word_pos_item.toString().split('/')[0] for word_pos_item in Tokenizer.segment(sentence)])

def to_string(sentence,return_generator=False):
    start_jvm_for_hanlp()
    Tokenizer = jpype.JClass('com.hankcs.hanlp.tokenizer.StandardTokenizer')
    if return_generator:
        return (word_pos_item.toString().split('/') for word_pos_item in Tokenizer.segment(sentence))
    else:
        return [(word_pos_item.toString().split('/')[0],word_pos_item.toString().split('/')[1]) for word_pos_item in Tokenizer.segment(sentence)]

keep_pos="q,qg,qt,qv,s,t,tg,g,gb,gbc,gc,gg,gm,gp,m,mg,Mg,mq,n,an,vn,ude1,nr,ns,nt,nz,nb,nba,nbc,nbp,nf,ng,nh,nhd,o,nz,nx,ntu,nts,nto,nth,ntch,ntcf,ntcb,ntc,nt,nsf,ns,nrj,nrf,nr2,nr1,nr,nnt,nnd,nn,nmc,nm,nl,nit,nis,nic,ni,nhm,nhd"
keep_pos_nouns=set(keep_pos.split(","))
keep_pos_v="v,vd,vg,vf,vl,vshi,vyou,vx,vi"
keep_pos_v=set(keep_pos_v.split(","))
keep_pos_p=set(['p','pbei','pba'])
# 需要去掉的词性，此集合中的词性根据hanlp官方的词性列表添加
drop_pos_set=set(['xu','xx','y','yg','wh','wky','wkz','wp','ws','wyy','wyz','wb','u','ud','ude1','ude2','ude3','udeng','udh','p','rr'])
han_pattern=re.compile(r'[^\dA-Za-z\u3007\u4E00-\u9FCB\uE815-\uE864]+')

def seg_sentences(sentence,with_filter=True,return_generator=False):
    segs=to_string(sentence,return_generator=return_generator)
    if with_filter:
        # 根据drop_pos_set 过滤不需要的词性
        g = [word_pos_pair[0] for word_pos_pair in segs if len(word_pos_pair)==2 and word_pos_pair[0]!=' ' and word_pos_pair[1] not in drop_pos_set]
    else:
        g = [word_pos_pair[0] for word_pos_pair in segs if len(word_pos_pair)==2 and word_pos_pair[0]!=' ']
    return iter(g) if return_generator else g

def cut_hanlp(raw_sentence, return_list=True):
    if len(raw_sentence.strip()) > 0:
        return to_string(raw_sentence) if return_list else iter(to_string(raw_sentence))