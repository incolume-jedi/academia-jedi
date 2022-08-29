<?php return array (
  'plugins.generic.usageStats.settings.logging' => 'Opções de log de acessos',
  'plugins.generic.usageStats.settings.createLogFiles' => 'Criar arquivos de log',
  'plugins.generic.usageStats.settings.createLogFiles.description' => 'Ativar esta opção fará com que o plugin crie arquivos de log dentro da sua pasta de arquivos. Os arquivos devem ser usados para extração de dados estatísticos. Caso não deseje criar mais arquivos de log, deixe a opção desabilitada e use os arquivos de log do próprio servidor.',
  'plugins.generic.usageStats.settings.logParseRegex' => 'Expressão regular de tratamento de arquivos de log',
  'plugins.generic.usageStats.settings.logParseRegex.description' => 'A expressão regular padrão pode ser usada para tratar arquivos de log do apache em formato combinado, bem como os arquivos de log do plugin. Caso seus arquivos de log estejam em formato diferente, será necessário inserir uma regex capaz de tratá-los e recuperar os valores esperados. Veja UsageStatsLoader::_getDataFromLogEntry() para mais informações.',
  'plugins.generic.usageStats.settings.saved' => 'Configurações do plugin de estatísticas de uso salvas com sucesso',
  'plugins.generic.usageStats.openFileFailed' => 'O arquivo {$file} não pôde ser aberto e foi rejeitado.',
  'plugins.generic.usageStats.invalidLogEntry' => 'A linha {$lineNumber} do arquivo {$file} não é uma entrada de log válida e o arquivo foi rejeitado.',
  'plugins.generic.usageStats.displayName' => 'Estatísticas de uso',
  'plugins.generic.usageStats.description' => 'Apresentar estatísticas de uso de objetos de dados. Pode usar arquivos de log de acesso para extrair estatísticas.',
  'plugins.generic.usageStats.settings.dataPrivacyOption' => 'Opção de privacidade de dados',
  'plugins.generic.usageStats.settings.dataPrivacyOption.saltFilepath' => 'Caminho de arquivo para entropia de anonimato',
  'plugins.generic.usageStats.settings.dataPrivacyOption.saltFilepath.invalid' => 'O arquivo não pode ser gravado.',
  'plugins.generic.usageStats.settings.dataPrivacyOption.requirements' => 'Para garantir a privacidade dos dados, você deve especificar um arquivo legível e gravável pelo usuário do webserver para conter um valor de entropia de senha gerado aleatoriamente. Este arquivo não deve ser incluídos em backups de modo a garantir a proteção da privacidade. O valor é gerado aleatoriamente usando a função mcrypt_create_iv, o que requer a bilbioteca PHP mcrypt; a função openssl_random_pseudo_bytes, que requer o PHP openssl; o arquivo /dev/urandom, que só funciona em sistemas *nix; ou a função mt_rand, que não é criptograficamente segura. Assim, se você estiver usando um servidor Windows, certifique-se que você instale ou o PHP mcrypt ou habilitade o openssl para ter o valor de entropia gerado de forma criptograficamente segura.',
  'plugins.generic.usageStats.settings.dataPrivacyOption.description' => 'Ative essa opção para usar uma versão do plug-in que respeite as legislações de privacidade, ou seja, que está registrando endereços IP com hash, informa os usuários sobre o rastreamento e fornece uma opção de desabilitar para os usuários. Nota: quando utilizar esta opção, você não será capaz de usar os recursos de geolocalização do plugin.',
  'plugins.generic.usageStats.settings.dataPrivacyOption.requiresSalt' => 'Habilitar a privacidade dos dados requer um arquivo de entropia (salt).',
  'plugins.generic.usageStats.settings.dataPrivacyOption.excludesCity' => 'Habilitando a privacidade dos dados exclui Cidade como uma estatística opcional.',
  'plugins.generic.usageStats.settings.dataPrivacyOption.excludesRegion' => 'Habilitando a privacidade dos dados exclui Região como uma estatística opcional.',
  'plugins.generic.usageStats.settings.dataPrivacyCheckbox' => 'Respeitar a privacidade dos dados',
  'plugins.generic.usageStats.settings.optionalColumns' => 'Informações estatísticas opcionais',
  'plugins.generic.usageStats.settings.optionalColumns.description' => 'Ativar ou desativar a coleta das seguintes informações opcionais. Isso vai influenciar sobre os possíveis relatórios de estatísticas você pode recuperar, e também terá um impacto sobre o tamanho do banco de dados. NÃO MUDE a menos que você entenda completamente o que você está fazendo.',
  'plugins.generic.usageStats.settings.optionalColumns.cityRequiresRegion' => 'A coluna opcional "Cidade" requer a coluna opcional "Região".',
  'plugins.generic.usageStats.settings.archives' => 'Arquivos',
  'plugins.generic.usageStats.settings.compressArchives.description' => 'Ative essa opção para compactar arquivos de log usando a ferramenta gzip (você terá que definir a configuração gzip dentro config.inc.php). Se você tem um site de alto tráfego, é uma boa ideia permitir isso para economizar algum espaço em disco.',
  'plugins.generic.usageStats.settings.compressArchives' => 'Comprimir arquivos',
  'plugins.generic.usageStats.usageStatsLoaderName' => 'Tarefa do carregador de arquivo de estatísticas de uso',
  'plugins.generic.usageStats.removeUrlError' => 'O número da linha {$lineNumber} do arquivo {$file} contém uma URL que o sistema não pode remover a url base.',
  'plugins.generic.usageStats.loadDataError' => 'Não foi possível carregar os dados extraídos do arquivo {$file}. O arquivo foi transferido para novo processamento.',
  'plugins.generic.usageStats.pluginNotEnabled' => 'O plugin de estatísticas de uso está desativado. Nenhum arquivo de log processado.',
  'plugins.generic.usageStats.processingPathNotEmpty' => 'O diretório {$directory} não está vazio. Isto poderia indicar que um processo falhou anteriormente, ou um processo está executando atualmente. Este arquivo será automaticamente reprocessado se você estiver usando oscheduledTasksAutoStage.xml, caso contrário, você precisará mover manualmente os arquivos órfãos no diretório de processamento de volta para o diretório principal.',
  'plugins.reports.usageStats.report.displayName' => 'Relatório de estatísticas de uso do sistema',
  'plugins.reports.usageStats.report.description' => 'Relatório padrão de estatísticas de uso (compatível com COUNTER)',
  'plugins.generic.usageStats.optout.displayName' => 'Informações Privadas de Estatística de Uso',
  'plugins.generic.usageStats.optout.description' => 'Informações Privadas de Estatística de Uso',
  'plugins.generic.usageStats.optout.title' => 'Informações de Estatísticas de Uso',
  'plugins.generic.usageStats.optout.shortDesc' => 'Nós registramos estatísticas de uso de forma anônima. Por favor, leia as <a href="{$privacyInfo}"> informações de privacidade </a> para mais detalhes.',
  'plugins.generic.usageStats.optin' => 'Aceitar',
  'plugins.generic.usageStats.optout' => 'Rejeitar',
  'plugins.generic.usageStats.optout.done' => '
		<p>Recusa à coleta de estatísticas de uso realizada com sucesso. Enquanto esta mensagem estiver sendo apresentada, nenhuma estatística será coletada pelo sistema. Clique no botão a seguir para reverter essa decisão.</p>',
  'plugins.generic.usageStats.optout.cookie' => '
		<p> Se desejar, você pode optar por não participar do processo de coleta de dados. Ao clicar no botão de desativação abaixo, você pode decidir ativamente não participar da análise estatística. Ao clicar no botão de desativação, um <em> cookie </em> está sendo criado no seu sistema para armazenar sua decisão. Se as configurações de privacidade do seu navegador levarem os cookies a serem excluídos automaticamente, você terá que desativar novamente na próxima vez que acessar este site. O cookie é válido apenas para um navegador. Se você usar um navegador diferente, precisará desativar novamente. Nenhuma informação individual é armazenada dentro deste cookie. Esta concessão de cookies é válida por um ano após o seu último acesso. </p>
		<p>Note que registros de atividade do servidor de hospedagem não são afetados por esta decisão, sendo específicas para este sistema. Veja nossa <a href="{$privacyStatementUrl}">política de privacidade</a>.</p>',
  'plugins.reports.usageStats.metricType' => 'PKP/COUNTER',
  'plugins.reports.usageStats.metricType.full' => 'Estatísticas do Public Knowledge Project (compatível com COUNTER)',
  'plugins.generic.usageStats.settings.statsDisplayOptions' => 'Opções para exibição de estatísticas',
  'plugins.generic.usageStats.settings.statsDisplayOptions.display' => 'Mostrar gráfico de estatísticas da submissão para o leitor',
  'plugins.generic.usageStats.settings.statsDisplayOptions.chartType' => 'Escolha o tipo de gráfico para exibir as estatísticas de download',
  'plugins.generic.usageStats.settings.statsDisplayOptions.chartType.bar' => 'Barra',
  'plugins.generic.usageStats.settings.statsDisplayOptions.chartType.line' => 'Linha',
  'plugins.generic.usageStats.settings.statsDisplayOptions.datasetMaxCount' => 'Definir o número máximo de dados para apresentar ao mesmo tempo para um ponto do eixo x-específica. Um valor mais alto pode gerar gráficos difíceis de entender . Algo entre 3 e 5 é adequado.',
  'plugins.generic.usageStats.statsSum' => 'Somar todos os downloads de arquivos',
  'plugins.generic.usageStats.noStats' => 'Não há dados estatísticos.',
  'plugins.generic.usageStats.monthInitials' => 'Jan Fev Mar Abr Mai Jun Jul Ago Set Out Nov Dez',
  'plugins.generic.usageStats.settings.statsDisplayOptions.contextWide' => 'Essas configurações serão aplicadas apenas às estatísticas de uso em {$contextName}.',
  'plugins.generic.usageStats.downloads' => 'Downloads',
  'plugins.generic.usageStats.optout.description.long.ojs2' => '
		<h3>Informações gerais sobre privacidade</h3>
		<p>Veja nossa <a href="{$privacyStatementUrl}">política geral de privacidade</a>.</p>
		<h3>Estatísticas de uso</h3>
		<p>Para permitir a análise de uso e impacto do periódico e dos artigos publicados, são coletados e registrados os acessos as páginas: página inicial, edições, artigos, composições finais e arquivos suplementares. No processo de coleta, todos os dados são tornados anônimos. Nenhuma informação pessoal é registrada. Os endereços de IP são obfuscados por meio de uma criptografia (usando <em>SHA 256</em>) combinada com uma <em>chave de segurança de 64 caracteres</em> que é <em>gerada randomicamente e alterada diariamente</em> de forma automática. Portanto, não há como reconstruir os endereços de IP.</p>
		<p>As seguintes informações são coletadas, além do endereço de IP a ser ofuscado:</p>
		<ul>
		<li>Tipo de acesso (administração, leitura, etc.)</li>
		<li>Hora da acessoo</li>
		<li>Endereço acessado</li>
		<li>Código de status HTTP</li>
		<li>Navegador</li>
		</ul>
		<p>Os dados coletados são usados apenas para propósitos de avaliação. Nenhum endereço de IP é mapeado a IDs de usuário. É tecnicamente impossível rastrear um conjunto específicos de dados a um IP específico.</p>',
  'plugins.generic.usageStats.optout.description.long.omp' => '
		<h3>Informações sobre Privacidade</h3>
		<p>Por favor verifique nossa <a href="{$privacyStatementUrl}">declaração de privacidade</a>.</p>
		<h3>Estatíticas de Uso</h3>
		<p> Para poder analisar o uso e o impacto de nossas publicações, coletamos e registramos o acesso à página inicial, categorias, séries, livros e arquivos. No processo, todos os dados são anonimizados. Nenhuma informação pessoal é registrada. Os endereços IP são anonimizados por meio de hash (usando <em> SHA 256 </em>) em combinação com um <em> sal seguro de 64 caracteres </em>, que é automaticamente <em> gerado aleatoriamente e substituído diariamente </em>. Portanto, os endereços IP não podem ser reconstruídos. </p>
		<p>As informações seguintes são coletadas a partir dos endereços de IP anônimos:</p>
		<ul>
		<li>Tipo de acesso (i.e. administrativo)</li>
		<li>Tempo da visita</li>
		<li>URL visitada</li>
		<li>Código HTTP</li>
		<li>Navegador</li>
		</ul>
		<p>Os dados coletados são usados apenas para propósitos de avaliação. Nenhum endereço de IP é mapeado para identidades de usuários. É tecnicamente impossível rastrear um conjunto de dados a um IP específico</p>',
  'plugins.generic.usageStats.settings.statsDisplayOptions.siteWide.ojs2' => 'Cada revista pode substituir essas configurações na página de plugins da revista.',
  'plugins.generic.usageStats.settings.statsDisplayOptions.siteWide.omp' => 'Cada editora pode substituir essas configurações na página de plugins.',
);