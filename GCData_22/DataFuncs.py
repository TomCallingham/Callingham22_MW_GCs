import numpy as np
from ParseNames import process_names, name_parse,alt_name_parse, create_alt_name_list
from ParseProperty import property_parser, process_properties


def data_add_function(data, new_data, data_name, check_GCs=[]):
    '''Check GCs to trace where certain GCs come from'''
    new_data = parse_new_data(new_data)
    names = np.array(list(new_data.keys()), dtype="<U50")
    for name in names:
        gc_data = data.get(name, {})
        new_gc_data = new_data[name]
        data[name] = add_single_gc_data(gc_data, new_gc_data, data_name)

    if len(check_GCs) > 0:
        func_check_GCs(data, check_GCs)

    return data

def parse_new_data(new_data):
    original_names = np.array(list(new_data.keys()), dtype="<U50")
    names = process_names(original_names)
    parsed_new_data = {}
    for (name, original_name) in zip(names, original_names):
        parsed_new_data[name] = parse_gc_data(new_data[original_name])
        
    return parsed_new_data

def parse_gc_data(gc_data):
    original_props = np.array(list(gc_data.keys()))
    parsed_props = process_properties(original_props)
    parsed_gc_data = {}
    for (p, p0) in zip(parsed_props, original_props):
        parsed_gc_data[p] = gc_data[p0]
    return parsed_gc_data



def add_single_gc_data(gc_data, new_gc_data, data_name, asym_errors=True):
    if asym_errors:
        new_gc_data = create_asym_errors(new_gc_data)
    props = list(new_gc_data.keys())
    for p in props:
        prop_data = gc_data.get(p, {})
        prop_data[data_name] = new_gc_data[p]
        gc_data[p] = prop_data

    return gc_data


def create_asym_errors(gc_data):
    # If errors are not symmetric, create average errors
    props = list(gc_data.keys())
    asym_props = [p for p in props if p + "_err_1os" in props and p + "_err" not in props]
    for p in asym_props:
        # print(f"Averaging Errors for property {p}")
        x_1os = gc_data[p + "_err_1os"]
        x_1us = gc_data[p + "_err_1us"]
        x_err = 0.5 * (x_1os + np.abs(x_1us))
        gc_data[p + "_err"] = x_err
    return gc_data


def func_check_GCs(data, check_GCs):
    gcs = np.array(list(data.keys()))
    Ngcs = len(gcs)
    print(f"Number of total GCs: {Ngcs}")
    check_filt = np.isin(gcs, check_GCs)
    if check_filt.sum() > 0:
        print("Check GCs present!")
        print(gcs[check_filt])
    return

def data_dic_to_gc_dic(data_dic):
    original_columns = np.array(list(data_dic.keys()))
    Ncols = len(original_columns)
    Nrows = len(data_dic[original_columns[0]])
    data_array = np.empty((Nrows, Ncols), dtype="<U50")
    for n, col in enumerate(original_columns):
        data_array[:, n] = np.array(data_dic[col])
    return data_array_to_gc_dic(data_array, original_columns)

def gc_dic_to_data_dic(gc_dic):
    names = np.array(list(gc_dic.keys()))
    props = np.array([])
    for n in names:
        gc_props = np.array(list(gc_dic[n].keys()))
        new_props = gc_props[np.isin(gc_props,props,invert = True)]
        if len(new_props)>0:
            props = np.concatenate((props,new_props))
    data_dic = {"Name": names}
    for p in props:
        data_dic[p] = np.array([gc_dic[n].get(p,np.nan) for n in names])
    return data_dic

def data_array_to_gc_dic(data_array, original_columns):
    columns = process_properties(np.array(original_columns))
    names = process_data_array_names(columns, data_array)
    gc_dic = process_data_array_properties(names, columns, data_array)
    return gc_dic

def process_data_array_properties(names, columns, data_array):
    columns = np.array(columns)
    not_name = (columns != 'name')
    props = columns[not_name]
    props_data = data_array[:, not_name]
    props_data[np.isin(props_data, ['-', ''])] = 'NAN'
    props_data = props_data.astype(float)
    gc_dic = {}
    for ind_name, name in enumerate(names):
        gc_dic[name] = {}
        for (ind_p, p) in enumerate(props):
            x = props_data[ind_name, ind_p]
            if x != np.nan and np.isfinite(x):
                gc_dic[name][p] = x
    return gc_dic

def process_data_array_names(columns, data_array):
    name_column = (columns == 'name')
    Nname_col = name_column.sum()
    if Nname_col == 0:
        print('Error, No names found')
    elif Nname_col == 1:
        names = data_array[:, name_column].reshape(-1)
    elif Nname_col > 1:
        names = data_array[:, name_column].reshape(-1, Nname_col)
    new_names = process_names(names)
    return new_names