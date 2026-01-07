from typing import ClassVar
from mcp.server.fastmcp import FastMCP
import garth.stats.steps
from pydantic.dataclasses import dataclass
from starlette.responses import JSONResponse

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

server = FastMCP(
    "Garth - Garmin Connect",
    host="0.0.0.0",
)

@server.custom_route("/health", methods=["GET"])
async def health(request):
    return JSONResponse({"status": "ok"})
