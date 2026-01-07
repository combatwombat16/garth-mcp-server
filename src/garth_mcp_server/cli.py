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
        from mcp.server.transport_security import TransportSecuritySettings
        from starlette.middleware.cors import CORSMiddleware

        # Configure ALLOWED_HOSTS if provided
        allowed_hosts = os.getenv("ALLOWED_HOSTS")
        if allowed_hosts:
            server.settings.transport_security = TransportSecuritySettings(
                enable_dns_rebinding_protection=True,
                allowed_hosts=allowed_hosts.split(","),
            )
        else:
            # Disable DNS rebinding protection if no ALLOWED_HOSTS provided
            # and we're running on 0.0.0.0 (FastMCP default for non-localhost)
            server.settings.transport_security = TransportSecuritySettings(
                enable_dns_rebinding_protection=False
            )

        # Create ASGI app
        http_app = server.streamable_http_app()
        
        # Add middleware to the Starlette app
        http_app.add_middleware(
            CORSMiddleware,
            allow_origins=["*"],
            allow_methods=["*"],
            allow_headers=["*"],
        )
        
        uvicorn.run(
            http_app,
            host="0.0.0.0",
            port=args.port,
            log_level="info",
            proxy_headers=True,
            forwarded_allow_ips="*",
        )
    else:
        server.run(transport=args.transport)


if __name__ == "__main__":
    main()
