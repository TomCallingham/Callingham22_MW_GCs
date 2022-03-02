
labels = {}
labels["name"] = ["Name", "Names", "name", "names", "cluster", "NGC", "ngc", "name2", "Name2"]

# Chemistry
labels["Fe_H"] = ["Fe_H", "Met", "Metallicity"]
labels["Alpha_Fe"] = ["Alpha_Fe", "Alpha"]

# Age
labels["Age"] = ["Age"]

# Magnitude
labels["Mv"] = ["Mv", "Mvt"]
labels["m_Mv"] = ["m_Mv"]

# Mass
labels["Mass"] = ["Mass"]

# SkyObs
labels["dist"] = ["dsun", "dist", "Dist"]
labels["l_deg"] = ["l_deg"]
labels["b_deg"] = ["b_deg"]
labels["ra_deg"] = ["ra_deg"]
labels["dec_deg"] = ["dec_deg"]
labels["pmra"] = ["pmra"]
labels["pmdec"] = ["pmdec"]
labels["pmcorr"] = ["pmcorr"]
labels["vlos"] = ["vlos"]

property_parser = {}
for l in list(labels.keys()):
    for n in labels[l]:
        property_parser[n] = l

    if l not in ["name"]:
        for extra in ["", "_1os", "_1us"]:
            err_label = [l + "_err" + extra for l in labels[l]] + \
                [l + "_Err" + extra for lab in labels[l]]
            for n in err_label:
                property_parser[n] = l + "_err" + extra
                
def parse_columns(original_columns):
    known_labels = np.array(list(col_property_parser.keys()))
    unknown = np.isin(original_columns, known_labels, invert=True)
    if unknown.sum() > 0:
        print("Unknown labels:")
        print(np.array(original_columns)[unknown])
    parse_columns = np.array([property_parser.get(c, c) for c in original_columns])
    return parse_columns

def process_properties(props):
    known_props = list(poperty_parser.keys())
    new_prop = np.empty_like(props)
    for i, n in enumerate(kn):
        if n not in known_props:
            print(f"New GC: {n}")
            name_parse[n] = n
        new_names[i] = name_parse[n]
    return new_prop