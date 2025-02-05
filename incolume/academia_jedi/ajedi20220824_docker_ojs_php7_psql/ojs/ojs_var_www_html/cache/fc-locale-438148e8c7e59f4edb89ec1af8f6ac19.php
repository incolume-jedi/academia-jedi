<?php return array (
  'api.submissions.403.csrfTokenFailure' => 'Seu pedido foi negado, provavelmente devido ao seu acesso ter expirado. Recarregue a página.',
  'api.submissions.403.requestedOthersUnpublishedSubmissions' => 'Você pode ver apenas submissões não publicadas as quais foi designada.',
  'api.submissions.403.deleteSubmissionOutOfContext' => 'Você não pode apagar uma submissão que não está associada a esse contexto.',
  'api.submissions.403.unauthorizedDeleteSubmission' => 'Você não tem permissões para apagar essa submissão.',
  'api.404.resourceNotFound' => 'O recurso requisitado não foi encontrado.',
  'api.submissions.400.missingRequired' => 'Seu pedido não pode ser atendido pois informação requerida está faltando.',
  'api.submissions.400.invalidIssueIdentifiers' => 'O volume requisitado, número ou ano não é válido.',
  'api.submissions.unknownError' => 'Ocorreu um erro não esperado. Por favor recarregue a página e tente novamente. Se o erro persistir contacte o suporte técnico.',
  'api.stats.400.wrongTimelineInterval' => 'Sua solicitação não é válida. O intervalo de tempo deve ser \'dia\' ou \' mês\'.',
  'api.stats.400.lateDateRange' => 'A data final não pode ser posterior a ontem.',
  'api.stats.400.earlyDateRange' => 'A data de início não pode ser anterior a 01-01-2001.',
  'api.stats.400.wrongDateRange' => 'A data de início não pode ser posterior à data de término.',
  'api.stats.400.wrongDateFormat' => 'A data deve estar no formato AAAA-MM-DD.',
  'api.submissions.403.userCantEdit' => 'Você não tem permissão para editar esta publicação.',
  'api.publicFiles.500.badFilesDir' => 'O diretório de arquivos públicos não foi encontrado ou os arquivos não podem ser salvos nele. Entre em contato com seu administrador para resolver esse problema.',
  'api.publicFiles.413.noDirSpace' => 'Você não possui espaço suficiente no diretório do usuário. O arquivo que você está carregando tem {$fileUploadSize} kb e você tem {$dirSizeLeft} kb restantes.',
  'api.publicFiles.403.unauthorized' => 'Você não tem permissão para transferir arquivos.',
  'api.publicFiles.400.mimeTypeNotMatched' => 'O arquivo que você enviou não corresponde à extensão do arquivo. Isso pode acontecer quando um arquivo foi renomeado para um tipo incompatível, por exemplo, alterando photo.png para photo.jpg.',
  'api.publicFiles.400.invalidImage' => 'A imagem que você transferiu não é válida.',
  'api.publicFiles.400.extensionNotSupported' => 'Você pode fazer transferência apenas dos seguintes tipos de arquivos: {$fileTypes}.',
  'api.publication.403.cantDeletePublished' => 'Você deve despublicar esta publicação antes de poder excluí-la.',
  'api.publication.403.cantEditStatus' => 'Você não pode modificar o status diretamente através da API. Em vez disso, use os pontos de extremidade /publish e /unpublish.',
  'api.publication.403.cantEditPublished' => 'Você não pode editar esta publicação, porque ela já está publicada.',
  'api.publication.403.alreadyUnpublished' => 'A publicação que você deseja despublicar não está publicada.',
  'api.publication.403.alreadyPublished' => 'A publicação que você deseja publicar já está publicada.',
  'api.emailTemplates.404.templateNotFound' => 'O modelo de e-mail solicitado não foi encontrado.',
  'api.404.endpointNotFound' => 'A URL solicitada não foi reconhecida.',
  'api.403.unauthorized' => 'Você não está autorizado para acessar o recurso solicitado.',
  'api.400.paramNotSupported' => 'O parâmetro {$param} não é suportado.',
  'api.vocabs.400.vocabNotSupported' => 'O vocabulário {$vocab} não é suportado.',
  'api.vocabs.400.localeNotSupported' => 'O idioma {$locale} não é suportado.',
  'api.themes.404.themeUnavailable' => 'O tema ativo, {$themePluginPath}, não está habilitado e pode não ter sido instalado.',
  'api.temporaryFiles.400.config' => 'O arquivo não pôde ser enviado por causa de um erro de configuração no servidor. Por favor, entre em contato com o administrador do sistema.',
  'api.temporaryFiles.400.fileSize' => 'Arquivos maiores do que {$maxSize} não podem ser enviados.',
  'api.temporaryFiles.409.uploadFailed' => 'Um ou mais arquivos não foram enviados.',
  'api.temporaryFiles.400.noUpload' => 'Nenhum arquivo a ser carregado foi encontrado com a solicitação.',
  'api.submissions.404.siteWideEndpoint' => 'Este terminal não está disponível em um contexto. Ele deve ser acessado no namespace de todo o site.',
  'api.stats.400.invalidOrderDirection' => 'Requisição inválida. O valor orderDirection precisa ser `desc` (descendente) ou `asc` (ascendente) .',
);