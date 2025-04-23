import base64

# Lê o arquivo original (ex: DOCX)
with open("roteiro_extensao.docx", 'rb') as file:
    binario = file.read()

# Codifica para base64
base64_str = base64.b64encode(binario).decode("utf-8")

# Salva a string base64 em texto
with open("arq_base64.txt", "w") as f:
    f.write(base64_str)

# Lê a string base64 do arquivo
with open("arq_base64.txt", "r") as f:
    base64_lida = f.read()

# Decodifica de volta para binário
conteudo_original = base64.b64decode(base64_lida)

# Salva com a extensão original (docx, neste caso!)
with open("recuperado.docx", "wb") as f:
    f.write(conteudo_original)
