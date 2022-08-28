from PyPDF2 import PdfReader, PdfWriter
def process(character):
    reader = PdfReader("5E_CharacterSheet_Fillable.pdf")
    writer = PdfWriter()

    page = reader.pages[0]
    fields = reader.get_fields()

    writer.add_page(page)

    writer.update_page_form_field_values(
        writer.pages[0], {"PlayerName": character.player_name, 
                        "ClassLevel": character.charclass + " 1", 
                        "CharacterName": character.char_name,
                        "Background": character.background,
                        "Race " : character.heritage,
                        "HPMax": character.max_hp,
                        "HPCurrent": character.max_hp,
                        "Speed": character.speed,
                        "Initiative": int(character.stats["DEXmod"]),
                        "ProfBonus": character.ProfBonus,
                        "STR": int(character.stats["STR"]),
                        "STRmod": int(character.stats["STRmod"]) ,
                        "DEX": int(character.stats["DEX"]),
                        "DEXmod ": int(character.stats["DEXmod"]),
                        "CON": int(character.stats["CON"]),
                        "CONmod": int(character.stats["CONmod"]) ,
                        "INT": int(character.stats["INT"]),
                        "INTmod": int(character.stats["INTmod"]) ,
                        "WIS": int(character.stats["WIS"]),
                        "WISmod": int(character.stats["WISmod"]) ,
                        "CHA": int(character.stats["CHA"]),
                        "CHamod": int(character.stats["CHAmod"]) ,}

    )

    # write "output" to PyPDF2-output.pdf
    with open("filled-out.pdf", "wb") as output_stream:
        writer.write(output_stream)
    return
# process('h')