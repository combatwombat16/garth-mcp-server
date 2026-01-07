from typing import ClassVar
from mcp.server.fastmcp import FastMCP
import garth.stats.steps
from pydantic.dataclasses import dataclass

# Monkey-patch garth.DailySteps to handle cases where Garmin returns null for step_goal
@dataclass
class PatchedDailySteps(garth.stats.steps.Stats):
    total_steps: int | None
    total_distance: int | None
    step_goal: int | None

    _path: ClassVar[str] = garth.stats.steps.DailySteps._path
    _page_size: ClassVar[int] = garth.stats.steps.DailySteps._page_size

garth.stats.steps.DailySteps = PatchedDailySteps
garth.DailySteps = PatchedDailySteps

from starlette.responses import JSONResponse

server = FastMCP(
    "Garth - Garmin Connect",
    transport_security=TransportSecuritySettings(
        enable_dns_rebinding_protection=False,
    )
)

@server.custom_route("/health", methods=["GET"])
async def health(request):
    return JSONResponse({"status": "ok"})
