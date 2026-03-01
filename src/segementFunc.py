
def segement_customer(row):
    if row["R_score"]>=3 and row['F_score']>=3 and row['M_score']>=3:
        return "Champions"
    elif row["F_score"]>=3 and row['M_score']>=2:
        return "Loyal_cusomter"
    if row["R_score"]>=3 and row['F_score']<=3:
        return "Potenial Loyalists"
    if row["R_score"]<=2 and row['F_score']>=2 and row['M_score']>=2:
        return "At risk"
    else:
        return "Lost customers"
