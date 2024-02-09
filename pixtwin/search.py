import os
import time
from pprint import pprint
from dotenv import load_dotenv
from elasticsearch import Elasticsearch

load_dotenv()

CLOUD_ID = os.environ['ELASTIC_CLOUD_ID']
API_KEY = os.environ['ELASTIC_API_KEY']

class Search:
    def __init__(self):
        self.index = 'pixtwin'
        self.es = Elasticsearch(cloud_id=CLOUD_ID,api_key=API_KEY)
        client_info = self.es.info()
        print('Connected to Elasticsearch!')
        pprint(client_info)

    def create_index(self):

        body = {
            'mappings': {
                'properties': {
                    'image': {
                        'type': 'text'
                    },
                    'image_vector': {
                        'type': 'dense_vector',
                        'dims': 512
                    }
                }
            }
        }

        self.es.indices.delete(index=self.index,ignore_unavailable=True)
        self.es.indices.create(index=self.index, body=body)

    def insert_document(self, document):
        return self.es.index(index=self.index, body=document)

    def similarity_by_nn(self, query_vector):
        body = {
            'query': {
                'script_score': {
                    'query': {
                        'match_all': {}
                    },
                    'script': {
                        'source': 'cosineSimilarity(params.query_vector, "image_vector") + 1.0',
                        'params': {'query_vector': query_vector}
                    }
                }
            }
        }

        result = self.es.search(index=self.index,body=body)
        return result