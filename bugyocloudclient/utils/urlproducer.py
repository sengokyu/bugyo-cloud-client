from bugyocloudclient.config import URL_TEMPLATES
from bugyocloudclient.models.clientparam import ClientParam


def produce_url(endpoint: str, param: ClientParam):
    """
    endpointに応じたURLを返します。
    """
    if endpoint not in URL_TEMPLATES:
        raise RuntimeError('Unknown key ', endpoint)

    return URL_TEMPLATES[endpoint].format(param.tenant_code, param.user_code)
