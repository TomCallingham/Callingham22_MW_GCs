import numpy as np


def save_dic_csv(data_dic, output_File):
    props = list(data_dic.keys())
    n_rows = len(data_dic[props[0]])
    lines = ""
    for p in props:
        lines += p + ","
    lines = lines[:-1] + "\n"
    for n in range(n_rows):
        for p in props:
            lines += str(data_dic[p][n]) + ","
        lines = lines[:-1] + "\n"
    with open(output_File, 'w') as file:
        file.write(lines)
    print(f"Saved Dictionary as csv: {output_File}")
    return


def load_dic_csv(fname, skip=1):
    array = np.loadtxt(fname, skiprows=skip, dtype=str, delimiter=',')
    with open(fname) as f:
        content = f.readlines()
    props = content[0].strip().split(',')
    Nrows, Ncols = np.shape(array)
    data_dic = {p: array[:, i] for i, p in enumerate(props)}
    for p in props:
        try:
            x = data_dic[p]
            x[np.isin(x, ["-", ""])] = "NAN"
            data_dic[p] = x.astype(float)
        except Exception:
            pass
    print(f"Loaded {Nrows} rows, of {Ncols} properties:")
    print(props)
    return data_dic
