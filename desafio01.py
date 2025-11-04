from classes.Cliente import Cliente
from classes.Conta import Conta

# Testando o código

cliente1 = Cliente("123", "João", "Rua X")
cliente2 = Cliente("224", "Maria", "Rua Y")
cliente3 = Cliente("345", "Joaquim", "Rua W")
cliente4 = Cliente("678", "Ana", "Rua Z")

conta1 = Conta([cliente1, cliente2], 111, 0)
conta2 = Conta([cliente3, cliente4], 222, 100)

conta2.gerar_saldo()
# conta2.gerar_dados()