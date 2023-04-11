---
sidebar_position: 2
---

# List datasets

List all datasets owned by the user.

**NOTE:** Your user information is automatically added to the request using the `.env` file.

## Example

```python
import twinlab_client as tl

tl.list_datasets(server, verbose=True)
```
