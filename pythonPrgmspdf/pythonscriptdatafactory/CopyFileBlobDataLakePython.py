from azure.common.credentials import ServicePrincipalCredentials
from azure.mgmt.resource import ResourceManagementClient
from azure.mgmt.datafactory import DataFactoryManagementClient
from azure.mgmt.datafactory.models import *
from datetime import datetime, timedelta
import time


def print_item(group):
    """Print an Azure object instance."""
    print("\tName: {}".format(group.name))
    print("\tId: {}".format(group.id))
    if hasattr(group, 'location'):
        print("\tLocation: {}".format(group.location))
    if hasattr(group, 'tags'):
        print("\tTags: {}".format(group.tags))
    if hasattr(group, 'properties'):
        print_properties(group.properties)
    print("\n")


def print_properties(props):
    """Print a ResourceGroup properties instance."""
    if props and hasattr(props, 'provisioning_state') and props.provisioning_state:
        print("\tProperties:")
        print("\t\tProvisioning State: {}".format(props.provisioning_state))
    print("\n")


def print_activity_run_details(activity_run):
    """Print activity run details."""
    print("\n\tActivity run details\n")
    print("\tActivity run status: {}".format(activity_run.status))
    if activity_run.status == 'Succeeded':
        print("\tNumber of bytes read: {}".format(
            activity_run.output['dataRead']))
        print("\tNumber of bytes written: {}".format(
            activity_run.output['dataWritten']))
        print("\tCopy duration: {}".format(
            activity_run.output['copyDuration']))
    else:
        print("\tErrors: {}".format(activity_run.error['message']))


# create the resource group
def create_resource_group(rg_name, rg_params, credentials, subscription_id):

    # This program creates this resource group.
    resource_client = ResourceManagementClient(credentials, subscription_id)
    # # comment out if the resource group already exits
    resource_client.resource_groups.create_or_update(rg_name, rg_params)


def create_data_factory(rg_name, df_name, adf_client):

    # The data factory name. It must be globally unique.
    # Create a data factory
    df_resource = Factory(location='CentralUS')
    df = adf_client.factories.create_or_update(rg_name, df_name, df_resource)
    print_item(df)
    while df.provisioning_state != 'Succeeded':
        df = adf_client.factories.get(rg_name, df_name)
        time.sleep(1)


def create_linked_service(ls_name, rg_name, df_name, adf_client):

    # Specify the name and key of your Azure Storage account
    storage_string = SecureString(
        'DefaultEndpointsProtocol=https;AccountName=vanistorageacct;AccountKey=RUK6/w9IYpZpCtAcD+LWNCqfnes+p9rqgJbQcnr/rQdiF6BTvWPUTB9E1jO7Lkyp0dGvr3aWOkC9CMAp2+YIFw==')
    ls_azure_storage = AzureStorageLinkedService(connection_string=storage_string)
    ls = adf_client.linked_services.create_or_update(rg_name, df_name, ls_name, ls_azure_storage)
    print_item(ls)


def create_linked_service_datalake(rg_name, df_name, ls_name):

    # location = 'CentralUS'
    # adlaAcctClient = DataLakeAnalyticsAccountManagementClient(credentials, subscription_id)
    # adlaJobClient = DataLakeAnalyticsJobManagementClient(credentials, 'azuredatalakeanalytics.net')
    # adlsAcctResult = adlsAcctClient.account.create(rg_name, adls, DataLakeStoreAccount(location=location)).wait()
    # adlaAcctResult = adlaAcctClient.account.create(rg_name, adla, DataLakeAnalyticsAccount(location=location, default_data_lake_store_account=adls,
    #                                                                 data_lake_store_accounts=[DataLakeStoreAccountInformation(name=adls)])).wait()

    # Specify the name and key of your Azure Storage account.
    storage_string = AzureDataLakeStoreLinkedService(*, data_lake_store_uri, additional_properties=None, connect_via=None,
                                    description: str = None, parameters = None, annotations = None, service_principal_id = None,
                                    service_principal_key = None, tenant = None, account_name = None, subscription_id = None,
                                    resource_group_name = None, encrypted_credential = None, ** kwargs)

    ls_azure_storage = AzureDataLakeStoreLinkedService(connection_string=storage_string)
    ls = adf_client.linked_services.create_or_update(rg_name, df_name, ls_name, ls_azure_storage)
    print_item(ls)


