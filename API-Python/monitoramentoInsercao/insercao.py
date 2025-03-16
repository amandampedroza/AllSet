import psutil  
from classes.BancoDeDados import BancoDeDados
from classes.Computador import Computador
from mysql.connector import connection, errorcode, Error
import time

CPU = False
RAM = False
disco = False
bateria = False
velocidadeDaRede = False

def programaInsercao(infinito):

    bd = BancoDeDados()
    BancoDeDados.setUsuario('Select')
    mydb = BancoDeDados.getConexao()

    informacaoCarro = Computador.getEnderecoMAC()    
    
    colunas = 'idConfiguracao, fkComponente, valorLimiteAlerta'
    FROM = 'configuracao JOIN carro ON fkCarro = idCarro WHERE enderecoMac = ' + informacaoCarro

    valores = (
        colunas,
        FROM,
            )

    resultados = BancoDeDados.select(valores)
    BancoDeDados.fecharConexao()
    
    qtdResultados = len(resultados)

    if(qtdResultados == 0):
        print("Nenhum resultado encontrado na nossa base de dados, encerrando opereação")
        return 

    idConfig = resultados[0][0]
    componentes = []
    limiarAlerta = []

    for linha in resultados:
        componentes.append(linha[1])
        limiarAlerta.append(linha[2])

    qtdComponentes = len(componentes)
    cont = 0

    while qtdComponentes > cont:
        componenteAtual = componentes[cont] 

        if componenteAtual == 1:
            # CPU
            CPU = True
            contCPU = cont
            
        elif componenteAtual == 2:
            # RAM
            RAM = True
            contRAM = cont
            # Processos que tá gostando mais RAM (Quando a RAM estiver alta)

        elif componenteAtual == 3: 
            # Disco
            disco = True
            contDisco = cont

        elif componenteAtual == 4:    
            # Bateria
            bateria = True
            contBateria = cont

        elif componenteAtual == 5:
            # Velocidade da rede
            velocidadeDaRede = True
            contRede = cont    

    BancoDeDados.setUsuario('Insert')
    mydb = BancoDeDados.getConexao()

    while True:

        if CPU:
            CPUAtual = Computador.getCPU()

            if CPUAtual >= limiarAlerta[contCPU]:
                
                sql = '(' + idConfig + ',' + CPUAtual + ');'
                BancoDeDados.insert(sql, mydb)
                
        if RAM:
            RAMAtual = Computador.getRAM()

            if RAMAtual >= limiarAlerta[contRAM]:
                
                sql = '(' + idConfig + ',' + RAMAtual + ');'
                BancoDeDados.insert(sql, mydb)
            
        if disco:
            discoAtual = Computador.getDisco()
            
            if discoAtual >= limiarAlerta[contDisco]:
                
                sql = '(' + idConfig + ',' + discoAtual + ');'
                BancoDeDados.insert(sql, mydb)

        if bateria:
            bateriaAtual = Computador.getBateria()

            if bateriaAtual >= limiarAlerta[contBateria]:
                
                sql = '(' + idConfig + ',' + bateriaAtual + ');'
                BancoDeDados.insert(sql, mydb)

        if velocidadeDaRede:
             
            velocidadeDaRedeAtual = Computador.getRede()   

            if velocidadeDaRedeAtual >= limiarAlerta[contCPU]:
                
                sql = '(' + idConfig + ',' + velocidadeDaRedeAtual + ');'
                BancoDeDados.insert(sql, mydb)

        time.sleep(5)

# Adicionar uma mensagem assim que começa o programa informando que está verificando a existência desse veículo no Banco de dados