# Troubleshooting


Para conexão com JDBC, devem ser definidos os parametros abaixo:

- allowPublicKeyRetrieval=true

- useSSL=false

[Erro "public key retrieval is not allowed" ao testar conexão no dbeaver:](https://cursos.alura.com.br/forum/topico-erro-public-key-retrieval-is-not-allowed-ao-fazer-test-connection-no-dbeaver-como-resolver-137427)

    Para usuários do DBeaver:

    Clique com o botão direito na sua conexão, escolha "Editar Conexão"

    Na tela "Configurações de conexão" (tela principal), clique em "Editar configurações do driver"

    Clique em "Propriedades da conexão"

    Clique com o botão direito na área "propriedades do usuário" e escolha "Adicionar nova propriedade"

    Adicione duas propriedades: "useSSL" e "allowPublicKeyRetrieval"

    Defina seus valores como "false" e "true" clicando duas vezes na coluna "value"

