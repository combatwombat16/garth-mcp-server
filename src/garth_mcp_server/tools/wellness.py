from datetime import date
import garth
from ..app import server
from ..auth import requires_garth_session

# Type alias for functions that return data from garth.connectapi
ConnectAPIResponse = str | dict | list | int | float | bool | None

@server.tool()
@requires_garth_session
def weekly_intensity_minutes(
    end_date: date | None = None, weeks: int = 1, garth_token: str | None = None
) -> str | list[garth.WeeklyIntensityMinutes]:
    """
    Get weekly intensity minutes data for a given date and number of weeks.
    If no date is provided, the current date will be used.
    If no weeks are provided, 1 week will be used.
    """
    return garth.WeeklyIntensityMinutes.list(end_date, weeks)


@server.tool()
@requires_garth_session
def daily_body_battery(
    end_date: date | None = None, days: int = 1, garth_token: str | None = None
) -> str | list[garth.DailyBodyBatteryStress]:
    """
    Get daily body battery data for a given date and number of days.
    If no date is provided, the current date will be used.
    If no days are provided, 1 day will be used.
    """
    return garth.DailyBodyBatteryStress.list(end_date, days)


@server.tool()
@requires_garth_session
def daily_hydration(
    end_date: date | None = None, days: int = 1, garth_token: str | None = None
) -> str | list[garth.DailyHydration]:
    """
    Get daily hydration data for a given date and number of days.
    If no date is provided, the current date will be used.
    If no days are provided, 1 day will be used.
    """
    return garth.DailyHydration.list(end_date, days)


@server.tool()
@requires_garth_session
def daily_steps(
    end_date: date | None = None, days: int = 1, garth_token: str | None = None
) -> str | list[garth.DailySteps]:
    """
    Get daily steps data for a given date and number of days.
    If no date is provided, the current date will be used.
    If no days are provided, 1 day will be used.
    """
    return garth.DailySteps.list(end_date, days)


@server.tool()
@requires_garth_session
def weekly_steps(
    end_date: date | None = None, weeks: int = 1, garth_token: str | None = None
) -> str | list[garth.WeeklySteps]:
    """
    Get weekly steps data for a given date and number of weeks.
    If no date is provided, the current date will be used.
    If no weeks are provided, 1 week will be used.
    """
    return garth.WeeklySteps.list(end_date, weeks)


@server.tool()
@requires_garth_session
def daily_hrv(
    end_date: date | None = None, days: int = 1, garth_token: str | None = None
) -> str | list[garth.DailyHRV]:
    """
    Get daily heart rate variability data for a given date and number of days.
    If no date is provided, the current date will be used.
    If no days are provided, 1 day will be used.
    """
    return garth.DailyHRV.list(end_date, days)


@server.tool()
@requires_garth_session
def hrv_data(
    end_date: date | None = None, days: int = 1, garth_token: str | None = None
) -> str | list[garth.HRVData]:
    """
    Get detailed HRV data for a given date and number of days.
    If no date is provided, the current date will be used.
    If no days are provided, 1 day will be used.
    """
    return garth.HRVData.list(end_date, days)


@server.tool()
@requires_garth_session
def daily_sleep(
    end_date: date | None = None, days: int = 1, garth_token: str | None = None
) -> str | list[garth.DailySleep]:
    """
    Get daily sleep summary data for a given date and number of days.
    If no date is provided, the current date will be used.
    If no days are provided, 1 day will be used.
    """
    return garth.DailySleep.list(end_date, days)


@server.tool()
@requires_garth_session
def get_body_composition(
    date: str | None = None, garth_token: str | None = None
) -> ConnectAPIResponse:
    """
    Get body composition data from Garmin Connect.
    date: Date for body composition data (YYYY-MM-DD format), if not provided returns latest
    """
    if date:
        endpoint = f"wellness-service/wellness/bodyComposition/{date}"
    else:
        endpoint = "wellness-service/wellness/bodyComposition"
    return garth.connectapi(endpoint)


@server.tool()
@requires_garth_session
def get_respiration_data(
    date: str, garth_token: str | None = None
) -> ConnectAPIResponse:
    """
    Get respiration data from Garmin Connect.
    date: Date for respiration data (YYYY-MM-DD format)
    """
    return garth.connectapi(f"wellness-service/wellness/dailyRespiration/{date}")


@server.tool()
@requires_garth_session
def get_spo2_data(date: str, garth_token: str | None = None) -> ConnectAPIResponse:
    """
    Get SpO2 (blood oxygen) data from Garmin Connect.
    date: Date for SpO2 data (YYYY-MM-DD format)
    """
    return garth.connectapi(f"wellness-service/wellness/dailyPulseOx/{date}")


@server.tool()
@requires_garth_session
def get_blood_pressure(
    date: str, garth_token: str | None = None
) -> ConnectAPIResponse:
    """
    Get blood pressure readings from Garmin Connect.
    date: Date for blood pressure data (YYYY-MM-DD format)
    """
    return garth.connectapi(f"wellness-service/wellness/dailyBloodPressure/{date}")


@server.tool()
@requires_garth_session
def nightly_sleep(
    end_date: date | None = None,
    nights: int = 1,
    sleep_movement: bool = False,
    garth_token: str | None = None,
) -> str | list[garth.SleepData]:
    """
    Get sleep stats for a given date and number of nights.
    If no date is provided, the current date will be used.
    If no nights are provided, 1 night will be used.
    sleep_movement provides detailed sleep movement data. If looking at
    multiple nights, it'll be a lot of data.
    """
    sleep_data = garth.SleepData.list(end_date, nights)
    if not sleep_movement:
        for night in sleep_data:
            if hasattr(night, "sleep_movement"):
                del night.sleep_movement
    return sleep_data


@server.tool()
@requires_garth_session
def daily_stress(
    end_date: date | None = None, days: int = 1, garth_token: str | None = None
) -> str | list[garth.DailyStress]:
    """
    Get daily stress data for a given date and number of days.
    If no date is provided, the current date will be used.
    If no days are provided, 1 day will be used.
    """
    return garth.DailyStress.list(end_date, days)


@server.tool()
@requires_garth_session
def weekly_stress(
    end_date: date | None = None, weeks: int = 1, garth_token: str | None = None
) -> str | list[garth.WeeklyStress]:
    """
    Get weekly stress data for a given date and number of weeks.
    If no date is provided, the current date will be used.
    If no weeks are provided, 1 week will be used.
    """
    return garth.WeeklyStress.list(end_date, weeks)


@server.tool()
@requires_garth_session
def daily_intensity_minutes(
    end_date: date | None = None, days: int = 1, garth_token: str | None = None
) -> str | list[garth.DailyIntensityMinutes]:
    """
    Get daily intensity minutes data for a given date and number of days.
    If no date is provided, the current date will be used.
    If no days are provided, 1 day will be used.
    """
    return garth.DailyIntensityMinutes.list(end_date, days)
