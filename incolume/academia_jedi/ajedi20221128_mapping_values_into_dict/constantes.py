# !/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "@britodfbr"  # pragma: no cover

labels = "Added Changed Deprecated Removed Fixed Security".split()

MSG = """
0.1.0           Added: initial commit
0.2.0           Added: implementação para def namespace
0.3.0           Added: incolumepy.utils.sequencia
0.4.0           Added: incolumepy.utils.fake_cpf adding
0.5.0           Added: incolumepy.utils.files adding
0.6.0           Added: automatic tests adding
0.7.0           Added: added incolumepy.utils.files.ll
0.7.1           Fix: atualizações no setup, e na apresentação da documentação
0.7.2           Changed: atualização EXAMPLE.rst
0.8.0           Added: ll() adicionado
0.9.0           Added: nonexequi para restrição de execução em serie
0.9.1           Fix: corrigido namespace
0.9.2           Fix: package incolumepy.utils.sequencias remaked into incolumepy.sequencias
0.9.3           Fix: Nova implementação para incolumepy.utils.utils.namespace
0.9.4           Fix: Chamada do pacote utils através do Namespace
1.0.0           Added: acrescentado o modulo decorator
1.0.1           Added: acrescentado o logging para realfilename
1.1.0           Added: Novas funcionalidades acrescentadas
1.1.1           Changed: Atualização de configurações
1.2.0           Changed: Unificado versionamento com pyproject.toml
1.3.0           Added: githooks acrescentados
1.3.1           Fixed: filemode para githooks corrigidos
1.3.2           Changed: Atualização do README
1.4.0           Added: Makefile adicionado com funções básicas
1.5.0           Added: Aplicado utilização de linters, e integrado ao tox e Makefile
1.6.0           Removed: Metodos obsoletos desativados
1.6.1           Fix: Diversas pequenas Correções
1.6.2           Changed: Refactor espectro de busca para namespace
1.6.3           Fix: Correção de pane FileNotFoundError
1.7.0           Added: Acrescentado milhar e key_sort_2_versions
2.0.0           Removed: Módulo incolumepy.utils.sequences deixou de existir; Changed: Gerenciador de pacotes alterado para poetry; Changed: Switch de testes alterado para pytest; Changed: Redefinição de estrutura; Deprecated: Funcionalidades obsoletas sinalizadas como deprecated; Changed: Atualização de teste para key_sort_2_versions
2.0.0-rc.0      Changed: Redefinição de estrutura
2.0.0-rc.1      Deprecated: Funcionalidades obsoletas sinalizadas como deprecated.
2.0.0-rc.2      Changed: Atualização de teste para key_sort_2_versions
2.1.0           Added: Módulo 'incolumepy.utils.url' acrescentado
2.2.0           Added: retrocompatibilidade Python3.6+ garantida.
2.3.0           Added: Acrescentado Método identify_dom_url_verbose
2.4.0           Added: Método update_changelog acrescentado
2.4.1           Fixed: Correções em update_changelog
2.5.0           Added: Geração do CHANGELOG, padronizado de acordo com 'keep a changelog'; e geração automática com entradas extraídas de git/tags.
2.5.1           Removed: Pacotes obsoletos removidos.
2.5.2           Changed: Correções lint style; Visual CHANGELOG
2.5.3           Changed: utils.files.realfilename Fatorado para sanar complexidade ciclomática.
2.5.4           Added: Documentação automatizada com sphinx2.6.0   Added: adicionado; Removed: Removido; Changed: Alterado; asdfafafafasf; afasdfasdfadsfasdf; asfasdfasdfasfasdf; Fixed: Corrigido; Alterado; Validado
"""

