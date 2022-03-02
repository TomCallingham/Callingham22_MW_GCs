import numpy as np
from NamePreferences import name_parse, alt_name_parse
def process_names(names):
    shape = np.shape(names)
    ndim = len(shape)
    if ndim==1:
        new_names = process_single_names(names)
    else:
        new_names = process_multiple_names(names)
    return new_names

def process_single_names(names):
    known_names = list(name_parse.keys())
    new_names = np.empty_like(names)
    for i, n in enumerate(names):
        n = alt_name_parse.get(n, n)
        if n not in known_names:
            print(f"New GC: {n}")
            name_parse[n] = n
        new_names[i] = name_parse[n]
    return new_names

def process_multiple_names(names):
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