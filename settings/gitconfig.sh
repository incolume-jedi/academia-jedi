#!/bin/sh

USER=`git config user.name`|| 'Desenvolvimento Incolume'
EMAIL=`git config user.email` || 'dev@incolume.com.br'

echo -n 'Iniciando configuração git .. '

# Usuário e email para serem exibidos nos commites:
git config --global user.name $USER
git config --global user.email $EMAIL

# Cache local para credenciais de autenticação (Usuário/Senha)
git config --global credential.helper cache

# Desabilitar verificação de Certificado digital
git config --global http.sslVerify false

# Redefinir tempo de expiração do registro de log (reflog)
git config --global gc.reflogExpire 12.months.ago

# Tratamento de espaços em branco
git config --global apply.whitespace nowarn
git config --global core.whitespace nowarn

# Definição de cores para o modo console
git config --global color.branch auto
git config --global color.diff auto
git config --global color.status auto
git config --global color.interactive auto

# Personalização individual de projeto para o diretório de git hooks
git config core.hooksPath .git-hooks

# Configuração de case para gitignore no repositório ativo
git config core.ignorecase true

# Criar Atalhos de comando:
  git config --global alias.co checkout;
  git config --global alias.br branch;
  git config --global alias.ci commit;
  git config --global alias.st status;
  git config --global alias.ls "log --stat";
  git config --global alias.lg 'log --graph --oneline --decorate --all';


# Logs detalhados em modo gráfico
git config --global alias.lsg "log --stat --graph";


# Pull tags
git config --global alias.pt '!git tag -l | xargs git tag -d && git fetch -t';

# Desfaz modificações de stash
git config --global alias.stash-unapply '!git stash show -p | git apply -R';

# Exibe os aliases configurados para sessão do usuário
git config --global alias.aliases "config --get-regexp alias";

echo 'Configuração git concluída'