def nol_emas_juftliklar(lugat: dict[str, int]) -> dict[str, int]:
    natija = {}

    for kalit, qiymat in lugat.items():
        if qiymat != 0:
            natija[kalit] = qiymat

    return natija

mahsulotlar = {
    "olma": 5,
    "banan": 0,
    "anor": 3,
    "gilos": 0,
    "shaftoli": 7
}

filtr_qilingan = nol_emas_juftliklar(mahsulotlar)
print(filtr_qilingan)