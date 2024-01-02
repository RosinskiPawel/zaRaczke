import tkinter as tk
import random
from tkinter import filedialog


class Poem(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Random Poem")
        self.geometry("500x500")
        self.lst1 = []
        self.lst2 = []
        self.columnconfigure(0, weight=1)

        self.rowconfigure([0, 1], weight=1)

        self.frame1 = tk.Frame(self)
        self.frame1.grid(row=0, column=0, sticky="snwe")
        self.frame1.columnconfigure([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], weight=1)
        self.frame1.rowconfigure([0, 1, 2, 3, 4, 5, 6], weight=1)

        self.labels_and_entries()

        self.frame2 = tk.Frame(self, relief=tk.SUNKEN, borderwidth=5)
        self.frame2.grid(row=1, column=0, sticky="nswe", padx=10, pady=0)
        self.frame2.columnconfigure([0, 1, 2, 3, 4, 5, 6], weight=1)
        self.frame2.rowconfigure([0, 1, 2, 3, 4, 5, 6], weight=1)
        self.lbl_poem = tk.Label(self.frame2, text=" ")
        self.lbl_poem.grid(row=0, column=3, sticky="we")

        self.save_btn = tk.Button(
            self.frame2, text="Save to file", command=self.fileToSave
        )
        self.save_btn.grid(row=6, column=3, pady=5)

    def labels_and_entries(self):
        self.lbl_titel = tk.Label(
            self.frame1, text="Enter yor favorite words, sapreted by commas."
        )
        self.lbl_titel.grid(row=0, column=3, sticky="ew", pady=0)
        label_names = [
            "Nouns:",
            "Verbs:",
            "Adjectives:",
            "Prepositines:",
            "Adverbs:",
        ]
        self.entry_list = []

        for i, lbl_name in enumerate(label_names):
            label = tk.Label(self.frame1, text=lbl_name)
            label.grid(row=i + 1, column=0, sticky="e", pady=0)

            entry = tk.Entry(self.frame1)
            entry.grid(row=i + 1, column=1, columnspan=9, sticky="we", padx=5, pady=0)
            self.entry_list.append(entry)

        self.generate_btn = tk.Button(
            self.frame1, text="Generate", command=self.click_generator
        )
        self.generate_btn.grid(row=6, column=3, pady=5)

    def click_generator(self):
        self.entries_list_creator()

        self.nouns = self.random_words(self.lst2[0])
        self.verbs = self.random_words(self.lst2[1])
        self.adj = self.random_words(self.lst2[2])
        self.preps = self.random_words(self.lst2[3])
        self.adv = self.random_words(self.lst2[4])

        a_or_an = "An" if self.adj[0][0].lower() in ["a", "e", "i", "o", "u"] else "A"
        self.lbl_poem["text"] = str(
            f"This is my poem\n\n{a_or_an} {self.adj[0]} {self.nouns[0]}\n{a_or_an} {self.adj[0]} {self.nouns[0]} {self.verbs[0]} {self.preps[0]} the {self.adj[1]} {self.nouns[1]} {self.adv[0]}, the {self.nouns[1]} {self.verbs[1]}\nthe {self.nouns[1]} {self.verbs[2]} {self.preps[1]} a {self.adj[2]} {self.nouns[2]}"
        )

    def entries_list_creator(self):
        # tworzy listę list z wpisów w entry

        for el in self.entry_list:
            value = el.get()
            self.lst1 = value.split(", ")
            if len(self.lst1) < 3:
                self.lbl_poem["text"] = "You have eneterd too few words."
            else:
                self.lst2.append(self.lst1)

        return self.lst2

    def random_words(self, lst):
        # wybiera trzy unikalne słowa z listy
        return random.sample(lst, 3)

    def fileToSave(self):
        # wybór pliku do zapisu
        self.fileName = filedialog.askopenfilename()
        with open(self.fileName, "w") as file:
            file.write(self.lbl_poem["text"])


if __name__ == "__main__":
    app = Poem()
    app.mainloop()
