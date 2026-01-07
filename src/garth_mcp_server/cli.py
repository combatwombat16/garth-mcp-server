import argparse
import os
from .app import server

transport=os.getenv("TRANSPORT", "stdio")
port=os.getenv("PORT", 8000)

def main():
    parser = argparse.ArgumentParser(description="Garth MCP Server")
    parser.add_argument(
        "--transport",
        choices=["stdio", "http"],
        default=transport,
        help="Transport to use (stdio or http)",
    )
    parser.add_argument("--port", type=int, default=port, help="Port for HTTP transport")

    args = parser.parse_args()
    if args.transport == "http":
        import uvicorn

        uvicorn.run(server.streamable_http_app, host="0.0.0.0", port=args.port, log_level="info")
    else:
        server.run(transport=args.transport)


if __name__ == "__main__":
    main()
