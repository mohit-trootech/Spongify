# Base Utils for Utility Classes & Functions
from django.apps import apps


def get_model(app_name: str, model_name: str):
    """
    returns a model given app_name and model_name

    Parameters
    ----------
    app_name : str
        auth app name
    model_name : str
        auth app's model name

    Returns
    -------
    _type_
        models instance based on app_name & model_name
    """
    try:
        return apps.get_model(app_name, model_name)
    except LookupError:
        return None
