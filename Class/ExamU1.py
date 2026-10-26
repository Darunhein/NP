"""
Explicación de los Cambios (Optimizaciones):
Compactación del Diccionario Principal (Líneas 1-9): En lugar de tener cada atributo en una línea nueva (lo que consumía ~45 líneas de código), declaré una sola lista de IPs y construí la información de cada dispositivo en una única línea. Usé nombres de llaves cortos (como "pol" en lugar de "policy") para ahorrar espacio horizontal sin perder claridad.

Evaluación de Política de Seguridad en 1 Línea (Líneas 11-14): En vez de usar bloques inmensos de if, elif y múltiples return, implementé una función validar() con operadores ternarios múltiples. Se lee así:

Retorna True si es ALLOW_ALL.
Si es BLOCK_IP, retorna True sólo si la IP del dispositivo no es la bloqueada.
Si es REQUIRED_IP (el último caso), retorna True sólo si las IPs coinciden. Retornar un Booleano (True o False) en lugar de cadenas de texto simplifica mucho las cosas.
Fusión de Ciclos de Impresión y Validación (Líneas 16-19): En lugar de crear una función dedicada para la impresión de múltiples líneas print(), lo integré todo en un solo bucle for utilizando f-strings de Python. Al mismo tiempo, en esa misma línea evaluamos si es válida usando otro pequeño operador ternario {'Válida' if validar(d) else 'Inválida'}.

Resumen usando Generadores Matemáticos (Líneas 21-26): Antes usabas un contador (ej. activos += 1) dentro de un gran bucle. La forma más "Pythonica" y compacta es usar la función sum() junto con comprensión de listas generadoras.

Ejemplo: sum(1 for d in disps.values() if d["status"] == "Activo") suma 1 por cada dispositivo que cumpla la condición.
Además, nos ahorramos calcular los dispositivos Inactivos o Inválidos creando variables adicionales. Simplemente le restamos los activos al total de equipos (usando len(disps)).
"""



# 1-5: IPs y Diccionario compactado a 1 línea por dispositivo para ahorrar espacio.
ips = ["192.168.1.10", "192.168.1.20", "192.168.1.30", "192.168.1.40", "192.168.1.50"]
disps = {
    101: {"ip": ips[0], "name": "Router", "pol": {"type": "ALLOW_ALL"}, "status": "Activo"},
    102: {"ip": ips[1], "name": "Switch", "pol": {"type": "BLOCK_IP", "ip": ips[1]}, "status": "Activo"},
    103: {"ip": ips[2], "name": "Firewall", "pol": {"type": "REQUIRED_IP", "ip": ips[2]}, "status": "Activo"},
    104: {"ip": ips[3], "name": "Servidor", "pol": {"type": "REQUIRED_IP", "ip": ips[4]}, "status": "Inactivo"},
    105: {"ip": ips[4], "name": "AP", "pol": {"type": "ALLOW_ALL"}, "status": "Activo"}
}
# 8: Validación simplificada usando retorno booleano y operador ternario (if/else en 1 línea).
def validar(d):
    p = d["pol"]
    return True if p["type"] == "ALLOW_ALL" else (d["ip"] != p["ip"] if p["type"] == "BLOCK_IP" else d["ip"] == p["ip"])
# 6,7,9: Ciclo unificado que imprime en 1 sola línea por equipo y evalúa la validez.
print("--- Estado de Dispositivos ---")
for id, d in disps.items():
    print(f"ID:{id} | {d['name']} | IP:{d['ip']} | {d['pol']['type']} | {d['status']} | Config: {'Válida' if validar(d) else 'Inválida'}")
# 10: Resumen optimizado usando sum() y generadores en vez de for-loops y múltiples contadores.
activos = sum(1 for d in disps.values() if d["status"] == "Activo")
validos = sum(1 for d in disps.values() if validar(d))
# Imprimimos todo el resumen calculando los inactivos/inválidos con restas.
print(f"\n--- Resumen ---\nActivos: {activos} | Inactivos: {len(disps)-activos} | Válidas: {validos} | Inválidas: {len(disps)-validos}")