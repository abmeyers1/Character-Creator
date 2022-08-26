from PyPDF2 import PdfReader, PdfWriter
def process(character):
    reader = PdfReader("5E_CharacterSheet_Fillable.pdf")
    writer = PdfWriter()

    page = reader.pages[0]
    fields = reader.get_fields()

    writer.add_page(page)

    writer.update_page_form_field_values(
        writer.pages[0], {"PlayerName": character.player_name, 
                        "ClassLevel": "1", 
                        "CharacterName": character.char_name,
                        "Background": character.char_back,
                        "Race" : character.char_heritage}

    )

    # write "output" to PyPDF2-output.pdf
    with open("filled-out.pdf", "wb") as output_stream:
        writer.write(output_stream)
    return
# process('h')