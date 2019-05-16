# -*- coding: utf-8 -*-
# @Time    : 2019/5/16 9:06 PM
# @Author  : alpface
# @Email   : xiaoyuan1314@me.com
# @File    : hanlp_standard_tokenizer.py
# @Software: PyCharm

import os, platform

import jpype


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


def to_string(sentence, return_generator=False):
    start_jvm_for_hanlp()
    Tokenizer = jpype.JClass('com.hankcs.hanlp.tokenizer.StandardTokenizer')
    if return_generator:
        return (word_pos_item.toString().split('/') for word_pos_item in Tokenizer.segment(sentence))
    else:
        return " ".join([word_pos_item.toString().split('/')[0] for word_pos_item in Tokenizer.segment(sentence)])


def seg_sentences(sentence, with_filter=True, return_generator=False):
    segs = to_string(sentence, return_generator=return_generator)
    drop_pos_set = set(['xu', 'xx', 'y', 'yg', 'wh', 'wky', 'wkz', 'wp', 'ws', 'wyy', 'wyz', 'wb', 'u', 'ud', 'ude1', 'ude2', 'ude3',
         'udeng', 'udh'])
    if with_filter:
        g = [word_pos_pair[0] for word_pos_pair in segs if
             len(word_pos_pair) == 2 and word_pos_pair[0] != ' ' and word_pos_pair[1] not in drop_pos_set]
    else:
        g = [word_pos_pair[0] for word_pos_pair in segs if len(word_pos_pair) == 2 and word_pos_pair[0] != ' ']
    return iter(g) if return_generator else g


def cut_hanlp(raw_sentence, return_list=True):
    if len(raw_sentence.strip()) > 0:
        return to_string(raw_sentence) if return_list else iter(to_string(raw_sentence))