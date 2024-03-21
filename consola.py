from datetime import datetime

class CalculadoraLiquidacion:
    def __init__(self, valor_uvt=39205):
        self.valor_uvt = valor_uvt

    def calcular_liquidacion(self, salario, fecha_inicio, fecha_fin):
        if salario < 0:
            raise ValueError("El salario básico no puede ser negativo")

        fecha_inicio = datetime.strptime(fecha_inicio, "%d/%m/%Y")
        fecha_fin = datetime.strptime(fecha_fin, "%d/%m/%Y")
        dias_totales = (fecha_fin - fecha_inicio).days + 1
        dias_faltantes = 30 - fecha_fin.day
        valor_diario = salario / 30
        liquidacion = valor_diario * dias_faltantes

        return round(liquidacion)

    def calcular_indemnizacion(self, salario, motivo, meses_trabajados):
        motivos_validos = ['despido', 'renuncia', 'retiro']
        motivo_lower = motivo.lower()

        if motivo_lower not in motivos_validos:
            raise ValueError(f"El motivo de terminación '{motivo}' no es válido. Los motivos válidos son: {', '.join(motivos_validos)}")

        factor_despido = 0.5 if motivo_lower == 'despido' else 0.0
        valor_indemnizacion = salario * meses_trabajados * factor_despido

        return valor_indemnizacion

    def calcular_vacaciones(self, salario_mensual, dias_trabajados):
        if dias_trabajados < 0:
            raise ValueError("Los días acumulados de vacaciones no pueden ser negativos")

        valor_diario = salario_mensual / 30
        valor_vacaciones = (salario_mensual * dias_trabajados) / 720

        return round(valor_vacaciones)

    def calcular_cesantias(self, salario_mensual, dias_trabajados):
        if dias_trabajados < 0:
            raise ValueError("Los días trabajados no pueden ser negativos")

        cesantias = (salario_mensual * dias_trabajados) / 360
        return round(cesantias)

    def calcular_intereses_cesantias(self, cesantias, vacaciones):
        if cesantias < 0:
            raise ValueError("El valor de las cesantías no puede ser negativo")
        if vacaciones < 0:
            raise ValueError("El valor de las vacaciones no puede ser negativo")

        valor_intereses_cesantias = (cesantias + vacaciones) * 0.12
        return valor_intereses_cesantias

    def calcular_prima(self, salario_mensual, dias_trabajados):
        prima = salario_mensual * (dias_trabajados / 360)
        return round(prima / 2)

    def calcular_retencion(self, salario_basico):
        if not isinstance(salario_basico, (int, float)):
            raise ValueError("El salario básico debe ser un número")

        retencion = 0

        salario_basico = float(salario_basico)

        if salario_basico <= 42412:
            pass
        elif salario_basico <= 636132:
            ingreso_uvt = salario_basico / self.valor_uvt
            base_uvt = ingreso_uvt - 95
            base_pesos = base_uvt * self.valor_uvt
            retencion = (base_pesos * 0.19) + (10 * self.valor_uvt)

        return round(retencion)

    def imprimir_resultados(self, indemnizacion, vacaciones, cesantias, intereses_cesantias, primas, retencion_fuente, total_pagar):
        if total_pagar < 0:
            raise ValueError("El total a pagar no puede ser negativo")

        print("Resultados:")
        print(f"Indemnización: {indemnizacion}")
        print(f"Vacaciones: {vacaciones}")
        print(f"Cesantías: {cesantias}")
        print(f"Intereses sobre cesantías: {intereses_cesantias}")
        print(f"Prima: {primas}")
        print(f"Retención en la fuente: {retencion_fuente}")
        print(f"Total a pagar: {total_pagar}")


if __name__ == "__main__":
    calculadora = CalculadoraLiquidacion()
    
    salario = float(input("Ingrese el salario básico: "))
    fecha_inicio = input("Ingrese la fecha de inicio (DD/MM/YYYY): ")
    fecha_fin = input("Ingrese la fecha de fin (DD/MM/YYYY): ")
    motivo = input("Ingrese el motivo de terminación (despido/renuncia/retiro): ")
    meses_trabajados = int(input("Ingrese los meses trabajados: "))
    dias_trabajados = int(input("Ingrese los días trabajados: "))

    indemnizacion = calculadora.calcular_indemnizacion(salario, motivo, meses_trabajados)
    vacaciones = calculadora.calcular_vacaciones(salario, dias_trabajados)
    cesantias = calculadora.calcular_cesantias(salario, dias_trabajados)
    intereses_cesantias = calculadora.calcular_intereses_cesantias(cesantias, vacaciones)
    primas = calculadora.calcular_prima(salario, dias_trabajados)
    retencion_fuente = calculadora.calcular_retencion(indemnizacion + vacaciones + cesantias + intereses_cesantias + primas)
    total_pagar = indemnizacion + vacaciones + cesantias + intereses_cesantias + primas - retencion_fuente

    calculadora.imprimir_resultados(indemnizacion, vacaciones, cesantias, intereses_cesantias, primas, retencion_fuente, total_pagar)
