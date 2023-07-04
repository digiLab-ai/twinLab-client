# Examples

You can then run the example examples in the [examples](./scripts/api) directory:
```shell
poetry run python scripts/api/<event_name>.py ...
```

Get user information:
```shell
poetry run python scripts/api/get_user.py
```

Get version information:
```shell
poetry run python scripts/api/get_versions.py
```

List datasets:
```shell
poetry run python scripts/api/list_datasets.py
```

Upload dataset:
```shell
poetry run python scripts/api/upload_dataset.py <path/to/dataset.csv> <dataset_id>
poetry run python scripts/api/upload_dataset.py resources/datasets/biscuits.csv biscuits
```

View dataset:
```shell
poetry run python scripts/api/view_dataset.py <dataset_id>
poetry run python scripts/api/view_dataset.py biscuits
```

Summarise a dataset:
```shell
poetry run python scripts/api/summarise_dataset.py <dataset_id>
poetry run python scripts/api/summarise_dataset.py biscuits
```

List models:
```shell
poetry run python scripts/api/list_models.py
```

Train model:
```shell
poetry run python scripts/api/train_model.py <path/to/parameters.json> <model_id> <processor>
poetry run python scripts/api/train_model.py resources/campaigns/biscuits/params.json biscuits-model cpu
```

Get the model status:
```shell
poetry run python scripts/api/status_model.py <model_id>
poetry run python scripts/api/status_model.py biscuits-model
```

Summarise model:
```shell
poetry run python scripts/api/summarise_model.py <model_id>
poetry run python scripts/api/summarise_model.py biscuits-model
```

Predict using a trained model:
```shell
poetry run python scripts/api/use_model.py <path/to/inputs.csv> <model_id> <method> <processor>
poetry run python scripts/api/use_model.py resources/campaigns/biscuits/eval.csv biscuits-model predict cpu
```

Delete model:
```shell
poetry run python scripts/api/delete_model.py <model_id>
poetry run python scripts/api/delete_model.py biscuits-model
```

Delete dataset:
```shell
poetry run python scripts/api/delete_dataset.py <dataset_id>
poetry run python scripts/api/delete_dataset.py biscuits
```