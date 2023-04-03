# twinLab client

Headless interface to the `twinLab` library.

## Installation
```bash
poetry install
```

## Environment setup
```bash
cp .env.example .env
```
and fill in your group and user names.

## Commands

Local or cloud testing:
```python
poetry run python scripts/trigger.py local_or_cloud
```
where the `local_or_cloud` flag is either `local` or `cloud` and where `trigger.py` can be replaced with any of the scripts in the `script` directory.
You need to have a local server for the `twinlab-cloud` repository running for local testing.

## Notebooks

Check out the `notebooks` directory for some examples to get started!
