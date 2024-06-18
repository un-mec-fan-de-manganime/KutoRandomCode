import tkinter as tk
from tkinter import messagebox
import random
import string

# Fonction pour générer le mot de passe
def generer_mot_de_passe():
    try:
        # Structure du mot de passe
        structure = 'lLlLLNN@'
        
        # Caractères utilisables
        lettres_majuscules = string.ascii_uppercase
        lettres_minuscules = string.ascii_lowercase
        chiffres = string.digits
        caracteres_speciaux = string.punctuation
        
        # Générer le mot de passe en respectant la structure
        mot_de_passe = []
        for char_type in structure:
            if char_type == 'L':
                mot_de_passe.append(random.choice(lettres_majuscules))
            elif char_type == 'l':
                mot_de_passe.append(random.choice(lettres_minuscules))
            elif char_type == 'N':
                mot_de_passe.append(random.choice(chiffres))
            elif char_type == '@':
                mot_de_passe.append(random.choice(caracteres_speciaux))
        
        # Mélanger les caractères
        random.shuffle(mot_de_passe)
        
        # Convertir la liste en chaîne de caractères
        mot_de_passe_genere = ''.join(mot_de_passe)
        entry_mot_de_passe.delete(0, tk.END)
        entry_mot_de_passe.insert(0, mot_de_passe_genere)
    except Exception as e:
        messagebox.showerror("Erreur", str(e))

# Création de la fenêtre principale
root = tk.Tk()
root.title("Générateur de Mot de Passe")

# Création des widgets
bouton_generer = tk.Button(root, text="Générer Mot de Passe", command=generer_mot_de_passe)
bouton_generer.pack(pady=10)

entry_mot_de_passe = tk.Entry(root, width=20, font=("Courier", 14, "bold"))
entry_mot_de_passe.pack(pady=10)

# Lancement de la boucle principale
root.mainloop()
