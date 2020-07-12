def lower_byindex(string: str, index: int) -> str:
    """
    Lower string by index
    :param string:
    :return: lowered by index string
    """
    return "".join([s.lower() if i == index else s for i, s in enumerate(string)])
