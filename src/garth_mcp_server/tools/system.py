from datetime import date
import garth
from ..app import server
from ..auth import requires_garth_session

# Type alias for functions that return data from garth.connectapi
ConnectAPIResponse = str | dict | list | int | float | bool | None

@server.tool()
@requires_garth_session
def get_connectapi_endpoint(
    endpoint: str, garth_token: str | None = None
) -> ConnectAPIResponse:
    """
    Get the data from a given Garmin Connect API endpoint.
    This is a generic tool that can be used to get data from any Garmin Connect API endpoint.
    """
    return garth.connectapi(endpoint)


@server.tool()
@requires_garth_session
def snapshot(
    from_date: date, to_date: date, garth_token: str | None = None
) -> ConnectAPIResponse:
    """
    Get the snapshot for a given date range. This is a good starting point for
    getting data for a given date range. It can be used in combination with
    the get_connectapi_endpoint tool to get data from any Garmin Connect API
    endpoint.
    """
    return garth.connectapi(f"mobile-gateway/snapshot/detail/v2/{from_date}/{to_date}")
