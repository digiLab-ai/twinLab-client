import pandas as pd
import requests

from .settings import ENV


class Campaign:
    def __init__(self, meta: dict):
        """
        Construct a new campaign object.
        """

        self.inputs = meta["inputs"]
        self.outputs = meta["outputs"]
        self.estimator_type = meta["estimator_type"]
        self.train_test_split = meta["train_test_split"]

    def fit(self, data: pd.DataFrame):
        """
        Train an emulator on the given data.
        """

        self.data_id = self._upload_data(data)
        self._train_surrogate()

    def predict(self, xs: pd.DataFrame):
        """
        Use the pickled emulator to predict the outputs for the given inputs.
        """
        return True, False

    def _upload_data(self, data: pd.DataFrame):
        """
        Upload data to S3 bucket, store the identifier string.
        """
        pass

    def _train_surrogate(self):
        """
        Train a surrogate model on the data.
        """
        pass
