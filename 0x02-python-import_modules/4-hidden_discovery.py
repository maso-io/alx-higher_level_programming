#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4

    # get hidden_4 namespace
    names = dir(hidden_4)

    # filter out names starting with `__`
    filtered_names = []
    for name in names:
        if not name.startswith('__'):
            filtered_names.append(name)

    sorted_names = sorted(filtered_names)

    for name in sorted_names:
        print(name)
