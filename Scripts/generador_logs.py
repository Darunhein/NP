"""
==============================================================================
GUÍA DE PRÁCTICA: GENERADOR DE LOGS DE RED EN FORMATO JSONL CON PYTHON
==============================================================================

OBJETIVO DE LA PRÁCTICA
------------------------------------------------------------------------------
Aprenderás a escribir un script de Python limpio, modular y documentado
que simule y registre eventos de tráfico de red en un archivo con formato
JSON Lines (.jsonl).


¿QUÉ ES UN ARCHIVO JSONL?
------------------------------------------------------------------------------
Un archivo JSONL (JSON Lines) almacena un objeto JSON válido en CADA LÍNEA.
Es un estándar muy utilizado en análisis de logs, ciberseguridad y Big Data
porque permite procesar archivos masivos línea por línea sin consumir
demasiada memoria RAM.

Ejemplo de contenido de un archivo .jsonl:
{"timestamp": "2026-11-01T12:00:00", "ip_origen": "192.168.1.10", "evento": "CONEXION_OK"}
{"timestamp": "2026-11-01T12:00:05", "ip_origen": "10.0.0.55", "evento": "ACCESO_DENEGADO"}


ESTRUCTURA DE DOCUMENTACIÓN DE FUNCIONES (DOCSTRING)
------------------------------------------------------------------------------
Cada función que escribas debe contener un bloque de documentación en la
parte superior con el siguiente formato:
"""
# def nombre_de_funcion(parametro1):
"""
Descripción corta de lo que hace la función.

Autor: Nombre del Alumno
Fecha de creación: YYYY-MM-DD

Parámetros:
parametro1 (tipo): Explicación de para qué sirve.

Salida:
tipo: Explicación del dato que devuelve.
"""

"""
CÓDIGO FUENTE COMPLETO (generador_logs.py)
------------------------------------------------------------------------------
"""

import json
import random
import re
import socket
import subprocess
import platform
from datetime import datetime

# ==========================================
# Configuración Global
# ==========================================
ARCHIVO_LOG = "network_logs.jsonl"


def obtener_ip_local():
    """
    Obtiene la dirección IP local del equipo actual.

    Autor: Dario Alejandro Sosa Pacheco
    Fecha de creación: 2026-11-05

    Parámetros:
    Ninguno.

    Salida:
    str: Dirección IP local activa del equipo.
    """
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            s.connect(("8.8.8.8", 80))
            return s.getsockname()[0]
    except Exception:
        try:
            return socket.gethostbyname(socket.gethostname())
        except Exception:
            return "127.0.0.1"


def obtener_gateway_red():
    """
    Obtiene la puerta de enlace predeterminada del sistema.

    Autor: Dario Alejandro Sosa Pacheco
    Fecha de creación: 2026-11-05

    Parámetros:
    Ninguno.

    Salida:
    str: Dirección IP del gateway o 'No disponible'.
    """
    sistema = platform.system().lower()

    try:
        if sistema == "darwin":
            salida = subprocess.check_output(
                ["route", "-n", "get", "default"],
                text=True,
                stderr=subprocess.STDOUT,
            )
            coincidencia = re.search(r"gateway:\s+([0-9.]+)", salida)
            if coincidencia:
                return coincidencia.group(1)

        elif sistema == "linux":
            for comando in (["ip", "route", "show", "default"], ["route", "-n"]):
                try:
                    salida = subprocess.check_output(
                        comando, text=True, stderr=subprocess.STDOUT
                    )
                    coincidencia = re.search(
                        r"(?:default|0\.0\.0\.0)\s+([0-9.]+)", salida
                    )
                    if coincidencia:
                        return coincidencia.group(1)
                except Exception:
                    continue

        elif sistema == "windows":
            salida = subprocess.check_output(
                ["ipconfig"], text=True, stderr=subprocess.STDOUT
            )
            coincidencia = re.search(
                r"Predeterminado.*?:\s*([0-9.]+)", salida, re.IGNORECASE
            )
            if coincidencia:
                return coincidencia.group(1)
    except Exception:
        pass

    return "No disponible"


