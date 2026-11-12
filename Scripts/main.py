import MiDespositivo
import generador_logs

if __name__ == "__main__"    :
    
    print("Ejecutando main:")

    MiDespositivo.guardar_info_dispositivo("device_data.jsonl")
    MiDespositivo.guardar_comando_red("device_data.jsonl")

    print("Proceso main terminado.")

    # print("Ejecutando main:")

    # generador_logs.obtener_info_red()

    # print("Proceso main terminado:")