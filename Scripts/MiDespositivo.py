""" 
if "__main__" = __main__ :
  funciones
"""

import json
import os
import platform
import socket
import subprocess
import uuid
import output
from datetime import datetime
try:
   import psutil
except ImportError:
   psutil = None
def guardar_info_dispositivo(jsonl_file="device_data.jsonl"):
   """
   Obtiene información del dispositivo mediante librerías Python
   y la agrega a un archivo JSONL.
   """
   #OutPut
   print("Guardando informacion del dispositivo...")
   print(output.salida)

   data = {
        "timestamp": datetime.utcnow().isoformat(),
        "hostname": socket.gethostname(),
        "fqdn": socket.getfqdn(),
        "ip": socket.gethostbyname(socket.gethostname()),
        "mac": ":".join(
            f"{(uuid.getnode() >> ele) & 0xff:02x}"
            for ele in range(40, -1, -8)
        ),
        "system": platform.system(),
        "release": platform.release(),
        "version": platform.version(),
        "machine": platform.machine(),
        "processor": platform.processor(),
        "python_version": platform.python_version(),
   }
   if psutil:
        data.update({
            "cpu_count_logical": psutil.cpu_count(),
            "cpu_count_physical": psutil.cpu_count(logical=False),
            "memory_total": psutil.virtual_memory().total,
            "memory_available": psutil.virtual_memory().available,
            "disk_partitions": [
                {
                    "device": p.device,
                    "mountpoint": p.mountpoint,
                    "fstype": p.fstype
                }
                for p in psutil.disk_partitions()
            ],
            "network_interfaces": {
                k: [str(addr.address) for addr in v]
                for k, v in psutil.net_if_addrs().items()
            }
        })
   with open(jsonl_file, "a", encoding="utf-8") as f:
        f.write(json.dumps(data, ensure_ascii=False) + "\n")
def guardar_comando_red(jsonl_file="device_data.jsonl"):
   """
   Ejecuta ipconfig o ifconfig dependiendo del sistema operativo
   y guarda la salida en JSONL.
   """
   sistema = platform.system()
   try:
        if sistema == "Windows":
            resultado = subprocess.run(
                ["ipconfig", "/all"],
                capture_output=True,
                text=True,
                encoding="utf-8",
                errors="ignore"
            )
            salida = resultado.stdout
            comando = "ipconfig /all"
        else:
            resultado = subprocess.run(
                ["ifconfig"],
                capture_output=True,
                text=True
            )
            salida = resultado.stdout
            comando = "ifconfig"
        data = {
            "timestamp": datetime.utcnow().isoformat(),
            "command": comando,
            "output": salida
        }
        with open(jsonl_file, "a", encoding="utf-8") as f:
            f.write(json.dumps(data, ensure_ascii=False) + "\n")
   except Exception as e:
        with open(jsonl_file, "a", encoding="utf-8") as f:
            f.write(json.dumps({
                "timestamp": datetime.utcnow().isoformat(),
                "error": str(e)
            }) + "\n")