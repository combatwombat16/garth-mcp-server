import asyncio
import os
import sys
from garth_mcp_server.app import server
import garth_mcp_server.tools  # This registers all tools
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

async def get_steps(days: int = 1, token: str | None = None):
    """
    Manually request step data from the daily_steps tool.
    """
    print(f"--- Requesting daily steps for the last {days} day(s) ---")
    
    arguments = {"days": days}
    if token:
        arguments["garth_token"] = token
        
    try:
        # Check if we need to login or if we are using a token
        if token:
            print("Using provided garth_token...")
        else:
            email = os.getenv("GARMIN_EMAIL")
            print(f"Using credentials for: {email}")

        # Call the tool using the FastMCP server instance
        result = await server.call_tool("daily_steps", arguments)
        
        # The result is a list of MCP Content objects (likely TextContent)
        if isinstance(result, list):
            for i, content in enumerate(result, 1):
                print(f"\n[Entry {i}]")
                if hasattr(content, "text"):
                    print(content.text)
                else:
                    print(content)
        else:
            print(result)
            
    except Exception as e:
        print(f"\n[!] Error calling tool: {e}")
        print("\nMake sure you have set GARMIN_EMAIL and GARMIN_PASSWORD in your .env file,")
        print("or provide a valid garth_token as an argument.")

if __name__ == "__main__":
    # Allow passing number of days as a command line argument
    days_to_fetch = 1
    if len(sys.argv) > 1:
        try:
            days_to_fetch = int(sys.argv[1])
        except ValueError:
            print(f"Invalid days argument: {sys.argv[1]}. Defaulting to 1.")

    asyncio.run(get_steps(days=days_to_fetch))
