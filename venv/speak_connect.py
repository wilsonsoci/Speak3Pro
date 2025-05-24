import sqlite3
from datetime import datetime

def exportar_usuarios_para_txt():
    """
    Exporta dados da tabela usuarios para um arquivo TXT formatado
    """
    # Configurações
    banco_dados = 'speakthreepro.db'  # Nome do arquivo SQLite
    arquivo_saida = 'usuarios_exportados.txt'
    
    try:
        # 1. Conectar ao banco de dados
        conn = sqlite3.connect(banco_dados)
        cursor = conn.cursor()
        
        # 2. Obter informações da tabela
        cursor.execute("PRAGMA table_info(usuarios)")
        colunas_info = cursor.fetchall()
        colunas = [coluna[1] for coluna in colunas_info]
        
        # 3. Consulta ordenada por nome
        cursor.execute("""
        SELECT id, nome, cpf, data_nascimento, nacionalidade, email 
        FROM usuarios 
        ORDER BY nome COLLATE NOCASE ASC
        """)
        
        usuarios = cursor.fetchall()
        
        # 4. Preparar dados para exportação
        linhas = []
        
        # Cabeçalho
        cabecalho = f"{'ID':<5} | {'Nome':<25} | {'CPF':<15} | {'Nascimento':<12} | {'Nacionalidade':<15} | {'Email'}"
        separador = "-" * len(cabecalho)
        linhas.append(cabecalho)
        linhas.append(separador)
        
        # Dados formatados
        for usuario in usuarios:
            # Formatar data (se existir)
            data_nasc = usuario[3]
            if data_nasc:
                try:
                    data_formatada = datetime.strptime(data_nasc, '%Y-%m-%d').strftime('%d/%m/%Y')
                except:
                    data_formatada = data_nasc
            else:
                data_formatada = 'N/A'
            
            linha = f"{usuario[0]:<5} | {usuario[1]:<25} | {usuario[2]:<15} | {data_formatada:<12} | {usuario[4]:<15} | {usuario[5]}"
            linhas.append(linha)
        
        # 5. Escrever no arquivo
        with open(arquivo_saida, 'w', encoding='utf-8') as f:
            f.write("\n".join(linhas))
        
        print(f"Dados exportados com sucesso para '{arquivo_saida}'")
        print(f"Total de registros exportados: {len(usuarios)}")
        
        return True
    
    except sqlite3.Error as e:
        print(f"Erro no SQLite: {e}")
        return False
    except Exception as e:
        print(f"Erro inesperado: {e}")
        return False
    finally:
        if 'conn' in locals():
            conn.close()

# Executar a exportação
if __name__ == "__main__":
    exportar_usuarios_para_txt()