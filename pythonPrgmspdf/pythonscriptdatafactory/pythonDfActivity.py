import token
import adal
import requests
import os
import json

authentication_endpoint = 'https://login.microsoftonline.com/'
resource = 'https://management.core.windows.net/'
tenant_id ='eb20330a-b375-43c2-a621-3d5443b27184'
application_id ='6bca1d02-5896-48c9-8da2-404cb245c4b2'
application_secret = '.tgDUMEjZMB2.wsvQckDkY.YO_hxx649'


# get an Azure access token using the adal library
context = adal.AuthenticationContext(authentication_endpoint + tenant_id)
token_response = context.acquire_token_with_client_credentials(resource, application_id, application_secret)

access_token = token_response.get('accessToken')
# print(access_token)

headers = {'Content-Type': 'application/json', 'Authorization':  'Bearer ' + access_token}

params = {'api-version': '2017-05-10'}

#Creating Resource Group
# url = 'https://management.azure.com/subscriptions/48b9dd42-97d6-47c1-8227-eb67af109112/resourceGroups/vanipythonrg'
#
# data = {'location': 'Central US'}
#
# r = requests.put(url, data=json.dumps(data), headers=headers, params=params)
#
# print(json.dumps(r.json(), indent=4, separators=(',', ': ')))


#creating Storage Account
# data = {'location': 'Central US',
#   "properties": {
#
#       "encryption": {
#               "services": {
#                        "blob": {
#                                "enabled": 'true'
#                        }
#               },
#               "keySource": "Microsoft.Storage"
#       }
#   },
#   "sku": {
#       "name": "Standard_RAGRS"
#   },
#   "kind": "Storage"
#         }
#
# url = 'https://management.azure.com/subscriptions/48b9dd42-97d6-47c1-8227-eb67af109112/resourceGroups/' \
#     'vanipythonrg/providers/Microsoft.Storage/storageAccounts/vanistoragepython'
# paramsblob = {'api-version': '2017-10-01'}
# r = requests.put(url, data=json.dumps(data), headers=headers, params=paramsblob)
# print(json.dumps(r.json(), indent=4, separators=(',', ': ')))

# Create Data Lake Storage
# data = {
#     "location": "Central US",
#     "properties": {
#         "defaultDataLakeStoreAccount": "vaniadlpython",
#         "dataLakeStoreAccounts": [
#             {
#                 "name": "vaniadlpython"
#             }]
#     }
# }
#
# url = 'https://management.azure.com/subscriptions/48b9dd42-97d6-47c1-8227-eb67af109112/resourceGroups/' \
#       'vanipythonrg/providers/Microsoft.DataLakeStore/accounts/vaniadlpython'
# paramsdatalake = {'api-version': '2016-11-01'}
# r = requests.put(url, data=json.dumps(data), headers=headers, params=paramsdatalake)
# print(json.dumps(r.json(), indent=4, separators=(',', ': ')))

# Create Data Factory
# data = {
#     'location': 'Central US'
#         }
# url = 'https://management.azure.com/subscriptions/48b9dd42-97d6-47c1-8227-eb67af109112/resourceGroups/' \
#       'vanipythonrg/providers/Microsoft.DataFactory/factories/vanipythondatafactory?api-version=2018-06-01'
# headers = {'content-type': 'application/json', 'Authorization': 'Bearer ' + access_token}
# response = requests.put(url=url, data=json.dumps(data), headers=headers)
# print(response.text)

# Create Linked Service
# url = 'https://management.azure.com/subscriptions/48b9dd42-97d6-47c1-8227-eb67af109112/resourceGroups/' \
#       'vanipythonrg/providers/Microsoft.DataFactory/factories/vanipythondatafactory/linkedservices/' \
#       'AzureDataLakeLinkedService?api-version=2018-06-01'
# data = {
#     "properties": {
#         "type": "AzureDataLakeStore",
#         "typeProperties": {
#             "dataLakeStoreUri": "https://vanidatalakebatch.azuredatalakestore.net/webhdfs/v1",
#             "servicePrincipalId": "6bca1d02-5896-48c9-8da2-404cb245c4b2",
#             "servicePrincipalKey": {
#                 "type": "SecureString",
#                 "value": ".tgDUMEjZMB2.wsvQckDkY.YO_hxx649"
#             },
#             "tenant": "eb20330a-b375-43c2-a621-3d5443b27184"
#         }
#
#     }
# }
# headers = {'content-type': 'application/json', 'Authorization': 'Bearer ' + access_token}
# response = requests.put(url=url, data=json.dumps(data), headers=headers)
# print(response.text)

