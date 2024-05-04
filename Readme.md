## Desafio

<p>Fomos contratados por um grande banco para desenvolver o seu novo sistema. Esse banco deseja modernizar suas operações e para isso escolheu a linguagem Python. Para a primeira versão do sistema devemos implementar apenas 3 operações: depósito, saque e extrato.</p>

### Operação de depósito

<p>Deve ser possível depositar valores positivos para a minha conta bancária. A v1 do projeto trabalha apenas com 1 usuário, dessa forma não precisamos nos preocupar em identificar qual é o número da agência e conta bancária. Todos os depósitos devem ser armazenados em uma variável e exibidos na operação de extrato.</p>

#### Operação de Saque

<p>O sistema deve permitir realizar 3 saques diários com limite máximo de R$ 500,00 por saque. Caso o usuário não tenha saldo em conta, o sistema deve exibir uma mensagem informando que não será possível sacar o dinheiro por falta de saldo. Todos os saques devem ser armazenados em uma variável e exibidos na operação de extrato.</p>

#### Operação de extrato

<p>Essa operação develistar todos os depósitos e saques realizados na conta. No fim da listagem deve ser exibido o saldo atual da conta.</p>
<p>Os valores devem ser exibidos utulizando o formado R$ XXX,XX, exemplo:

1500.45 = R$ 1500.45</p>

### Etapas do segundo desafio

Precisamos deixar nosso cógido mais modularizado, para isso vamos criar funções para as operações existentes: sacar, depositar e visializar histórico. Além disso, para a versão 2 do nosso sistema precisamos criar duas novas funções: criar usuário (cliente do banco) e criar conta corrente (vincular com usuário).

#### **Regras**

* Separação em funções</br>
  Devemos criar funções para todas as operações do sistema. Para exercitar tudo o que aprendemos neste módulo, cada função vai ter uma regra na passagem de argumentos. O retorno e a forma como serão chamadas, pode ser definida por você da forma que achar melhor.

* Saque</br>
  Deve receber os argumentos apenas por nome (keyword only). Sugestão de argumentos: Saldo, valor, extrato, limite, numero_saques, limite_saques. Sugestão de retorno: Saldo e extrado.

* Depósito</br>
  deve receber os argumentos apenas por posição (positional only). Sugestão de argumentos: saldo, valor, extrato. Sugestão de retorno: saldo e extrato.

* Extrato</br>
  Deve receber os argumentos por posição e nome (positional only e keyword only). Argumentos posicionais: saldo, argumentos nomeados: extrato.

* Novas funções</br>
  Criar usuário e criar conta corrente. Fique a vontade para adicionar mais funções, exemplo: listar contas.

* Criar usuário (cliente)</br>
  o programa deve armazenar os usuários em uma lista, um usuário é composto por: nome, data de nascimento, cpf e endereço. O endereço é uma string com o formato: logradouro, número - bairro - caidade/sigla estado. Deve ser armazenado somente os números do cpf. não podemos cadastrar 2 usuários com o mesmo cpf.

* Criar conta corrente</br>
  O programa deve armazenar contas em uma lista, uma conta é composta por: agência, número da conta e usuário. O número da conta é sequencial, iniciando em 1. O número da agência é fixo: "0001". O usuário pode ter mais de uma conta mais uma conta pertence a somente um usuário.

**DICA**: para vincular um usuário a uma conta, filtre a lista de usuários buscando o número do cpf informado para cada usuário da lista.