import pathlib
import re


def main():
    base_path = './'
    pattern = 'tests/data/templates/*/*.sql'
    re_pattern = pattern.replace('**', '*').replace('*', '(.*)')
    result = {}
    print('paths by', pattern)
    for path in pathlib.Path(base_path).glob(pattern):
        r = result
        k = None
        for p in re.search(re_pattern, str(path)).groups():
            if k is None:
                k = p
                continue
            else:
                r[k] = {}
                r = r[k]
                k = p
                continue
        if k:
            r[k] = str(path)
    print(result)


if __name__ == '__main__':
    main()
