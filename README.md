# Test gRPC Project

This is a test project, using gRPC with Python 3.13, which attempts to reproduce https://github.com/getsentry/sentry-python/issues/4389.

## Setup

1. Make sure you have uv installed.

2. Run `uv sync` to create the virtual environment and install the needed dependencies.

3. Activate the virtual environment:

```bash
source .venv/bin/activate
```

4. Run the gRPC server:

```bash
opentelemetry-instrument python -m server
```

5. In a separate window, run the client, and observe the correct output, without any errors (neither in the server, nor in the client).
