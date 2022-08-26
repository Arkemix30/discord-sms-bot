def class_name_to_lower(name: str) -> str:
    if name:
        x = list(name)
        new_array = []
        for i, v in enumerate(x):
            if v.isupper():
                if i > 0:
                    new_array.append("_")

            new_array.append(v.lower())
        return "".join(new_array)
    else:
        return ""


def row2dict(row):
    d = {}
    for column in row.keys():
        d[column] = getattr(row, column)

    return d
