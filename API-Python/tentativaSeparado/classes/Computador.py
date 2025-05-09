import psutil  

class Computador:
    
    @staticmethod
    def converter_bytes(bytes):
        if(bytes <= 0):
            return 0
        conversao = round(float((bytes)/ (1024 ** 3)), 2)
        return conversao

    @staticmethod
    def getEnderecoMAC():
        informacaoNet = psutil.net_if_addrs()
        # Informações relacionadas a dados da Net, por exemplo IPV4, o que queremos nesse caso é o endereço MAC

        for interface, enderecos in informacaoNet.items():
        # Está buscando os endereços
            for endereco in enderecos:
                if endereco.family == psutil.AF_LINK:  # AF_LINK representa o MAC Address
                    # Aqui é o que tem que mudar pra pegar o MAC, pra pegar o IPV4 por exemplo seria: psutil.AF_INET ou colocando o 6 no final para pegar o IPV6
                
                    if ":" in endereco.address:
                        macArrumado = endereco.address.replace(":", "")
                    elif "-" in endereco.address:
                        macArrumado = endereco.address.replace("-", "")

                    return macArrumado
    
        return 'NadaEncontrado'
    
    @staticmethod
    def getCPU():
        porcentagemCPU = psutil.cpu_percent(interval=1)

        return porcentagemCPU
    
    @staticmethod
    def getBateria():
        porcentagemBateria = psutil.sensors_battery().percent
        return porcentagemBateria

    @staticmethod
    def getRAM():
        memoriaVirtual = psutil.virtual_memory()
        RAMusado = Computador.converter_bytes(memoriaVirtual.used)
        
        return RAMusado

    @staticmethod
    def getDisco():
        discoTotal = psutil.disk_usage('C:\\')
        # Não funciona no Linux, pois no Linux é necessário ser o '/' no lugar, pois o armazenamento dele está lá, mas a nível de simulação, por todos notebooks serem windows, optamos por manter o padrão de Windows

        armUsado = Computador.converter_bytes(discoTotal.free)

        return armUsado
    
    @staticmethod
    def getRede():
         
        pass 

    # Pegar o IPV4 tbm
    # Pegar os processos