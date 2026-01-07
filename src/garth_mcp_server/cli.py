import argparse
import os

from .app import server


def main():
    parser = argparse.ArgumentParser(description="Garth MCP Server")
    parser.add_argument(
        "--transport",
        choices=["stdio", "http"],
        default=os.getenv("TRANSPORT", "stdio"),
        help="Transport to use (stdio or http)",
    )
    parser.add_argument("--port", type=int, default=os.getenv("PORT", 8000), help="Port for HTTP transport")

    args = parser.parse_args()

    if args.transport == "http":
        import uvicorn

        uvicorn.run(server.streamable_http_app, host="0.0.0.0", port=args.port)
    else:
        server.run(transport="stdio")


if __name__ == "__main__":
    main()
