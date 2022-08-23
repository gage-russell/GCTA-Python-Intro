def id_data_type(id_this: any, data_type: any) -> str | tuple:
    """

    :param data_type: 
    :param id_this:
    :return:
    """
    try:
        type_object = type(id_this)
    except Exception as exc:
        return exc.__class__.__name__, exc

    exclusion_set = (' ', '\'', '\"', '\"\"\"', '<', '>')
    clean_id = ''.join([i for i in list(str(type_object).lstrip('<class ')) if i not in exclusion_set])
    return clean_id == data_type


print("Helper functions successfully loaded!")
