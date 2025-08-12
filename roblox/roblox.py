#!/usr/bin/env python3
"""
maze_single_gui.py

Interfaz gráfica simplificada:
- La verdad (“true”) siempre es 12 giros.
- El usuario ingresa su predicción (un entero).
- Calcula métricas (TP, FP, FN, TN, Precision, Recall, Accuracy)
  y muestra la matriz de confusión para este único ejemplo.
"""

import tkinter as tk
from tkinter import messagebox
from sklearn.metrics import confusion_matrix

GROUND_TRUTH = 12  # siempre 12 giros
POS_CLASS    = 12  # definimos la “clase positiva” como 12

def calculate_metrics():
    pred_str = entry.get().strip()
    if not pred_str:
        messagebox.showwarning("Atención", "Por favor, ingresa tu predicción.")
        return

    try:
        pred = int(pred_str)
    except ValueError:
        messagebox.showerror("Error de formato", "Introduce un número entero.")
        return

    true = [GROUND_TRUTH]
    pred_list = [pred]

    # Cálculo de TP, FP, FN, TN para un solo ejemplo
    tp = 1 if pred == POS_CLASS == GROUND_TRUTH else 0
    fp = 1 if pred == POS_CLASS and GROUND_TRUTH != POS_CLASS else 0
    fn = 1 if pred != POS_CLASS and GROUND_TRUTH == POS_CLASS else 0
    tn = 1 if pred != POS_CLASS and GROUND_TRUTH != POS_CLASS else 0

    precision = tp / (tp + fp) if (tp + fp) > 0 else 0.0
    recall    = tp / (tp + fn) if (tp + fn) > 0 else 0.0
    accuracy  = (tp + tn) / 1  # sobre un único caso

    # Matriz de confusión (binary)
    labels = [POS_CLASS, f"≠{POS_CLASS}"]
    # Convertimos las listas a binario: positivo si ==12, negativo si !=12
    true_bin = [1 if v == POS_CLASS else 0 for v in true]
    pred_bin = [1 if v == POS_CLASS else 0 for v in pred_list]
    cm = confusion_matrix(true_bin, pred_bin, labels=[1,0])

    # Mostrar resultados
    text.config(state=tk.NORMAL)
    text.delete("1.0", tk.END)
    text.insert(tk.END, f"Verdad (ground truth): {GROUND_TRUTH}\n")
    text.insert(tk.END, f"Predicción         : {pred}\n\n")

    text.insert(tk.END, f"TP: {tp}   FP: {fp}\n")
    text.insert(tk.END, f"FN: {fn}   TN: {tn}\n\n")

    text.insert(tk.END, f"Precision : {precision*100:.2f}%\n")
    text.insert(tk.END, f"Recall    : {recall*100:.2f}%\n")
    text.insert(tk.END, f"Accuracy  : {accuracy*100:.2f}%\n\n")

    text.insert(tk.END, "Matriz de confusión (binaria):\n")
    text.insert(tk.END, "      Pred=12  Pred≠12\n")
    text.insert(tk.END, f"V=12   {cm[0,0]}        {cm[0,1]}\n")
    text.insert(tk.END, f"V≠12   {cm[1,0]}        {cm[1,1]}\n")

    text.config(state=tk.DISABLED)


# --- Construcción de la ventana ---
root = tk.Tk()
root.title("Predicción de Giros en el Laberinto")

frame = tk.Frame(root, padx=10, pady=10)
frame.pack(fill=tk.BOTH, expand=True)

tk.Label(frame, text="Predice cuántos giros (entero):").grid(row=0, column=0, sticky="w")
entry = tk.Entry(frame, width=20)
entry.grid(row=1, column=0, pady=(0,10))

btn = tk.Button(frame, text="Calcular métricas", command=calculate_metrics)
btn.grid(row=2, column=0, pady=(0,10))

text = tk.Text(frame, height=12, state=tk.DISABLED)
text.grid(row=3, column=0, sticky="nsew")

frame.columnconfigure(0, weight=1)
frame.rowconfigure(3, weight=1)

root.mainloop()
