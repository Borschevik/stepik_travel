def module_to_dict(module) -> dict:
    """
    Transforms module to dict

    :param: Python module
    :return: dict
    """
    return {key: getattr(module, key) for key in dir(module) if not key.startswith("_")}