def obtener_mac_red():
    """
    Obtiene la dirección MAC de la interfaz de red principal.

    Autor: Dario Alejandro Sosa Pacheco
    Fecha de creación: 2026-11-05

    Parámetros:
    Ninguno.

    Salida:
    str: Dirección MAC de la red o 'No disponible'.
    """
    sistema = platform.system().lower()

    try:
        if sistema == "darwin":
            salida = subprocess.check_output(
                ["ifconfig", "-a"], text=True, stderr=subprocess.STDOUT
            )
            coincidencia = re.search(r"ether\s+([0-9A-Fa-f:]+)", salida)
            if coincidencia:
                return coincidencia.group(1)

        elif sistema == "linux":
            salida = subprocess.check_output(
                ["ip", "link"], text=True, stderr=subprocess.STDOUT
            )
            coincidencia = re.search(r"link/ether\s+([0-9A-Fa-f:]+)", salida)
            if coincidencia:
                return coincidencia.group(1)

        elif sistema == "windows":
            salida = subprocess.check_output(
                ["ipconfig", "/all"], text=True, stderr=subprocess.STDOUT
            )
            coincidencia = re.search(
                r"Direcci[oó]n\s+f[ií]sica.*?:\s*([0-9A-Fa-f-]+)", salida
            )
            if coincidencia:
                return coincidencia.group(1)
    except Exception:
        pass

    return "No disponible"


def obtener_info_red():
    """
    Reúne la información de red más relevante del equipo.

    Autor: Dario Alejandro Sosa Pacheco
    Fecha de creación: 2026-11-05

    Parámetros:
    Ninguno.

    Salida:
    dict: Diccionario con hostname, IP local, gateway y MAC.
    """
    return {
        "hostname": socket.gethostname(),
        "ip_local": obtener_ip_local(),
        "gateway": obtener_gateway_red(),
        "mac_address": obtener_mac_red(),
        "sistema_operativo": platform.system(),
        "version_sistema": platform.release(),
    }


def mostrar_info_red():
    """
    Muestra en pantalla la información técnica de la red del equipo.

    Autor: Dario Alejandro Sosa Pacheco
    Fecha de creación: 2026-11-05

    Parámetros:
    Ninguno.

    Salida:
    dict: Información válida de red mostrada en consola.
    """
    info = obtener_info_red()
    print("=== INFORMACIÓN DE RED ===")
    for clave, valor in info.items():
        print(f"{clave}: {valor}")
    return info


def generar_ip():
    """
    Genera una dirección IPv4 aleatoria.

    Autor: Dario Alejandro Sosa Pacheco
    Fecha de creación: 2026-11-01

    Parámetros:
    Ninguno.

    Salida:
    str: Dirección IP ficticia en formato "X.X.X.X".
    """
    return f"{random.randint(1, 223)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(1, 254)}"


def crear_evento_red(ip_origen, ip_destino):
    """
    Crea un diccionario que representa un evento de red con datos simulados.

    Autor: Dario Alejandro Sosa Pacheco
    Fecha de creación: 2026-11-01

    Parámetros:
    ip_origen (str): Dirección IP de la máquina que envía los datos.
    ip_destino (str): Dirección IP del servidor o equipo de destino.

    Salida:
    dict: Diccionario con la información detallada del evento registrado.
    """
    puertos_comunes = [80, 443, 22, 53, 8080]
    estados = ["PERMITIDO", "BLOQUEADO", "SOSPECHOSO"]
    protocolos = ["TCP", "UDP"]

    evento = {
        "timestamp": datetime.now().isoformat(),
        "ip_origen": ip_origen,
        "ip_destino": ip_destino,
        "puerto_destino": random.choice(puertos_comunes),
        "protocolo": random.choice(protocolos),
        "bytes_enviados": random.randint(64, 4096),
        "estado": random.choice(estados),
        "latencia_ms": random.randint(1, 500),
        "usuario": random.choice(["admin", "usuario", "invitado"])
    }
    return evento


