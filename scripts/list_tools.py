import asyncio
import argparse
from mcp import ClientSession
from mcp.client.streamable_http import streamable_http_client

async def list_mcp_tools(url: str):
    """
    Connect to an MCP server via Streamable HTTP and list its tools.
    """
    print(f"Connecting to MCP server at: {url}...")
    
    try:
        async with streamable_http_client(url) as (read_stream, write_stream, get_session_id):
            print("Connected to stream.")
            async with ClientSession(read_stream, write_stream) as session:
                print("Initializing session...")
                # Initialize the session
                await session.initialize()
                
                # List tools
                print("Fetching tools list...")
                result = await session.list_tools()
                
                tools = result.tools
                print(f"\nDiscovered {len(tools)} tools:")
                print("-" * 60)
                print(f"{'#':<3} | {'Tool Name':<30} | {'Description'}")
                print("-" * 60)
                
                for i, tool in enumerate(tools, 1):
                    description = tool.description or "No description provided"
                    # Truncate description if too long
                    if len(description) > 60:
                        description = description[:57] + "..."
                    print(f"{i:<3} | {tool.name:<30} | {description}")
                
                print("-" * 60)
                
    except ExceptionGroup as eg:
        print(f"\n[!] Error Group: {eg}")
        for i, e in enumerate(eg.exceptions):
            print(f"  Exception {i+1}: {e}")
            if hasattr(e, "__notes__"):
                print(f"  Notes: {e.__notes__}")
    except Exception as e:
        print(f"\n[!] Error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="List tools from an MCP server via Streamable HTTP")
    parser.add_argument(
        "--url", 
        default="http://localhost:8000/mcp", 
        help="The URL of the MCP server's endpoint (default: http://localhost:8000/mcp)"
    )
    
    args = parser.parse_args()
    
    try:
        asyncio.run(list_mcp_tools(args.url))
    except KeyboardInterrupt:
        print("\nInterrupted by user.")
