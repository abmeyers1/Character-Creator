"""
11 Str Save
18 - dex save
19 - con save
20 - int save
21 - wis save
22 - Cha save
23 - acro
24 - animal
25 - arcana
26 - athletics
27 - decep
28 - history
29 - insight
30 -intim
31 - invest
32 - med
33 - nature
34- percep
35 - perform
36- persuasion
37- religion
38 - sleight of hand
39- stealth
40 -  survival



# 309
# 3010 - 3083 
"""
from PyPDF2 import PdfReader, PdfWriter

for i in range (11,41):
    reader = PdfReader("5E_CharacterSheet_Fillable.pdf")
    writer = PdfWriter()

    page = reader.pages[0]
    fields = reader.get_fields()

    writer.add_page(page)

    writer.update_page_form_field_values(
        writer.pages[0], {f"Check Box {i}":"/Yes"}
    )

    with open(f"./Checks/Checkbox_{i}.pdf", "wb") as output_stream:
        writer.write(output_stream)
    