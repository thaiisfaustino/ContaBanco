# O banco Banco Delas é um banco moderno e eficiente, com vantagens exclusivas para clientes mulheres. 
# Modele um sistema orientado a objetos para representar contas correntes em do Banco Delas seguindo os requisitos abaixo. 
# 1. Cada conta corrente pode ter um ou mais clientes como titular. 
# 2. O banco controla apenas o nome, o telefone e a renda mensal de cada cliente. 
# 3. A conta corrente apresenta um saldo e uma lista de operações de saques e depósitos. 
# Quando a cliente fizer um saque, diminuiremos o saldo da conta corrente. Quando ela fizer um depósito, aumentaremos o saldo. 
# 4. Clientes mulheres possuem em suas contas um cheque especial de valor igual à sua renda mensal, ou seja, elas podem sacar valores que deixam a sua conta com valor negativo até renda_mensal. 
# 5. Clientes homens por enquanto não têm direito a cheque especial. 
# Para modelar seu sistema, utilize obrigatoriamente os conceitos "classe", "herança" e "polimorfismo". 
# Opcionalmente, você pode também utilizar "propriedades", "encapsulamento" e "classe abstrata". 

class ContaBancoDelas:
  def __init__(self, nome, telefone, renda, sexo, conta): 
    self.nome = str 
    self.telefone = int 
    self.renda = 0 
    self.sexo = str 
    self.conta = int
    self.saldo_total = 0 
    self.conta_mulher = 'F'
    self.limite = self.renda 
    self.saldo = 0 

  def deposito(self): 
    self.saldo = deposito 
    self.saldo_total += self.saldo 
    return f'Deposito efetuado com sucesso! Saldo atual de R${self.saldo_total}' 

  def saque(self):
    if ((self.sexo == 'F') and (self.saldo >= saque or saque <= self.limite)): 
      self.saldo = saque 
      saldo_total += self.saldo 
      return f'Saque realizado com sucesso! Saldo atual de R${self.saldo_total}' 

    elif (self.sexo != 'F' and self.saldo >= saque):
      self.saldo = saque 
      self.saldo_total += self.saldo 
      return f'Saque realizado com sucesso! Saldo atual de R${self.saldo_total}' 

    else: 
      return 'Saldo insuficiente. Saldo atual de R${self.saldo_total}' 

  def __str__(self): 
    return f'Nome: {self.nome}, Telefone: {self.telefone}, Renda R${self.renda}, Sexo: {self.sexo}, Conta: {self.conta}' 

class ContaEspecial (ContaBancoDelas): 
  def __init__(self, nome, telefone, renda): 
    super().__init__(nomr, telefone, renda, 'F') 
    self.nome = nome 

class ContaComum(ContaBancoDelas): 
  def __init__(self, nome, telefone, renda: float, sexo: str, conta: int): 
    self.nome = str 
    self.telefone = int 
    self.renda = float 
    self.sexo = str 
    self.conta = int 
    self.saldo_total = 0 
    self.conta_mulher = 'Mulher' 
    self.limite = self.renda 
    self.saldo = 0 

  def deposito(self): 
    self.saldo = deposito 
    saldo_total += self.saldo 
    return f'Deposito efetuado com sucesso! Saldo atual de R${self.saldo_total}' 

  def saque(self, saque): 
    if ((self.sexo == 'F') and (self.saldo >= saque or saque <= self.limite)): 
      self.saldo = saque 
      saldo_total += self.saldo 
      return f'Saque realizado com sucesso! Saldo atual de R${self.saldo_total}' 

    elif (self.sexo == 'M' and self.saldo >= saque): 
      self.saldo = saque 
      self.saldo_total += self.saldo 
      return f'Saque realizado com sucesso! Saldo atual de R${self.saldo_total}' 

    else: 
      return 'Saldo insuficiente. Saldo atual de R${self.saldo_total}' 

  def __str__(self): 
    return f'Nome: {self.nome}, Telefone: {self.telefone}, Renda R${self.renda}, Sexo: {self.sexo}, Conta: {self.conta}' 

class ContaEspecial: 
  def __init__(self, nome, telefone, renda, sexo, conta): 
    self.nome = str 
    self.telefone = int 
    self.renda = float 
    self.sexo = str 
    self.conta = int 
    self.saldo_total = 0 
    self.conta_mulher = 'F' 
    self.limite = self.renda 
    self.saldo = 0 

  def deposito(self): 
    self.saldo = deposito 
    saldo_total += self.saldo 
    return f'Deposito efetuado com sucesso! Saldo atual de R${self.saldo_total}' 

  def saque(self, saque): 
    if ((self.sexo == 'F') and (self.saldo >= saque or saque <= self.limite)): 
      self.saldo = saque 
      saldo_total += self.saldo 
      return f'Saque realizado com sucesso! Saldo atual de R${self.saldo_total}' 

    elif (self.sexo != 'F' and self.saldo >= saque): 
      self.saldo = saque 
      self.saldo_total += self.saldo 
      return f'Saque realizado com sucesso! Saldo atual de R${self.saldo_total}' 

    else: 
      return 'Saldo insuficiente. Saldo atual de R${self.saldo_total}' 

  def __str__(self): 
    return f'Nome: {self.nome}, Telefone: {self.telefone}, Renda R${self.renda}, Sexo: {self.sexo}, Conta: {self.conta}' 

class ContaEspecial(ContaBancoDelas): 
  def __init__(self, nome, telefone, renda): 
    super().__init__(nome, telefone, renda, F) 
    self.nome = nome 

class ContaBasica(ContaBancoDelas): 
  def __init__(self, nome, telefone, renda): 
    super().__init__(nome, telefone, renda, M) 
    self.nome = nome 