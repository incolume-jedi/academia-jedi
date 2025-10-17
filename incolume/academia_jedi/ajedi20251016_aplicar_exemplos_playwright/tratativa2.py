"""Exemplo 2."""

from icecream import ic
from playwright.sync_api import Locator, expect, sync_playwright

str_html = """
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">
<html lang="pt-br" >
<head >

<link rel="shortcut icon" sizes="any" href="favicon/favicon.ico" />
<link rel="icon" type="image/svg+xml" href="favicon/favicon.svg" />
<link rel="apple-touch-icon" href="favicon/apple-touch-icon.png" />
<link rel="manifest" href="favicon/site.webmanifest" />
<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1"/>
<meta name="robots" content="noindex"/>
<meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
<title>SEI - Controle de Processos</title>
<link href="/infra_css/infra-tooltip.css?4.1.5-2.29.0" rel="stylesheet" type="text/css" media="all"/>
<link href="/infra_css/infra-barra-progresso.css?4.1.5-2.29.0" rel="stylesheet" type="text/css" media="all"/>
<link href="/infra_css/infra-impressao-global.css?4.1.5-2.29.0" rel="stylesheet" type="text/css" media="print"/>
<link href="/infra_css/infra-ajax.css?4.1.5-2.29.0" rel="stylesheet" type="text/css" media="all"/>
<link href="/infra_js/calendario/v2/infra-calendario.css?4.1.5-2.29.0" rel="stylesheet" type="text/css" media="all"/>
<link href="/infra_js/arvore/infra-arvore.css?4.1.5-2.29.0" rel="stylesheet" type="text/css" media="all"/>
<link href="/infra_js/mapa/infra-mapa.css?4.1.5-2.29.0" rel="stylesheet" type="text/css" media="all"/>
<link href="/infra_js/jquery/jquery-ui-1.13.2/jquery-ui.min.css?1.13.2" rel="stylesheet" type="text/css" media="all"/>
<link href="/infra_js/jquery/jquery-ui-1.13.2/jquery-ui.structure.min.css?1.13.2" rel="stylesheet" type="text/css" media="all"/>
<link href="/infra_js/jquery/jquery-ui-1.13.2/jquery-ui.theme.min.css?1.13.2" rel="stylesheet" type="text/css" media="all"/>
<link href="/infra_js/multiple-select/multiple-select.min.css?4.1.5-2.29.0" rel="stylesheet" type="text/css" media="all"/>
<link href="/infra_js/modal/jquery.modalLink-1.0.0.css?4.1.5-2.29.0" rel="stylesheet" type="text/css" media="all"/>
<link href="/infra_css/bootstrap/bootstrap-4.6.2.min.css?4.1.5-2.29.0" rel="stylesheet" type="text/css" media="all"/>
<link href="/infra_css/bootstrap/menu-bootstrap.css?4.1.5-2.29.0" rel="stylesheet" type="text/css" media="all"/>
<link href="/infra_css/infra-global-esquema-3.css?4.1.5-2.29.0" rel="stylesheet" type="text/css" media="all"/>
<link href="/infra_css/esquemas/azul_celeste/infra-esquema-3.css?4.1.5-2.29.0" rel="stylesheet" type="text/css" media="all"/>
<link href="css/infra-local-esquema-3.css?4.1.5-2.29.0" rel="stylesheet" type="text/css" media="all"/>
<style></style><style type="text/css" >
<!--/*--><![CDATA[/*><!--*/
@media only print {

  #divInfraAreaTelaD,
  #divTabelaProcesso,
  #divTabelaProcesso div{
    display:block;
    min-height:100%;
    width: auto !important;
    height: auto !important;
    overflow: visible !important;
  }

  #divInfraAreaTelaE,
  #divBotoesControleProcessos,
  #divFiltro,
  div.infraAreaPaginacao{
    display:none !important;
  }

  a {
    text-decoration:none !important;
  }
}

#divFiltro{
  margin: 15px 0 2px 0;
}


div.caixaFiltroControle{
  background-color:#fff;
  color:#7F7F7F;
  padding: 2px 6px;
  border-radius: 4px;
  box-shadow: 0 0.125rem 0.5rem rgba(0, 0, 0, .3), 0 0.0625rem 0.125rem rgba(0, 0, 0, .2);
  z-index:101;
}

div.caixaFiltroControle p{
  display:inline;
  vertical-align:top;
  font-size:0.875rem;
  line-height:24px;
}

div.caixaFiltroControle img{
  vertical-align:bottom;
}

div.caixaFiltroControle a:focus{
  outline:1px dotted black;
}

div.caixaFiltroControle a:hover{
  text-decoration:none;
}

a.botaoFecharFiltro{
  float:right;
  cursor:pointer;
  color: #fff;
  border-radius: 10px;
  background: #605F61;
  font-size: 16px;
  font-weight: bold;
  display: inline-block;
  line-height: 1px;
  padding: 9px 5px;
  margin-top:-9px;
  margin-right:-15px;
}

.botaoFecharFiltro:before {
    content: "×";
}

table.tabelaControle,
  tr.infraTrClara td  {
  border:0;
}

table.tabelaControle td {
  text-align:center;
}

a.ancMarcador{
  font-size: 0.875rem;
  text-decoration:none !important;
  border:1px solid #d0d0d0;
  padding:4px;
  margin:2px;
  -moz-border-radius: 4px;
  border-radius: 4px;
  -webkit-border-radius: 4px;
  float:left;
  background-color:#f5f5f5;
}

a.ancMarcador img{
  padding: 0 4px 0 0;
}

a.ancMarcador div{
  display:table-cell;
}

.divLink .ancoraPadraoPreta{
  padding: 0px;
}

.divLink:not(:first-child){
  margin-left:2.5em !important;
}

.divLink:last-child{
  margin-right:15px;
}

#divInfraBtnTopo{
  flex: 0 0 100%;
  max-width: 100%;
}


/*]]>*/-->
</style>
<script type="text/javascript">var INFRA_PATH_CSS="/infra_css",INFRA_PATH_IMAGENS="/infra_css/imagens",INFRA_PATH_JS="/infra_js",INFRA_PATH_SVG="/infra_css/svg",INFRA_LUPA_TIPO_JANELA=2,INFRA_BARRA_TIPO_JANELA=2,INFRA_TIPO_ALERTA=1;</script>
<script type="text/javascript" charset="utf-8" src="/infra_js/jquery/jquery-3.7.0.min.js?3.7.0"></script>
<script type="text/javascript" charset="utf-8" src="/infra_js/jquery/jquery-ui-1.13.2/jquery-ui.min.js?1.13.2"></script>
<script type="text/javascript" charset="utf-8" src="/infra_js/multiple-select/multiple-select.min.js?4.1.5-2.29.0"></script>
<script type="text/javascript" charset="utf-8" src="/infra_js/ddslick/jquery.ddslick.min.js?4.1.5-2.29.0"></script>
<script type="text/javascript" charset="utf-8" src="/infra_js/modal/jquery.modalLink-1.0.0.js?4.1.5-2.29.0"></script>
<script type="text/javascript" charset="iso-8859-1" src="/infra_js/InfraPaginaEsquema3.js?4.1.5-2.29.0"></script>
<script type="text/javascript" charset="iso-8859-1" src="/infra_js/InfraBotaoMenu.js?4.1.5-2.29.0"></script>
<script type="text/javascript" charset="iso-8859-1" src="/infra_js/InfraUtil.js?4.1.5-2.29.0"></script>
<script type="text/javascript" charset="iso-8859-1" src="/infra_js/InfraCookie.js?4.1.5-2.29.0"></script>
<script type="text/javascript" charset="iso-8859-1" src="/infra_js/InfraUpload.js?4.1.5-2.29.0"></script>
<script type="text/javascript" charset="iso-8859-1" src="/infra_js/InfraTabelaDinamica.js?4.1.5-2.29.0"></script>
<script type="text/javascript" charset="iso-8859-1" src="/infra_js/InfraLupas.js?4.1.5-2.29.0"></script>
<script type="text/javascript" charset="iso-8859-1" src="/infra_js/InfraSelectEditavel.js?4.1.5-2.29.0"></script>
<script type="text/javascript" charset="iso-8859-1" src="/infra_js/InfraAjax.js?4.1.5-2.29.0"></script>
<script type="text/javascript" charset="iso-8859-1" src="/infra_js/InfraTooltip.js?4.1.5-2.29.0"></script>
<script type="text/javascript" charset="iso-8859-1" src="/infra_js/calendario/v2/InfraCalendario.js?4.1.5-2.29.0"></script>
<script type="text/javascript" charset="iso-8859-1" src="/infra_js/arvore/InfraArvore.js?4.1.5-2.29.0"></script>
<script type="text/javascript" charset="iso-8859-1" src="/infra_js/maskedpwd/MaskedPassword.min.js?4.1.5-2.29.0"></script>
<script type="text/javascript" charset="utf-8" src="/infra_js/bootstrap/bootstrap-4.6.2.min.js?4.1.5-2.29.0"></script>
<script type="text/javascript" charset="utf-8" src="/infra_js/bootstrap/infra-menu-bootstrap.js?4.1.5-2.29.0"></script>
<script type="text/javascript" charset="utf-8" src="/infra_js/touch/jquery.ui.touch-punch.min.js?4.1.5-2.29.0"></script>
<script type="text/javascript" charset="utf-8" src="/infra_js/hotkeys/jquery.hotkeys.js?4.1.5-2.29.0"></script>
<script type="text/javascript" charset="iso-8859-1" src="js/sei.js?4.1.5-2.29.0"></script>

<script type="text/javascript" charset="iso-8859-1" >
<!--//--><![CDATA[//><!--

//<script>


  $( document ).ready(function() {

    $('#ancLiberarMeusProcessos').click(function(){
      verMeusProcessos('T')
    });

    $('#ancLiberarMarcador').click(function(){
      filtrarMarcador(null);
    });

    $('#ancLiberarTipoProcedimento').click(function(){
      filtrarTipoProcedimento(null);
    });

    $('#ancLiberarTipoPrioridade').click(function(){
      filtrarTipoPrioridade(null);
    });

  });


  var objLupaBlocoPesquisa = null;
  var bolCarregando = true;

  function inicializar(){

    $('#divInfraBarraLocalizacao').prependTo( $('#divControleProcessosConteudo') );

    if($('#divInfraBarraAcesso').length){
      $('#divInfraBarraAcesso').prependTo( $('#divControleProcessosConteudo') );
    }

    //$('.tabelaControle tr td:nth-child(2) > *').attr('tabindex',1009);

        seiConfigurarTabIndexSinalizacoes('tblProcessosRecebidos','1001');
    seiConfigurarTabIndexSinalizacoes('tblProcessosGerados','1002');


    if (infraIsBreakpointBootstrap("lg")){
      infraExibirMenuSistemaEsquema();
      }


        infraAbrirJanelaModal('controlador.php?acao=novidade_mostrar&infra_sistema=100000100&infra_unidade_atual=110000302&infra_hash=573e5d97cf36b2d58bc1344f7f1ff30e79a87b8940add478d4c11474310277c7',950,500,false);

    objLupaBlocoPesquisa = new infraLupaText('txtBloco','hdnIdBloco','controlador.php?acao=bloco_selecionar_processo&tipo_selecao=1&id_object=objLupaBlocoPesquisa&infra_sistema=100000100&infra_unidade_atual=110000302&infra_hash=a3aafecafe15fbcb0e743082ba84de3873ef7b25fcb04238f8640a29971669b3');
    objLupaBlocoPesquisa.finalizarSelecao = function(){
      document.getElementById('frmProcedimentoControlar').action = 'controlador.php?acao=rel_bloco_protocolo_cadastrar&acao_origem=procedimento_controlar&acao_retorno=procedimento_controlar&infra_sistema=100000100&infra_unidade_atual=110000302&infra_hash=c13bfc58c0f695aa7c109e89cb489595d8c145a3504038f3d9ba2b1304b8d1e3';
      document.getElementById('frmProcedimentoControlar').submit();
    };

    if (infraGetAnchor()==null && !infraDispositivoMovel()){
            if (document.getElementById('tblProcessosRecebidos')!=null){
        document.getElementById('tblProcessosRecebidos').focus();
      }else if (document.getElementById('tblProcessosGerados')!=null) {
        document.getElementById('tblProcessosGerados').focus();
      }
          }

    infraEfeitoTabelas();

  }

  function acaoPendenciaMultipla(bolMsg){
    if ('R' == 'R'){
      if (document.getElementById('hdnGeradosItensSelecionados').value=='' && document.getElementById('hdnRecebidosItensSelecionados').value==''){
        if (bolMsg){
          alert('Nenhum processo selecionado.');
        }
        return false;
      }
      document.getElementById('hdnGeradosItemId').value = '';
      document.getElementById('hdnRecebidosItemId').value = '';
    }else{
      if (document.getElementById('hdnDetalhadoItensSelecionados').value==''){
        if (bolMsg){
          alert('Nenhum processo selecionado.');
        }
        return false;
      }
      document.getElementById('hdnDetalhadoItemId').value = '';
    }

    return true;
  }

  function acaoControleProcessos(link, requerSelecionado, aceitaSigiloso){
    if ((!requerSelecionado || acaoPendenciaMultipla(true)) && (aceitaSigiloso || !bloquearSigilosoSelecionado())){
      document.getElementById('frmProcedimentoControlar').action = link;
      document.getElementById('frmProcedimentoControlar').submit();
    }
  }

  function acaoBlocoProcessar(){
    if (acaoPendenciaMultipla(true) && !bloquearSigilosoSelecionado()){
      document.getElementById('txtBloco').value = '';
      document.getElementById('hdnIdBloco').value = '';
      objLupaBlocoPesquisa.selecionar(700,500,true);
    }
  }

  function acaoRemoverMarcadorProcessar(link, requerSelecionado, aceitaSigiloso){
    if (!bloquearNenhumComMarcadorSelecionado()) {
      acaoControleProcessos(link, requerSelecionado, aceitaSigiloso);
    }
  }

  function bloquearSigilosoSelecionado(){

    var sigilosos = document.getElementById('hdnIdSigilosos').value;

    if (sigilosos!='') {

      selecionados = '';

      if ('R' == 'R') {

        if (document.getElementById('hdnGeradosItensSelecionados').value!='') {
          selecionados = document.getElementById('hdnGeradosItensSelecionados').value;
        }

        if (document.getElementById('hdnRecebidosItensSelecionados').value!='') {
          if (selecionados!='') {
            selecionados += ',';
          }
          selecionados += document.getElementById('hdnRecebidosItensSelecionados').value;
        }

      } else {
        selecionados = document.getElementById('hdnDetalhadoItensSelecionados').value;
      }

      if (selecionados!='') {

        sigilosos = sigilosos.split(',');
        selecionados = selecionados.split(',');

        for (var i = 0; i<sigilosos.length; i++) {
          for (var j = 0; j<selecionados.length; j++) {
            if (sigilosos[i]==selecionados[j]) {
              alert('Operação não aplicável em processo sigiloso.');
              return true;
            }
          }
        }
      }
    }
    return false;
  }

  function bloquearNenhumComMarcadorSelecionado(){

    var commarcador = document.getElementById('hdnIdComMarcador').value;

    if (commarcador!='') {

      selecionados = '';

      if ('R' == 'R') {

        if (document.getElementById('hdnGeradosItensSelecionados').value!='') {
          selecionados = document.getElementById('hdnGeradosItensSelecionados').value;
        }

        if (document.getElementById('hdnRecebidosItensSelecionados').value!='') {
          if (selecionados!='') {
            selecionados += ',';
          }
          selecionados += document.getElementById('hdnRecebidosItensSelecionados').value;
        }

      } else {
        selecionados = document.getElementById('hdnDetalhadoItensSelecionados').value;
      }

      if (selecionados!='') {

        commarcador = commarcador.split(',');
        selecionados = selecionados.split(',');

        for (var i = 0; i<commarcador.length; i++) {
          for (var j = 0; j<selecionados.length; j++) {
            if (commarcador[i]==selecionados[j]) {
              return false;
            }
          }
        }
      }
    }
    alert('Nenhum processo com marcador selecionado.');
    return true;
  }


  function listarCredenciais(){
    infraAbrirJanelaModal('',500,300);
  }

  function trocarVisualizacao(valor){
    document.getElementById('hdnTipoVisualizacao').value = valor;
    document.getElementById('frmProcedimentoControlar').submit();
  }

  function verMeusProcessos(valor){
    document.getElementById('hdnMeusProcessos').value = valor;
    document.getElementById('frmProcedimentoControlar').submit();
  }

  function filtrarMarcador(idMarcador){
    document.getElementById('hdnIdMarcador110000302').value = idMarcador;
    if (idMarcador==null){
      document.getElementById('frmProcedimentoControlar').action = 'controlador.php?acao=procedimento_controlar&acao_origem=procedimento_controlar&tipo_visualizacao=R&tipo_filtro=M&infra_sistema=100000100&infra_unidade_atual=110000302&infra_hash=5bf2ab82fa58dc83778cfdce8a8e84ac4e749c4142326afdb7720ff7a5463077';
    }else{
      document.getElementById('frmProcedimentoControlar').action = 'controlador.php?acao=procedimento_controlar&acao_origem=procedimento_controlar&tipo_visualizacao=R&infra_sistema=100000100&infra_unidade_atual=110000302&infra_hash=7f42efee458f082c0e24e8e0ce3962162d86b993e0c7a5d5e1e1b7b655fa7d8f';
    }

    document.getElementById('frmProcedimentoControlar').submit();
  }

  function filtrarTipoProcedimento(idTipoProcedimento){
    document.getElementById('hdnIdTipoProcedimento110000302').value = idTipoProcedimento;

    if (idTipoProcedimento == null){
      document.getElementById('frmProcedimentoControlar').action = 'controlador.php?acao=procedimento_controlar&acao_origem=procedimento_controlar&tipo_visualizacao=R&tipo_filtro=P&infra_sistema=100000100&infra_unidade_atual=110000302&infra_hash=57e573aa01619b68b3267b0c4847c7bcb2dafd403077f20a4d5ebd893e20677f';
    }else{
      document.getElementById('frmProcedimentoControlar').action = 'controlador.php?acao=procedimento_controlar&acao_origem=procedimento_controlar&tipo_visualizacao=R&infra_sistema=100000100&infra_unidade_atual=110000302&infra_hash=7f42efee458f082c0e24e8e0ce3962162d86b993e0c7a5d5e1e1b7b655fa7d8f';
    }

    document.getElementById('frmProcedimentoControlar').submit();
  }

  function filtrarTipoPrioridade(idTipoPrioridade){
    document.getElementById('hdnIdTipoPrioridade110000302').value = idTipoPrioridade;

    if (idTipoPrioridade == null){
      document.getElementById('frmProcedimentoControlar').action = 'controlador.php?acao=procedimento_controlar&acao_origem=procedimento_controlar&tipo_visualizacao=R&tipo_filtro=R&infra_sistema=100000100&infra_unidade_atual=110000302&infra_hash=56826f4c967ac7517c31560e11fdb828768ff5f01f0fa14e790ddcbda26f0fc3';
    }else{
      document.getElementById('frmProcedimentoControlar').action = 'controlador.php?acao=procedimento_controlar&acao_origem=procedimento_controlar&tipo_visualizacao=R&infra_sistema=100000100&infra_unidade_atual=110000302&infra_hash=7f42efee458f082c0e24e8e0ce3962162d86b993e0c7a5d5e1e1b7b655fa7d8f';
    }

    document.getElementById('frmProcedimentoControlar').submit();
  }

  function alterarVisualizacaoTabela(campo, valor, campoEsconder){
    document.getElementById(campo).value = valor;
    document.getElementById(campoEsconder).value = "false";
    document.getElementById('frmProcedimentoControlar').submit();
  }


  //</script>

//--><!]]>
</script>
</head>
<body onload="inicializar();"  >
<button onclick="infraMoverParaTopo()" id="btnInfraTopo" class="infraButton infraCorBarraSistema" ><img src="/infra_css/svg/topo.svg?2.29.0" title="Voltar ao Topo" alt="Voltar ao Topo" tabindex="32767"></button>
<div id="divInfraAreaGlobal" class="vh-100 vw-100 d-flex flex-column m-0 border-0" >

      <nav id="navInfraBarraNavegacao" class="  navbar navbar-expand-md infraBarraNavegacao infraCorBarraSistema p-0">

        <div id="divInfraBarraSistema" class="flex-column w-100 h-100 infraBarraSistema"  >
           <div id="divInfraBarraSistemaLinha"></div>
           <h6  class="pl-3 mb-0 mx-0 d-none d-md-block infraCorBarraSuperior">PRESIDÊNCIA DA REPÚBLICA</h6>
           <h6  class="pl-3 mb-0 mx-0 d-md-none infraCorBarraSuperior">PR</h6>

          <div id="divInfraBarraSistemaMovel" class="flex-row d-flex pb-0  pl-3 d-md-none media infraBarraSistemaMovel">
            <div class="d-flex flex-grow-1 infraBarraSistemaMovelE" >

               <div class="align-self-center mt-1">
                   <span id="spnInfraIdentificacaoSistema"><img src="svg/sei_barra.svg?4.1.5-2.29.0" title="Sistema Eletrônico de Informações - Versão 4.1.5"/><span class="infraTituloLogoSistema">4.1.5</span></span>
               </div>
            </div>
            <div class="infraBarraSistemaMovelD d-flex flex-shrink-0">
              <div class="nav-item d-flex d-md-flex py-md-0 py-2"><a id="lnkInfraMenuSistema" onclick="infraClicarMenuBootstrap()" href="#" target="_self"  title="Exibir/Ocultar Menu do Sistema" tabindex="65" class="nav-link align-self-center"><span class="font-weight-bold" style="padding:.1rem .5rem;">Menu</span></a></div ><div class=" nav-item px-1 d-flex d-md-flex  py-md-0 py-2">
                  <div class="input-group align-self-center ">
                  <a id="lnkInfraUnidade" href="#" onclick="window.location.href='controlador.php?acao=infra_trocar_unidade&infra_sistema=100000100&infra_unidade_atual=110000302&infra_hash=d751666c0d3d5193628d302d57dd66d756dd04d66d897324d30cdf9d292b5149';" class="form-control infraAcaoBarraConjugada" title="Centro de Estudos Jurídicos" tabindex="66">CEJ/SAJ/CC/PR</a>

             </div >
          </div>

        <a class="navbar-toggler px-1 border-0 flex-grow-0 mr-2 align-self-center media" data-toggle="collapse" data-target="#divInfraBarraSistemaPadrao" aria-controls="divInfraBarraSistemaPadrao" aria-expanded="false">
              <img id="imgInfraMenuPontosTopo" class=" align-self-center infraImg"  width="24" height="24" src="/infra_css/svg/menu_pontos_topo.svg?2.29.0" tabindex="100" title="Exibir/Ocultar Ações"/>
            </a>

            </div>
          </div>

          <div id="divInfraBarraSistemaPadrao" class="navbar p-0 infraCorBarraSistema  collapse navbar-collapse align-self-center infraBarraSistemaPadrao">
            <div id="divInfraBarraSistemaPadraoE" class="nav-link p-0 pl-3 d-none d-md-flex infraBarraSistemaPadraoE">

              <div class="align-self-center"><img src="svg/sei_barra.svg?4.1.5-2.29.0" title="Sistema Eletrônico de Informações - Versão 4.1.5"/><span class="infraTituloLogoSistema">4.1.5</span></div>
            </div>
            <div id="divInfraBarraSistemaPadraoD" class="navbar-nav  flex-grow-1 justify-content-end infraBarraSistemaPadraoD">
                 <div class="nav-item d-none d-md-flex py-md-0 py-2"><a id="lnkInfraMenuSistema" onclick="infraClicarMenuBootstrap()" href="#" target="_self"  title="Exibir/Ocultar Menu do Sistema" tabindex="51" class="nav-link align-self-center"><span class="font-weight-bold" style="padding:.1rem .5rem;">Menu</span></a></div > <div class="nav-item px-1 media d-flex py-md-0 ">
                 <form class="form-inline align-self-center w-100" id="frmProtocoloPesquisaRapida" method="post" action="controlador.php?acao=protocolo_pesquisa_rapida&infra_sistema=100000100&infra_unidade_atual=110000302&infra_hash=474b1edf022fbc2aa762edd67c5648d77a6ded1b4adaad7a94ef742cd231ddd2">
                  <div class="input-group">
                    <input type="text" id="txtPesquisaRapida" name="txtPesquisaRapida" class="form-control" placeholder="Pesquisar..." style="font-size:.8rem;height:24px;width:190px;border:0;" tabindex="52" />
                    <span class="input-group-btn">
                      <span id="spnInfraUnidade" class="btn infraAcaoBarraConjugada">
                      <img src="svg/pesquisa_rapida.svg?4.1.5-2.29.0" width="20" height="20" onclick="document.getElementById('frmProtocoloPesquisaRapida').submit();" title="Pesquisa Rápida" alt="Pesquisa Rápida" tabindex="53" class="infraImg" />
                      </span>
                    </span>
                  </div>
                 </form>
             </div >
          <div class=" nav-item px-1 d-none d-md-flex  py-md-0 py-2">
                  <div class="input-group align-self-center ">
                  <a id="lnkInfraUnidade" href="#" onclick="window.location.href='controlador.php?acao=infra_trocar_unidade&infra_sistema=100000100&infra_unidade_atual=110000302&infra_hash=d751666c0d3d5193628d302d57dd66d756dd04d66d897324d30cdf9d292b5149';" class="form-control infraAcaoBarraConjugada" title="Centro de Estudos Jurídicos" tabindex="54">CEJ/SAJ/CC/PR</a>

             </div >
          </div>
          <div class="nav-item d-flex infraAcaoBarraSistema">
            <a class="align-self-center  d-none d-md-block" id="lnkControleProcessos" href="#" onclick="window.location.href='controlador.php?acao=procedimento_controlar&reset=1&infra_sistema=100000100&infra_unidade_atual=110000302&infra_hash=00088c6cbae70841355677c0268cc540f47ca51656fefe3c6f83d8e23f96f700'" title="Controle de Processos" tabindex="55">
              <img src="svg/controle_processos_barra.svg?4.1.5-2.29.0" class="infraImg" title="Controle de Processos" />
            </a>

            <span title="Controle de Processos"  class=" nav-link d-flex d-md-none" >
               <img src="svg/controle_processos_barra.svg?4.1.5-2.29.0" class="infraImg" title="Controle de Processos" />
               <a class="align-self-center text-white pl-1"  href="controlador.php?acao=procedimento_controlar&reset=1&infra_sistema=100000100&infra_unidade_atual=110000302&infra_hash=00088c6cbae70841355677c0268cc540f47ca51656fefe3c6f83d8e23f96f700" title="Controle de Processos" tabindex="56" >
                Controle de Processos
               </a>
            </span>
          </div >
          <div class="nav-item d-flex infraAcaoBarraSistema">
            <a class="align-self-center  d-none d-md-block" id="lnkPainelControle" href="#" onclick="window.location.href='controlador.php?acao=painel_controle_visualizar&infra_sistema=100000100&infra_unidade_atual=110000302&infra_hash=ad4fcac398179b8898c413e8764dc36b45c7e8dd8e1afe5d85d15eb3cda0fd02'" title="Painel de Controle" tabindex="57">
              <img src="svg/painel_controle_barra.svg?4.1.5-2.29.0" class="infraImg" title="Painel de Controle" />
            </a>

            <span title="Painel de Controle"  class=" nav-link d-flex d-md-none" >
               <img src="svg/painel_controle_barra.svg?4.1.5-2.29.0" class="infraImg" title="Painel de Controle" />
               <a class="align-self-center text-white pl-1"  href="controlador.php?acao=painel_controle_visualizar&infra_sistema=100000100&infra_unidade_atual=110000302&infra_hash=ad4fcac398179b8898c413e8764dc36b45c7e8dd8e1afe5d85d15eb3cda0fd02" title="Painel de Controle" tabindex="58" >Painel de Controle</a>
            </span>
          </div >
          <div class="nav-item d-flex infraAcaoBarraSistema">

            <a class="align-self-center  d-none d-md-block"  target="_blank" href="controlador.php?acao=novidade_mostrar&mostrar_todas=1&infra_sistema=100000100&infra_unidade_atual=110000302&infra_hash=6187eb9c11a4e6596f1735f99cd838fe554f401cc28583e5c7e0e8dc8f57fa62" title="Novidades" tabindex="59">
              <img src="svg/novidades.svg?4.1.5-2.29.0" class="infraImg" title="Novidades" />
            </a>

            <span title="Novidades"  class=" nav-link   d-flex d-md-none" >
               <img src="svg/novidades.svg?4.1.5-2.29.0" class="infraImg" title="Novidades" />
               <a class="align-self-center text-white pl-1"  target="_blank" href="controlador.php?acao=novidade_mostrar&mostrar_todas=1&infra_sistema=100000100&infra_unidade_atual=110000302&infra_hash=6187eb9c11a4e6596f1735f99cd838fe554f401cc28583e5c7e0e8dc8f57fa62" title="Novidades" tabindex="60">
                Novidades
               </a>
            </span>
         </div >
    <div class="nav-item d-md-flex infraAcaoBarraSistema">
      <a class="align-self-center  d-none d-md-block" id="lnkInfraAcessibilidadeSistema" href="#" onclick="window.location.href='controlador.php?acao=infra_acessibilidade_exibir&infra_sistema=100000100&infra_unidade_atual=110000302&infra_hash=cde5107ef0391706a646feb1204a94d4142514dfa16652cb1340999d53f854db';" title="Acessibilidade"  tabindex="61">
        <img src="/infra_css/svg/acessibilidade_topo.svg?2.29.0" height="24" width="24" class="infraImg" title="Acessibilidade"  />
      </a>
      <span class=" nav-link   d-flex d-md-none" >
         <img src="/infra_css/svg/acessibilidade_topo.svg?2.29.0" height="24" width="24" class="infraImg" title="Acessibilidade"/>
         <a class="align-self-center text-white pl-1" id="lnkInfraAcessibilidadeSistema" href="#" onclick="window.location.href='controlador.php?acao=infra_acessibilidade_exibir&infra_sistema=100000100&infra_unidade_atual=110000302&infra_hash=cde5107ef0391706a646feb1204a94d4142514dfa16652cb1340999d53f854db';" title="Acessibilidade" >Acessibilidade</a>
      </span>
     </div>

    <div class="nav-item d-md-flex infraAcaoBarraSistema">
      <a class="align-self-center  d-none d-md-block" id="lnkInfraConfiguracaoSistema" href="controlador.php?acao=infra_configurar&infra_sistema=100000100&infra_unidade_atual=110000302&infra_hash=4ef7c7a79353e34e55318a336b1945127685a23e3f42ed74fae1a3208190799a" title="Configurações do Sistema"  tabindex="62">
        <img src="/infra_css/svg/configuracao.svg?2.29.0" height="24" width="24" class="infraImg" title="Configurações do Sistema"  />
      </a>
      <span class=" nav-link   d-flex d-md-none" >
         <img src="/infra_css/svg/configuracao.svg?2.29.0" height="24" width="24" class="infraImg" title="Configurações do Sistema"/>
         <a class="align-self-center text-white pl-1" id="lnkInfraConfiguracaoSistema" href="controlador.php?acao=infra_configurar&infra_sistema=100000100&infra_unidade_atual=110000302&infra_hash=4ef7c7a79353e34e55318a336b1945127685a23e3f42ed74fae1a3208190799a" title="Configurações do Sistema" >
          Configurações
         </a>
      </span>
     </div>

      <div class="nav-item d-md-flex infraAcaoBarraSistema">
      <a class="align-self-center  d-none d-md-block" id="lnkUsuarioSistema" href="controlador.php?acao=infra_acesso_usuario_listar&infra_sistema=100000100&infra_unidade_atual=110000302&infra_hash=20acc12c303b5908cbfe805294434c27aca7726e87ffe8c71471c12c4bb91dd0" title="Ricardo Brito do Nascimento (ricardobn/PR)" tabindex="63">
        <img src="/infra_css/svg/usuario_topo.svg?2.29.0" height="24" width="24" class="infraImg"  title="Ricardo Brito do Nascimento (ricardobn/PR)"  />
      </a>
      <span title="Ricardo Brito do Nascimento (ricardobn/PR)"  class=" nav-link   d-flex d-md-none" >
         <img src="/infra_css/svg/usuario_topo.svg?2.29.0" height="24" width="24" class="infraImg"  title="Ricardo Brito do Nascimento (ricardobn/PR)"  />
         <a class="align-self-center text-white pl-1" id="lnkUsuarioSistema" href="controlador.php?acao=infra_acesso_usuario_listar&infra_sistema=100000100&infra_unidade_atual=110000302&infra_hash=20acc12c303b5908cbfe805294434c27aca7726e87ffe8c71471c12c4bb91dd0" title="Ricardo Brito do Nascimento (ricardobn/PR)" >
          Ricardo Brito do Nascimento (ricardobn/PR)
         </a>
      </span>
      </div>

    <div class="nav-item pr-2 media infraAcaoBarraSistema">
    <a class="align-self-center d-none d-md-block" id="lnkInfraSairSistema" href="controlador.php?acao=sair&infra_sistema=100000100&infra_unidade_atual=110000302&infra_hash=25f220a0745a50551438eb0abc07a16e388c5946bc10f5fa21177794c263f06c" title="Sair do Sistema"  tabindex="64">
      <img src="/infra_css/svg/sair.svg?2.29.0" height="24" width="24" class="infraImg"/>
    </a>
    <span class=" nav-link d-flex d-md-none">
      <img src="/infra_css/svg/sair.svg?2.29.0" height="24" width="24"  class="infraImg"/>
       <a id="lnkInfraSairSistema" class="align-self-center text-white pl-1" href="controlador.php?acao=sair&infra_sistema=100000100&infra_unidade_atual=110000302&infra_hash=25f220a0745a50551438eb0abc07a16e388c5946bc10f5fa21177794c263f06c" title="Sair do Sistema" >
        Sair
      </a>
    </span>
    </div>


            </div>
          </div>
        </div>
      </nav>
     <div id="divInfraAreaTela" style="min-height:0;"  class="w-100  flex-grow-1 d-flex flex-row  divInfraAreaTela">
<div id="divInfraAreaTelaE" class=" divInfraAreaTelaE d-flex flex-column  infraAreaTelaEExibeGrande infraAreaTelaEEscondePequeno  " >
<div id="divInfraSidebarMenu" class="infraSidebarMenu flex-grow-1"><div id="divInfraPesquisarMenu"><input type="text" autocomplete="off" id="txtInfraPesquisarMenu" class="infraPesquisarMenu infraText" onkeyup="infraFiltrarMenuBootstrap()" placeholder="Pesquisar no Menu" title="Pesquisar no Menu"/></div><ul id="infraMenu">
<li><a id="linkMenu0" style="padding-left:5px" link="acompanhamento_listar" href="controlador.php?acao=acompanhamento_listar&infra_item_menu=0&infra_sistema=100000100&infra_unidade_atual=110000302&infra_hash=e67c7a685fdb4bf31770f2979593411d115d1735a19b48a5803aed2934d6eb5f"><img src="menu/acompanhamento_especial.svg?4.1.5-2.29.0" width="24" height="24"/><span>Acompanhamento Especial</span></a></li>
<li><a id="linkMenu1" style="padding-left:5px" link="base_conhecimento_pesquisar" href="controlador.php?acao=base_conhecimento_pesquisar&infra_item_menu=1&infra_sistema=100000100&infra_unidade_atual=110000302&infra_hash=f66535ccdaefbe6faa359102a118b259f87a9b7cc5500b4b673e94bb585d9832"><img src="menu/base_conhecimento.svg?4.1.5-2.29.0" width="24" height="24"/><span>Base de Conhecimento</span></a></li>
<li><a id="linkMenu2" style="padding-left:5px" data-toggle="collapse" class="infraAnchorMenu" href="#submenu2" role="button" aria-expanded="false" aria-controls="collapseMenu"><img src="menu/blocos.svg?4.1.5-2.29.0" width="24" height="24"/><span>Blocos</span><img src="/infra_css/imagens/menu_seta.png" class="infraImgSetaMenu" style="width:12px;"/></a>
<ul class="collapse" id="submenu2">
<li><a id="linkMenu3" style="padding-left:35px" link="bloco_assinatura_listar" href="controlador.php?acao=bloco_assinatura_listar&infra_item_menu=3&infra_sistema=100000100&infra_unidade_atual=110000302&infra_hash=3f74ec11f47466b4ba9bc5be95d82074d7e0054ec86b9f866c15d2d4cb71ff24"><span>Assinatura</span></a></li>
<li><a id="linkMenu4" style="padding-left:35px" link="bloco_interno_listar" href="controlador.php?acao=bloco_interno_listar&infra_item_menu=4&infra_sistema=100000100&infra_unidade_atual=110000302&infra_hash=fc9f07054275976caa29b10620fdd601121b1ae0836196bc18bab116412c09ea"><span>Internos</span></a></li>
<li><a id="linkMenu5" style="padding-left:35px" link="bloco_reuniao_listar" href="controlador.php?acao=bloco_reuniao_listar&infra_item_menu=5&infra_sistema=100000100&infra_unidade_atual=110000302&infra_hash=a9f12c6c1debdd4c28d0ea410972add2fc8d33d77c9a0f566f14808cc5aca79f"><span>Reunião</span></a></li>
</ul>
</li>
<li><a id="linkMenu6" style="padding-left:5px" link="contato_listar" href="controlador.php?acao=contato_listar&infra_item_menu=6&infra_sistema=100000100&infra_unidade_atual=110000302&infra_hash=07e731ed8cdd7efe2953753228328ed193122d8fb2f71347241b1a810f00fae9"><img src="menu/contatos.svg?4.1.5-2.29.0" width="24" height="24"/><span>Contatos</span></a></li>
<li><a id="linkMenu7" style="padding-left:5px" link="controle_prazo_listar" href="controlador.php?acao=controle_prazo_listar&infra_item_menu=7&infra_sistema=100000100&infra_unidade_atual=110000302&infra_hash=f7c8b90dc980d2dbcc280f16c030c5681de90d62e0d6a66afecbd30e0dca04aa"><img src="menu/controle_prazo.svg?4.1.5-2.29.0" width="24" height="24"/><span>Controle de Prazos</span></a></li>
<li><a id="linkMenu8" style="padding-left:5px" link="procedimento_controlar" href="controlador.php?acao=procedimento_controlar&reset=1&infra_item_menu=8&infra_sistema=100000100&infra_unidade_atual=110000302&infra_hash=68955fd59499098172faf8a3d195cda3ee4b1f406230231844ab564e1add807c"><img src="menu/controle_processos.svg?4.1.5-2.29.0" width="24" height="24"/><span>Controle de Processos</span></a></li>
<li><a id="linkMenu9" style="padding-left:5px" data-toggle="collapse" class="infraAnchorMenu" href="#submenu9" role="button" aria-expanded="false" aria-controls="collapseMenu"><img src="menu/estatisticas.svg?4.1.5-2.29.0" width="24" height="24"/><span>Estatísticas</span><img src="/infra_css/imagens/menu_seta.png" class="infraImgSetaMenu" style="width:12px;"/></a>
<ul class="collapse" id="submenu9">
<li><a id="linkMenu10" style="padding-left:35px" link="gerar_estatisticas_unidade" href="controlador.php?acao=gerar_estatisticas_unidade&infra_item_menu=10&infra_sistema=100000100&infra_unidade_atual=110000302&infra_hash=3fdccd8a8f5cb35b7a183b63ff1771f1cdaddc09b0e9a36598b9b3e91ef68a0e"><span>Unidade</span></a></li>
<li><a id="linkMenu11" style="padding-left:35px" link="gerar_estatisticas_desempenho_processos" href="controlador.php?acao=gerar_estatisticas_desempenho_processos&infra_item_menu=11&infra_sistema=100000100&infra_unidade_atual=110000302&infra_hash=526f4feabf1cf997ee39acc48b35d9377d7158a7ab5f3f8c591569f41a6b5a43"><span>Desempenho de Processos</span></a></li>
</ul>
</li>
<li><a id="linkMenu12" style="padding-left:5px" link="protocolo_modelo_listar" href="controlador.php?acao=protocolo_modelo_listar&infra_item_menu=12&infra_sistema=100000100&infra_unidade_atual=110000302&infra_hash=8e1306a1fa96e61e7e487b774005aa57de2ed54a19febf601a11c0b6e8090d93"><img src="menu/favoritos.svg?4.1.5-2.29.0" width="24" height="24"/><span>Favoritos</span></a></li>
<li><a id="linkMenu13" style="padding-left:5px" data-toggle="collapse" class="infraAnchorMenu" href="#submenu13" role="button" aria-expanded="false" aria-controls="collapseMenu"><img src="menu/grupos.svg?4.1.5-2.29.0" width="24" height="24"/><span>Grupos</span><img src="/infra_css/imagens/menu_seta.png" class="infraImgSetaMenu" style="width:12px;"/></a>
<ul class="collapse" id="submenu13">
<li><a id="linkMenu14" style="padding-left:35px" link="grupo_contato_listar" href="controlador.php?acao=grupo_contato_listar&infra_item_menu=14&infra_sistema=100000100&infra_unidade_atual=110000302&infra_hash=6a2003cc7a387a371548b657f3315fd63c8e00591485ea3ee7b4d1525de8c309"><span>Contatos</span></a></li>
<li><a id="linkMenu15" style="padding-left:35px" link="grupo_email_listar" href="controlador.php?acao=grupo_email_listar&infra_item_menu=15&infra_sistema=100000100&infra_unidade_atual=110000302&infra_hash=5398b4854ece5da3d39ae139081a5170e48535a253d5fe33fcd9639046e3fae5"><span>E-Mail</span></a></li>
<li><a id="linkMenu16" style="padding-left:35px" link="grupo_unidade_listar" href="controlador.php?acao=grupo_unidade_listar&infra_item_menu=16&infra_sistema=100000100&infra_unidade_atual=110000302&infra_hash=833dd4943fd6905fef66138f5f76787ab32c9d91c8953016c10a32f15862b903"><span>Envio</span></a></li>
</ul>
</li>
<li><a id="linkMenu17" style="padding-left:5px" link="procedimento_escolher_tipo" href="controlador.php?acao=procedimento_escolher_tipo&infra_item_menu=17&infra_sistema=100000100&infra_unidade_atual=110000302&infra_hash=6db4461903881dc99f9fa9acde44d1620a7ac0f1126d22ce2a78ea7879e63ead"><img src="menu/iniciar_processo.svg?4.1.5-2.29.0" width="24" height="24"/><span>Iniciar Processo</span></a></li>
<li><a id="linkMenu18" style="padding-left:5px" link="marcador_listar" href="controlador.php?acao=marcador_listar&infra_item_menu=18&infra_sistema=100000100&infra_unidade_atual=110000302&infra_hash=8723329911572e8d84756161a7ecd1f5e121b0593bb3093e9314f3186723e750"><img src="menu/marcadores.svg?4.1.5-2.29.0" width="24" height="24"/><span>Marcadores</span></a></li>
<li><a id="linkMenu19" style="padding-left:5px" link="painel_controle_visualizar" href="controlador.php?acao=painel_controle_visualizar&infra_item_menu=19&infra_sistema=100000100&infra_unidade_atual=110000302&infra_hash=ba79c5bb8bf51c247a63f412f1c433d1c273afcbd8bd0c4fae62d1d8092cd822"><img src="menu/painel_controle.svg?4.1.5-2.29.0" width="24" height="24"/><span>Painel de Controle</span></a></li>
<li><a id="linkMenu20" style="padding-left:5px" link="protocolo_pesquisar" href="controlador.php?acao=protocolo_pesquisar&infra_item_menu=20&infra_sistema=100000100&infra_unidade_atual=110000302&infra_hash=429ae7a6953b6499e92321b4cecd18afc010d72a7d5ae75814cb778a95c95df9"><img src="menu/pesquisa.svg?4.1.5-2.29.0" width="24" height="24"/><span>Pesquisa</span></a></li>
<li><a id="linkMenu21" style="padding-left:5px" link="controle_unidade_gerar" href="controlador.php?acao=controle_unidade_gerar&infra_item_menu=21&infra_sistema=100000100&infra_unidade_atual=110000302&infra_hash=0a629f10c1ca968884a2fc19307d3c5baa954b1a1943d7d6ef3874764d9c30a7"><img src="menu/pontos_controle.svg?4.1.5-2.29.0" width="24" height="24"/><span>Pontos de Controle</span></a></li>
<li><a id="linkMenu22" style="padding-left:5px" link="procedimento_sobrestado_listar" href="controlador.php?acao=procedimento_sobrestado_listar&infra_item_menu=22&infra_sistema=100000100&infra_unidade_atual=110000302&infra_hash=e342daebb7c105311eaf9af193cb6808950f4b5c1ce83355d2f47098cb38191a"><img src="menu/processos_sobrestados.svg?4.1.5-2.29.0" width="24" height="24"/><span>Processos Sobrestados</span></a></li>
<li><a id="linkMenu23" style="padding-left:5px" link="reabertura_programada_listar" href="controlador.php?acao=reabertura_programada_listar&infra_item_menu=23&infra_sistema=100000100&infra_unidade_atual=110000302&infra_hash=367b13508fa13dd1dc6a42e6cb804c1075181d31fa551dd8f336ead71903b7ff"><img src="menu/reabertura_programada.svg?4.1.5-2.29.0" width="24" height="24"/><span>Reabertura Programada</span></a></li>
<li><a id="linkMenu24" style="padding-left:5px" data-toggle="collapse" class="infraAnchorMenu" href="#submenu24" role="button" aria-expanded="false" aria-controls="collapseMenu"><img src="menu/relatorios.svg?4.1.5-2.29.0" width="24" height="24"/><span>Relatórios</span><img src="/infra_css/imagens/menu_seta.png" class="infraImgSetaMenu" style="width:12px;"/></a>
<ul class="collapse" id="submenu24">
<li><a id="linkMenu25" style="padding-left:35px" link="atividade_unidade_pesquisar" href="controlador.php?acao=atividade_unidade_pesquisar&infra_item_menu=25&infra_sistema=100000100&infra_unidade_atual=110000302&infra_hash=39ef0a4622a219bae5d17e86a2c40627118f00c72d9a1e6db1d35f30e35f22cb"><span>Atividade na Unidade</span></a></li>
<li><a id="linkMenu26" style="padding-left:35px" link="md_pet_adm_vinc_consultar" href="controlador.php?acao=md_pet_adm_vinc_consultar&infra_item_menu=26&infra_sistema=100000100&infra_unidade_atual=110000302&infra_hash=8582f865f459c7b8fdfa661cdf2c65cc9f613715dbed473562d467b3d7d8bd55"><span>Vinculações e Procurações Eletrônicas</span></a></li>
<li><a id="linkMenu27" style="padding-left:35px" link="md_pet_int_relatorio_listar" href="controlador.php?acao=md_pet_int_relatorio_listar&infra_item_menu=27&infra_sistema=100000100&infra_unidade_atual=110000302&infra_hash=c6c3226ce141c11501cbb6939754df45b460d75343c111b26b3b3ebd0bb3d716"><span>Intimações Eletrônicas</span></a></li>
<li><a id="linkMenu28" style="padding-left:35px" data-toggle="collapse" class="infraAnchorMenu" href="#submenu28" role="button" aria-expanded="false" aria-controls="collapseMenu"><span>Processos Litigiosos</span><img src="/infra_css/imagens/menu_seta.png" class="infraImgSetaMenu" style="width:12px;"/></a>
<ul class="collapse" id="submenu28">
<li><a id="linkMenu29" style="padding-left:50px" link="md_lit_relatorio_antecedente" href="controlador.php?acao=md_lit_relatorio_antecedente&infra_item_menu=29&infra_sistema=100000100&infra_unidade_atual=110000302&infra_hash=866fbc86f563df421d3d9155a484c6cc0702084beb5887d17b69e9fc8fde6666"><span>Antecendentes</span></a></li>
<li><a id="linkMenu30" style="padding-left:50px" link="md_lit_relatorio_reincidencia" href="controlador.php?acao=md_lit_relatorio_reincidencia&infra_item_menu=30&infra_sistema=100000100&infra_unidade_atual=110000302&infra_hash=6e8b070d4affce6df9e238d1b6644a50d1c3048d24555fb1e42d825d2cb4919c"><span>Reincidências Específicas</span></a></li>
</ul>
</li>
</ul>
</li>
<li><a id="linkMenu31" style="padding-left:5px" link="retorno_programado_listar" href="controlador.php?acao=retorno_programado_listar&infra_item_menu=31&infra_sistema=100000100&infra_unidade_atual=110000302&infra_hash=f7031fe057c5d4b812bccac61f03e5a22587a094de7b149312bd003b8ec487d4"><img src="menu/retorno_programado.svg?4.1.5-2.29.0" width="24" height="24"/><span>Retorno Programado</span></a></li>
<li><a id="linkMenu32" style="padding-left:5px" link="texto_padrao_interno_listar" href="controlador.php?acao=texto_padrao_interno_listar&infra_item_menu=32&infra_sistema=100000100&infra_unidade_atual=110000302&infra_hash=ea36ab1b66a8dee3cdb49e100eaeddd3bc5220cb58739891498b80f16abc9c84"><img src="menu/texto_padrao.svg?4.1.5-2.29.0" width="24" height="24"/><span>Textos Padrão</span></a></li>
<li><a id="linkMenu33" style="padding-left:5px" link="pen_procedimento_expedido_listar" title="Blocos de Trâmite Externo" data-toggle="collapse" class="infraAnchorMenu" href="#submenu33" role="button" aria-expanded="false" aria-controls="collapseMenu"><img src="modulos/pen/imagens/menu//pen_tramite_externo_lote.svg?4.1.5-2.29.0" width="24" height="24"/><span>Tramita GOV.BR</span><img src="/infra_css/imagens/menu_seta.png" class="infraImgSetaMenu" style="width:12px;"/></a>
<ul class="collapse" id="submenu33">
<li><a id="linkMenu34" style="padding-left:35px" link="md_pen_tramita_em_bloco" href="controlador.php?acao=md_pen_tramita_em_bloco&infra_item_menu=34&infra_sistema=100000100&infra_unidade_atual=110000302&infra_hash=84eebe376114b3d18d80ac7ff8dae6e4e9cdc56a6b319171f13d5ac9100f0ee9"><span>Blocos de Trâmite Externo</span></a></li>
<li><a id="linkMenu35" style="padding-left:35px" link="pen_procedimento_expedido_listar" href="controlador.php?acao=pen_procedimento_expedido_listar&infra_item_menu=35&infra_sistema=100000100&infra_unidade_atual=110000302&infra_hash=80d20b605dc855ac89a677f05d43eba528153b4c07dcc78cc76031343ded42bd"><span>Processos em Tramitação Externa</span></a></li>
</ul>
</li>
</ul>
</div>
<script type="text/javascript">infraSetarMenuBootstrap("procedimento_controlar")</script><!--LOGO--><script>document.querySelector("div.infraSidebarMenu").style.overflowY = "visible";</script><div style="font-size: 12px; text-align: center; background-color: #f5f6f7"><div style="height: 12px; margin-bottom: 22px; background-color: var(--color-primary-default);"></div><p style="text-align: left; margin: 15px 5px 5px 5px;"><strong style="font-weight: bolder">Abra o aplicativo do SEI! e faça a leitura do código abaixo para sincronizá-lo com sua conta.</strong></p><img style="margin: 20px auto 6px;" align="center" src="data:image/png;base64, iVBORw0KGgoAAAANSUhEUgAAAFYAAABWAQMAAABvmPO0AAAABlBMVEX///8AAABVwtN+AAAACXBIWXMAAA7EAAAOxAGVKw4bAAABUElEQVQ4jXXTQWoFMQgGYMFtwKsI2Qa8uuA2kKsE3ArW15b2OaVhmPlWifF3AP5ZkiP4XvG8zYyLnNedwM3TccxUc3laXGws++OxVN394dozE+f53v/HkvNrfdbza4ABulnvZ9W/Fo9zjPbY2kzr2oxdpdzmSXgdhpNqMw0zFANmbn59zE8M0uY6BXPfzKqtOckHzy0TmqeickytWprZ1hkmEUebcclZviWdm4k2xazntf+bK4ktYter5nfLAWOUrQbNFHVc5PDLzViXCRCd1dzmCNZ10VY3+JHNOYZ1rzCFqxUdN0u9HNepqJsBDHUpnuDmmkmu0YiF3ZU+Xb/k3j1nJOGo7kIzV6ZMxrYfJsxhKZndVd1ecWcNfbMkUwht527GsbJOuq9M3zx91pBJhacPr2V3Cyg/jSkQWD1/d+XGKtOq8831j8hGCXJo/md9AA+MoDIfjdYaAAAAAElFTkSuQmCC" /></div></div>
<div id="divInfraAreaTelaD"  class=" flex-grow-1 px-3" >
<div id="divInfraBarraLocalizacao" class="infraBarraLocalizacao" tabindex="450">Controle de Processos</div>


<form id="frmProcedimentoControlar" class="h-100" method="post" action="controlador.php?acao=procedimento_controlar&acao_origem=procedimento_controlar&tipo_filtro=&infra_sistema=100000100&infra_unidade_atual=110000302&infra_hash=2467d741470dd362e2a36ff90c1330c505c666270c84db919acd883e0e343ea3">
  <div id="divControleProcessosConteudo"   class="h-100  d-flex flex-column">

    <div  class="barraBotoesSEIMovel">
        <a class="btn d-md-none" data-toggle="collapse" href="#collapseControle" role="button" aria-expanded="true" aria-controls="collapseControle" title="Exibir/Ocultar Ícones" tabindex="451">
          <img src="/infra_css/svg/menu_pontos.svg" width="32" height="32" />
        </a>
    </div>

    <div class="collapse d-md-block" id="collapseControle">
        <div id="divBotoesControleProcessos" class="barraBotoesSEI">
          <a href="#" onclick="return acaoControleProcessos('controlador.php?acao=procedimento_enviar&acao_origem=procedimento_controlar&acao_retorno=procedimento_controlar&infra_sistema=100000100&infra_unidade_atual=110000302&infra_hash=b7f519acfab8d5de3c7cee9144e8c3b7d1ee22ea35667c72e1aca0469995f1e8', true, false);" tabindex="452" ><img src="svg/processo_enviar.svg?18" alt="Enviar Processo" title="Enviar Processo"/></a>
<a href="#" onclick="return acaoControleProcessos('controlador.php?acao=procedimento_atualizar_andamento&acao_origem=procedimento_controlar&acao_retorno=procedimento_controlar&infra_sistema=100000100&infra_unidade_atual=110000302&infra_hash=7f8ef9f48a8c99cd2ff6fb318a2699061efa077a76b293346dd27adaea02ad36', true, true);" tabindex="452" ><img src="svg/processo_atualizar_andamento.svg?18" alt="Atualizar Andamento" title="Atualizar Andamento"/></a>
<a href="#" onclick="return acaoControleProcessos('controlador.php?acao=procedimento_atribuicao_cadastrar&acao_origem=procedimento_controlar&acao_retorno=procedimento_controlar&infra_sistema=100000100&infra_unidade_atual=110000302&infra_hash=925773e9f69fc6eefa56cba4802a786baa4e44f662ad0bac03c55009fc944761', true, false);" tabindex="452" ><img src="svg/processo_atribuir.svg?18"  alt="Atribuição de Processos" title="Atribuição de Processos"/></a>
<a href="#" onclick="return acaoBlocoProcessar();" tabindex="452" ><img src="svg/bloco_incluir_protocolo.svg?18"  alt="Incluir em Bloco" title="Incluir em Bloco"/></a>
<a href="#" onclick="return acaoControleProcessos('controlador.php?acao=procedimento_sobrestar&acao_origem=procedimento_controlar&acao_retorno=procedimento_controlar&infra_sistema=100000100&infra_unidade_atual=110000302&infra_hash=987acd71cfd0cea788577d721095d37ca3243fb9a6459af0eeedd017ab119e1c', true, false);" tabindex="452" ><img src="svg/processo_sobrestar.svg?18"  alt="Sobrestar Processo" title="Sobrestar Processo"/></a>
<a href="#" onclick="return acaoControleProcessos('controlador.php?acao=procedimento_concluir&acao_origem=procedimento_controlar&acao_retorno=procedimento_controlar&infra_sistema=100000100&infra_unidade_atual=110000302&infra_hash=ed1b39d17e4c456e0688650648a0b28d71a2f3d6c02b12bf693d1c4832ae1545', true, true);" tabindex="452" ><img src="svg/processo_concluir.svg?18"  alt="Concluir Processo nesta Unidade" title="Concluir Processo nesta Unidade"/></a>
<a href="#" onclick="return acaoControleProcessos('controlador.php?acao=anotacao_registrar&acao_origem=procedimento_controlar&acao_retorno=procedimento_controlar&infra_sistema=100000100&infra_unidade_atual=110000302&infra_hash=a823daac01ffc1051f979b3b4ced84978949715f2e59c3408219ce9915aae963', true, true);" tabindex="452" ><img src="svg/anotacao_cadastro.svg?18"  alt="Anotações" title="Anotações"/></a>
<a href="#" onclick="return acaoControleProcessos('controlador.php?acao=acompanhamento_cadastrar&acao_origem=procedimento_controlar&acao_retorno=procedimento_controlar&infra_sistema=100000100&infra_unidade_atual=110000302&infra_hash=32b659a700c41cea279219f49a3a8d0446be990d37b1a1cee842f9f0f3a9f2f4', true, true);" tabindex="452" ><img src="svg/acompanhamento_especial_cadastro.svg?18"  alt="Acompanhamento Especial" title="Acompanhamento Especial"/></a>
<a href="#" onclick="return acaoControleProcessos('controlador.php?acao=documento_gerar_multiplo&acao_origem=procedimento_controlar&acao_retorno=procedimento_controlar&infra_sistema=100000100&infra_unidade_atual=110000302&infra_hash=24e0c9c265571c37bf8881f20e28623bb8d211036d8d45801ac05f8264c6485e', true, true);" tabindex="452" ><img src="svg/documento_incluir.svg?18"  alt="Incluir Documento" title="Incluir Documento"/></a>
<a href="#" onclick="return acaoControleProcessos('controlador.php?acao=andamento_situacao_gerenciar&acao_origem=procedimento_controlar&acao_retorno=procedimento_controlar&infra_sistema=100000100&infra_unidade_atual=110000302&infra_hash=b64236d85a07142b7aebc8590e04b198bbfbe95a470bfdd902cac595fe7a1150', true, false);" tabindex="452" ><img src="svg/situacao_gerenciar.svg?18"  alt="Gerenciar Ponto de Controle" title="Gerenciar Ponto de Controle"/></a>
<a href="#" onclick="return acaoControleProcessos('controlador.php?acao=andamento_marcador_cadastrar&acao_origem=procedimento_controlar&acao_retorno=procedimento_controlar&infra_sistema=100000100&infra_unidade_atual=110000302&infra_hash=83eafe0f130822a52895e900ecb16413abf58fddbcc0d02002e8c1505d438767', true, true);" tabindex="452" ><img src="svg/marcador_adicionar.svg?18"  alt="Adicionar Marcador" title="Adicionar Marcador"/></a>
<a href="#" onclick="return acaoRemoverMarcadorProcessar('controlador.php?acao=andamento_marcador_remover&acao_origem=procedimento_controlar&acao_retorno=procedimento_controlar&infra_sistema=100000100&infra_unidade_atual=110000302&infra_hash=e105722893f9089f1b72f4116db646bf3144ad1ce50b72d96761703aff5ef3cb', true, true);" tabindex="452" ><img src="svg/marcador_remover.svg?18"  alt="Remover Marcador" title="Remover Marcador"/></a>
<a href="#" onclick="return acaoControleProcessos('controlador.php?acao=controle_prazo_definir&acao_origem=procedimento_controlar&acao_retorno=procedimento_controlar&infra_sistema=100000100&infra_unidade_atual=110000302&infra_hash=31097fc4978033c13a3c45a4d3311c31b79c837f721bea21456c92a9a6b06670', true, true);" tabindex="452" ><img src="svg/controle_prazo_gerenciar.svg?18"  alt="Controle de Prazos" title="Controle de Prazos"/></a>
        </div>
    </div>

    <div id="divFiltro" class="row justify-content-center justify-content-md-start">

<div class=" col-6 p-1 col-md-auto mr-md-3 "><a id="lnkVisualizacaoDetalhada" href="javascript:void(0);" onclick="trocarVisualizacao('D');" class="ancoraPadraoPreta p-0" tabindex="453">Visualização detalhada</a></div>

<div class=" col-6 p-1 col-md-auto mr-md-3  "><a id="lnkAtribuidosMim" href="javascript:void(0);" onclick="verMeusProcessos('M');" class="ancoraPadraoPreta p-0" tabindex="454">Ver atribuídos a mim</a></div>

<div class=" col-6 p-1 col-md-auto mr-md-3 "><a href="controlador.php?acao=procedimento_controlar&acao_origem=procedimento_controlar&tipo_filtro=M&infra_sistema=100000100&infra_unidade_atual=110000302&infra_hash=3281a16f7d913b167e1b367b3e1059db27f0d16fd6150aaf7436b36a4e237eea" class="ancoraPadraoPreta p-0" tabindex="455">Ver por marcadores</a></div>

<div class=" col-6 p-1 col-md-auto mr-md-3  "><a href="controlador.php?acao=procedimento_controlar&acao_origem=procedimento_controlar&tipo_filtro=P&infra_sistema=100000100&infra_unidade_atual=110000302&infra_hash=5efad74186f11b0a85273febee3a17deee01fe08b4c4d96265753b6eb36b2bc1" class="ancoraPadraoPreta p-0" tabindex="456">Ver por tipo</a></div>

<div class=" col-6 p-1 col-md-auto mr-md-3  "><a href="controlador.php?acao=procedimento_controlar&acao_origem=procedimento_controlar&tipo_filtro=R&infra_sistema=100000100&infra_unidade_atual=110000302&infra_hash=758fb64d4a1d1ed503e3a0753f3721d0121b966959aeb22d3a59dc8a8f1813f9" class="ancoraPadraoPreta p-0" tabindex="457">Ver por prioridade</a></div>
    </div>
    <div style="overflow-y: auto;min-height: 200px;margin-top:5px;" class="flex-grow-1 row mx-0 mb-0  d-flex divTabelaProcesso" id="divTabelaProcesso">
        <div class="d-flex justify-content-center w-100 d-md-none" style="height: 25px;">
                <a class="ml-0 mt-1 pl-0 ancoraPadraoAzul   d-md-none mx-auto"  href="#" onclick="alterarVisualizacaoTabela('hdnExibirRecebidos','true','hdnExibirGerados')" tabindex="1003" >
                  Processos Recebidos
                </a>
                 <a class="ml-0 mt-1 pl-0 ancoraPadraoAzul  d-md-none mx-auto" href="#" onclick="alterarVisualizacaoTabela('hdnExibirGerados','true','hdnExibirRecebidos')"  tabindex="1004" >
                    Processos Gerados
                </a>
        </div>     <div id="divRecebidos" class="ml-0  pl-0 d-none  d-md-block  col-12 col-md-6">
<div id="divRecebidosAreaPaginacaoSuperior" class="infraAreaPaginacao">
</div>
<div id="divRecebidosAreaTabela" class="infraAreaTabela" >
<table id="tblProcessosRecebidos" width="100%" border="0" cellspacing="0" cellpadding="1" class="infraTable tabelaControle" summary="Tabela de Processos Recebidos." tabindex="1001">
<caption class="infraCaption">Processos recebidos (15 registros):</caption><tr><th class="infraTh" width="5%"><a href="javascript:void(0);" id="lnkInfraCheck" onclick="infraSelecaoMultipla('Recebidos');" tabindex="1001"><img src="/infra_css/svg/check.svg" id="imgRecebidosCheck" title="Selecionar Tudo" alt="Selecionar Tudo" class="infraImg"/></a></th>
<th class="infraTh" colspan="3">Recebidos</th>
</tr>
<tr id="P7106570" class="infraTrClara">
<td><a id="lnkRecebidosID-7106570" name="ID-7106570"></a><input class="infraCheckbox" id="chkRecebidosItem0" name="chkRecebidosItem0" tabindex="1001" title="00001.006805/2025-13" type="checkbox" value="7106570" aria-label="Não recebido / Tipo Envio de Informações / Especificação Normas legais pendentes de regulamentação (Ref: Ofício nº 1646/2025/CC/PR)" onclick="infraSelecionarItens(this,'Recebidos');"/></td>
<td width="20%"><img src='modulos/peticionamento/imagens/svg/peticionamento_processo_novo.svg?18' onmouseout='return infraTooltipOcultar();' onmouseover='return infraTooltipMostrar("Processo Novo: 16/10/2025","Peticionamento Eletrônico");' style='width:24px;'  /></td>
<td><a class="processoNaoVisualizado" href="controlador.php?acao=procedimento_trabalhar&acao_origem=procedimento_controlar&acao_retorno=procedimento_controlar&id_procedimento=7106570&infra_sistema=100000100&infra_unidade_atual=110000302&infra_hash=d2cd237e44c155d41b0e47cb613a5c8fbf252ff56b4da92572b54b33055abbe9" aria-label="Envio de Informações / Normas legais pendentes de regulamentação (Ref: Ofício nº 1646/2025/CC/PR)" onmouseover="return infraTooltipMostrar('Normas legais pendentes de regulamentação (Ref: Ofício nº 1646/2025/CC/PR)','Envio de Informações');" onmouseout="return infraTooltipOcultar();" tabindex="1001">00001.<wbr>006805/2025-13</a></td>
<td width="10%">&nbsp;</td>
</tr>
<tr id="P6779498" class="infraTrClara">
<td><a id="lnkRecebidosID-6779498" name="ID-6779498"></a><input class="infraCheckbox" id="chkRecebidosItem1" name="chkRecebidosItem1" tabindex="1001" title="00025.001307/2025-14" type="checkbox" value="6779498" aria-label="Tipo Pedidos e informações diversas - Outros / Especificação Alojamento Programa de Intercâmbio SAJ 2025" onclick="infraSelecionarItens(this,'Recebidos');"/></td>
<td width="20%"><img src='modulos/peticionamento/imagens/svg/peticionamento_intercorrente.svg?18' onmouseout='return infraTooltipOcultar();' onmouseover='return infraTooltipMostrar("Intercorrente: 15/10/2025","Peticionamento Eletrônico");' style='width:24px;' /></td>
<td><a class="processoVisualizado" href="controlador.php?acao=procedimento_trabalhar&acao_origem=procedimento_controlar&acao_retorno=procedimento_controlar&id_procedimento=6779498&infra_sistema=100000100&infra_unidade_atual=110000302&infra_hash=9e9e33f7a853f07b6a1836ddbdc2be84fc0bbdbda0bf55a4cec23f06b9b1de0c" aria-label="Pedidos e informações diversas - Outros / Alojamento Programa de Intercâmbio SAJ 2025" onmouseover="return infraTooltipMostrar('Alojamento Programa de Intercâmbio SAJ 2025','Pedidos e informações diversas - Outros');" onmouseout="return infraTooltipOcultar();" tabindex="1001">00025.<wbr>001307/2025-14</a></td>
<td width="10%">(<a href="controlador.php?acao=procedimento_atribuicao_listar&acao_retorno=procedimento_controlar&id_usuario_atribuicao=100014422&id_procedimento=6779498&infra_sistema=100000100&infra_unidade_atual=110000302&infra_hash=9ca29d678f76e6517a54d40ca06a0a2dd2769ec73b28bacc7927a10960cd46cf" title="Atribuído para Emerson Nogueira Santana" class="ancoraSigla" tabindex="1001">emerson.santana</a>)</td>
</tr>
<tr id="P7093872" class="infraTrClara">
<td><a id="lnkRecebidosID-7093872" name="ID-7093872"></a><input class="infraCheckbox" id="chkRecebidosItem2" name="chkRecebidosItem2" tabindex="1001" title="00001.006667/2025-72" type="checkbox" value="7093872" aria-label="Tipo Envio de Informações / Especificação OFÍCIO SEI Nº 6266/2025/MPO - Normas legais pendentes de regulamentação. Processo SEI/PR nº 00025.00" onclick="infraSelecionarItens(this,'Recebidos');"/></td>
<td width="20%"><img src='modulos/peticionamento/imagens/svg/peticionamento_processo_novo.svg?18' onmouseout='return infraTooltipOcultar();' onmouseover='return infraTooltipMostrar("Processo Novo: 10/10/2025","Peticionamento Eletrônico");' style='width:24px;'  /></td>
<td><a class="processoVisualizado" href="controlador.php?acao=procedimento_trabalhar&acao_origem=procedimento_controlar&acao_retorno=procedimento_controlar&id_procedimento=7093872&infra_sistema=100000100&infra_unidade_atual=110000302&infra_hash=e03e8ae71d639c0cd298225d627264e902bafd8ecae46102ff8586001f0ee8e2" aria-label="Envio de Informações / OFÍCIO SEI Nº 6266/2025/MPO - Normas legais pendentes de regulamentação. Processo SEI/PR nº 00025.00" onmouseover="return infraTooltipMostrar('OFÍCIO SEI Nº 6266/2025/MPO - Normas legais pendentes de regulamentação. Processo SEI/PR nº 00025.00','Envio de Informações');" onmouseout="return infraTooltipOcultar();" tabindex="1001">00001.<wbr>006667/2025-72</a></td>
<td width="10%">&nbsp;</td>
</tr>
<tr id="P7096637" class="infraTrClara">
<td><a id="lnkRecebidosID-7096637" name="ID-7096637"></a><input class="infraCheckbox" id="chkRecebidosItem3" name="chkRecebidosItem3" tabindex="1001" title="00001.006711/2025-44" type="checkbox" value="7096637" aria-label="Tipo Documentos para a Casa Civil da Presidência da República / Especificação Normas legais pendentes de regulamentação." onclick="infraSelecionarItens(this,'Recebidos');"/></td>
<td width="20%"><img src='modulos/peticionamento/imagens/svg/peticionamento_processo_novo.svg?18' onmouseout='return infraTooltipOcultar();' onmouseover='return infraTooltipMostrar("Processo Novo: 13/10/2025","Peticionamento Eletrônico");' style='width:24px;'  /></td>
<td><a class="processoVisualizado" href="controlador.php?acao=procedimento_trabalhar&acao_origem=procedimento_controlar&acao_retorno=procedimento_controlar&id_procedimento=7096637&infra_sistema=100000100&infra_unidade_atual=110000302&infra_hash=c5a5f8f1092e6331d0c5d2525e18803d8c22ae7cd1387c92f3edda6f617cff33" aria-label="Documentos para a Casa Civil da Presidência da República / Normas legais pendentes de regulamentação." onmouseover="return infraTooltipMostrar('Normas legais pendentes de regulamentação.','Documentos para a Casa Civil da Presidência da República');" onmouseout="return infraTooltipOcultar();" tabindex="1001">00001.<wbr>006711/2025-44</a></td>
<td width="10%">&nbsp;</td>
</tr>
<tr id="P7045049" class="infraTrClara">
<td><a id="lnkRecebidosID-7045049" name="ID-7045049"></a><input class="infraCheckbox" id="chkRecebidosItem4" name="chkRecebidosItem4" tabindex="1001" title="00063.002635/2025-73" type="checkbox" value="7045049" aria-label="Tipo GPPR - Poder Judiciário / Especificação Referência: Medida Cautelar Na Ação Direta De Inconstitucionalidade 7236" onclick="infraSelecionarItens(this,'Recebidos');"/></td>
<td width="20%"></td>
<td><a class="processoVisualizado" href="controlador.php?acao=procedimento_trabalhar&acao_origem=procedimento_controlar&acao_retorno=procedimento_controlar&id_procedimento=7045049&infra_sistema=100000100&infra_unidade_atual=110000302&infra_hash=3d5759094b348d372aa2382043629aab6536cb88627baebeaa3532eaad86b7bb" aria-label="GPPR - Poder Judiciário / Referência: Medida Cautelar Na Ação Direta De Inconstitucionalidade 7236" onmouseover="return infraTooltipMostrar('Referência: Medida Cautelar Na Ação Direta De Inconstitucionalidade 7236','GPPR - Poder Judiciário');" onmouseout="return infraTooltipOcultar();" tabindex="1001">00063.<wbr>002635/2025-73</a></td>
<td width="10%">(<a href="controlador.php?acao=procedimento_atribuicao_listar&acao_retorno=procedimento_controlar&id_usuario_atribuicao=100002832&id_procedimento=7045049&infra_sistema=100000100&infra_unidade_atual=110000302&infra_hash=2cd0b1e9dfc1ec5759ca7130d651887ae41af49d170dab555322871966c7345f" title="Atribuído para Jussimara Campos Matsumoto de Miranda" class="ancoraSigla" tabindex="1001">jussimaracmm</a>)</td>
</tr>
<tr id="P6824238" class="infraTrClara">
<td><a id="lnkRecebidosID-6824238" name="ID-6824238"></a><input class="infraCheckbox" id="chkRecebidosItem5" name="chkRecebidosItem5" tabindex="1001" title="00025.001483/2025-48" type="checkbox" value="6824238" aria-label="Tipo Acordo de Cooperação Técnica" onclick="infraSelecionarItens(this,'Recebidos');"/></td>
<td width="20%"></td>
<td><a class="processoVisualizado" href="controlador.php?acao=procedimento_trabalhar&acao_origem=procedimento_controlar&acao_retorno=procedimento_controlar&id_procedimento=6824238&infra_sistema=100000100&infra_unidade_atual=110000302&infra_hash=49f8adf9d225b2c3d2db4c52f4d6c4f836994e093371aa1a7b364eda67b746bd" aria-label="Acordo de Cooperação Técnica" onmouseover="return infraTooltipMostrar('','Acordo de Cooperação Técnica');" onmouseout="return infraTooltipOcultar();" tabindex="1001">00025.<wbr>001483/2025-48</a></td>
<td width="10%">(<a href="controlador.php?acao=procedimento_atribuicao_listar&acao_retorno=procedimento_controlar&id_usuario_atribuicao=100014182&id_procedimento=6824238&infra_sistema=100000100&infra_unidade_atual=110000302&infra_hash=8dfbb4d43514acce9ca944af5950a823f366d4270d793eb4796d3087854f2a9d" title="Atribuído para Felipe Augusto Romão" class="ancoraSigla" tabindex="1001">felipe.romao</a>)</td>
</tr>
<tr id="P6641446" class="infraTrClara">
<td><a id="lnkRecebidosID-6641446" name="ID-6641446"></a><input class="infraCheckbox" id="chkRecebidosItem6" name="chkRecebidosItem6" tabindex="1001" title="00063.000895/2025-12" type="checkbox" value="6641446" aria-label="Tipo GPPR - Poder Judiciário / Especificação EMB.DECL. NOS EMB.DECL. NA AÇÃO DIRETA DE INCONSTITUCIONALIDADE 2.111 DISTRITO FEDERAL" onclick="infraSelecionarItens(this,'Recebidos');"/></td>
<td width="20%"></td>
<td><a class="processoVisualizado" href="controlador.php?acao=procedimento_trabalhar&acao_origem=procedimento_controlar&acao_retorno=procedimento_controlar&id_procedimento=6641446&infra_sistema=100000100&infra_unidade_atual=110000302&infra_hash=fd2da7f0add8915e3bc4341fcfb35b6e1dd7b96254f1937fdc5ca0012c42dac8" aria-label="GPPR - Poder Judiciário / EMB.DECL. NOS EMB.DECL. NA AÇÃO DIRETA DE INCONSTITUCIONALIDADE 2.111 DISTRITO FEDERAL" onmouseover="return infraTooltipMostrar('EMB.DECL. NOS EMB.DECL. NA AÇÃO DIRETA DE INCONSTITUCIONALIDADE 2.111 DISTRITO FEDERAL','GPPR - Poder Judiciário');" onmouseout="return infraTooltipOcultar();" tabindex="1001">00063.<wbr>000895/2025-12</a></td>
<td width="10%">(<a href="controlador.php?acao=procedimento_atribuicao_listar&acao_retorno=procedimento_controlar&id_usuario_atribuicao=100002258&id_procedimento=6641446&infra_sistema=100000100&infra_unidade_atual=110000302&infra_hash=8d91dba22cbd6af3ec78de6610adb8ec1db567751108d7a4dc60e74be2f86980" title="Atribuído para Fernanda Rodrigues Saldanha de Azevedo" class="ancoraSigla" tabindex="1001">fernandarsa</a>)</td>
</tr>
<tr id="P6999751" class="infraTrClara">
<td><a id="lnkRecebidosID-6999751" name="ID-6999751"></a><input class="infraCheckbox" id="chkRecebidosItem7" name="chkRecebidosItem7" tabindex="1001" title="00063.002465/2025-27" type="checkbox" value="6999751" aria-label="Tipo GPPR - Poder Judiciário / Especificação AÇÃO DIRETA DE INCONSTITUCIONALIDADE 4.245 DISTRITO FEDERAL" onclick="infraSelecionarItens(this,'Recebidos');"/></td>
<td width="20%"></td>
<td><a class="processoVisualizado" href="controlador.php?acao=procedimento_trabalhar&acao_origem=procedimento_controlar&acao_retorno=procedimento_controlar&id_procedimento=6999751&infra_sistema=100000100&infra_unidade_atual=110000302&infra_hash=7893983956a381e8c2a6b30450519424cd16a2bdf078da5aac871d40a5f40191" aria-label="GPPR - Poder Judiciário / AÇÃO DIRETA DE INCONSTITUCIONALIDADE 4.245 DISTRITO FEDERAL" onmouseover="return infraTooltipMostrar('AÇÃO DIRETA DE INCONSTITUCIONALIDADE 4.245 DISTRITO FEDERAL','GPPR - Poder Judiciário');" onmouseout="return infraTooltipOcultar();" tabindex="1001">00063.<wbr>002465/2025-27</a></td>
<td width="10%">(<a href="controlador.php?acao=procedimento_atribuicao_listar&acao_retorno=procedimento_controlar&id_usuario_atribuicao=100002258&id_procedimento=6999751&infra_sistema=100000100&infra_unidade_atual=110000302&infra_hash=8a0f1aedd2720343ba6a1f684ff9385ead8de313dd07f08b209fe9aefeee3497" title="Atribuído para Fernanda Rodrigues Saldanha de Azevedo" class="ancoraSigla" tabindex="1001">fernandarsa</a>)</td>
</tr>
<tr id="P6928110" class="infraTrClara">
<td><a id="lnkRecebidosID-6928110" name="ID-6928110"></a><input class="infraCheckbox" id="chkRecebidosItem8" name="chkRecebidosItem8" tabindex="1001" title="00180.000519/2025-83" type="checkbox" value="6928110" aria-label="Tipo Segurança da Informação - Implementação de Ações" onclick="infraSelecionarItens(this,'Recebidos');"/></td>
<td width="20%"><a href="javascript:void(0);" aria-label="Um documento foi incluído ou assinado neste processo" onmouseover="return infraTooltipMostrar('Um documento foi incluído ou assinado neste processo');" onmouseout="return infraTooltipOcultar();"><img src="svg/exclamacao.svg?18" class="imagemStatus" /></a></td>
<td><a class="processoVisualizado" href="controlador.php?acao=procedimento_trabalhar&acao_origem=procedimento_controlar&acao_retorno=procedimento_controlar&id_procedimento=6928110&infra_sistema=100000100&infra_unidade_atual=110000302&infra_hash=ae0620be8181917b41b5f9b5d3dba54bd7ecc57019d5de5852e6a4dcf8d0c97e" aria-label="Segurança da Informação - Implementação de Ações" onmouseover="return infraTooltipMostrar('','Segurança da Informação - Implementação de Ações');" onmouseout="return infraTooltipOcultar();" tabindex="1001">00180.<wbr>000519/2025-83</a></td>
<td width="10%">(<a href="controlador.php?acao=procedimento_atribuicao_listar&acao_retorno=procedimento_controlar&id_usuario_atribuicao=100002693&id_procedimento=6928110&infra_sistema=100000100&infra_unidade_atual=110000302&infra_hash=2bc0f096f99386396e6c53234b9d0032bb3879a130b26489b976bc8001fe4d97" title="Atribuído para Ricardo Brito do Nascimento" class="ancoraSigla" tabindex="1001">ricardobn</a>)</td>
</tr>
<tr id="P2113814" class="infraTrClara">
<td><a id="lnkRecebidosID-2113814" name="ID-2113814"></a><input class="infraCheckbox" id="chkRecebidosItem9" name="chkRecebidosItem9" tabindex="1001" title="00025.000498/2020-84" type="checkbox" value="2113814" aria-label="Tipo Acordo de Cooperação Técnica / Especificação Portal da Legislação - C927 e CFSTF" onclick="infraSelecionarItens(this,'Recebidos');"/></td>
<td width="20%"><a href="controlador.php?acao=andamento_marcador_gerenciar&acao_origem=procedimento_controlar&acao_retorno=procedimento_controlar&id_procedimento=2113814&infra_sistema=100000100&infra_unidade_atual=110000302&infra_hash=893dd648a542ee2479028a71df4ad8f5e48111c5ca9f8e6ba29b7fc789e0989f" aria-label="Marcador / Acordos de Cooperação Técnica / STF/CNJ/STJ/ENFAM - Disponibilização de hiperlinks do sistema Corpus927 - Vencimento em 24/05/2025" onmouseover="return infraTooltipMostrar('STF/CNJ/STJ/ENFAM - Disponibilização de hiperlinks do sistema Corpus927 - Vencimento em 24/05/2025','Acordos de Cooperação Técnica');" onmouseout="return infraTooltipOcultar();"><img src="svg/marcador_laranja.svg?18" class="imagemStatus" /></a><a href="controlador.php?acao=controle_prazo_definir&acao_origem=procedimento_controlar&acao_retorno=procedimento_controlar&id_controle_prazo=1797&id_procedimento=2113814&infra_sistema=100000100&infra_unidade_atual=110000302&infra_hash=52292eb55bf0ba6bea612fce77bc72df4fa3549fa46df7c824d192a92392048d" aria-label="Controle de Prazo / hansmpf 26/05/2025 (atrasado 144 dias)" onmouseover="return infraTooltipMostrar('hansmpf 26/05/2025 (atrasado 144 dias)','Controle de Prazo');" onmouseout="return infraTooltipOcultar();"><img src="svg/controle_prazo3.svg?18" class="imagemStatus" /></a></td>
<td><a class="processoVisualizado" href="controlador.php?acao=procedimento_trabalhar&acao_origem=procedimento_controlar&acao_retorno=procedimento_controlar&id_procedimento=2113814&infra_sistema=100000100&infra_unidade_atual=110000302&infra_hash=afa6ddf9dc8e73955e55ad49223bc83329f06ffe25055666466da95e1709625a" aria-label="Acordo de Cooperação Técnica / Portal da Legislação - C927 e CFSTF" onmouseover="return infraTooltipMostrar('Portal da Legislação - C927 e CFSTF','Acordo de Cooperação Técnica');" onmouseout="return infraTooltipOcultar();" tabindex="1001">00025.<wbr>000498/2020-84</a></td>
<td width="10%">(<a href="controlador.php?acao=procedimento_atribuicao_listar&acao_retorno=procedimento_controlar&id_usuario_atribuicao=100002258&id_procedimento=2113814&infra_sistema=100000100&infra_unidade_atual=110000302&infra_hash=f48e23628754ee9c4793e72f9b1a31ce0d8c01a94fd42ba1c5e752414c4f354c" title="Atribuído para Fernanda Rodrigues Saldanha de Azevedo" class="ancoraSigla" tabindex="1001">fernandarsa</a>)</td>
</tr>
<tr id="P6455190" class="infraTrClara">
<td><a id="lnkRecebidosID-6455190" name="ID-6455190"></a><input class="infraCheckbox" id="chkRecebidosItem10" name="chkRecebidosItem10" tabindex="1001" title="00025.000292/2025-69" type="checkbox" value="6455190" aria-label="Tipo Patrimônio - Serviços Gráficos / Especificação Impressão de edição da Revista Jurídica da Presidência - RJP" onclick="infraSelecionarItens(this,'Recebidos');"/></td>
<td width="20%"><a href="controlador.php?acao=andamento_marcador_gerenciar&acao_origem=procedimento_controlar&acao_retorno=procedimento_controlar&id_procedimento=6455190&infra_sistema=100000100&infra_unidade_atual=110000302&infra_hash=24e1b7a537d4c8b1fe5bfce9cb2eaf1a1c5801b37cc0818dee2d9d8d77aecb27" aria-label="Marcador / Revista RJP" onmouseover="return infraTooltipMostrar('','Revista RJP');" onmouseout="return infraTooltipOcultar();"><img src="svg/marcador_rosa.svg?18" class="imagemStatus" /></a></td>
<td><a class="processoVisualizado" href="controlador.php?acao=procedimento_trabalhar&acao_origem=procedimento_controlar&acao_retorno=procedimento_controlar&id_procedimento=6455190&infra_sistema=100000100&infra_unidade_atual=110000302&infra_hash=9c6ab7234496af4be39d33d2069eba6d21060f5d5033307519548a0e94d69af1" aria-label="Patrimônio - Serviços Gráficos / Impressão de edição da Revista Jurídica da Presidência - RJP" onmouseover="return infraTooltipMostrar('Impressão de edição da Revista Jurídica da Presidência - RJP','Patrimônio - Serviços Gráficos');" onmouseout="return infraTooltipOcultar();" tabindex="1001">00025.<wbr>000292/2025-69</a></td>
<td width="10%">(<a href="controlador.php?acao=procedimento_atribuicao_listar&acao_retorno=procedimento_controlar&id_usuario_atribuicao=100014182&id_procedimento=6455190&infra_sistema=100000100&infra_unidade_atual=110000302&infra_hash=2539bbca3dc31f51de3b604c2b112e13540536c25198dd90071a512a08133d22" title="Atribuído para Felipe Augusto Romão" class="ancoraSigla" tabindex="1001">felipe.romao</a>)</td>
</tr>
<tr id="P5357572" class="infraTrClara">
<td><a id="lnkRecebidosID-5357572" name="ID-5357572"></a><input class="infraCheckbox" id="chkRecebidosItem11" name="chkRecebidosItem11" tabindex="1001" title="00025.005081/2023-51" type="checkbox" value="5357572" aria-label="Tipo Acordo de Cooperação Técnica / Especificação SAJ/CC-PR e Universidade do Estado do Rio de Janeiro - UERJ" onclick="infraSelecionarItens(this,'Recebidos');"/></td>
<td width="20%"><a href="controlador.php?acao=andamento_marcador_gerenciar&acao_origem=procedimento_controlar&acao_retorno=procedimento_controlar&id_procedimento=5357572&infra_sistema=100000100&infra_unidade_atual=110000302&infra_hash=90c860fe43a1bed9272388eda1e0b534ebf69f9dd5c97ca4b14a47439bb4e18d" aria-label="Marcador / Acordos de Cooperação Técnica / UERJ - Novo ACT" onmouseover="return infraTooltipMostrar('UERJ - Novo ACT','Acordos de Cooperação Técnica');" onmouseout="return infraTooltipOcultar();"><img src="svg/marcador_laranja.svg?18" class="imagemStatus" /></a></td>
<td><a class="processoVisualizado" href="controlador.php?acao=procedimento_trabalhar&acao_origem=procedimento_controlar&acao_retorno=procedimento_controlar&id_procedimento=5357572&infra_sistema=100000100&infra_unidade_atual=110000302&infra_hash=1710dcbca3bf7e8f25336942f064ea801c5014190c338131b1328290b22c3609" aria-label="Acordo de Cooperação Técnica / SAJ/CC-PR e Universidade do Estado do Rio de Janeiro - UERJ" onmouseover="return infraTooltipMostrar('SAJ/CC-PR e Universidade do Estado do Rio de Janeiro - UERJ','Acordo de Cooperação Técnica');" onmouseout="return infraTooltipOcultar();" tabindex="1001">00025.<wbr>005081/2023-51</a></td>
<td width="10%">(<a href="controlador.php?acao=procedimento_atribuicao_listar&acao_retorno=procedimento_controlar&id_usuario_atribuicao=100013482&id_procedimento=5357572&infra_sistema=100000100&infra_unidade_atual=110000302&infra_hash=01d059692474db826827af75dfe07e8ae03c16cdd8e49c60ca21c751a55ebb5f" title="Atribuído para Betina Stefanello Lima" class="ancoraSigla" tabindex="1001">betina.lima</a>)</td>
</tr>
<tr id="P6606937" class="infraTrClara">
<td><a id="lnkRecebidosID-6606937" name="ID-6606937"></a><input class="infraCheckbox" id="chkRecebidosItem12" name="chkRecebidosItem12" tabindex="1001" title="00063.000721/2025-41" type="checkbox" value="6606937" aria-label="Tipo GPPR - Poder Judiciário / Especificação AÇÃO DIRETA DE INCONSTITUCIONALIDADE 5.043 DISTRITO FEDERAL" onclick="infraSelecionarItens(this,'Recebidos');"/></td>
<td width="20%"></td>
<td><a class="processoVisualizado" href="controlador.php?acao=procedimento_trabalhar&acao_origem=procedimento_controlar&acao_retorno=procedimento_controlar&id_procedimento=6606937&infra_sistema=100000100&infra_unidade_atual=110000302&infra_hash=c753def9b95b1cabe09c57a00aade9b23224d58b809015e27c797a11251be6e1" aria-label="GPPR - Poder Judiciário / AÇÃO DIRETA DE INCONSTITUCIONALIDADE 5.043 DISTRITO FEDERAL" onmouseover="return infraTooltipMostrar('AÇÃO DIRETA DE INCONSTITUCIONALIDADE 5.043 DISTRITO FEDERAL','GPPR - Poder Judiciário');" onmouseout="return infraTooltipOcultar();" tabindex="1001">00063.<wbr>000721/2025-41</a></td>
<td width="10%">(<a href="controlador.php?acao=procedimento_atribuicao_listar&acao_retorno=procedimento_controlar&id_usuario_atribuicao=100002258&id_procedimento=6606937&infra_sistema=100000100&infra_unidade_atual=110000302&infra_hash=67587528adfe94353d772148d82dc33a3b621c431eb917a1ec9f1f910a6e8f75" title="Atribuído para Fernanda Rodrigues Saldanha de Azevedo" class="ancoraSigla" tabindex="1001">fernandarsa</a>)</td>
</tr>
<tr id="P6360188" class="infraTrClara">
<td><a id="lnkRecebidosID-6360188" name="ID-6360188"></a><input class="infraCheckbox" id="chkRecebidosItem13" name="chkRecebidosItem13" tabindex="1001" title="00025.002883/2024-90" type="checkbox" value="6360188" aria-label="Tipo Consultas - Outros Entes" onclick="infraSelecionarItens(this,'Recebidos');"/></td>
<td width="20%"><a href="controlador.php?acao=andamento_marcador_gerenciar&acao_origem=procedimento_controlar&acao_retorno=procedimento_controlar&id_procedimento=6360188&infra_sistema=100000100&infra_unidade_atual=110000302&infra_hash=a848aa9c3580b966cf895336f651808d4a91511a6d9b84845e9829b7bfb502e3" aria-label="Marcador / Portal da Legislação" onmouseover="return infraTooltipMostrar('','Portal da Legislação');" onmouseout="return infraTooltipOcultar();"><img src="svg/marcador_verde_amazonas.svg?18" class="imagemStatus" /></a></td>
<td><a class="processoVisualizado" href="controlador.php?acao=procedimento_trabalhar&acao_origem=procedimento_controlar&acao_retorno=procedimento_controlar&id_procedimento=6360188&infra_sistema=100000100&infra_unidade_atual=110000302&infra_hash=6a625bb1953774c80ad8bb8462e49da6b2c126ec5a1fe2f6c785f6fb4d57472f" aria-label="Consultas - Outros Entes" onmouseover="return infraTooltipMostrar('','Consultas - Outros Entes');" onmouseout="return infraTooltipOcultar();" tabindex="1001">00025.<wbr>002883/2024-90</a></td>
<td width="10%">(<a href="controlador.php?acao=procedimento_atribuicao_listar&acao_retorno=procedimento_controlar&id_usuario_atribuicao=100002832&id_procedimento=6360188&infra_sistema=100000100&infra_unidade_atual=110000302&infra_hash=2aa8491695ccb4474367be671e2914a62fcb4c7743f65fb0597c27bdd8cb398d" title="Atribuído para Jussimara Campos Matsumoto de Miranda" class="ancoraSigla" tabindex="1001">jussimaracmm</a>)</td>
</tr>
<tr id="P5806875" class="infraTrClara">
<td><a id="lnkRecebidosID-5806875" name="ID-5806875"></a><input class="infraCheckbox" id="chkRecebidosItem14" name="chkRecebidosItem14" tabindex="1001" title="00742.001334/2024-01" type="checkbox" value="5806875" aria-label="Tipo Pedidos e informações diversas - Outros / Especificação CAPACITAÇÃO SOBRE DECRETO 12.002, DE 22/04/2024" onclick="infraSelecionarItens(this,'Recebidos');"/></td>
<td width="20%"><a href="controlador.php?acao=andamento_marcador_gerenciar&acao_origem=procedimento_controlar&acao_retorno=procedimento_controlar&id_procedimento=5806875&infra_sistema=100000100&infra_unidade_atual=110000302&infra_hash=f28ba33c0035e8444ce8c8442091488ae5d444ac742a1c18de37b40ba7715d46" aria-label="Marcador / Eventos e Reuniões" onmouseover="return infraTooltipMostrar('','Eventos e Reuniões');" onmouseout="return infraTooltipOcultar();"><img src="svg/marcador_ouro.svg?18" class="imagemStatus" /></a></td>
<td><a class="processoVisualizado" href="controlador.php?acao=procedimento_trabalhar&acao_origem=procedimento_controlar&acao_retorno=procedimento_controlar&id_procedimento=5806875&infra_sistema=100000100&infra_unidade_atual=110000302&infra_hash=a8d6621e3849c2c9ec31c64c0ccccd6435a907fdfe622ce0838336f3b527e7dc" aria-label="Pedidos e informações diversas - Outros / CAPACITAÇÃO SOBRE DECRETO 12.002, DE 22/04/2024" onmouseover="return infraTooltipMostrar('CAPACITAÇÃO SOBRE DECRETO 12.002, DE 22/04/2024','Pedidos e informações diversas - Outros');" onmouseout="return infraTooltipOcultar();" tabindex="1001">00742.<wbr>001334/2024-01</a></td>
<td width="10%">(<a href="controlador.php?acao=procedimento_atribuicao_listar&acao_retorno=procedimento_controlar&id_usuario_atribuicao=100002258&id_procedimento=5806875&infra_sistema=100000100&infra_unidade_atual=110000302&infra_hash=87535bfb69a909fbf24fc7b71fad685f57ea7bf9382389410a84a716f29030e8" title="Atribuído para Fernanda Rodrigues Saldanha de Azevedo" class="ancoraSigla" tabindex="1001">fernandarsa</a>)</td>
</tr>
</table>
</div>

<input type="hidden" id="hdnRecebidosNroItens" name="hdnRecebidosNroItens" value="15"/>
<input type="hidden" id="hdnRecebidosItemId" name="hdnRecebidosItemId" value=""/>
<input type="hidden" id="hdnRecebidosItens" name="hdnRecebidosItens" value="7106570,6779498,7093872,7096637,7045049,6824238,6641446,6999751,6928110,2113814,6455190,5357572,6606937,6360188,5806875"/>
<input type="hidden" id="hdnRecebidosItensHash" name="hdnRecebidosItensHash" value="0d85923c996d34601d0f4f0d0584cff23fef9a23f18e8ca304248c1c0d7c67ec"/>
<input type="hidden" id="hdnRecebidosItensSelecionados" name="hdnRecebidosItensSelecionados" value=""/>

<input type="hidden" id="hdnGeradosNroItens" name="hdnGeradosNroItens" value="15"/>
<input type="hidden" id="hdnGeradosItemId" name="hdnGeradosItemId" value=""/>
<input type="hidden" id="hdnGeradosItens" name="hdnGeradosItens" value="7109475,7052447,6961944,5494260,7073755,7008152,7058253,6961920,6894790,2991883,6430741,6513567,5767955,6299248,4779694"/>
<input type="hidden" id="hdnGeradosItensHash" name="hdnGeradosItensHash" value="b88a599946c2d41db47956a614bc079e0a70aa91aea8afcce230b9f35462edb0"/>
<input type="hidden" id="hdnGeradosItensSelecionados" name="hdnGeradosItensSelecionados" value=""/>

<input type="hidden" id="hdnInfraSelecoes" name="hdnInfraSelecoes" value="Recebidos,Gerados"/>
<div id="divRecebidosAreaPaginacaoInferior" class="infraAreaPaginacao">
</div>

<input type="hidden" id="hdnRecebidosPaginaAtual" name="hdnRecebidosPaginaAtual" value="0"/>
<input type="hidden" id="hdnRecebidosHashCriterios" name="hdnRecebidosHashCriterios" value="78225ad2dec3cc10efae2a8519af7be3"/>
  </div>
  <div id="divGerados" class=" ml-0 pl-0  d-none d-md-block col-12 col-md-6">
<div id="divGeradosAreaPaginacaoSuperior" class="infraAreaPaginacao">
</div>
<div id="divGeradosAreaTabela" class="infraAreaTabela" >
<table id="tblProcessosGerados" width="100%" border="0" cellspacing="0" cellpadding="1" class="infraTable tabelaControle" summary="Tabela de Processos Gerados." tabindex="1002">
<caption class="infraCaption">Processos gerados (15 registros):</caption><tr><th class="infraTh" width="5%"><a href="javascript:void(0);" id="lnkInfraCheck" onclick="infraSelecaoMultipla('Gerados');" tabindex="1002"><img src="/infra_css/svg/check.svg" id="imgGeradosCheck" title="Selecionar Tudo" alt="Selecionar Tudo" class="infraImg"/></a></th>
<th class="infraTh" colspan="3">Gerados</th>
</tr>
<tr id="P7109475" class="infraTrClara">
<td><a id="lnkGeradosID-7109475" name="ID-7109475"></a><input class="infraCheckbox" id="chkGeradosItem0" name="chkGeradosItem0" tabindex="1002" title="00025.002374/2025-48" type="checkbox" value="7109475" aria-label="Tipo Acordo de Cooperação Técnica" onclick="infraSelecionarItens(this,'Gerados');"/></td>
<td width="20%"><a href="controlador.php?acao=andamento_marcador_gerenciar&acao_origem=procedimento_controlar&acao_retorno=procedimento_controlar&id_procedimento=7109475&infra_sistema=100000100&infra_unidade_atual=110000302&infra_hash=b1c23e5215cda464378f0c040f8ba6e09f5894de03083eefd689515ce049bf0a" aria-label="Marcador / Acordos de Cooperação Técnica / ACT UnB 2025" onmouseover="return infraTooltipMostrar('ACT UnB 2025','Acordos de Cooperação Técnica');" onmouseout="return infraTooltipOcultar();"><img src="svg/marcador_laranja.svg?18" class="imagemStatus" /></a></td>
<td><a class="processoVisualizado" href="controlador.php?acao=procedimento_trabalhar&acao_origem=procedimento_controlar&acao_retorno=procedimento_controlar&id_procedimento=7109475&infra_sistema=100000100&infra_unidade_atual=110000302&infra_hash=05a52e7e5853454c6c8392b297a9973ef3218cccc68b48e51add3d5ffd0ee0c6" aria-label="Acordo de Cooperação Técnica" onmouseover="return infraTooltipMostrar('','Acordo de Cooperação Técnica');" onmouseout="return infraTooltipOcultar();" tabindex="1002">00025.<wbr>002374/2025-48</a></td>
<td width="10%">&nbsp;</td>
</tr>
<tr id="P7052447" class="infraTrClara">
<td><a id="lnkGeradosID-7052447" name="ID-7052447"></a><input class="infraCheckbox" id="chkGeradosItem1" name="chkGeradosItem1" tabindex="1002" title="00025.002226/2025-23" type="checkbox" value="7052447" aria-label="Tipo Pessoal: Processo Seletivo - Edital de Oportunidades / Especificação Programa de Intercambio SAJ (15ª ed) - Termos de compromissos individuais; e outros documentos" onclick="infraSelecionarItens(this,'Gerados');"/></td>
<td width="20%"><a href="controlador.php?acao=andamento_marcador_gerenciar&acao_origem=procedimento_controlar&acao_retorno=procedimento_controlar&id_procedimento=7052447&infra_sistema=100000100&infra_unidade_atual=110000302&infra_hash=890d6e81c45cbaa060e794bfcfb8472b7e59d6ffb538e0d4ee6f8469cd8d0698" aria-label="Marcador / Programa de Intercâmbio / Ate 24/10/2025 23:59&#13;Termos de compromissos individuais; e outros documentos" onmouseover="return infraTooltipMostrar('Ate 24/10/2025 23:59\nTermos de compromissos individuais; e outros documentos','Programa de Intercâmbio');" onmouseout="return infraTooltipOcultar();"><img src="svg/marcador_ouro.svg?18" class="imagemStatus" /></a></td>
<td><a class="processoVisualizado" href="controlador.php?acao=procedimento_trabalhar&acao_origem=procedimento_controlar&acao_retorno=procedimento_controlar&id_procedimento=7052447&infra_sistema=100000100&infra_unidade_atual=110000302&infra_hash=5ef5239cee72302e3f2d0e42eaa07292dcb00a70f4e9f220da96676938ff31f3" aria-label="Pessoal: Processo Seletivo - Edital de Oportunidades / Programa de Intercambio SAJ (15ª ed) - Termos de compromissos individuais; e outros documentos" onmouseover="return infraTooltipMostrar('Programa de Intercambio SAJ (15ª ed) - Termos de compromissos individuais; e outros documentos','Pessoal: Processo Seletivo - Edital de Oportunidades');" onmouseout="return infraTooltipOcultar();" tabindex="1002">00025.<wbr>002226/2025-23</a></td>
<td width="10%">(<a href="controlador.php?acao=procedimento_atribuicao_listar&acao_retorno=procedimento_controlar&id_usuario_atribuicao=100002693&id_procedimento=7052447&infra_sistema=100000100&infra_unidade_atual=110000302&infra_hash=e2ffe5b8baa18d389c6ce2d071c673e548723573849b932e26c571cc0402a200" title="Atribuído para Ricardo Brito do Nascimento" class="ancoraSigla" tabindex="1002">ricardobn</a>)</td>
</tr>
<tr id="P6961944" class="infraTrClara">
<td><a id="lnkGeradosID-6961944" name="ID-6961944"></a><input class="infraCheckbox" id="chkGeradosItem2" name="chkGeradosItem2" tabindex="1002" title="00025.001931/2025-11" type="checkbox" value="6961944" aria-label="Tipo Pedidos e informações diversas - Outros / Especificação Programa Intercâmbio SAJ (15ª ed) -  Solicitação para emissão de crachá personalizado para o evento" onclick="infraSelecionarItens(this,'Gerados');"/></td>
<td width="20%"><a href="controlador.php?acao=andamento_marcador_gerenciar&acao_origem=procedimento_controlar&acao_retorno=procedimento_controlar&id_procedimento=6961944&infra_sistema=100000100&infra_unidade_atual=110000302&infra_hash=0bbac4cec30847b6aa53adab4edf1085a3dc2e1b6601a785777bfcbec9b46a85" aria-label="Marcador / Programa de Intercâmbio / Ate 21/10/2025 23:59&#13;Credenciamento" onmouseover="return infraTooltipMostrar('Ate 21/10/2025 23:59\nCredenciamento','Programa de Intercâmbio');" onmouseout="return infraTooltipOcultar();"><img src="svg/marcador_ouro.svg?18" class="imagemStatus" /></a></td>
<td><a class="processoVisualizado" href="controlador.php?acao=procedimento_trabalhar&acao_origem=procedimento_controlar&acao_retorno=procedimento_controlar&id_procedimento=6961944&infra_sistema=100000100&infra_unidade_atual=110000302&infra_hash=a3c39388f7dbef1213a714cc0f6a2f2bc9a48341d0d74d2a7f67fcf86e06ae54" aria-label="Pedidos e informações diversas - Outros / Programa Intercâmbio SAJ (15ª ed) -  Solicitação para emissão de crachá personalizado para o evento" onmouseover="return infraTooltipMostrar('Programa Intercâmbio SAJ (15ª ed) -  Solicitação para emissão de crachá personalizado para o evento','Pedidos e informações diversas - Outros');" onmouseout="return infraTooltipOcultar();" tabindex="1002">00025.<wbr>001931/2025-11</a></td>
<td width="10%">(<a href="controlador.php?acao=procedimento_atribuicao_listar&acao_retorno=procedimento_controlar&id_usuario_atribuicao=100002693&id_procedimento=6961944&infra_sistema=100000100&infra_unidade_atual=110000302&infra_hash=85347a5c2e422263bdd5896496cceff16e67bf864caf737e2c438ad5ad6401c9" title="Atribuído para Ricardo Brito do Nascimento" class="ancoraSigla" tabindex="1002">ricardobn</a>)</td>
</tr>
<tr id="P5494260" class="infraTrClara">
<td><a id="lnkGeradosID-5494260" name="ID-5494260"></a><input class="infraCheckbox" id="chkGeradosItem3" name="chkGeradosItem3" tabindex="1002" title="00025.000289/2024-64" type="checkbox" value="5494260" aria-label="Tipo Envio de Informações / Especificação Documentos modelo" onclick="infraSelecionarItens(this,'Gerados');"/></td>
<td width="20%"><a href="controlador.php?acao=anotacao_registrar&acao_origem=procedimento_controlar&acao_retorno=procedimento_controlar&id_protocolo=5494260&infra_sistema=100000100&infra_unidade_atual=110000302&infra_hash=97916ac8a3c596092c11ccbbcc8aa1288001061ec4559cfaefaa8b746c6524ee" aria-label="Anotação / Modelos de documentos para processos de novos ACTs 2024 / hansmpf em 22/02/2024 17:29" onmouseover="return infraTooltipMostrar('Modelos de documentos para processos de novos ACTs 2024','hansmpf em 22/02/2024 17:29');" onmouseout="return infraTooltipOcultar();"><img src="svg/anotacao1.svg?18" class="imagemStatus" /></a></td>
<td><a class="processoVisualizado" href="controlador.php?acao=procedimento_trabalhar&acao_origem=procedimento_controlar&acao_retorno=procedimento_controlar&id_procedimento=5494260&infra_sistema=100000100&infra_unidade_atual=110000302&infra_hash=7a72a06f0c787c52cb5699ed6cd8a63aa32ceaca93576ce9b045257c2cc153a2" aria-label="Envio de Informações / Documentos modelo" onmouseover="return infraTooltipMostrar('Documentos modelo','Envio de Informações');" onmouseout="return infraTooltipOcultar();" tabindex="1002">00025.<wbr>000289/2024-64</a></td>
<td width="10%">(<a href="controlador.php?acao=procedimento_atribuicao_listar&acao_retorno=procedimento_controlar&id_usuario_atribuicao=100013821&id_procedimento=5494260&infra_sistema=100000100&infra_unidade_atual=110000302&infra_hash=37433e34f81daf194a6b1ce07140d9752c152c22ef19955a9bd2f5f08672ed25" title="Atribuído para Ana Paula Ferreira Sebastião" class="ancoraSigla" tabindex="1002">ana.sebastiao</a>)</td>
</tr>
<tr id="P7073755" class="infraTrClara">
<td><a id="lnkGeradosID-7073755" name="ID-7073755"></a><input class="infraCheckbox" id="chkGeradosItem4" name="chkGeradosItem4" tabindex="1002" title="00025.002284/2025-57" type="checkbox" value="7073755" aria-label="Tipo Pessoal - Comunicação/Orientação / Especificação Exercício de servidores aprovados no CNU - ATPS" onclick="infraSelecionarItens(this,'Gerados');"/></td>
<td width="20%"></td>
<td><a class="processoVisualizado" href="controlador.php?acao=procedimento_trabalhar&acao_origem=procedimento_controlar&acao_retorno=procedimento_controlar&id_procedimento=7073755&infra_sistema=100000100&infra_unidade_atual=110000302&infra_hash=73942ca7d6129f7d27f79ec7782951a582135ceb9f3b3cc8eb1adcf868b35804" aria-label="Pessoal - Comunicação/Orientação / Exercício de servidores aprovados no CNU - ATPS" onmouseover="return infraTooltipMostrar('Exercício de servidores aprovados no CNU - ATPS','Pessoal - Comunicação/Orientação');" onmouseout="return infraTooltipOcultar();" tabindex="1002">00025.<wbr>002284/2025-57</a></td>
<td width="10%">(<a href="controlador.php?acao=procedimento_atribuicao_listar&acao_retorno=procedimento_controlar&id_usuario_atribuicao=100002258&id_procedimento=7073755&infra_sistema=100000100&infra_unidade_atual=110000302&infra_hash=1804d748cf920972801d6b2261e2af8f152ce047bf52abc1e7847e23b7fe0eeb" title="Atribuído para Fernanda Rodrigues Saldanha de Azevedo" class="ancoraSigla" tabindex="1002">fernandarsa</a>)</td>
</tr>
<tr id="P7008152" class="infraTrClara">
<td><a id="lnkGeradosID-7008152" name="ID-7008152"></a><input class="infraCheckbox" id="chkGeradosItem5" name="chkGeradosItem5" tabindex="1002" title="00025.002084/2025-02" type="checkbox" value="7008152" aria-label="Tipo Pessoal: Processo Seletivo - Edital de Oportunidades / Especificação Programa de Estágio em Direito SAJ - Processo Seletivo nº 001/2025" onclick="infraSelecionarItens(this,'Gerados');"/></td>
<td width="20%"><a href="controlador.php?acao=anotacao_registrar&acao_origem=procedimento_controlar&acao_retorno=procedimento_controlar&id_protocolo=7008152&infra_sistema=100000100&infra_unidade_atual=110000302&infra_hash=297d6340c807d5e22345b388a394724633d1805ab825fdcfacd691866109ed76" aria-label="Anotação / Seleção Programa de Estágio em Direito / ana.sebastiao em 10/09/2025 14:48" onmouseover="return infraTooltipMostrar('Seleção Programa de Estágio em Direito','ana.sebastiao em 10/09/2025 14:48');" onmouseout="return infraTooltipOcultar();"><img src="svg/anotacao1.svg?18" class="imagemStatus" /></a></td>
<td><a class="processoVisualizado" href="controlador.php?acao=procedimento_trabalhar&acao_origem=procedimento_controlar&acao_retorno=procedimento_controlar&id_procedimento=7008152&infra_sistema=100000100&infra_unidade_atual=110000302&infra_hash=463c1e3db5fddc785fcb132a8e6c54211fa3f9264c9e3aa98ff84377103a6073" aria-label="Pessoal: Processo Seletivo - Edital de Oportunidades / Programa de Estágio em Direito SAJ - Processo Seletivo nº 001/2025" onmouseover="return infraTooltipMostrar('Programa de Estágio em Direito SAJ - Processo Seletivo nº 001/2025','Pessoal: Processo Seletivo - Edital de Oportunidades');" onmouseout="return infraTooltipOcultar();" tabindex="1002">00025.<wbr>002084/2025-02</a></td>
<td width="10%">(<a href="controlador.php?acao=procedimento_atribuicao_listar&acao_retorno=procedimento_controlar&id_usuario_atribuicao=100013821&id_procedimento=7008152&infra_sistema=100000100&infra_unidade_atual=110000302&infra_hash=ff1d7023e8ff11606830980ca7b4a54f70e05826c73c4ff166aa223d3407553e" title="Atribuído para Ana Paula Ferreira Sebastião" class="ancoraSigla" tabindex="1002">ana.sebastiao</a>)</td>
</tr>
<tr id="P7058253" class="infraTrClara">
<td><a id="lnkGeradosID-7058253" name="ID-7058253"></a><input class="infraCheckbox" id="chkGeradosItem6" name="chkGeradosItem6" tabindex="1002" title="00025.002240/2025-27" type="checkbox" value="7058253" aria-label="Tipo Envio de Informações" onclick="infraSelecionarItens(this,'Gerados');"/></td>
<td width="20%"><a href="controlador.php?acao=anotacao_registrar&acao_origem=procedimento_controlar&acao_retorno=procedimento_controlar&id_protocolo=7058253&infra_sistema=100000100&infra_unidade_atual=110000302&infra_hash=000ac56ba7d7dc3c7c063f728dfaaecdd5309df19fc678b57fa2a0c6780b9434" aria-label="Anotação / oficio - regulamentação de leis ordinárias / ana.sebastiao em 29/09/2025 16:09" onmouseover="return infraTooltipMostrar('oficio - regulamentação de leis ordinárias','ana.sebastiao em 29/09/2025 16:09');" onmouseout="return infraTooltipOcultar();"><img src="svg/anotacao1.svg?18" class="imagemStatus" /></a></td>
<td><a class="processoVisualizado" href="controlador.php?acao=procedimento_trabalhar&acao_origem=procedimento_controlar&acao_retorno=procedimento_controlar&id_procedimento=7058253&infra_sistema=100000100&infra_unidade_atual=110000302&infra_hash=46c24166c031934d2a36fc5e2c401c4f50b0d0d11109650c05bbbcff18677c8e" aria-label="Envio de Informações" onmouseover="return infraTooltipMostrar('','Envio de Informações');" onmouseout="return infraTooltipOcultar();" tabindex="1002">00025.<wbr>002240/2025-27</a></td>
<td width="10%">(<a href="controlador.php?acao=procedimento_atribuicao_listar&acao_retorno=procedimento_controlar&id_usuario_atribuicao=100013821&id_procedimento=7058253&infra_sistema=100000100&infra_unidade_atual=110000302&infra_hash=f221d390590d0a362a169542b1091b2406038a46634968785455aed0eb265895" title="Atribuído para Ana Paula Ferreira Sebastião" class="ancoraSigla" tabindex="1002">ana.sebastiao</a>)</td>
</tr>
<tr id="P6961920" class="infraTrClara">
<td><a id="lnkGeradosID-6961920" name="ID-6961920"></a><input class="infraCheckbox" id="chkGeradosItem7" name="chkGeradosItem7" tabindex="1002" title="00025.001930/2025-69" type="checkbox" value="6961920" aria-label="Tipo Pedidos e informações diversas - Outros / Especificação Programa Intercâmbio SAJ (15ª ed) - Solicitação de transporte para os participantes" onclick="infraSelecionarItens(this,'Gerados');"/></td>
<td width="20%"><a href="controlador.php?acao=andamento_marcador_gerenciar&acao_origem=procedimento_controlar&acao_retorno=procedimento_controlar&id_procedimento=6961920&infra_sistema=100000100&infra_unidade_atual=110000302&infra_hash=ce38bd77316468a53c0927bd1383e4e5c0772c906914e0d204465ca1da6c7ef5" aria-label="Marcador / Programa de Intercâmbio / Ate 31/10/2025 23:59&#13;Transporte" onmouseover="return infraTooltipMostrar('Ate 31/10/2025 23:59\nTransporte','Programa de Intercâmbio');" onmouseout="return infraTooltipOcultar();"><img src="svg/marcador_ouro.svg?18" class="imagemStatus" /></a></td>
<td><a class="processoVisualizado" href="controlador.php?acao=procedimento_trabalhar&acao_origem=procedimento_controlar&acao_retorno=procedimento_controlar&id_procedimento=6961920&infra_sistema=100000100&infra_unidade_atual=110000302&infra_hash=7376f5993b88e33cf08dfe88361f78f72f57bdc85dbc2a56d5a945ae74826f0c" aria-label="Pedidos e informações diversas - Outros / Programa Intercâmbio SAJ (15ª ed) - Solicitação de transporte para os participantes" onmouseover="return infraTooltipMostrar('Programa Intercâmbio SAJ (15ª ed) - Solicitação de transporte para os participantes','Pedidos e informações diversas - Outros');" onmouseout="return infraTooltipOcultar();" tabindex="1002">00025.<wbr>001930/2025-69</a></td>
<td width="10%">(<a href="controlador.php?acao=procedimento_atribuicao_listar&acao_retorno=procedimento_controlar&id_usuario_atribuicao=100002693&id_procedimento=6961920&infra_sistema=100000100&infra_unidade_atual=110000302&infra_hash=112bd81eb47a132e08f7ed0475dc9dde1658e3ba3a87ab3d557736606da45a80" title="Atribuído para Ricardo Brito do Nascimento" class="ancoraSigla" tabindex="1002">ricardobn</a>)</td>
</tr>
<tr id="P6894790" class="infraTrClara">
<td><a id="lnkGeradosID-6894790" name="ID-6894790"></a><input class="infraCheckbox" id="chkGeradosItem8" name="chkGeradosItem8" tabindex="1002" title="00025.001726/2025-48" type="checkbox" value="6894790" aria-label="Tipo Acordo de Cooperação Técnica / Especificação SAJ/CC-PR e Universidade XXX" onclick="infraSelecionarItens(this,'Gerados');"/></td>
<td width="20%"><a href="controlador.php?acao=anotacao_registrar&acao_origem=procedimento_controlar&acao_retorno=procedimento_controlar&id_protocolo=6894790&infra_sistema=100000100&infra_unidade_atual=110000302&infra_hash=74efda7fdb96cc379f52512f720fade94444ccb0ef290b7a7c86b50daf67fe37" aria-label="Anotação / modelo em construção / ana.sebastiao em 05/08/2025 13:44" onmouseover="return infraTooltipMostrar('modelo em construção','ana.sebastiao em 05/08/2025 13:44');" onmouseout="return infraTooltipOcultar();"><img src="svg/anotacao1.svg?18" class="imagemStatus" /></a></td>
<td><a class="processoVisualizado" href="controlador.php?acao=procedimento_trabalhar&acao_origem=procedimento_controlar&acao_retorno=procedimento_controlar&id_procedimento=6894790&infra_sistema=100000100&infra_unidade_atual=110000302&infra_hash=33bce75555d852bba8df6431b2b15508758d7768ce7af34b83c483e46bdbfec2" aria-label="Acordo de Cooperação Técnica / SAJ/CC-PR e Universidade XXX" onmouseover="return infraTooltipMostrar('SAJ/CC-PR e Universidade XXX','Acordo de Cooperação Técnica');" onmouseout="return infraTooltipOcultar();" tabindex="1002">00025.<wbr>001726/2025-48</a></td>
<td width="10%">&nbsp;</td>
</tr>
<tr id="P2991883" class="infraTrClara">
<td><a id="lnkGeradosID-2991883" name="ID-2991883"></a><input class="infraCheckbox" id="chkGeradosItem9" name="chkGeradosItem9" tabindex="1002" title="00025.001060/2021-02" type="checkbox" value="2991883" aria-label="Tipo Tecnologia - Desenvolvimento e Manutenção de Sistemas e Portais" onclick="infraSelecionarItens(this,'Gerados');"/></td>
<td width="20%"><a href="controlador.php?acao=anotacao_registrar&acao_origem=procedimento_controlar&acao_retorno=procedimento_controlar&id_protocolo=2991883&infra_sistema=100000100&infra_unidade_atual=110000302&infra_hash=9ec9b3027fee5631b9c3743aa15db762814daede5f3ecfb505cafb65cecbcbeb" aria-label="Anotação / Verificar se a demanda foi totalmente atendida, caso negativo dar andamento. / fernandarsa em 22/05/2023 17:51" onmouseover="return infraTooltipMostrar('Verificar se a demanda foi totalmente atendida, caso negativo dar andamento.','fernandarsa em 22/05/2023 17:51');" onmouseout="return infraTooltipOcultar();"><img src="svg/anotacao1.svg?18" class="imagemStatus" /></a><a href="controlador.php?acao=andamento_marcador_gerenciar&acao_origem=procedimento_controlar&acao_retorno=procedimento_controlar&id_procedimento=2991883&infra_sistema=100000100&infra_unidade_atual=110000302&infra_hash=b76057b4b087203f0c62901f76bc68ca537d91c2e85903cab064e843b4b1153a" aria-label="Marcador / Solicitações à DITEC" onmouseover="return infraTooltipMostrar('','Solicitações à DITEC');" onmouseout="return infraTooltipOcultar();"><img src="svg/marcador_prata.svg?18" class="imagemStatus" /></a></td>
<td><a class="processoVisualizado" href="controlador.php?acao=procedimento_trabalhar&acao_origem=procedimento_controlar&acao_retorno=procedimento_controlar&id_procedimento=2991883&infra_sistema=100000100&infra_unidade_atual=110000302&infra_hash=41abe915f3c5cbbba744ae2324b633f0e25d6aef384c0577bff9befe1b8c92e6" aria-label="Tecnologia - Desenvolvimento e Manutenção de Sistemas e Portais" onmouseover="return infraTooltipMostrar('','Tecnologia - Desenvolvimento e Manutenção de Sistemas e Portais');" onmouseout="return infraTooltipOcultar();" tabindex="1002">00025.<wbr>001060/2021-02</a></td>
<td width="10%">(<a href="controlador.php?acao=procedimento_atribuicao_listar&acao_retorno=procedimento_controlar&id_usuario_atribuicao=100002258&id_procedimento=2991883&infra_sistema=100000100&infra_unidade_atual=110000302&infra_hash=b8449d56546db699cef30243dd463f821033ff5b7a30970ae49c318b357343ca" title="Atribuído para Fernanda Rodrigues Saldanha de Azevedo" class="ancoraSigla" tabindex="1002">fernandarsa</a>)</td>
</tr>
<tr id="P6430741" class="infraTrClara">
<td><a id="lnkGeradosID-6430741" name="ID-6430741"></a><input class="infraCheckbox" id="chkGeradosItem10" name="chkGeradosItem10" tabindex="1002" title="00025.000207/2025-62" type="checkbox" value="6430741" aria-label="Tipo Administrativo - Processo Organizacional / Especificação Composição do Conselho Editorial da Revista Jurídica da Presidência - RJP" onclick="infraSelecionarItens(this,'Gerados');"/></td>
<td width="20%"><a href="controlador.php?acao=andamento_marcador_gerenciar&acao_origem=procedimento_controlar&acao_retorno=procedimento_controlar&id_procedimento=6430741&infra_sistema=100000100&infra_unidade_atual=110000302&infra_hash=d487a0647b7698d71b85e74972729aaf2217f980caa2ad1f085e71055b96338f" aria-label="Marcador / Revista RJP" onmouseover="return infraTooltipMostrar('','Revista RJP');" onmouseout="return infraTooltipOcultar();"><img src="svg/marcador_rosa.svg?18" class="imagemStatus" /></a></td>
<td><a class="processoVisualizado" href="controlador.php?acao=procedimento_trabalhar&acao_origem=procedimento_controlar&acao_retorno=procedimento_controlar&id_procedimento=6430741&infra_sistema=100000100&infra_unidade_atual=110000302&infra_hash=9b5f33db38f2d7949aaae48e2cb328516896db671a2573dd12a42cd0a58b7904" aria-label="Administrativo - Processo Organizacional / Composição do Conselho Editorial da Revista Jurídica da Presidência - RJP" onmouseover="return infraTooltipMostrar('Composição do Conselho Editorial da Revista Jurídica da Presidência - RJP','Administrativo - Processo Organizacional');" onmouseout="return infraTooltipOcultar();" tabindex="1002">00025.<wbr>000207/2025-62</a></td>
<td width="10%">(<a href="controlador.php?acao=procedimento_atribuicao_listar&acao_retorno=procedimento_controlar&id_usuario_atribuicao=100014182&id_procedimento=6430741&infra_sistema=100000100&infra_unidade_atual=110000302&infra_hash=7e4394b6500d7571f74a49f2378e4aabfcd8b9b7ddf8f5f18199fcff2c1d070c" title="Atribuído para Felipe Augusto Romão" class="ancoraSigla" tabindex="1002">felipe.romao</a>)</td>
</tr>
<tr id="P6513567" class="infraTrClara">
<td><a id="lnkGeradosID-6513567" name="ID-6513567"></a><input class="infraCheckbox" id="chkGeradosItem11" name="chkGeradosItem11" tabindex="1002" title="00025.000450/2025-81" type="checkbox" value="6513567" aria-label="Tipo Pessoal - Frequência Mensal / Especificação Frequência dos Estagiários - CEJ/SAJ - 2025" onclick="infraSelecionarItens(this,'Gerados');"/></td>
<td width="20%"></td>
<td><a class="processoVisualizado" href="controlador.php?acao=procedimento_trabalhar&acao_origem=procedimento_controlar&acao_retorno=procedimento_controlar&id_procedimento=6513567&infra_sistema=100000100&infra_unidade_atual=110000302&infra_hash=36612fb83ad56cc21d508b5213fe6af1ad272383ec766a0bdf736155db7c1fc4" aria-label="Pessoal - Frequência Mensal / Frequência dos Estagiários - CEJ/SAJ - 2025" onmouseover="return infraTooltipMostrar('Frequência dos Estagiários - CEJ/SAJ - 2025','Pessoal - Frequência Mensal');" onmouseout="return infraTooltipOcultar();" tabindex="1002">00025.<wbr>000450/2025-81</a></td>
<td width="10%">(<a href="controlador.php?acao=procedimento_atribuicao_listar&acao_retorno=procedimento_controlar&id_usuario_atribuicao=100002693&id_procedimento=6513567&infra_sistema=100000100&infra_unidade_atual=110000302&infra_hash=5a3572a6a00df65b96ba2ed9ab20d809ef20b3291573066c4d577e6fcfa78617" title="Atribuído para Ricardo Brito do Nascimento" class="ancoraSigla" tabindex="1002">ricardobn</a>)</td>
</tr>
<tr id="P5767955" class="infraTrClara">
<td><a id="lnkGeradosID-5767955" name="ID-5767955"></a><input class="infraCheckbox" id="chkGeradosItem12" name="chkGeradosItem12" tabindex="1002" title="00025.001074/2024-61" type="checkbox" value="5767955" aria-label="Tipo Documentação - Transferência de Acervo para o Arquivo Central e Recolhimento ao Arquivo Nacional / Especificação Centro de Estudos Jurídicos - CEJ/SAJ/CC-PR" onclick="infraSelecionarItens(this,'Gerados');"/></td>
<td width="20%"><a href="controlador.php?acao=anotacao_registrar&acao_origem=procedimento_controlar&acao_retorno=procedimento_controlar&id_protocolo=5767955&infra_sistema=100000100&infra_unidade_atual=110000302&infra_hash=22ec61d1bd1161546dc19fff9f122e5b89160689729d2759017f5e28d48cf627" aria-label="Anotação / O Arquivo Central não está aceitando transferências no momento. Aguardar liberação de espaço físico. / hansmpf em 15/10/2024 17:19" onmouseover="return infraTooltipMostrar('O Arquivo Central não está aceitando transferências no momento. Aguardar liberação de espaço físico.','hansmpf em 15/10/2024 17:19');" onmouseout="return infraTooltipOcultar();"><img src="svg/anotacao1.svg?18" class="imagemStatus" /></a><a href="controlador.php?acao=andamento_marcador_gerenciar&acao_origem=procedimento_controlar&acao_retorno=procedimento_controlar&id_procedimento=5767955&infra_sistema=100000100&infra_unidade_atual=110000302&infra_hash=6008a9063e3fab06eedf53374baaac2a24be5bb683ff9ab0998528b2bde1aa3b" aria-label="Marcador / Gestão documental" onmouseover="return infraTooltipMostrar('','Gestão documental');" onmouseout="return infraTooltipOcultar();"><img src="svg/marcador_bege.svg?18" class="imagemStatus" /></a></td>
<td><a class="processoVisualizado" href="controlador.php?acao=procedimento_trabalhar&acao_origem=procedimento_controlar&acao_retorno=procedimento_controlar&id_procedimento=5767955&infra_sistema=100000100&infra_unidade_atual=110000302&infra_hash=f72cf5ee98cb5fdc9e5c5e44406353c23ae0958ea56b5460432d151f028351f8" aria-label="Documentação - Transferência de Acervo para o Arquivo Central e Recolhimento ao Arquivo Nacional / Centro de Estudos Jurídicos - CEJ/SAJ/CC-PR" onmouseover="return infraTooltipMostrar('Centro de Estudos Jurídicos - CEJ/SAJ/CC-PR','Documentação - Transferência de Acervo para o Arquivo Central e Recolhimento ao Arquivo Nacional');" onmouseout="return infraTooltipOcultar();" tabindex="1002">00025.<wbr>001074/2024-61</a></td>
<td width="10%">(<a href="controlador.php?acao=procedimento_atribuicao_listar&acao_retorno=procedimento_controlar&id_usuario_atribuicao=100002693&id_procedimento=5767955&infra_sistema=100000100&infra_unidade_atual=110000302&infra_hash=2c4548d22d9140620127e271889257d7dde7c7db8eee159699cd9f469013cff4" title="Atribuído para Ricardo Brito do Nascimento" class="ancoraSigla" tabindex="1002">ricardobn</a>)</td>
</tr>
<tr id="P6299248" class="infraTrClara">
<td><a id="lnkGeradosID-6299248" name="ID-6299248"></a><input class="infraCheckbox" id="chkGeradosItem13" name="chkGeradosItem13" tabindex="1002" title="00025.002684/2024-81" type="checkbox" value="6299248" aria-label="Tipo Pessoal: Processo Seletivo - Edital de Oportunidades / Especificação Programa de Estágio em Direito SAJ - Processo Seletivo nº 001/2025" onclick="infraSelecionarItens(this,'Gerados');"/></td>
<td width="20%"><a href="controlador.php?acao=andamento_marcador_gerenciar&acao_origem=procedimento_controlar&acao_retorno=procedimento_controlar&id_procedimento=6299248&infra_sistema=100000100&infra_unidade_atual=110000302&infra_hash=f04e654ddb613119176b5679feb1ad6ed3dd4caf7e24698da14aee5c9d89cdeb" aria-label="Marcador / Estagiários" onmouseover="return infraTooltipMostrar('','Estagiários');" onmouseout="return infraTooltipOcultar();"><img src="svg/marcador_roxo.svg?18" class="imagemStatus" /></a></td>
<td><a class="processoVisualizado" href="controlador.php?acao=procedimento_trabalhar&acao_origem=procedimento_controlar&acao_retorno=procedimento_controlar&id_procedimento=6299248&infra_sistema=100000100&infra_unidade_atual=110000302&infra_hash=2898148e69c43d1247a224011f7522c50b2def15346a39df1d898771ee1ad01a" aria-label="Pessoal: Processo Seletivo - Edital de Oportunidades / Programa de Estágio em Direito SAJ - Processo Seletivo nº 001/2025" onmouseover="return infraTooltipMostrar('Programa de Estágio em Direito SAJ - Processo Seletivo nº 001/2025','Pessoal: Processo Seletivo - Edital de Oportunidades');" onmouseout="return infraTooltipOcultar();" tabindex="1002">00025.<wbr>002684/2024-81</a></td>
<td width="10%">(<a href="controlador.php?acao=procedimento_atribuicao_listar&acao_retorno=procedimento_controlar&id_usuario_atribuicao=100002258&id_procedimento=6299248&infra_sistema=100000100&infra_unidade_atual=110000302&infra_hash=e8e93025c0dfc72e67696ecf0a1dbcbf98d168bbc5099d8f1bb6952970aeb0d9" title="Atribuído para Fernanda Rodrigues Saldanha de Azevedo" class="ancoraSigla" tabindex="1002">fernandarsa</a>)</td>
</tr>
<tr id="P4779694" class="infraTrClara">
<td><a id="lnkGeradosID-4779694" name="ID-4779694"></a><input class="infraCheckbox" id="chkGeradosItem14" name="chkGeradosItem14" tabindex="1002" title="00025.003480/2023-87" type="checkbox" value="4779694" aria-label="Tipo Envio de Informações / Especificação Inconstitucionalidade do inciso IX do artigo 7º da Lei nº 8.906, de 4 de julho de 1994." onclick="infraSelecionarItens(this,'Gerados');"/></td>
<td width="20%"><a href="controlador.php?acao=anotacao_registrar&acao_origem=procedimento_controlar&acao_retorno=procedimento_controlar&id_protocolo=4779694&infra_sistema=100000100&infra_unidade_atual=110000302&infra_hash=ac40dd09599ac8b1d4186559001ece2508f5c2269103b6714a7d7073d2a043ce" aria-label="Anotação / Fernanda fará o encaminhamento devido. / hansmpf em 14/06/2023 18:08" onmouseover="return infraTooltipMostrar('Fernanda fará o encaminhamento devido.','hansmpf em 14/06/2023 18:08');" onmouseout="return infraTooltipOcultar();"><img src="svg/anotacao1.svg?18" class="imagemStatus" /></a><a href="controlador.php?acao=andamento_marcador_gerenciar&acao_origem=procedimento_controlar&acao_retorno=procedimento_controlar&id_procedimento=4779694&infra_sistema=100000100&infra_unidade_atual=110000302&infra_hash=4be4296feabe583da751cef0dd8185023903b5cb0c1560c959a03704dbe445de" aria-label="Marcador / Portal da Legislação" onmouseover="return infraTooltipMostrar('','Portal da Legislação');" onmouseout="return infraTooltipOcultar();"><img src="svg/marcador_verde_amazonas.svg?18" class="imagemStatus" /></a></td>
<td><a class="processoVisualizado" href="controlador.php?acao=procedimento_trabalhar&acao_origem=procedimento_controlar&acao_retorno=procedimento_controlar&id_procedimento=4779694&infra_sistema=100000100&infra_unidade_atual=110000302&infra_hash=44a4df7864ccac4311a3a53e0ee5e3103a73734388a5be02a2cc58efc8a5eb85" aria-label="Envio de Informações / Inconstitucionalidade do inciso IX do artigo 7º da Lei nº 8.906, de 4 de julho de 1994." onmouseover="return infraTooltipMostrar('Inconstitucionalidade do inciso IX do artigo 7º da Lei nº 8.906, de 4 de julho de 1994.','Envio de Informações');" onmouseout="return infraTooltipOcultar();" tabindex="1002">00025.<wbr>003480/2023-87</a></td>
<td width="10%">(<a href="controlador.php?acao=procedimento_atribuicao_listar&acao_retorno=procedimento_controlar&id_usuario_atribuicao=100002258&id_procedimento=4779694&infra_sistema=100000100&infra_unidade_atual=110000302&infra_hash=234c1a8cddb8d3f2a730ed1846b5cad91d644ac98446681ee5e13a796fe6e348" title="Atribuído para Fernanda Rodrigues Saldanha de Azevedo" class="ancoraSigla" tabindex="1002">fernandarsa</a>)</td>
</tr>
</table>
</div>
<div id="divGeradosAreaPaginacaoInferior" class="infraAreaPaginacao">
</div>

<input type="hidden" id="hdnGeradosPaginaAtual" name="hdnGeradosPaginaAtual" value="0"/>
<input type="hidden" id="hdnGeradosHashCriterios" name="hdnGeradosHashCriterios" value="dca05dbd0d59b1672fab94262d4b57d3"/>
  </div>
</div>
    <input type="hidden" id="hdnTipoVisualizacao" name="hdnTipoVisualizacao" value="R" />
    <input type="hidden" id="hdnExibirRecebidos" name="hdnExibirRecebidos" value="false" />
    <input type="hidden" id="hdnExibirGerados" name="hdnExibirGerados" value="false" />
    <input type="hidden" id="hdnMeusProcessos" name="hdnMeusProcessos" value="T" />
    <input type="hidden" id="hdnIdBloco" name="hdnIdBloco" value="" />
    <input type="text" id="txtBloco" name="txtBloco" value=""  style="display:none"/>
    <input type="hidden" id="hdnIdSigilosos" value="" />
    <input type="hidden" id="hdnIdComMarcador" value="2113814,6455190,5357572,6360188,5806875,7109475,7052447,6961944,6961920,2991883,6430741,5767955,6299248,4779694" />
    <input type="hidden" id="hdnIdMarcador110000302" name="hdnIdMarcador110000302" value="" />
    <input type="hidden" id="hdnIdTipoProcedimento110000302" name="hdnIdTipoProcedimento110000302" value="" />
    <input type="hidden" id="hdnIdTipoPrioridade110000302" name="hdnIdTipoPrioridade110000302" value="" />
    <input type="hidden" id="hdnFlagControleProcessos" name="hdnFlagControleProcessos" value="1" />
  </div>
</form>

  <script>    divInfraMoverTopo = document.getElementById("divTabelaProcesso");</script>
</div>
</div>
</div>
<input type="hidden" id="hdnInfraPrefixoCookie" name="hdnInfraPrefixoCookie" value="PR_SEI_ricardobn"/>
<div id="infraDivImpressao" class="infraImpressao"></div>
<div id="infraBs-xs" class="d-none d-xs-block"></div>
<div id="infraBs-sm" class="d-none d-sm-block"></div>
<div id="infraBs-md" class="d-none d-md-block"></div>
<div id="infraBs-lg" class="d-none d-lg-block"></div>
</body>
</html>
"""


