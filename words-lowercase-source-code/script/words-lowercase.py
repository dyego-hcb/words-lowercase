def converter_para_minusculo(nome_arquivo_entrada, nome_arquivo_saida):
    try:
        with open(nome_arquivo_entrada, 'r') as arquivo_entrada:
            conteudo = arquivo_entrada.read()

        conteudo_minusculo = conteudo.lower()

        with open(nome_arquivo_saida, 'w') as arquivo_saida:
            arquivo_saida.write(conteudo_minusculo)

        print("Conversão concluída com sucesso.")

    except FileNotFoundError:
        print(f"Arquivo {nome_arquivo_entrada} não encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")


nome_arquivo_entrada = './input/in.txt'
nome_arquivo_saida = './output/out.txt'
converter_para_minusculo(nome_arquivo_entrada, nome_arquivo_saida)