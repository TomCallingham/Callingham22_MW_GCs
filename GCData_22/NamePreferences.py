# Variant_Names
alt_name_parse = {}
# Terzan
alt_name_parse = alt_name_parse | {f"Ter{i}": f"Terzan{i}" for i in range(1, 15)}

# Palomar
alt_name_parse = alt_name_parse | {f"Palomar{i}": f"Pal{i}" for i in range(1, 20)}

# Djorg
alt_name_parse = alt_name_parse | {f"Djor{i}": f"Djorg{i}" for i in range(1, 4)}
alt_name_parse = alt_name_parse | {f"Dorg{i}": f"Djorg{i}" for i in range(1, 4)}
alt_name_parse = alt_name_parse | {f"Dor{i}": f"Djorg{i}" for i in range(1, 4)}

# 2MassSurvey
alt_name_parse["2MS-GC01"] = "GLIMPSE01"
alt_name_parse["2MASSGC01"] = "GLIMPSE01"
alt_name_parse["2MS-GC02"] = "GLIMPSE02"
alt_name_parse["2MASSGC02"] = "GLIMPSE02"

# NGC 3 digit
alt_name_parse["NGC0104"] = "NGC104"
alt_name_parse["NGC0288"] = "NGC288"
alt_name_parse["NGC0362"] = "NGC362"

# Eso NGCs
alt_name_parse["ESO280SC06"] = "ESO-SC06"
alt_name_parse["ESO452SC11"] = "ESO452"

# Ryu Gys
alt_name_parse["Ryu05"] = "Ryu059"
alt_name_parse["Ryu87"] = "Ryu879"

# Set Preferences for Names
name_parse = {}
name_parse["1636-283"] = "ESO452"
name_parse["NGC104"] = "47Tuc"
name_parse["NGC1904"] = "M79"
name_parse["NGC4590"] = "M68"
name_parse["NGC5024"] = "M53"
name_parse["NGC5139"] = "oCen"
name_parse["NGC5272"] = "M3"
name_parse["NGC5904"] = "M5"
name_parse["NGC6838"] = "M71"

name_parse["NGC7078"] = "M15"
name_parse["NGC6341"] = "M92"

name_parse["RLGC1"] = "Ryu059"
name_parse["RLGC2"] = "Ryu879"

name_parse["ESO280"] = "ESO-SC06"
name_parse["ESO371"] = "E3"

name_parse['Laevens1'] = "Crater"

name_parse["Arp1"] = "Pal14"