def create_linked_dataset(ds_name, ls_name, rg_name, df_name, dsOut_name, adf_client):

    # Create an Azure blob data set (input)
    ds_ls = LinkedServiceReference(ls_name)
    blob_path = 'blobcontainer/input'
    blob_filename = 'input.txt'
    ds_azure_blob = AzureBlobDataset(ds_ls, folder_path=blob_path, file_name=blob_filename)
    ds = adf_client.datasets.create_or_update(rg_name, df_name, ds_name, ds_azure_blob)
    print_item(ds)

    # Create an Azure blob dataset (output)
    output_blobpath = 'blobcontainer/output'
    dsOut_azure_blob = AzureBlobDataset(ds_ls, folder_path=output_blobpath)
    dsOut = adf_client.datasets.create_or_update(rg_name, df_name, dsOut_name, dsOut_azure_blob)
    print_item(dsOut)
    

# Create a copy activity
def create_copy_activity(ds_name, dsOut_name, rg_name, df_name, p_name, adf_client):

    # Create a copy activity
    act_name = 'copyBlobToDataLake'
    blob_source = BlobSource()
    blob_sink = BlobSink()
    dsin_ref = DatasetReference(ds_name)
    dsOut_ref = DatasetReference(dsOut_name)
    copy_activity = CopyActivity(act_name, inputs=[dsin_ref], outputs=[dsOut_ref], source=blob_source, sink=blob_sink)

    # Create a pipeline with the copy activity
    params_for_pipeline = {}
    p_obj = PipelineResource(activities=[copy_activity], parameters=params_for_pipeline)
    p = adf_client.pipelines.create_or_update(rg_name, df_name, p_name, p_obj)
    print_item(p)


def create_monitor_pipeline(rg_name, df_name, p_name, adf_client):

    # Create a pipeline run
    run_response = adf_client.pipelines.create_run(rg_name, df_name, p_name, {})

    # Monitor the pipeline run
    time.sleep(30)
    pipeline_run = adf_client.pipeline_runs.get(rg_name, df_name, run_response.run_id)
    print("\n\tPipeline run status: {}".format(pipeline_run.status))
    activity_runs_paged = list(adf_client.activity_runs.list_by_pipeline_run(rg_name, df_name, pipeline_run.run_id,
                                                                             datetime.now() - timedelta(1),
                                                                             datetime.now() + timedelta(1)))
    print_activity_run_details(activity_runs_paged[0])


def main():


    rg_name = 'cg1vanicentralus'
    rg_params = {'location': 'centralus'}
    df_name = 'cg1df'
    # Specify your Active Directory client ID, client secret, and tenant ID
    credentials = ServicePrincipalCredentials(client_id='50af3e84-daae-4cd6-baca-d9900b9dada2',
                                              secret='3HmM=M-V]tnyQ.vAhnT9IiSXYLMYTY02',
                                              tenant='524b0e96-35a3-46ef-ade3-a76c1936a890')
    # Azure subscription ID
    subscription_id = '540bcf3e-716f-4ab5-b499-68e5285ea954'
    # Create an Azure Storage linked service
    ls_name = 'storageLinkedService-vani'
    ds_name = 'ds_in'
    dsOut_name = 'ds_out'
    p_name = 'copyBlobToDataLake'
    adls = 'cg1datalake'
    adla = 'cg1datalakeanaly'
    adf_client = DataFactoryManagementClient(credentials, subscription_id)

    create_resource_group(rg_name, rg_params, credentials, subscription_id)
    create_data_factory(rg_name, df_name, adf_client)
    create_linked_service(ls_name, rg_name, df_name, adf_client)
    create_linked_dataset(ds_name, ls_name, rg_name, df_name, dsOut_name, adf_client)
    create_copy_activity(ds_name, dsOut_name, rg_name, df_name, p_name, adf_client)
    create_monitor_pipeline(rg_name, df_name, p_name, adf_client)


main()

