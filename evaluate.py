###########################
#
#
# Send query to ES, parse the result and get the execution time
#
###############

from es_conf import connect_elasticsearch
import json
import sys

if len(sys.argv)==3:
    query_file, index = tuple(sys.argv[1:3])
else:
    print("error: not good number of documents")
    exit()

print("files: ", query_file,index)
# open queries files and get queries into json object
with open(query_file) as f:  
    queries=json.load(f)

INDEX=index  # set index here

NB_EXECUTION=1

es=connect_elasticsearch()

execution_time=list()
for i in range(len(queries)):
    #print(json.dumps(queries[i]))
    execution_time=list()
    for _ in range(NB_EXECUTION):
        query_result=es.search(index=INDEX, body=json.dumps(queries[i]), size=0)
        execution_time.append(query_result['took'])
    
    print("query: ", i, "average execution time", sum(execution_time)/len(execution_time))