

class Mensagem:
    def __init__(self,destinatario,mensagem,assunto):
        self.destinatario=destinatario
        self.assunto=assunto
        self.mensagem=mensagem
        self.tipo="Mensagem"

    def enviar_mensagem(self):
        if self.tipo=="Email":
            return f"{self.tipo}({self.destinatario}). Assunto: {self.assunto}"
        else:
            return f"{self.tipo}({self.destinatario}).{self.assunto} {self.mensagem}"
    
class Email(Mensagem):
    def __init__(self, destinatario, corpo, assunto):
        super().__init__(destinatario,corpo, assunto)
        self.corpo=corpo
        self.tipo="Email"

    def enviar_mensagem(self):
        return super().enviar_mensagem()
    
class SMS(Mensagem):
    def __init__(self, numero, mensagem):
        super().__init__(numero, mensagem, assunto="")
        self.numero = numero
        self.tipo = "SMS"

    def enviar_mensagem(self):
        return super().enviar_mensagem()
    
class NotificacaoPush(Mensagem):
    def __init__(self, dispositivo_id, mensagem):
        super().__init__(dispositivo_id, mensagem, assunto="")
        self.dispositivo_id = dispositivo_id
        self.tipo = "Notificacao Push"

    def enviar_mensagem(self):
        return super().enviar_mensagem()

    
def realizar_envio(mensagem):
    print(mensagem.enviar_mensagem())

email = Email(destinatario="joao.silva@email.com", assunto="Reunião",corpo="Reuni~ao marcada para as 10h.")
sms = SMS(numero="912345678", mensagem="A sua Encomenda Chegou!")
notificacao = NotificacaoPush(dispositivo_id="abc123", mensagem="Tem uma Nova Mensagem.")

realizar_envio(email)
realizar_envio(sms)
realizar_envio(notificacao)