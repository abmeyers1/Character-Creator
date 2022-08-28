from PyPDF2 import PdfReader, PdfWriter

# Used for testing PDF filling


reader = PdfReader("5E_CharacterSheet_Fillable.pdf")
writer = PdfWriter()

page = reader.pages[0]
fields = reader.get_fields()

writer.add_page(page)

writer.update_page_form_field_values(
    writer.pages[0], {"PlayerName": "Alex Meyers", 
                        "ClassLevel": "1", 
                        "CharacterName": "Bort the wise",
                        "Background": "dog",
                        'Race ': "Elf",     
                        "Alignment": "Good",
                        "Speed": 30,
                        "STR": 10,
                        "DEX": 10,
                        "CON": 10,
                        "INT": 10,
                        "WIS": 10,
                        "CHA": 10,}

)

# write "output" to PyPDF2-output.pdf
with open("filled-out2.pdf", "wb") as output_stream:
    writer.write(output_stream)
