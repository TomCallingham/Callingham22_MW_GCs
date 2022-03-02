import numpy as np
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
            err_label = [lab + "_err" + extra for lab in labels[l]] + \
                [lab + "_Err" + extra for lab in labels[l]]
            for n in err_label:
                property_parser[n] = l + "_err" + extra


def process_properties(props):
    known_props = np.array(list(property_parser.keys()))
    new_props = props[np.isin(props, known_props, invert=True)]
    for p in new_props:
        print(f"New Prop: {p}")
        property_parser[p] = p
    parsed_props = np.array([property_parser[p] for p in props])
    return parsed_props
