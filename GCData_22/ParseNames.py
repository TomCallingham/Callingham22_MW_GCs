import numpy as np
from NamePreferences import name_parse, alt_name_parse


def process_names(names):
    shape = np.shape(names)
    ndim = len(shape)
    if ndim == 1:
        new_names = process_single_names(names)
    else:
        new_names = process_multiple_names(names)
    return new_names


# def process_single_names(names):
#     known_names = list(name_parse.keys())
#     for n in names:
#         if n not
#     # new_names = np.empty_like(names)
#     # for i, n in enumerate(names):
#     #     n = alt_name_parse.get(n, n)
#     #     if n not in known_names:
#     #         print(f"New GC: {n}")
#     #         name_parse[n] = n
#     #     new_names[i] = name_parse[n]
#     return parsed_names


def process_single_names(names):
    known_names = np.array(list(name_parse.keys()))
    names = np.array([alt_name_parse.get(n, n) for n in names])
    new_names = names[np.isin(names, known_names, invert=True)]
    for n in new_names:
        print(f"New GC: {n}")
        name_parse[n] = n
    parsed_names = np.array([name_parse[n] for n in names])
    return parsed_names


def process_multiple_names(names):
    ''' Given array of names and alternate names, finds the preferred name and update 
    the parser'''
    known_names = list(name_parse.keys())
    nGCs = np.shape(names)[0]
    new_names = np.empty((nGCs), dtype='<U50')
    for i in range(nGCs):
        gc_names = names[i, :]
        in_filt = np.isin(gc_names, known_names) * (gc_names != '')
        if in_filt.sum() > 0:
            n = gc_names[in_filt][0]
            new_names[i] = name_parse[alt_name_parse.get(n, n)]
            for n in gc_names:
                name_parse[n] = new_names[i]
        else:
            gc_nam = gc_names[gc_names != ''][0]
            gc_nam = alt_name_parse.get(gc_nam, gc_nam)
            for n in gc_names:
                name_parse[n] = gc_nam
            new_names[i] = gc_nam
    return new_names


def create_alt_name_list(name_parse):
    '''Given the name parser, find a list of alternate names'''
    known_names = list(name_parse.keys())
    alt_name_dic = {n: [] for n in known_names}
    for n in known_names:
        name = name_parse[n]
        if name != n:
            alt_name_dic[name].append(n)
    return alt_name_dic
