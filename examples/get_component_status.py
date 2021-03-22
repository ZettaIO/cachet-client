import os
import sys
import logging
import requests
import cachetclient

from cachetclient.v1 import enums
from cachetclient.v1 import components
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

logger = logging.getLogger('status')
logger.setLevel(logging.INFO)


# Environment Constants
CACHET_ENDPOINT = "https://cachet_endpoint_url/api/v1"

# Components examples
COMPONENTS = {
    "component_name_1": {'Name': 'component_name_1', 'Description': 'component 1'},
    "component_name_2": {'Name': 'component_name_2', 'Description': 'component 2'},
    "component_name_3": {'Name': 'component_name_3', 'Description': 'component 3'},
    "component_name_4": {'Name': 'component_name_4', 'Description': 'component 4'},
}


# Component Statuses
COMPONENT_STATUSES = {
    1: {'ID': 1, 'Name': 'Operational', 'Description': 'The component is working'},
    2: {'ID': 2, 'Name': 'Performance Issues', 'Description': 'The component is experiencing some slowness.'},
    3: {'ID': 3, 'Name': 'Partial Outage', 'Description': 'The component may not be working for everybody. This could be a geographical issue for example.'},
    4: {'ID': 4, 'Name': 'Major Outage', 'Description': 'The component is not working for anybody.'}
}


def get_cachet_client(cachet_endpoint):
    client = cachetclient.Client(
        endpoint=cachet_endpoint,
        version='1',
        verify_tls=False,
        api_token='token'
    )
    return client


def get_resource_id_by_name(endpoint_cachet, component_name):
    try:
        req = requests.request("GET", f"{endpoint_cachet}/components?name={component_name}", verify=False)
        logger.info(f"Getting ID from: {req.url}...")
    except:
        logger.error(f"The Cachet component: {component_name} does not exist")
    else:
        if 'data' in req.json():
            if req.json()['meta']['pagination']['total'] == 0:
                logger.error(f"Cachet component: {component_name} does not exist")
            else:
                return req.json()['data'][0]['id']


def get_incident_by_resource_id(endpoint_cachet, component_id):
    try:
        req = requests.request("GET", f"{endpoint_cachet}/incidents?component_id={component_id}&per_page=1", verify=False)
        logger.info(f"Getting ID from: {req.url}...")
    except:
        logger.error(f"The Cachet component resource: {component_id} does not exist")
    else:
        if 'data' in req.json():
            if req.json()['meta']['pagination']['count'] == 0:
                logger.error(f"Cachet Incident for resource: {component_id} does not exist")
            else:
                return req.json()['data'][0]['message']


def get_resource_status_by_name(endpoint_cachet, component_name):
    try:
        req = requests.request("GET", f"{endpoint_cachet}/components?name={component_name}", verify=False)
        logger.info(f"Getting Status from: {req.url}...")
    except:
        logger.error(f"The Cachet component resource: {component_name} does not exist")
    else:
        if 'data' in req.json():
            if req.json()['meta']['pagination']['count'] == 0:
                logger.error(f"Cachet Status for resource: {component_name} does not exist")
            else:
                status_id = req.json()['data'][0]['status']
                status_name = COMPONENT_STATUSES[status_id].get('Name')
                status_desc = COMPONENT_STATUSES[status_id].get('Description')
                status = f"{status_name} - {status_desc}"
                return status


def check_resource_status_id(cachet_endpoint, component_name):
    logger.info(f"Connecting to: {cachet_endpoint}")
    client = get_cachet_client(cachet_endpoint)

    if client.ping():
        logger.info(f"Cachet endpoint is reachable at: {cachet_endpoint}")

    logger.info(f"Getting status of resource: {component_name}")
    resource_id = get_resource_id_by_name(cachet_endpoint, component_name)
    status_id = client.component_groups.components.get(resource_id).status
    incident_status = get_resource_status_by_name(cachet_endpoint, component_name)

    if status_id == COMPONENT_STATUSES[1].get('ID'):
        logger.info(f"{component_name} is up with status: {incident_status}")
        return True
    else:
        logger.warning(f"{component_name} is down with status: {incident_status}")
        return False


def check_resource_status_name(cachet_endpoint, component_name):
    logger.info(f"Connecting to: {cachet_endpoint}")
    client = get_cachet_client(cachet_endpoint)

    if client.ping():
        logger.info(f"Cachet endpoint is reachable at: {cachet_endpoint}")

    logger.info(f"Getting status of resource: {component_name}")
    resource_id = get_resource_id_by_name(cachet_endpoint, component_name)
    status_name = client.component_groups.components.get(resource_id).status_name
    logger.info(f"{component_name} is: {status_name}")

    return status_name


def is_resource_up():
    logger.info("Getting resource by id...")
    return check_resource_status_id(CACHET_ENDPOINT, COMPONENTS['component_name_1'].get('Name'))


def main():
    success = is_resource_up()
    return 0 if success else 1


if __name__ == "__main__":
    logging.basicConfig(format="%(levelname)s: %(message)s")
    sys.exit(main())
