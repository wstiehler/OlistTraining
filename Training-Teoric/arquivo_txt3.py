from datetime import datetime

data_hora = datetime.now()

arquivo = open('arquivo_log.txt', 'a')
arquivo.write(f'{data_hora}\n')
arquivo.close()



#Escrevendo log sempre no mesmo arquivo