def action1(elements: list[Locator]) -> None:
    """Iteration over list locator."""
    for i, element in enumerate(elements):
        ic(i, element.inner_html())

def action2(elements: list[Locator]) -> None:
    """Iteration over list locator."""
    for i, element in enumerate(elements):
        ic(i, element.evaluate_all('els => els.map(el => el.href)'))

def action3(elements: list[Locator]) -> None:
    """Iteration over list locator."""
    for i, element in enumerate(elements):
        ic(i, element.evaluate_all('list => list.map(el => el.textContent)'))
        ic(i, element.evaluate_all('list => list.map(el => el.href)'))
        ic(i, element.evaluate_all('list => list.map(el => el.ariaLabel)'))

def action4(elements: list[Locator]) -> None:
    """Iteration over list locator."""
    for i, element in enumerate(elements):
        ic(i, element.evaluate_all('list => list.map(el => el.textContent)'))
        ic(i, element.evaluate_all('list => list.map(el => el.href)'))
        ic(i, element.get_attribute('href'))
        ic(i, element.get_attribute('aria-label'))


def actions(url: str = 'http://localhost:8000') -> None:
    """Automation."""
    with sync_playwright() as handler:
        browser = handler.chromium.launch(headless=False)
        ic()
        with browser.new_context() as context:
            page = context.new_page()
            page.goto(url)
            ic()
            process_receved = page.locator('#tblProcessosRecebidos')
            expect(process_receved).to_be_visible()
            ic(process_receved)
            action1(process_receved.locator('tr').all())
            action1(process_receved.locator('tr').locator('//td[3]').all())
            action1(process_receved.locator('tr').locator('nth=3').all())  # fail get 3th tr
            action1(process_receved.locator('tr').locator('//td[3]>>a').all())
            action2(process_receved.locator('tr').locator('//td[3]>>a').all())
            action3(process_receved.locator('tr').locator('//td[3]>>a').all())
            action4(process_receved.locator('tr').locator('//td[3]>>a').all())

