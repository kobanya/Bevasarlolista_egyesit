#NB. 2023.04.26

import tkinter as tk
from tkinter import scrolledtext

def mentes():
    nev = nev_input.get().capitalize()
    termekek = termekek_input.get().split(",")

    # fájlba írás
    with open('bevasarlas.csv', 'a') as f:
        sor = nev + ',' + ','.join(termekek) + '\n'
        f.write(sor)

def betoltes():
    # Előző tartalom törlése
    scrolled_text.delete('1.0', tk.END)

    with open('bevasarlas.csv', 'r') as f:
        sorok = f.read().splitlines()
        for sor in sorok:
            sor_text = sor.replace(",", "\t\t")
            scrolled_text.insert(tk.END, sor_text + "\n")

def change_color(event):
    widget = event.widget
    widget.tag_configure('selected', background='light blue')

    selection = widget.tag_ranges(tk.SEL)
    if selection:
        widget.tag_add('selected', selection[0], selection[1])

# GUI létrehozása
root = tk.Tk()
root.title("Bevásárlólista")

# Név beviteli mező létrehozása
nev_label = tk.Label(root, text="Név:")
nev_label.grid(row=0, column=0, sticky="w")

nev_input = tk.Entry(root)
nev_input.grid(row=0, column=1)

# Termékek beviteli mező létrehozása
termekek_label = tk.Label(root, text="Termékek:")
termekek_label.grid(row=1, column=0, sticky="w")

termekek_input = tk.Entry(root)
termekek_input.grid(row=1, column=1)

# Mentés gomb létrehozása
mentes_button = tk.Button(root, text="Mentés", command=mentes)
mentes_button.grid(row=2, column=0)

# Betöltés gomb létrehozása
betoltes_button = tk.Button(root, text="Ablak betöltése", command=betoltes)
betoltes_button.grid(row=2, column=1)

# Táblázat létrehozása
scrolled_text = scrolledtext.ScrolledText(root, width=100, height=15)
scrolled_text.grid(row=3, columnspan=2, padx=10, pady=10)

# Táblázat sorok kattinthatóvá tétele
scrolled_text.bind('<Button-1>', change_color)

# Azonos termékek számolása
def azonos_termekek_szamolasa():
    termekek = []
    with open('bevasarlas.csv', 'r') as f:
        for sor in f:
            nev, termek_lista = sor.strip().split(',')
            termekek.extend(termek_lista.split(','))
    termekek_szama = {termek: termekek.count(termek) for termek in set(termekek)}
    scrolled_text.insert(tk.END, "\nAzonos termékek száma:\n")
    for termek, db in termekek_szama.items():
        scrolled_text.insert(tk.END, f"{termek}: {db}\n")


def osszesites():
    termekek = {}
    with open('bevasarlas.csv', 'r') as f:
        for sor in f:
            nev, termek_lista = sor.strip().split(',', maxsplit=1)
            for termek in termek_lista.split(','):
                termek = termek.strip().capitalize()
                if termek in termekek:
                    termekek[termek] += 1
                else:
                    termekek[termek] = 1

    # Új ScrolledText mező létrehozása az összesített lista megjelenítéséhez
    scrolled_text_osszesites = scrolledtext.ScrolledText(root, width=50, height=15)
    scrolled_text_osszesites.grid(row=6, columnspan=2, padx=10, pady=10)

    # Az összesített lista kiírása táblázatos formában
    scrolled_text_osszesites.insert(tk.END, "Termékek összesítése:\n\n")
    scrolled_text_osszesites.insert(tk.END, "Termék\t\tDarabszám\n")
    scrolled_text_osszesites.insert(tk.END, "------\t\t---------\n")
    for termek, db in termekek.items():
        scrolled_text_osszesites.insert(tk.END, f"{termek}\t\t{db}\n")


# Összesítés gomb létrehozása
osszesites_gomb = tk.Button(root, text="Termékek összesítése", command=osszesites)
osszesites_gomb.grid(row=5, columnspan=2, pady=10)


root.mainloop()
