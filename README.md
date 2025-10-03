# INF1407 Trabalho da G1

## Membros do grupo
- Felipe de Aragão Falcão 2120360
- Ricardo Bastos Leta Vieira, 2110526

## Link para a imagem docker
https://github.com/ricleta/INF1407-Trabalho1/pkgs/container/inf1407-trabalho1

- Puxar imagem
```
docker pull ghcr.io/ricleta/inf1407-trabalho1:1.0
```
- Rodar imagem
```
docker run -p 8000:8000 --name inf1407-trabalho1 ghcr.io/ricleta/inf1407-trabalho1:1.0
```

## Escopo do site
O site "Avaliações de Jogos" foi desenvolvido em Python com o framework Django. O objetivo principal é criar uma plataforma onde **Desenvolvedores de Jogos** (GameDevs) e **Avaliações** (Reviewers) possam interagir. A aplicação implementa um sistema de login e perfis de usuário com permissões baseadas em grupos, garantindo que cada tipo de usuário tenha acesso a funcionalidades específicas. A interface foi construída com HTML e CSS, sem a utilização de JavaScript.

O site oferece as seguintes funcionalidades principais:
- **CRUD de Jogos:** Apenas usuários do grupo **GameDevs** podem adicionar, visualizar, editar e excluir seus próprios jogos.
- **CRUD de Avaliações:** Apenas usuários do grupo **Reviewers** podem adicionar, visualizar, editar e excluir suas próprias avaliações.
- **Controle de Acesso:** A visibilidade de páginas e funcionalidades é restrita de acordo com o grupo do usuário logado.

## Manual do Usuário
### Visões do Usuário

- **Usuário Anônimo:** Acesso apenas à página inicial, cadastro (`signup`) e login.
- **Usuário GameDev:** Acesso à página inicial, à lista completa de jogos, à sua própria lista de jogos e às funcionalidades de CRUD para jogos. Não pode criar, visualizar, editar ou excluir avaliações.
- **Usuário Reviewer:** Acesso à página inicial, à lista completa de jogos, à sua própria lista de avaliações e às funcionalidades de CRUD para avaliações. Não pode gerenciar jogos.
- **Administrador:** Acesso a todas as funcionalidades do painel administrativo do Django (`/admin`).

### Manual de Uso

#### Login e Cadastro
- Acesse a página inicial e clique em `Login` ou `Cadastrar-se` para gerenciar sua conta.
- No cadastro, você deve selecionar o tipo de conta que deseja criar (**GameDev** ou **Reviewers**).

#### CRUD Avaliações (apenas para usuários Reviewers)
1. **Create (Criar Avaliação):**
   - Na página inicial, clique em `Minhas Avaliações`.
   - Clique no botão `Criar nova avaliação`.
   - Preencha o formulário, selecionando um jogo, atribuindo uma nota de 1 a 10 e escrevendo um comentário.
   - O formulário valida se você já avaliou o jogo.
   - Clique em `Criar Avaliação` para salvar.
2. **Read (Visualizar Avaliações):**
   - Acesse a página `Minhas Avaliações` para ver todas as avaliações que você criou.
   - A página `Lista de Jogos` exibe todos os jogos disponíveis, incluindo a sua própria avaliação e também de outros usuários.
3. **Update (Atualizar Avaliação):**
   - Na página `Minhas Avaliações`, clique em `Atualizar` ao lado da avaliação que deseja modificar.
   - Altere a nota ou o comentário. O jogo associado à avaliação não pode ser alterado.
   - Clique em `Atualizar` para salvar as alterações.
4. **Delete (Excluir Avaliação):**
   - Na página `Minhas Avaliações`, clique em `Excluir` ao lado da avaliação que deseja remover.
   - Confirme a exclusão na próxima página.

#### CRUD Jogos (apenas para usuários GameDev)
1. **Create (Criar Jogo):**
   - Na página inicial, clique em `Meus Jogos`.
   - Clique no botão `Criar novo jogo`.
   - Preencha o formulário com o título, plataformas, descrição e data de lançamento.
   - Clique em `Criar Jogo` para salvar.
2. **Read (Visualizar Jogos):**
   - A página `Meus Jogos` mostra todos os jogos que você publicou.
   - A página `Lista de Jogos` exibe todos os jogos disponíveis no sistema, publicados por qualquer desenvolvedor.
3. **Update (Atualizar Jogo):**
   - Na página `Meus Jogos`, clique em `Atualizar` ao lado do jogo que deseja modificar.
   - Altere as informações necessárias no formulário.
   - Clique em `Atualizar Jogo` para salvar as alterações.
4. **Delete (Excluir Jogo):**
   - Na página `Meus Jogos`, clique em `Excluir` ao lado do jogo que deseja remover.
   - Confirme a exclusão na próxima página.

### O que funcionou
- **Login e Logout:** O sistema de autenticação, incluindo a criação de usuários com perfis distintos.
- **Controle de Acesso:** As permissões baseadas em grupos (`GameDev` e `Reviewers`) estão funcionando corretamente, redirecionando usuários não autorizados.
- **CRUD de Jogos:** A criação, leitura, atualização e exclusão de jogos estão funcionando conforme o esperado.
- **CRUD de Avaliações:** A criação, leitura, atualização e exclusão de avaliações estão funcionando corretamente, com a restrição de que cada usuário só pode gerenciar suas próprias avaliações.
- **Validação de Formulários:** As validações de campos (`required`, `max_length`, `min_length`, etc.) estão funcionando para garantir a integridade dos dados.
- **Conexão com Banco de Dados:** A persistência dos dados no banco de dados SQLite está funcionando.

### O que *não* funcionou 
- **Atualização de Avaliação:** Quando uma avaliação está sendo atualizada, o campo `game` no formulário `ReviewForm` deveria ter o dropdown menu desabilitado, permitindo apenas a visualização do jogo original da avaliação. Atualmente, o campo está habilitado, embora só permita a seleção do jogo já avaliado.
- **Atualização de Games:** Quando um game está sendo atualizado, o campo `platforms` no formulário `GamesForm` deveria já mostrar qual/is a/as opção/ções de plataformas que já tinham sido previamente selecionadas. Atualmente, o campo é resetado ao entrar na página como se não tivesse nenhuma plataforma selecionada anteriormente.
