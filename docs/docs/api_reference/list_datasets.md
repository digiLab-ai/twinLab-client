---
sidebar_position: 3
---

# List datasets

List datasets that have been uploaded to the `twinLab` cloud.

**NOTE:** Your user information is automatically added to the request using the `.env` file.

## Arguments

- `server`: `str`; {`"local"`, `"dev"`, `"stage"`, `"cloud"`}
- `verbose`: `bool`
- `debug`: `bool`

## Returns

A list of `str` dataset names, or `None` if there are no datasets

## Example

```python
import twinlab as tl

datasets = tl.list_datasets()
print(datasets)
```
