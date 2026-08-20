# Use a lightweight Python image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Install git and clean up to keep the image small
RUN apt-get update && apt-get install -y git && rm -rf /var/lib/apt/lists/*

# Copy the modern configuration file and source code
COPY pyproject.toml .
COPY src/ src/
COPY README.md .

# Install the package locally using pip
RUN pip install --no-cache-dir .

# Command to run the MCP server using stdio
ENTRYPOINT ["python", "-m", "todo_mcp"]
