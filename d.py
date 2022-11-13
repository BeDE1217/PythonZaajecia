
def table_start():
    return "<table>/n"
def table_end():
    return "</table>"

tekst_do_zapisania=""
with open('dane.csv')as plik:
    tekst_do_zapisania+=table_start()
    for linia in plik:
        for column in linia.split(','):
            tekst_do_zapisania+=table_end()
zapis=open("index.html", "w")
zapis.write(tekst_do_zapisania)
zapis.close()