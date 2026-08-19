from .server import mcp

if __name__ == "__main__":
    # Start the server using standard input/output (how MCP communicates)
    mcp.run(transport='stdio')
