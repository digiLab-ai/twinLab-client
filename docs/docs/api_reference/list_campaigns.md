---
sidebar_position: 6
---

# List campaigns

List all trained campaigns stored in the `twinLab` cloud.

**NOTE:** Your user information is automatically added to the request using the `.env` file.

## Arguments

- `server`: `str`; {`"local"`, `"dev"`, `"stage"`, `"cloud"`}
- `verbose`: `bool`
- `debug`: `bool`

## Example

```python
import twinlab as tl

tl.list_campaigns()
```
