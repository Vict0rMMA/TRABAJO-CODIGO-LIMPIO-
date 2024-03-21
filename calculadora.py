from datetime import datetime

class CalculadoraLiquidacion:
    def __init__(self, valor_uvt=39205):
        self.valor_uvt = valor_uvt

    def calcular_resultados_prueba(self, salario_basico, fecha_inicio_labores, fecha_ultimas_vacaciones, dias_acumulados_vacaciones):
        indemnizacion = self.calcular_liquidacion(salario_basico, fecha_inicio_labores, fecha_ultimas_vacaciones)
        vacaciones = self.calcular_vacaciones(salario_basico, dias_acumulados_vacaciones)
        cesantias = self.calcular_cesantias(salario_basico, dias_acumulados_vacaciones)
        intereses_cesantias = self.calcular_intereses_cesantias(cesantias, vacaciones)
        primas = self.calcular_prima(salario_basico, dias_acumulados_vacaciones)
        retencion_fuente = self.calcular_retencion(indemnizacion + vacaciones + cesantias + intereses_cesantias + primas)
        total_pagar = indemnizacion + vacaciones + cesantias + intereses_cesantias + primas - retencion_fuente
        return indemnizacion, vacaciones, cesantias, intereses_cesantias, primas, retencion_fuente, total_pagar

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
        if motivo.lower() not in motivos_validos:
            raise ValueError("El motivo de terminación no es válido")


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

    
    def calcular_indemnizacion(self, salario, motivo, meses_trabajados):
        motivos_validos = ['despido', 'renuncia', 'retiro']
        motivo_lower = motivo.lower()

        if motivo_lower not in motivos_validos:
            raise ValueError(f"El motivo de terminación '{motivo}' no es válido. Los motivos válidos son: {', '.join(motivos_validos)}")

        factor_despido = 0.5 if motivo_lower == 'despido' else 0.0
        valor_indemnizacion = salario * meses_trabajados * factor_despido

        return valor_indemnizacion



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