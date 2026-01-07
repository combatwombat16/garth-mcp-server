import argparse
import os
from .app import server
from starlette.middleware import Middleware
from starlette.middleware.cors import CORSMiddleware

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

        # Define middleware
        middleware = [
            Middleware(
                CORSMiddleware,
                allow_origins=["*"],
                allow_methods=["*"],
                allow_headers=["*"],
            )
        ]

        # Create ASGI app with middleware
        http_app = server.streamable_http_app(middleware=middleware)
        
        uvicorn.run(http_app, host="0.0.0.0", port=args.port, log_level="info")
    else:
        server.run(transport=args.transport)


if __name__ == "__main__":
    main()
