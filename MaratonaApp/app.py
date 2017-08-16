from model.Cliente import Cliente
from model.Funcionario import Funcionario
from model.Maratona import Maratona

def main():
  funcionario = Funcionario("Maria")
  cliente = Cliente("José")

  maratona = Maratona()

  maratona.correr(cliente)
  maratona.correr(funcionario)

if __name__ == "__main__":
  main()
