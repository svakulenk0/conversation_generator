#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on Apr 18, 2020
.. codeauthor: svitlana vakulenko
    <svitlana.vakulenko@gmail.com>

python fetch_relevant_passage.py path_to_car
'''
import argparse
from collections import defaultdict

from trec_car.read_data import *


def get_q_ps_map(path):
    """
    Collect ids of relevant documents
    """
    q_ps = defaultdict(list)
    with open(path) as f:
        for line in f.readlines():
            qid, _, docno, relevance = line.split()
            if int(relevance) > 0:
                q_ps[qid].append(docno)
    # print(q_ps.keys())
    return q_ps


def main(path):
    q_path = "../data/2_cast_topic_goats.qrel"
    q_ps = get_q_ps_map(q_path)

    car_ps = []
    marco_ps = []
    for ps in q_ps.values():
        for p in ps:
            dataset, para_id = p.split('_')
            if dataset == 'CAR':
                car_ps.append(para_id)
            elif dataset == 'MARCO':
                marco_ps.append(para_id)
    # print("%d relevant passages for %d questions"%(len(relevant_passages), len(q_ps)))
    print(car_ps)
    print(marco_ps)

    # search relevant paragraphs
    para_map = {}
    car_paragraphs = '%s/paragraphCorpus/dedup.articles-paragraphs.cbor' % path
    with open(car_paragraphs, 'rb') as f:
        for p in iter_paragraphs(f):
            if p.para_id in car_ps:
                texts = [elem.text if isinstance(elem, ParaText)
                         else elem.anchor_text
                         for elem in p.bodies]
                para_map['CAR_'+p.para_id] = ' '.join(texts)

    marco_paragraphs = '%s/ms_marco.tsv'
    with open(marco_paragraphs, encoding='utf-8') as f:
        for i, line in enumerate(f):
            para_id, para_text = line.rstrip().split('\t')
            if para_id in marco_ps:
                para_map['MARCO_'+para_id] = para_text

    output_path = '../data/2_cast_topic_goats.tsv'
    with open(output_path, 'w') as f_out:
        for q_id, para_id in q_ps.items():
            f_out.writeline("%s\t%s"%(q_id, para_map[para_id]))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('path', type=str)
    args = parser.parse_args()
    main(args.path)
