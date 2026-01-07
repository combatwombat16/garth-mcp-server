from urllib.parse import urlencode
import garth
from ..app import server
from ..auth import requires_garth_session

# Type alias for functions that return data from garth.connectapi
ConnectAPIResponse = str | dict | list | int | float | bool | None

@server.tool()
@requires_garth_session
def get_activities(
    start_date: str | None = None,
    limit: int | None = None,
    garth_token: str | None = None,
) -> ConnectAPIResponse:
    """
    Get list of activities from Garmin Connect.
    start_date: Start date for activities (YYYY-MM-DD format)
    limit: Maximum number of activities to return
    """
    params = {}
    if start_date:
        params["startDate"] = start_date
    if limit:
        params["limit"] = str(limit)

    endpoint = "activitylist-service/activities/search/activities"
    if params:
        endpoint += "?" + urlencode(params)
    return garth.connectapi(endpoint)


@server.tool()
@requires_garth_session
def get_activities_by_date(
    date: str, garth_token: str | None = None
) -> ConnectAPIResponse:
    """
    Get activities for a specific date from Garmin Connect.
    date: Date for activities (YYYY-MM-DD format)
    """
    return garth.connectapi(f"wellness-service/wellness/dailySummaryChart/{date}")


@server.tool()
@requires_garth_session
def get_activity_details(
    activity_id: str, garth_token: str | None = None
) -> ConnectAPIResponse:
    """
    Get detailed information for a specific activity.
    activity_id: Garmin Connect activity ID
    """
    return garth.connectapi(f"activity-service/activity/{activity_id}")


@server.tool()
@requires_garth_session
def get_activity_splits(
    activity_id: str, garth_token: str | None = None
) -> ConnectAPIResponse:
    """
    Get lap/split data for a specific activity.
    activity_id: Garmin Connect activity ID
    """
    return garth.connectapi(f"activity-service/activity/{activity_id}/splits")


@server.tool()
@requires_garth_session
def get_activity_weather(
    activity_id: str, garth_token: str | None = None
) -> ConnectAPIResponse:
    """
    Get weather data for a specific activity.
    activity_id: Garmin Connect activity ID
    """
    return garth.connectapi(f"activity-service/activity/{activity_id}/weather")


@server.tool()
@requires_garth_session
def monthly_activity_summary(
    month: int, year: int, garth_token: str | None = None
) -> ConnectAPIResponse:
    """
    Get the monthly activity summary for a given month and year.
    """
    return garth.connectapi(f"mobile-gateway/calendar/year/{year}/month/{month}")
