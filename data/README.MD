## TREC CAsT 2019 

Download relevance judgements for train and evaluation topics:
```
wget https://raw.githubusercontent.com/daltonj/treccastweb/master/2019/data/training/train_topics_mod.qrel
wget https://trec.nist.gov/data/cast/2019qrels.txt
```

## TrecQrel format

qid 0 docno relevance

where:

qid is the query number
0 is the literal 0
docno is the id of a document in your collection
relevance is how relevant is docno for qid

Example:
1 0 aldf.1864_12_000027 1



TREC CAsT 2019 judgments were graded on a three point scale (2 very relevant, 1 relevant, and 0 not relevant).
