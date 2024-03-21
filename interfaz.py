import tkinter as tk
from tkinter import messagebox
from calculadora import CalculadoraLiquidacion

class InterfazCalculadora(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculadora de Liquidación")
        self.geometry("400x300")

        self.calculadora = CalculadoraLiquidacion()

        tk.Label(self, text="Salario Básico:").pack()
        self.salario_entry = tk.Entry(self)
        self.salario_entry.pack()

        tk.Label(self, text="Fecha de inicio de labores (dd/mm/aaaa):").pack()
        self.fecha_inicio_entry = tk.Entry(self)
        self.fecha_inicio_entry.pack()

        tk.Label(self, text="Fecha de últimas vacaciones (dd/mm/aaaa):").pack()
        self.fecha_vacaciones_entry = tk.Entry(self)
        self.fecha_vacaciones_entry.pack()

        tk.Label(self, text="Días acumulados de vacaciones:").pack()
        self.dias_vacaciones_entry = tk.Entry(self)
        self.dias_vacaciones_entry.pack()

        self.calcular_button = tk.Button(self, text="Calcular", command=self.calcular)
        self.calcular_button.pack()

    def calcular(self):
        salario = float(self.salario_entry.get())
        fecha_inicio = self.fecha_inicio_entry.get()
        fecha_vacaciones = self.fecha_vacaciones_entry.get()
        dias_vacaciones = int(self.dias_vacaciones_entry.get())

        try:
            indemnizacion, vacaciones, cesantias, intereses_cesantias, primas, retencion_fuente, total_pagar = self.calculadora.calcular_resultados_prueba(
                salario, fecha_inicio, fecha_vacaciones, dias_vacaciones)

            messagebox.showinfo("Resultados", f"Indemnización: {indemnizacion}\nVacaciones: {vacaciones}\nCesantías: {cesantias}\nIntereses de Cesantías: {intereses_cesantias}\nPrimas: {primas}\nRetención en la fuente: {retencion_fuente}\nTotal a pagar: {total_pagar}")
        except ValueError as e:
            messagebox.showerror("Error", str(e))

if __name__ == "__main__":
    app = InterfazCalculadora()
    app.mainloop()
