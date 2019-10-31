import os

from cachetclient import v1
from cachetclient.httpclient import HttpClient


def Client(
        endpoint: str = None,
        api_token: str = None,
        version: str = None,
        verify_tls: bool = True) -> v1.Client:
    """
    Creates a cachet client. Use this fuction to create clients to ensure
    compatibility in the future.

    Args:
        endpoint (str): The api endpoint. for example 'https://status.examples.test/api/v1'.
                        The endpoint can also be specified using the ``CACHET_ENDPOINT`` env variable.
        api_token (str): The api token. Can also be specified using ``CACHET_API_TOKEN`` env variable.
        version (str): The api version. If not specified the version will be derived from the
                       endpoint url. The value "1" will create a v1 cachet client.
        verify_tls (bool): Enable/disable tls verify. When using self signed certificates this has to be ``False``.
    """
    if not api_token:
        api_token = os.environ.get('CACHET_API_TOKEN')

    if not api_token:
        raise ValueError(
            "No api_token specified. "
            "The endpoint must be supplied in the Client function "
            "or through the CACHET_API_TOKEN environment variable."
        )

    if not endpoint:
        endpoint = os.environ.get('CACHET_ENDPOINT')

    if not endpoint:
        raise ValueError(
            "No api endpoint specified. "
            "The token must be supplied in the Client function "
            "or through the CACHET_ENDPOINT environment variable."
        )

    if not version:
        version = detect_version(endpoint)

    return v1.Client(HttpClient(endpoint, api_token, verify_tls=verify_tls))


def detect_version(endpoint: str) -> str:
    """
    Detect the api version from endpoint url.
    Currently cachet only has a single "v1" endpoint but this may change in the future.
    """
    if endpoint.endswith('/v1'):
        return '1'

    raise ValueError(
        "Cannot determine api version based on endpoint '{}'. "
        "If the api version is not present in the url, "
        "please supply it on client creation.".format(endpoint)
    )
