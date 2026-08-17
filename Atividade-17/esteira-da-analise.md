# Esteira da Análise — BiblioTech

**Estudante:** Rodrigo Lima dos Santos Batista

## Funcionalidade 1: reservar livro

- **1. Fala do cliente:** "Quando o aluno escolhe o livro, que está em uso, ele fica reservado para quando for devovildo ele poder usar"
- **2. História de usuário:** Como leitor, quero reservar um livro, para quando disponivel er utilizado.
- **3. Requisito:** RF01 — O sistema deve reservar um livro em uso para o proximo leitor
- **4. Caso de uso (RF01):** Ator leitor → "Reservar livro" (verbo + objeto)

## Funcionalidade 2: buscar livro no acervo

- **1. Fala do cliente:** "O aluno deve coneguir buscar um livro que deseja, para efetuar a reserva"
- **2. História de usuário:** Como leitor, quero ter acesso ao catalogo de livros, para para reservar um deles.
- **3. Requisito:** RF02 — O sistema deve permitir que o catálogo de livros seja visto 
- **4. Caso de uso (RF02):** Ator leitor → "consultar catalogo" (verbo + objeto)

## Rastreabilidade

| Elipse no diagrama | Veio do requisito | Que veio da fala |
|---|---|---|
| | RF01 | "Quando o aluno escolhe o livro, que esta em uso, ele fica reservado para quando for devolvido ele poder usar" |
| | RF02 | "O aluno deve conseguir buscar um livro que deseja, para efetuar a reserva" |

<!-- Nível A: conte o caminho completo de cada funcionalidade,
     da fala do cliente até o que está desenhado no diagrama. -->

## Relacionamento entre casos de uso (nível A)

- Tipo: «extend» 
- Entre: Reservar livro e consultar catalogo
- Por que é esse e não o outro: Porque para reservar um livro nao eh necessario a execucao do consultar catalogo, para entao a reserva ser realizada. Ou seja uma reserva pode ser feita feita sem consulta para o fluxo funcionar

## Autoavaliação

**Conceito pretendido:** B (A / B / C)

- Conversei sobre esta atividade com: ninguém
- Esteira da análise: B
- Diagrama e notação: B
- Rastreabilidade: B
- Organização da entrega: B