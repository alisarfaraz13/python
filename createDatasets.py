#!/usr/bin/env python

import googleapiclient.discovery
from google.cloud import bigquery
from googleapiclient.errors import HttpError

project ='mydemo-170915'

def list_projects():
    bigquery_client = bigquery.Client()

    for project in bigquery_client.list_projects():
        print(project.project_id)


def list_datasets(project):
    "Lists all datasets in a given project"
    bigquery_client = bigquery.Client(project=project)

    for dataset in bigquery_client.list_datasets():
        print(dataset.name)


def create_dataset(dataset_name, project):
    "Craetes a dataset in a given project"
    bigquery_client = bigquery.Client(project=project)

    dataset = bigquery_client.dataset(dataset_name)

    dataset.create()

    print('Created dataset {}.'.format(dataset_name))
    
def run_query(project_id):
    
    bigquery_service = googleapiclient.discovery.build('bigquery', 'v2')
    try:
        query_request = bigquery_service.jobs()
        query_data = {
            'query': (
                'SELECT TOP(corpus, 10) as title, '
                'COUNT(*) as unique_words '
                'FROM [publicdata:samples.shakespeare];')
        }

        query_response = query_request.query(
            projectId=project_id,
            body=query_data).execute()
        
        
        print('Query Results:')
        for row in query_response['rows']:
            print('\t'.join(field['v'] for field in row['f']))
        

    except HttpError as err:
        print('Error: {}'.format(err.content))
        raise err

def main():
    list_projects()
    #list_datasets(project)
    #create_dataset('myDataSets',project)
    run_query(project)

if __name__=='__main__':
    main()
