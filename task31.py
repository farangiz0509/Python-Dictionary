def harf_sanoq(matn: str) -> dict[str, int]:
    soni = {}

    for harf in matn:
        if harf == ' ':
            continue
        soni[harf] = soni.get(harf, 0) + 1

    return soni
matn = input("matin kiriting: ")

natija = harf_sanoq(matn)
print(natija)