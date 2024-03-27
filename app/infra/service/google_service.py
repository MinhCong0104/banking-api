from googleapiclient.discovery import build
from google.oauth2.service_account import Credentials as ServiceAccountCredentials


def create_service(client_info, api_name, api_version):
    api_service_name = api_name
    api_version = api_version
    cred = ServiceAccountCredentials.from_service_account_info(client_info)

    try:
        service = build(api_service_name, api_version, credentials=cred)
        return service
    except Exception as e:
        return None
