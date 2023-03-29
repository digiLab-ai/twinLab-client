# twinLab client

Headless interface to the `twinLab` library.

## Installation

```bash
poetry install
```

## Commands

Local test:
```bash
poetry run python scripts/trigger.py local
```
where `trigger.py` can be replaced with any of the scripts in the `script` directory.
You need to have a local server for the `twinlab-cloud` repository running for local testing.

Cloud test:
```bash
poetry run python scripts/trigger.py cloud
```
where `trigger.py` can be replaced with any of the scripts in the `script` directory.

## Notebooks

Check out the `notebooks` directory for some examples to get started!
