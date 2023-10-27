import tkinter as tk

def berechne_werte():
    geschlecht = geschlecht_var.get()
    gewicht_str = kg_var.get().replace(',', '.')
    try:
        gewicht = float(gewicht_str)
    except ValueError:
        ergebnis_text.config(state=tk.NORMAL)
        ergebnis_text.delete(1.0, tk.END)
        ergebnis_text.insert(tk.END, "Ungültige Eingabe für Körpergewicht")
        ergebnis_text.config(state=tk.DISABLED)
        return

    if geschlecht == "Männer":
        protein = round(gewicht * 2.5, 2)
    else:
        protein = round(gewicht * 1.2, 2)

    kreatin = 5.0  # Kreatin nicht gerundet, da es eine feste Menge ist
    fett_prozent = 35
    kohlenhydrate_prozent = 50
    wasser = 3.0  # Wasser nicht gerundet, da es eine feste Menge ist

    fett = round((fett_prozent / 100) * protein, 2)
    kohlenhydrate = round((kohlenhydrate_prozent / 100) * protein, 2)

    ergebnis_text.config(state=tk.NORMAL)
    ergebnis_text.delete(1.0, tk.END)
    ergebnis_text.insert(tk.END, f"Protein: {protein}g\n")
    ergebnis_text.insert(tk.END, f"Kreatin: {kreatin}g\n")
    ergebnis_text.insert(tk.END, f"Fett: {fett}g\n")
    ergebnis_text.insert(tk.END, f"Kohlenhydrate: {kohlenhydrate}g\n")
    ergebnis_text.insert(tk.END, f"Wasser: {wasser} Liter\n")
    ergebnis_text.insert(tk.END, f"Aminosäuren: 20 Bis 60 gramm\n")

    ergebnis_text.config(state=tk.DISABLED)

# GUI
app = tk.Tk()
app.title("Nährstoffrechner")

geschlecht_label = tk.Label(app, text="Geschlecht:")
geschlecht_label.pack()
geschlecht_var = tk.StringVar()
geschlecht_var.set("Männer")
geschlecht_option = tk.OptionMenu(app, geschlecht_var, "Männer", "Frauen")
geschlecht_option.pack()

kg_label = tk.Label(app, text="Körpergewicht (in kg):")
kg_label.pack()
kg_var = tk.Entry(app)
kg_var.pack()

berechnen_button = tk.Button(app, text="Berechnen", command=berechne_werte)
berechnen_button.pack()

ergebnis_text = tk.Text(app, height=10, width=40)
ergebnis_text.pack()
ergebnis_text.config(state=tk.DISABLED)

app.mainloop()

