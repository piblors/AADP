from detector import analisar_texto

def main():
    limpar_terminal()
    print("BEM VINDO(A) AO AADP")
    print("-" * 10)
    print("Caso queira utilizar o doc de texto como entrada de dados, clique ENTER. Se não, copie e cole o texto a ser analisado aqui:")
    try:
        texto = input(">>> ").lower()
        if texto == "" or texto.isspace():
            with open("data/texto_para_busca.txt", "r", encoding="utf-8") as arquivo:
                texto = arquivo.read().lower()
    except FileNotFoundError:
        print("Arquivo Não Encontrado")

    resultado = analisar_texto(texto)
    print("\n")
    print('-'*10)
    print("\n")
    print("Resultado da análise:")
    print("Texto analisado:\n", texto)
    print('='*10)
    print(resultado)
    mostrar_resultado(resultado)

def limpar_terminal():
    import os
    os.system("cls" if os.name == "nt" else "clear")


def mostrar_resultado(resultado: dict) -> None:
    if resultado.get("dados_pessoais"):
        print("ATENÇÃO: foram detectados dados pessoais no texto.")
        tipos = resultado.get("tipos_detectados", [])
        if tipos:
            print("Tipos de dados pessoais identificados:")
            for tipo in tipos:
                print(f" - {tipo}")
        else:
            print("Nenhum tipo específico foi identificado.")
    else:
        print("Nenhum dado pessoal foi identificado no texto.")


if __name__ == "__main__":
    main()