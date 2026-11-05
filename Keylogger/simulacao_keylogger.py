
"""
SIMULACAO EDUCACIONAL DE KEYLOGGER
Projeto: Laboratorio de CyberSecurity

Demonstra registro de entradas ficticias.
Nao monitora o teclado real.
"""

from pathlib import Path

eventos_simulados = [
    "Usuario demonstrativo iniciou a sessao.",
    "Entrada ficticia: teste de seguranca.",
    "Entrada ficticia: laboratorio de Python.",
    "Usuario demonstrativo encerrou a simulacao."
]


def executar_simulacao():
    pasta = Path(__file__).parent
    arquivo = pasta / "registro_simulado.txt"

    print("=" * 45)
    print(" SIMULACAO EDUCACIONAL DE KEYLOGGER")
    print("=" * 45)

    with arquivo.open("w", encoding="utf-8") as registro:
        registro.write("REGISTRO FICTICIO - FINS EDUCACIONAIS\n")
        registro.write("=" * 45 + "\n\n")

        for evento in eventos_simulados:
            print(evento)
            registro.write(evento + "\n")

    print("\nSimulacao concluida.")
    print(f"Relatorio gerado em: {arquivo.name}")
    print("Nenhuma tecla real foi monitorada.")


if __name__ == "__main__":
    executar_simulacao()
