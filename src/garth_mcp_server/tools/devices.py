import garth
from ..app import server
from ..auth import requires_garth_session

# Type alias for functions that return data from garth.connectapi
ConnectAPIResponse = str | dict | list | int | float | bool | None

@server.tool()
@requires_garth_session
def get_devices(garth_token: str | None = None) -> ConnectAPIResponse:
    """
    Get connected devices from Garmin Connect.
    """
    return garth.connectapi("device-service/deviceregistration/devices")


@server.tool()
@requires_garth_session
def get_device_settings(
    device_id: str, garth_token: str | None = None
) -> ConnectAPIResponse:
    """
    Get settings for a specific device.
    device_id: Device ID from Garmin Connect
    """
    return garth.connectapi(
        f"device-service/deviceservice/device-info/settings/{device_id}"
    )


@server.tool()
@requires_garth_session
def get_gear(garth_token: str | None = None) -> ConnectAPIResponse:
    """
    Get gear information from Garmin Connect.
    """
    return garth.connectapi("gear-service/gear")


@server.tool()
@requires_garth_session
def get_gear_stats(gear_uuid: str, garth_token: str | None = None) -> ConnectAPIResponse:
    """
    Get usage statistics for specific gear.
    gear_uuid: UUID of the gear item
    """
    return garth.connectapi(f"gear-service/gear/stats/{gear_uuid}")
