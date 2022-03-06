import numpy as np
from ParseNames import process_names
from ParseProperty import process_properties


def data_add_function(data, new_data, data_name, check_GCs=[]):
    '''Check GCs to trace where certain GCs come from'''
    new_data = parse_new_data_dic(new_data)
    names = np.array(list(new_data.keys()), dtype="<U50")
    for name in names:
        gc_data = data.get(name, {})
        new_gc_data = new_data[name]
        data[name] = add_single_gc_data(gc_data, new_gc_data, data_name)

    func_check_GCs(data, check_GCs)

    return data


def parse_new_data_dic(new_data_dic):
    """Checks all names and props have been consistently parsed"""
    original_names = np.array(list(new_data_dic.keys()), dtype="<U50")
    names = process_names(original_names)
    parsed_new_data_dic = {}
    for (name, original_name) in zip(names, original_names):
        parsed_new_data_dic[name] = parse_gc_dic(new_data_dic[original_name])

    return parsed_new_data_dic


def parse_gc_dic(gc_dic):
    """Parses the properties of a gc_dic"""
    original_props = np.array(list(gc_dic.keys()))
    parsed_props = process_properties(original_props)
    parsed_gc_dic = {}
    for (p, p0) in zip(parsed_props, original_props):
        parsed_gc_dic[p] = gc_dic[p0]
    return parsed_gc_dic


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
    original_props = np.array(list(data_dic.keys()))
    parsed_props = process_properties(original_props)
    name_props = original_props[parsed_props == "name"]
    original_names = np.array([data_dic[p] for p in name_props]).transpose()
    names = process_names(original_names)

    original_props = original_props[parsed_props != "name"]
    parsed_props = parsed_props[parsed_props != "name"]
    gc_dic = {}
    for i, n in enumerate(names):
        gc_dic[n] = {p: data_dic[op][i]
                     for (op, p) in zip(original_props, parsed_props)}

    return gc_dic


def gc_dic_to_data_dic(gc_dic):
    names = np.array(list(gc_dic.keys()))
    props = np.array([])
    for n in names:
        gc_props = np.array(list(gc_dic[n].keys()))
        new_props = gc_props[np.isin(gc_props, props, invert=True)]
        if len(new_props) > 0:
            props = np.concatenate((props, new_props))
    data_dic = {"Name": names}
    for p in props:
        data_dic[p] = np.array([gc_dic[n].get(p, np.nan) for n in names])
    return data_dic
