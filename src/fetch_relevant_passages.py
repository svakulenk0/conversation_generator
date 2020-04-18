#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on Apr 18, 2020
.. codeauthor: svitlana vakulenko
    <svitlana.vakulenko@gmail.com>

'''
import pyndri
from collections import defaultdict


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


def main():
	path = "../data/2_cast_topic_goats.qrel"
	q_ps = get_q_ps_map(path)
	relevant_passages = [p for ps in q_ps.values() for p in ps]
	print("%d relevant passages for %d questions"%(len(relevant_passages), len(q_ps)))
	# print(relevant_passages)

	# load index
	index = pyndri.Index('/path/to/indri/index')
	# with pyndri.open(sys.argv[1]) as index:
	print('Index contains %d documents.' % index.document_count())


if __name__ == '__main__':
	main()
