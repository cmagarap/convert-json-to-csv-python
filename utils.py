import itertools

LIST_TYPES = (list, tuple)


def expand(item):
    """Expand a JSON object containing lists.

    Args:
        item (dict) : JSON data

    Returns:
        The expanded data in generator type.
    """
    # Collect values that exist in the form of lists or tuples.
    lists = (
        [(k, x) for x in v] if any(v) else [(k, None)]
        for k, v in item.items()
        if isinstance(v, LIST_TYPES)
    )

    # Calculate combinations of values in each list
    combos = map(dict, itertools.product(*lists))
    # Yield each combination
    for combo in combos:
        xitem = item.copy()
        xitem.update(combo)
        yield xitem


def flatten(item, join='.'):
    """Flattens a JSON object with nested structure.

    Args:
        item (dict) : JSON data
        join (str) : String literal that acts as connector to the key name.

    Returns:
        The flattened data in dictionary type.
    """
    return dict(iter_key_value(item, (), join))


def flatten_expand(item, join='.'):
    """Flattens and expands a JSON object with nested structure.

    Args:
        item (dict) : JSON data
        join (str) : String literal that acts as connector to the key name.

    Returns:
        The flattened and expanded data in generator type.
    """
    for expl in expand(item):
        flat = flatten(expl, join)
        items = filter(lambda x: isinstance(x, LIST_TYPES), flat.values())
        for item in items:
            yield from flatten_expand(flat, join)
            break
        else:
            yield flat


def flatten_list(item):
    """Flattens a list of list.

    Args:
        item (list) : Data in list type.

    Returns:
        The flattened list.
    """
    return [lst for data in item for lst in data]


def iter_key_value(item, parents=(), join='.'):
    """Iterate over key/values of item recursively.

    Args:
        item (dict) : JSON data
        parents (tuple) : Used for storing keys of the JSON data.
        join (str) : String literal that acts as connector to the key name.

    Returns:
        The key-value pair of the JSON data in generator type.
    """
    for key, val in item.items():
        path = parents + (key,)  # Assemble path parts
        key = str.join(join, path)  # join path parts

        # Recurse into nested dict
        if isinstance(val, dict) and any(val):
            yield from iter_key_value(val, path, join)

        # Or `None` if empty dict
        elif isinstance(val, dict):
            yield key, None

        # Otherwise, yield base case
        else:
            yield key, val
