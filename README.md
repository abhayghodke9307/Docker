# Docker
# HTTP Server with Query Params

This project implements a simple HTTP server that responds to incoming GET requests on the `/data` endpoint. It accepts two query parameters, `n` (file name) and `m` (line number), providing different responses based on the combination of these parameters.

## Requirements
- Set up an HTTP server.
- Accept GET requests on the `/data` endpoint.
- Accept query parameters `n` (file name) and `m` (line number).
- If both `n` and `m` are provided, return the content of file `/tmp/data/n.txt` at line number `m`.
- If only `n` is provided, return the entire content of file `/tmp/data/n.txt`.
- Each file is around 100MB in size, with more than 30 different files (e.g., 1.txt, 2.txt, ..., n.txt).

## Usage
1. Ensure you have Docker installed on your machine.
2. Create random text files with a size of around 100MB in the `/tmp/data/` directory.
3. Build the Docker image using the provided Dockerfile:
    ```bash
    docker build -t your_image_name .
    ```
4. Run the Docker container with the specified constraints (max 1500 MB RAM, 2 CPU cores):
    ```bash
    docker run -p 8080:8080 --memory 1500m --cpus 2 your_image_name
    ```

## Making Requests
- Make GET requests to the `/data` endpoint with the appropriate query parameters.
- Examples:
  - Request: `/data?n=1&m=30`
    Response: `vyAF9kLDTIbqkv5R7hFqGDXaxezu3WMV5pcPd6RdudWMqMGJBQ9YLOoCQt`
  - Request: `/data?n=1`
    Response: (Contents of file `/tmp/data/1.txt`)

## Notes
- The server is built using Python and Flask, but you can adapt it to other languages/frameworks as needed.
- Ensure you have generated random text files for development purposes in the `/tmp/data/` directory.
- The Dockerfile is compatible with both ARM and x86 architectures.



run the project
docker build -t your_image_name .
docker run -p 8080:8080 --memory 1500m --cpus 2 image_name
