def konversi_suhu(nilai, dari, ke):
    dari = dari.lower()
    ke = ke.lower()

    if dari not in ["c", "f", "k"] or ke not in ["c", "f", "k"]:
        return "Error: satuan tidak valid! Gunakan C, F, atau K."

    if dari == "k" and nilai < 0:
        return "Error: nilai Kelvin tidak boleh negatif!"

    if dari == "c":
        if ke == "f":
            return (nilai * 9/5) + 32
        elif ke == "k":
            return nilai + 273.15
        else:
            return nilai

    elif dari == "f":
        if ke == "c":
            return (nilai - 32) * 5/9
        elif ke == "k":
            return (nilai - 32) * 5/9 + 273.15
        else:
            return nilai

    elif dari == "k":
        if ke == "c":
            return nilai - 273.15
        elif ke == "f":
            return (nilai - 273.15) * 9/5 + 32
        else:
            return nilai
