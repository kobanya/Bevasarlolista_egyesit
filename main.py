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
    # frissíti az ablak tartalmát
    betoltes()
    osszesites()

def betoltes():
    # Előző tartalom törlése
    scrolled_text.delete('1.0', tk.END)

    with open('bevasarlas.csv', 'r') as f:
        sorok = f.read().splitlines()

        sorok.sort()
        for sor in sorok:
            sor_text = sor.replace(",", "\t\t")
            scrolled_text.insert(tk.END, sor_text + "\n")
    osszesites()

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

    # rendezés a kulcsok (termékek) alapján
    rendezett_termekek = sorted(termekek.items())

    # Új ScrolledText mező létrehozása az összesített lista megjelenítéséhez
    scrolled_text_osszesites = scrolledtext.ScrolledText(root, width=100, height=10)
    scrolled_text_osszesites.grid(row=6, columnspan=2, padx=20, pady=10)

    # Az összesített lista kiírása táblázatos formában

    scrolled_text_osszesites.insert(tk.END, "Termék\t\t\t\tDarabszám\n")
    scrolled_text_osszesites.insert(tk.END, "------\t\t\t\t---------\n")
    for termek, db in rendezett_termekek:
        scrolled_text_osszesites.insert(tk.END, f"{termek}\t\t\t\t{db}\n")



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

# Táblázat létrehozása
scrolled_text = scrolledtext.ScrolledText(root, width=100, height=15)
scrolled_text.grid(row=3, columnspan=2, padx=10, pady=10)


betoltes()

root.mainloop()