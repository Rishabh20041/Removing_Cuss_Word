import tkinter as tk
import re
cuss_words = ['Fuck off', 'piss off','Bugger off','Bloody hell','Bastard',' Motherfucker','Son of a bitch','Asshole']  
def censor_cuss_words():
    text = input_text.get("1.0", tk.END)
    for word in cuss_words:
        pattern = r"\b" + re.escape(word) + r"\b"  
        text = re.sub(pattern, "*" * len(word), text, flags=re.IGNORECASE) 
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, text)
window = tk.Tk()
window.title("Cuss Word Filter")
input_text = tk.Text(window, height=10, width=50)
input_text.pack(pady=10)
filter_button = tk.Button(window, text="Filter Cuss Words", command=censor_cuss_words)
filter_button.pack(pady=5)
output_text = tk.Text(window, height=10, width=50)
output_text.pack(pady=10)
window.mainloop()