def guardar_log_jsonl(evento, nombre_archivo=ARCHIVO_LOG):
    """
    Convierte un diccionario de evento en una línea JSON y la añade al archivo.

    Autor: Dario Alejandro Sosa Pacheco
    Fecha de creación: 2026-11-01

    Parámetros:
    evento (dict): Diccionario con el evento que se va a registrar.
    nombre_archivo (str): Nombre del archivo .jsonl donde se guardará.

    Salida:
    bool: True si la escritura fue exitosa, False en caso de error.
    """
    try:
        with open(nombre_archivo, "a", encoding="utf-8") as archivo:
            linea_json = json.dumps(evento, ensure_ascii=False)
            archivo.write(linea_json + "\n")
        return True
    except Exception as e:
        print(f"Error al guardar el log: {e}")
        return False


def simular_trafico(cantidad_eventos):
    """
    Coordina la generación y guardado de múltiples eventos de tráfico de red.

    Autor: Dario Alejandro Sosa Pacheco
    Fecha de creación: 2026-11-01

    Parámetros:
    cantidad_eventos (int): Número de registros que se desean generar.

    Salida:
    None
    """
    print(f"Iniciando simulación de {cantidad_eventos} eventos de red...")

    for _ in range(cantidad_eventos):
        ip_src = generar_ip()
        ip_dst = "192.168.1.1"

        evento = crear_evento_red(ip_src, ip_dst)
        guardar_log_jsonl(evento)

    print(f"¡Simulación completada! Se guardaron los registros en '{ARCHIVO_LOG}'.")


def leer_logs_bloqueados(nombre_archivo=ARCHIVO_LOG):
    """
    Lee un archivo JSONL y muestra los eventos cuya red fue bloqueada.

    Autor: Dario Alejandro Sosa Pacheco
    Fecha de creación: 2026-11-05

    Parámetros:
    nombre_archivo (str): Nombre del archivo .jsonl a revisar.

    Salida:
    list: Lista de eventos bloqueados.
    """
    registros_bloqueados = []

    try:
        with open(nombre_archivo, "r", encoding="utf-8") as archivo:
            for linea in archivo:
                linea = linea.strip()
                if not linea:
                    continue
                evento = json.loads(linea)
                if evento.get("estado") == "BLOQUEADO":
                    registros_bloqueados.append(evento)
    except FileNotFoundError:
        print(f"El archivo '{nombre_archivo}' no existe todavía.")
        return []

    print("=== EVENTOS BLOQUEADOS ===")
    if not registros_bloqueados:
        print("No hay eventos bloqueados.")
    else:
        for evento in registros_bloqueados:
            print(evento)

    return registros_bloqueados


# ==========================================
# Punto de entrada del programa
# ==========================================
if __name__ == "__main__":
    print("Ejecutando funciones de red de forma independiente...\n")
    mostrar_info_red()
    print("\nGenerando algunos eventos de prueba...")
    simular_trafico(5)
    print("\nConsultando eventos bloqueados...")
    leer_logs_bloqueados()

"""
EJERCICIOS SUGERIDOS
------------------------------------------------------------------------------
1. Modificar campos: Agrega un nuevo campo al diccionario dentro de la función
'crear_evento_red' (por ejemplo, "latencia_ms" o "usuario").

2. Leer y Filtrar Logs: Crea una función nueva llamada 'leer_logs_bloqueados()'
que abra el archivo .jsonl, lo lea línea por línea y muestre en pantalla
únicamente los registros donde el campo "estado" sea igual a "BLOQUEADO".
"""