# Create Dataset input for ADLS
# url = 'https://management.azure.com/subscriptions/48b9dd42-97d6-47c1-8227-eb67af109112/' \
#       'resourceGroups/vanipythonrg/providers/Microsoft.DataFactory/factories/vanipythondatafactory/' \
#       'datasets/AzureDataLakeStoreInput?api-version=2018-06-01'
#
# data = {
#     "name": "AzureDataLakeStoreInput",
#     "properties": {
#         "type": "AzureDataLakeStoreFile",
#         "linkedServiceName": {
#             "referenceName": "AzureDataLakeLinkedService",
#             "type": "LinkedServiceReference"
#         },
#         "typeProperties": {
#             "folderPath": "input",
#             "fileName": "bank_test.csv",
#             "format": {
#                 "type": "TextFormat",
#                 "columnDelimiter": ";",
#                 "rowDelimiter": "\n",
#                 "firstRowAsHeader": True,
#             }
#         }
#     }
# }
# headers = {'content-type': 'application/json', 'Authorization': 'Bearer ' + access_token}
# response = requests.put(url=url, data=json.dumps(data), headers=headers)
# print(response.text)

# Create Dataset output for ADLS
# url = 'https://management.azure.com/subscriptions/48b9dd42-97d6-47c1-8227-eb67af109112/' \
#       'resourceGroups/vanipythonrg/providers/Microsoft.DataFactory/factories/vanipythondatafactory/' \
#       'datasets/AzureDataLakeDatasetOutput?api-version=2018-06-01'
# data = {
#     "name": "AzureDataLakeDatasetOutput",
#     "properties": {
#         "type": "AzureDataLakeStoreFile",
#         "linkedServiceName": {
#             "referenceName": "AzureDataLakeLinkedService",
#             "type": "LinkedServiceReference"
#         },
#         "typeProperties": {
#             "folderPath": "output"
#         }
#     }
# }
# headers = {'content-type': 'application/json', 'Authorization': 'Bearer ' + access_token}
# response = requests.put(url=url, data=json.dumps(data), headers=headers)
# print(response.text)

# Create pipeline with copy activity
# url = 'https://management.azure.com/subscriptions/48b9dd42-97d6-47c1-8227-eb67af109112/resourceGroups/' \
#       'vanipythonrg/providers/Microsoft.DataFactory/factories/vanipythondatafactory/pipelines/pythonRestPipeline?api-version=2018-06-01'
# data = {
#     "name": "pythonRestPipeline",
#     "properties": {
#         "activities": [
#             {
#                 "name": "CopyFromADLSToADLS",
#                 "type": "Copy",
#                 "inputs": [
#                     {
#                         "referenceName": "AzureDataLakeStoreInput",
#                         "type": "DatasetReference"
#                     }
#                 ],
#                 "outputs": [
#                     {
#                         "referenceName": "AzureDataLakeDatasetOutput",
#                         "type": "DatasetReference"
#                     }
#                 ],
#                 "typeProperties": {
#                     "source": {
#                         "type": "DelimitedTextSource",
#                         "formatSettings": {
#                             "type": "DelimitedTextReadSetting",
#                         }
#                     },
#                     "sink": {
#                         "type": "DelimitedTextSource"
#                     }
#                 }
#              }
#         ]
#     }
# }
# headers = {'content-type': 'application/json', 'Authorization': 'Bearer ' + access_token}
# response = requests.put(url=url, data=json.dumps(data), headers=headers)
# print(response.text)

# Run Pipeline
url = 'https://management.azure.com/subscriptions/48b9dd42-97d6-47c1-8227-eb67af109112/resourceGroups/' \
      'vanipythonrg/providers/Microsoft.DataFactory/factories/vanipythondatafactory/pipelines/' \
      'pythonRestPipeline/createRun?api-version=2018-06-01'
headers = {'content-type': 'application/json', 'Authorization': 'Bearer ' + access_token}
response = requests.post(url=url, headers=headers)
print(response.text)

