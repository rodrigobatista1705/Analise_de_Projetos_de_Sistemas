# Atividade 18 – Diagrama de Classes do BiblioTech

Nome: Rodrigo Lima dos Santos Batista
Turma: 2° ano – Técnico em Informática Integrado

## Diagrama

![Diagrama de Classes do BiblioTech](diagrama-classes.png)

## Por que estes números (associação Bibliotecário – Empréstimo)

- Perto de Empréstimo eu coloquei 0..* porque o bibliotecário
pode realizar mais de um empréstimo.
- Perto de Bibliotecário eu coloquei 1 porque o empréstimo só
pode ser realizado por um unico bibliotecário.

## Rastreabilidade (nível B)

- A operação confirmarReserva() da classe Reserva atende ao
caso de uso 1.4