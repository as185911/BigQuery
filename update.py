import json
from google.cloud import bigquery
from google.cloud.bigquery import enums
from google.cloud.bigquery.job import query
BigQuery_client = bigquery.Client()

# update the json file to update the bigquery table
myjson=open('update.json','r')
jsondata=myjson.read()
obj=json.loads(jsondata)
list=obj['update']
for i in range(len(list)):
    print(i+1 ,list[i].get('string_field_2'))
    Environment=list[i].get('string_field_0')
    customer=list[i].get('string_field_1')
    service=list[i].get('string_field_2')
    service_version=list[i].get('string_field_4')
    samp_query="""
        UPDATE `ret-appops-ams-cug01-qa.AMSAz.AMSAzTb`
        SET string_field_4="""+"""\""""+service_version+"""\""""+"""
        WHERE  string_field_0="""+"""\""""+Environment+"""\""""+""" AND string_field_1="""+"""\""""+customer+"""\""""+""" AND string_field_2="""+"""\""""+service+"""\""""+"""
        """
    name_group_query = samp_query
    query_results = BigQuery_client.query(name_group_query)
