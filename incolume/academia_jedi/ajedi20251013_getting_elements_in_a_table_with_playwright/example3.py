"""Example 3."""

from __future__ import annotations

from icecream import ic
from playwright.sync_api import expect, sync_playwright

str_html = """
<html lang="pt-br">
<head>

<link rel="shortcut icon" sizes="any" href="favicon/favicon.ico">
<link rel="icon" type="image/svg+xml" href="favicon/favicon.svg">
<link rel="apple-touch-icon" href="favicon/apple-touch-icon.png">
<link rel="manifest" href="favicon/site.webmanifest">
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
<meta name="robots" content="noindex">
<meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
<title>SEI - Controle de Processos</title>
<link href="/infra_css/infra-tooltip.css?4.1.5-2.29.0" rel="stylesheet" type="text/css" media="all">
<link href="/infra_css/infra-barra-progresso.css?4.1.5-2.29.0" rel="stylesheet" type="text/css" media="all">
<link href="/infra_css/infra-impressao-global.css?4.1.5-2.29.0" rel="stylesheet" type="text/css" media="print">
<link href="/infra_css/infra-ajax.css?4.1.5-2.29.0" rel="stylesheet" type="text/css" media="all">
<link href="/infra_js/calendario/v2/infra-calendario.css?4.1.5-2.29.0" rel="stylesheet" type="text/css" media="all">
<link href="/infra_js/arvore/infra-arvore.css?4.1.5-2.29.0" rel="stylesheet" type="text/css" media="all">
<link href="/infra_js/mapa/infra-mapa.css?4.1.5-2.29.0" rel="stylesheet" type="text/css" media="all">
<link href="/infra_js/jquery/jquery-ui-1.13.2/jquery-ui.min.css?1.13.2" rel="stylesheet" type="text/css" media="all">
<link href="/infra_js/jquery/jquery-ui-1.13.2/jquery-ui.structure.min.css?1.13.2" rel="stylesheet" type="text/css" media="all">
<link href="/infra_js/jquery/jquery-ui-1.13.2/jquery-ui.theme.min.css?1.13.2" rel="stylesheet" type="text/css" media="all">
<link href="/infra_js/multiple-select/multiple-select.min.css?4.1.5-2.29.0" rel="stylesheet" type="text/css" media="all">
<link href="/infra_js/modal/jquery.modalLink-1.0.0.css?4.1.5-2.29.0" rel="stylesheet" type="text/css" media="all">
<link href="/infra_css/bootstrap/bootstrap-4.6.2.min.css?4.1.5-2.29.0" rel="stylesheet" type="text/css" media="all">
<link href="/infra_css/bootstrap/menu-bootstrap.css?4.1.5-2.29.0" rel="stylesheet" type="text/css" media="all">
<link href="/infra_css/infra-global-esquema-3.css?4.1.5-2.29.0" rel="stylesheet" type="text/css" media="all">
<link href="/infra_css/esquemas/azul_celeste/infra-esquema-3.css?4.1.5-2.29.0" rel="stylesheet" type="text/css" media="all">
<link href="css/infra-local-esquema-3.css?4.1.5-2.29.0" rel="stylesheet" type="text/css" media="all">
<style></style><style type="text/css">
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
<script type="text/javascript" charset="utf-8" src="/infra_js/ddslick/jquery.ddslick.min.js?4.1.5-2.29.0"></script><style id="css-ddslick" type="text/css">.dd-select{ border-radius:2px; border:solid 1px #ccc; position:relative; cursor:pointer;}.dd-desc { color:#aaa; display:block; overflow: hidden; font-weight:normal; line-height: 1.4em; }.dd-selected{ overflow:hidden; display:block; padding:10px; font-weight:bold;}.dd-pointer{ width:0; height:0; position:absolute; right:10px; top:50%; margin-top:-3px;}.dd-pointer-down{ border:solid 5px transparent; border-top:solid 5px #000; }.dd-pointer-up{border:solid 5px transparent !important; border-bottom:solid 5px #000 !important; margin-top:-8px;}.dd-options{ border:solid 1px #ccc; border-top:none; list-style:none; box-shadow:0px 1px 5px #ddd; display:none; position:absolute; z-index:2000; margin:0; padding:0;background:#fff; overflow:auto;}.dd-option{ padding:10px; display:block; border-bottom:solid 1px #ddd; overflow:hidden; text-decoration:none; color:#333; cursor:pointer;-webkit-transition: all 0.25s ease-in-out; -moz-transition: all 0.25s ease-in-out;-o-transition: all 0.25s ease-in-out;-ms-transition: all 0.25s ease-in-out; }.dd-options > li:last-child > .dd-option{ border-bottom:none;}.dd-option:hover{ background:#f3f3f3; color:#000;}.dd-selected-description-truncated { text-overflow: ellipsis; white-space:nowrap; }.dd-option-selected { background:#f6f6f6; }.dd-option-image, .dd-selected-image { vertical-align:middle; float:left; margin-right:5px; max-width:64px;}.dd-image-right { float:right; margin-right:15px; margin-left:5px;}.dd-container{ position:relative;}\u200b .dd-selected-text { font-weight:bold}\u200b</style>
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

<script type="text/javascript" charset="iso-8859-1">
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


        infraAbrirJanelaModal('controlador.php?acao=novidade_mostrar&infra_sistema=100000100&infra_unidade_atual=110000302&infra_hash=23ad56920ec8cc6b3dbbb184161a4ce4211801c26e2614096e7e7d62b3e70edc',950,500,false);

    objLupaBlocoPesquisa = new infraLupaText('txtBloco','hdnIdBloco','controlador.php?acao=bloco_selecionar_processo&tipo_selecao=1&id_object=objLupaBlocoPesquisa&infra_sistema=100000100&infra_unidade_atual=110000302&infra_hash=b89873510c60e79ae7979f4765c1c6635cabbf1ec80b7eb1f9c120dbc99ea17b');
    objLupaBlocoPesquisa.finalizarSelecao = function(){
      document.getElementById('frmProcedimentoControlar').action = 'controlador.php?acao=rel_bloco_protocolo_cadastrar&acao_origem=procedimento_controlar&acao_retorno=procedimento_controlar&infra_sistema=100000100&infra_unidade_atual=110000302&infra_hash=ff2cb2b2fcc1a48dff17eb7baabae98977e857d6c35ece51f517334d63e51558';
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
      document.getElementById('frmProcedimentoControlar').action = 'controlador.php?acao=procedimento_controlar&acao_origem=procedimento_controlar&tipo_visualizacao=R&tipo_filtro=M&infra_sistema=100000100&infra_unidade_atual=110000302&infra_hash=5e6bf7a197fcfdc0abb34083dd1801d62748c11874c05b2671a68809ab09a0c9';
    }else{
      document.getElementById('frmProcedimentoControlar').action = 'controlador.php?acao=procedimento_controlar&acao_origem=procedimento_controlar&tipo_visualizacao=R&infra_sistema=100000100&infra_unidade_atual=110000302&infra_hash=9d887ed9dbed84da78082a9e421f6254854c519c7f65388c56ee9dcb50ea2095';
    }

    document.getElementById('frmProcedimentoControlar').submit();
  }

  function filtrarTipoProcedimento(idTipoProcedimento){
    document.getElementById('hdnIdTipoProcedimento110000302').value = idTipoProcedimento;

    if (idTipoProcedimento == null){
      document.getElementById('frmProcedimentoControlar').action = 'controlador.php?acao=procedimento_controlar&acao_origem=procedimento_controlar&tipo_visualizacao=R&tipo_filtro=P&infra_sistema=100000100&infra_unidade_atual=110000302&infra_hash=2313eb952ef87e0efaa1b775b6d7cc425a2386f197550490de4b466296512e0c';
    }else{
      document.getElementById('frmProcedimentoControlar').action = 'controlador.php?acao=procedimento_controlar&acao_origem=procedimento_controlar&tipo_visualizacao=R&infra_sistema=100000100&infra_unidade_atual=110000302&infra_hash=9d887ed9dbed84da78082a9e421f6254854c519c7f65388c56ee9dcb50ea2095';
    }

    document.getElementById('frmProcedimentoControlar').submit();
  }

  function filtrarTipoPrioridade(idTipoPrioridade){
    document.getElementById('hdnIdTipoPrioridade110000302').value = idTipoPrioridade;

    if (idTipoPrioridade == null){
      document.getElementById('frmProcedimentoControlar').action = 'controlador.php?acao=procedimento_controlar&acao_origem=procedimento_controlar&tipo_visualizacao=R&tipo_filtro=R&infra_sistema=100000100&infra_unidade_atual=110000302&infra_hash=12d95188c88d9056bad71a8767654f275ec340bf629f95225b6f9ccc87392e74';
    }else{
      document.getElementById('frmProcedimentoControlar').action = 'controlador.php?acao=procedimento_controlar&acao_origem=procedimento_controlar&tipo_visualizacao=R&infra_sistema=100000100&infra_unidade_atual=110000302&infra_hash=9d887ed9dbed84da78082a9e421f6254854c519c7f65388c56ee9dcb50ea2095';
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
<body onload="inicializar();">
<button onclick="infraMoverParaTopo()" id="btnInfraTopo" class="infraButton infraCorBarraSistema"><img src="/infra_css/svg/topo.svg?2.29.0" title="Voltar ao Topo" alt="Voltar ao Topo" tabindex="32767"></button>
<div id="divInfraAreaGlobal" class="vh-100 vw-100 d-flex flex-column m-0 border-0">

      <nav id="navInfraBarraNavegacao" class="  navbar navbar-expand-md infraBarraNavegacao infraCorBarraSistema p-0">

        <div id="divInfraBarraSistema" class="flex-column w-100 h-100 infraBarraSistema">
           <div id="divInfraBarraSistemaLinha"></div>
           <h6 class="pl-3 mb-0 mx-0 d-none d-md-block infraCorBarraSuperior">PRESIDÊNCIA DA REPÚBLICA</h6>
           <h6 class="pl-3 mb-0 mx-0 d-md-none infraCorBarraSuperior">PR</h6>

          <div id="divInfraBarraSistemaMovel" class="flex-row d-flex pb-0  pl-3 d-md-none media infraBarraSistemaMovel">
            <div class="d-flex flex-grow-1 infraBarraSistemaMovelE">

               <div class="align-self-center mt-1">
                   <span id="spnInfraIdentificacaoSistema"><img src="svg/sei_barra.svg?4.1.5-2.29.0" title="Sistema Eletrônico de Informações - Versão 4.1.5"><span class="infraTituloLogoSistema">4.1.5</span></span>
               </div>
            </div>
            <div class="infraBarraSistemaMovelD d-flex flex-shrink-0">
              <div class="nav-item d-flex d-md-flex py-md-0 py-2"><a id="lnkInfraMenuSistema" onclick="infraClicarMenuBootstrap()" href="#" target="_self" title="Exibir/Ocultar Menu do Sistema" tabindex="65" class="nav-link align-self-center"><span class="font-weight-bold" style="padding:.1rem .5rem;">Menu</span></a></div><div class=" nav-item px-1 d-flex d-md-flex  py-md-0 py-2">
                  <div class="input-group align-self-center ">
                  <a id="lnkInfraUnidade" href="#" onclick="window.location.href='controlador.php?acao=infra_trocar_unidade&amp;infra_sistema=100000100&amp;infra_unidade_atual=110000302&amp;infra_hash=6c534f83f1cb81d6161a3b2d6b7d73329b776ab646e54e52ff9e7b651a7f7940';" class="form-control infraAcaoBarraConjugada" title="Centro de Estudos Jurídicos" tabindex="66">CEJ/SAJ/CC/PR</a>

             </div>
          </div>

        <a class="navbar-toggler px-1 border-0 flex-grow-0 mr-2 align-self-center media" data-toggle="collapse" data-target="#divInfraBarraSistemaPadrao" aria-controls="divInfraBarraSistemaPadrao" aria-expanded="false">
              <img id="imgInfraMenuPontosTopo" class=" align-self-center infraImg" width="24" height="24" src="/infra_css/svg/menu_pontos_topo.svg?2.29.0" tabindex="100" title="Exibir/Ocultar Ações">
            </a>

            </div>
          </div>

          <div id="divInfraBarraSistemaPadrao" class="navbar p-0 infraCorBarraSistema  collapse navbar-collapse align-self-center infraBarraSistemaPadrao">
            <div id="divInfraBarraSistemaPadraoE" class="nav-link p-0 pl-3 d-none d-md-flex infraBarraSistemaPadraoE">

              <div class="align-self-center"><img src="svg/sei_barra.svg?4.1.5-2.29.0" title="Sistema Eletrônico de Informações - Versão 4.1.5"><span class="infraTituloLogoSistema">4.1.5</span></div>
            </div>
            <div id="divInfraBarraSistemaPadraoD" class="navbar-nav  flex-grow-1 justify-content-end infraBarraSistemaPadraoD">
                 <div class="nav-item d-none d-md-flex py-md-0 py-2"><a id="lnkInfraMenuSistema" onclick="infraClicarMenuBootstrap()" href="#" target="_self" title="Exibir/Ocultar Menu do Sistema" tabindex="51" class="nav-link align-self-center"><span class="font-weight-bold" style="padding:.1rem .5rem;">Menu</span></a></div> <div class="nav-item px-1 media d-flex py-md-0 ">
                 <form class="form-inline align-self-center w-100" id="frmProtocoloPesquisaRapida" method="post" action="controlador.php?acao=protocolo_pesquisa_rapida&amp;infra_sistema=100000100&amp;infra_unidade_atual=110000302&amp;infra_hash=2188c4a4097fb55f39532d648a951d3230f22c23a28f1ebe36e3dc3dcd2465e3">
                  <div class="input-group">
                    <input type="text" id="txtPesquisaRapida" name="txtPesquisaRapida" class="form-control" placeholder="Pesquisar..." style="font-size:.8rem;height:24px;width:190px;border:0;" tabindex="52">
                    <span class="input-group-btn">
                      <span id="spnInfraUnidade" class="btn infraAcaoBarraConjugada">
                      <img src="svg/pesquisa_rapida.svg?4.1.5-2.29.0" width="20" height="20" onclick="document.getElementById('frmProtocoloPesquisaRapida').submit();" title="Pesquisa Rápida" alt="Pesquisa Rápida" tabindex="53" class="infraImg">
                      </span>
                    </span>
                  </div>
                 </form>
             </div>
          <div class=" nav-item px-1 d-none d-md-flex  py-md-0 py-2">
                  <div class="input-group align-self-center ">
                  <a id="lnkInfraUnidade" href="#" onclick="window.location.href='controlador.php?acao=infra_trocar_unidade&amp;infra_sistema=100000100&amp;infra_unidade_atual=110000302&amp;infra_hash=6c534f83f1cb81d6161a3b2d6b7d73329b776ab646e54e52ff9e7b651a7f7940';" class="form-control infraAcaoBarraConjugada" title="Centro de Estudos Jurídicos" tabindex="54">CEJ/SAJ/CC/PR</a>

             </div>
          </div>
          <div class="nav-item d-flex infraAcaoBarraSistema">
            <a class="align-self-center  d-none d-md-block" id="lnkControleProcessos" href="#" onclick="window.location.href='controlador.php?acao=procedimento_controlar&amp;reset=1&amp;infra_sistema=100000100&amp;infra_unidade_atual=110000302&amp;infra_hash=e658d9d9d798cb242b9cfdc227b37e338f10ee34466cd06c9dcb71939e47ed8f'" title="Controle de Processos" tabindex="55">
              <img src="svg/controle_processos_barra.svg?4.1.5-2.29.0" class="infraImg" title="Controle de Processos">
            </a>

            <span title="Controle de Processos" class=" nav-link d-flex d-md-none">
               <img src="svg/controle_processos_barra.svg?4.1.5-2.29.0" class="infraImg" title="Controle de Processos">
               <a class="align-self-center text-white pl-1" href="controlador.php?acao=procedimento_controlar&amp;reset=1&amp;infra_sistema=100000100&amp;infra_unidade_atual=110000302&amp;infra_hash=e658d9d9d798cb242b9cfdc227b37e338f10ee34466cd06c9dcb71939e47ed8f" title="Controle de Processos" tabindex="56">
                Controle de Processos
               </a>
            </span>
          </div>
          <div class="nav-item d-flex infraAcaoBarraSistema">
            <a class="align-self-center  d-none d-md-block" id="lnkPainelControle" href="#" onclick="window.location.href='controlador.php?acao=painel_controle_visualizar&amp;infra_sistema=100000100&amp;infra_unidade_atual=110000302&amp;infra_hash=bee5c4c975e3cdf3ae8d23be705d63df8596c4362d353f0498768611eb9338c6'" title="Painel de Controle" tabindex="57">
              <img src="svg/painel_controle_barra.svg?4.1.5-2.29.0" class="infraImg" title="Painel de Controle">
            </a>

            <span title="Painel de Controle" class=" nav-link d-flex d-md-none">
               <img src="svg/painel_controle_barra.svg?4.1.5-2.29.0" class="infraImg" title="Painel de Controle">
               <a class="align-self-center text-white pl-1" href="controlador.php?acao=painel_controle_visualizar&amp;infra_sistema=100000100&amp;infra_unidade_atual=110000302&amp;infra_hash=bee5c4c975e3cdf3ae8d23be705d63df8596c4362d353f0498768611eb9338c6" title="Painel de Controle" tabindex="58">Painel de Controle</a>
            </span>
          </div>
          <div class="nav-item d-flex infraAcaoBarraSistema">

            <a class="align-self-center  d-none d-md-block" target="_blank" href="controlador.php?acao=novidade_mostrar&amp;mostrar_todas=1&amp;infra_sistema=100000100&amp;infra_unidade_atual=110000302&amp;infra_hash=bf6fd24c3bf595138de110835496bd566e1818a8e707586a423f4e781db8b1c1" title="Novidades" tabindex="59">
              <img src="svg/novidades.svg?4.1.5-2.29.0" class="infraImg" title="Novidades">
            </a>

            <span title="Novidades" class=" nav-link   d-flex d-md-none">
               <img src="svg/novidades.svg?4.1.5-2.29.0" class="infraImg" title="Novidades">
               <a class="align-self-center text-white pl-1" target="_blank" href="controlador.php?acao=novidade_mostrar&amp;mostrar_todas=1&amp;infra_sistema=100000100&amp;infra_unidade_atual=110000302&amp;infra_hash=bf6fd24c3bf595138de110835496bd566e1818a8e707586a423f4e781db8b1c1" title="Novidades" tabindex="60">
                Novidades
               </a>
            </span>
         </div>
    <div class="nav-item d-md-flex infraAcaoBarraSistema">
      <a class="align-self-center  d-none d-md-block" id="lnkInfraAcessibilidadeSistema" href="#" onclick="window.location.href='controlador.php?acao=infra_acessibilidade_exibir&amp;infra_sistema=100000100&amp;infra_unidade_atual=110000302&amp;infra_hash=b2003b0a4d2a97d22b2358851345353ad084f2fdad012affb7d32ba9d95effbb';" title="Acessibilidade" tabindex="61">
        <img src="/infra_css/svg/acessibilidade_topo.svg?2.29.0" height="24" width="24" class="infraImg" title="Acessibilidade">
      </a>
      <span class=" nav-link   d-flex d-md-none">
         <img src="/infra_css/svg/acessibilidade_topo.svg?2.29.0" height="24" width="24" class="infraImg" title="Acessibilidade">
         <a class="align-self-center text-white pl-1" id="lnkInfraAcessibilidadeSistema" href="#" onclick="window.location.href='controlador.php?acao=infra_acessibilidade_exibir&amp;infra_sistema=100000100&amp;infra_unidade_atual=110000302&amp;infra_hash=b2003b0a4d2a97d22b2358851345353ad084f2fdad012affb7d32ba9d95effbb';" title="Acessibilidade">Acessibilidade</a>
      </span>
     </div>

    <div class="nav-item d-md-flex infraAcaoBarraSistema">
      <a class="align-self-center  d-none d-md-block" id="lnkInfraConfiguracaoSistema" href="controlador.php?acao=infra_configurar&amp;infra_sistema=100000100&amp;infra_unidade_atual=110000302&amp;infra_hash=3152c5ac8baf729c22cc9e336441c6d3039cdcb6fd7c2b9eee476f21d3608c31" title="Configurações do Sistema" tabindex="62">
        <img src="/infra_css/svg/configuracao.svg?2.29.0" height="24" width="24" class="infraImg" title="Configurações do Sistema">
      </a>
      <span class=" nav-link   d-flex d-md-none">
         <img src="/infra_css/svg/configuracao.svg?2.29.0" height="24" width="24" class="infraImg" title="Configurações do Sistema">
         <a class="align-self-center text-white pl-1" id="lnkInfraConfiguracaoSistema" href="controlador.php?acao=infra_configurar&amp;infra_sistema=100000100&amp;infra_unidade_atual=110000302&amp;infra_hash=3152c5ac8baf729c22cc9e336441c6d3039cdcb6fd7c2b9eee476f21d3608c31" title="Configurações do Sistema">
          Configurações
         </a>
      </span>
     </div>

      <div class="nav-item d-md-flex infraAcaoBarraSistema">
      <a class="align-self-center  d-none d-md-block" id="lnkUsuarioSistema" href="controlador.php?acao=infra_acesso_usuario_listar&amp;infra_sistema=100000100&amp;infra_unidade_atual=110000302&amp;infra_hash=f4d59232c985b1fe3063fc3c17d302114f0e02dfa5f0962cef26d4d05c5e411e" title="Ricardo Brito do Nascimento (ricardobn/PR)" tabindex="63">
        <img src="/infra_css/svg/usuario_topo.svg?2.29.0" height="24" width="24" class="infraImg" title="Ricardo Brito do Nascimento (ricardobn/PR)">
      </a>
      <span title="Ricardo Brito do Nascimento (ricardobn/PR)" class=" nav-link   d-flex d-md-none">
         <img src="/infra_css/svg/usuario_topo.svg?2.29.0" height="24" width="24" class="infraImg" title="Ricardo Brito do Nascimento (ricardobn/PR)">
         <a class="align-self-center text-white pl-1" id="lnkUsuarioSistema" href="controlador.php?acao=infra_acesso_usuario_listar&amp;infra_sistema=100000100&amp;infra_unidade_atual=110000302&amp;infra_hash=f4d59232c985b1fe3063fc3c17d302114f0e02dfa5f0962cef26d4d05c5e411e" title="Ricardo Brito do Nascimento (ricardobn/PR)">
          Ricardo Brito do Nascimento (ricardobn/PR)
         </a>
      </span>
      </div>

    <div class="nav-item pr-2 media infraAcaoBarraSistema">
    <a class="align-self-center d-none d-md-block" id="lnkInfraSairSistema" href="controlador.php?acao=sair&amp;infra_sistema=100000100&amp;infra_unidade_atual=110000302&amp;infra_hash=a270e1eb1545b8daccb9c5f2d6e7107e078dfe6cc213d32f28689b1c18413ecc" title="Sair do Sistema" tabindex="64">
      <img src="/infra_css/svg/sair.svg?2.29.0" height="24" width="24" class="infraImg">
    </a>
    <span class=" nav-link d-flex d-md-none">
      <img src="/infra_css/svg/sair.svg?2.29.0" height="24" width="24" class="infraImg">
       <a id="lnkInfraSairSistema" class="align-self-center text-white pl-1" href="controlador.php?acao=sair&amp;infra_sistema=100000100&amp;infra_unidade_atual=110000302&amp;infra_hash=a270e1eb1545b8daccb9c5f2d6e7107e078dfe6cc213d32f28689b1c18413ecc" title="Sair do Sistema">
        Sair
      </a>
    </span>
    </div>


            </div>
          </div>
        </div>
      </nav>
     <div id="divInfraAreaTela" style="min-height:0;" class="w-100  flex-grow-1 d-flex flex-row  divInfraAreaTela">
<div id="divInfraAreaTelaE" class="divInfraAreaTelaE d-flex flex-column infraAreaTelaEExibeGrande infraMenuAnimacao infraAreaTelaEExibePequeno">
<div id="divInfraSidebarMenu" class="infraSidebarMenu flex-grow-1" style="overflow-y: visible;"><div id="divInfraPesquisarMenu"><input type="text" autocomplete="off" id="txtInfraPesquisarMenu" class="infraPesquisarMenu infraText" onkeyup="infraFiltrarMenuBootstrap()" placeholder="Pesquisar no Menu" title="Pesquisar no Menu"></div><ul id="infraMenu">
<li><a id="linkMenu0" style="padding-left:5px" link="acompanhamento_listar" href="controlador.php?acao=acompanhamento_listar&amp;infra_item_menu=0&amp;infra_sistema=100000100&amp;infra_unidade_atual=110000302&amp;infra_hash=d94398a5bf3dc4046564d4facac9fdeaaa5744d276f0641262c578c28100dfbc"><img src="menu/acompanhamento_especial.svg?4.1.5-2.29.0" width="24" height="24"><span>Acompanhamento Especial</span></a></li>
<li><a id="linkMenu1" style="padding-left:5px" link="base_conhecimento_pesquisar" href="controlador.php?acao=base_conhecimento_pesquisar&amp;infra_item_menu=1&amp;infra_sistema=100000100&amp;infra_unidade_atual=110000302&amp;infra_hash=82be708d91e56a8a85795019c7cca692f5f02038176cea6b3b4f3771886be3bb"><img src="menu/base_conhecimento.svg?4.1.5-2.29.0" width="24" height="24"><span>Base de Conhecimento</span></a></li>
<li><a id="linkMenu2" style="padding-left:5px" data-toggle="collapse" class="infraAnchorMenu" href="#submenu2" role="button" aria-expanded="false" aria-controls="collapseMenu"><img src="menu/blocos.svg?4.1.5-2.29.0" width="24" height="24"><span>Blocos</span><img src="/infra_css/imagens/menu_seta.png" class="infraImgSetaMenu" style="width:12px;"></a>
<ul class="collapse" id="submenu2">
<li><a id="linkMenu3" style="padding-left:35px" link="bloco_assinatura_listar" href="controlador.php?acao=bloco_assinatura_listar&amp;infra_item_menu=3&amp;infra_sistema=100000100&amp;infra_unidade_atual=110000302&amp;infra_hash=6c675b6ddb44d34f231c85d47f77861ff58bfa87e5e7a95b73119893cd79e84e"><span>Assinatura</span></a></li>
<li><a id="linkMenu4" style="padding-left:35px" link="bloco_interno_listar" href="controlador.php?acao=bloco_interno_listar&amp;infra_item_menu=4&amp;infra_sistema=100000100&amp;infra_unidade_atual=110000302&amp;infra_hash=5c97d6c10bb80d98f5484abcdb12545fa3a66a2d5ddbd8c692c0f922e675c59d"><span>Internos</span></a></li>
<li><a id="linkMenu5" style="padding-left:35px" link="bloco_reuniao_listar" href="controlador.php?acao=bloco_reuniao_listar&amp;infra_item_menu=5&amp;infra_sistema=100000100&amp;infra_unidade_atual=110000302&amp;infra_hash=440cd3ecea1085ba1507de8b16e2b4dd28319b3795d6f0f0f41fd7a1379a274f"><span>Reunião</span></a></li>
</ul>
</li>
<li><a id="linkMenu6" style="padding-left:5px" link="contato_listar" href="controlador.php?acao=contato_listar&amp;infra_item_menu=6&amp;infra_sistema=100000100&amp;infra_unidade_atual=110000302&amp;infra_hash=74fa3b990da079b8d5f24401c5605c7366b8524ea8780213a85517380d242fa7"><img src="menu/contatos.svg?4.1.5-2.29.0" width="24" height="24"><span>Contatos</span></a></li>
<li><a id="linkMenu7" style="padding-left:5px" link="controle_prazo_listar" href="controlador.php?acao=controle_prazo_listar&amp;infra_item_menu=7&amp;infra_sistema=100000100&amp;infra_unidade_atual=110000302&amp;infra_hash=34632f292ca87f27789dee16b001e88c3da390513dd932d618f318b18fdeab33"><img src="menu/controle_prazo.svg?4.1.5-2.29.0" width="24" height="24"><span>Controle de Prazos</span></a></li>
<li><a id="linkMenu8" style="padding-left:5px" link="procedimento_controlar" href="controlador.php?acao=procedimento_controlar&amp;reset=1&amp;infra_item_menu=8&amp;infra_sistema=100000100&amp;infra_unidade_atual=110000302&amp;infra_hash=df3f462f1c06ca744248da91310b169efd1972d79a3056ccda1f98aaca9466ff"><img src="menu/controle_processos.svg?4.1.5-2.29.0" width="24" height="24"><span>Controle de Processos</span></a></li>
<li><a id="linkMenu9" style="padding-left:5px" data-toggle="collapse" class="infraAnchorMenu" href="#submenu9" role="button" aria-expanded="false" aria-controls="collapseMenu"><img src="menu/estatisticas.svg?4.1.5-2.29.0" width="24" height="24"><span>Estatísticas</span><img src="/infra_css/imagens/menu_seta.png" class="infraImgSetaMenu" style="width:12px;"></a>
<ul class="collapse" id="submenu9">
<li><a id="linkMenu10" style="padding-left:35px" link="gerar_estatisticas_unidade" href="controlador.php?acao=gerar_estatisticas_unidade&amp;infra_item_menu=10&amp;infra_sistema=100000100&amp;infra_unidade_atual=110000302&amp;infra_hash=8c4f2c110379ad5cdcc7f4c3cf1791589e3030da6a2c35b4a99e7e0405e6fb38"><span>Unidade</span></a></li>
<li><a id="linkMenu11" style="padding-left:35px" link="gerar_estatisticas_desempenho_processos" href="controlador.php?acao=gerar_estatisticas_desempenho_processos&amp;infra_item_menu=11&amp;infra_sistema=100000100&amp;infra_unidade_atual=110000302&amp;infra_hash=551ab100a16fb670cd4471582afb2cfd1e2574cfda8e13958fc87cb6a12934d6"><span>Desempenho de Processos</span></a></li>
</ul>
</li>
<li><a id="linkMenu12" style="padding-left:5px" link="protocolo_modelo_listar" href="controlador.php?acao=protocolo_modelo_listar&amp;infra_item_menu=12&amp;infra_sistema=100000100&amp;infra_unidade_atual=110000302&amp;infra_hash=962102068b3c335bb8360fd02cf4145cf9245bfdc5d20fb6f1b84b2f406d6ef4"><img src="menu/favoritos.svg?4.1.5-2.29.0" width="24" height="24"><span>Favoritos</span></a></li>
<li><a id="linkMenu13" style="padding-left:5px" data-toggle="collapse" class="infraAnchorMenu" href="#submenu13" role="button" aria-expanded="false" aria-controls="collapseMenu"><img src="menu/grupos.svg?4.1.5-2.29.0" width="24" height="24"><span>Grupos</span><img src="/infra_css/imagens/menu_seta.png" class="infraImgSetaMenu" style="width:12px;"></a>
<ul class="collapse" id="submenu13">
<li><a id="linkMenu14" style="padding-left:35px" link="grupo_contato_listar" href="controlador.php?acao=grupo_contato_listar&amp;infra_item_menu=14&amp;infra_sistema=100000100&amp;infra_unidade_atual=110000302&amp;infra_hash=4a2de7bcc418aa53b879fe09f810b3080c78e88ec0bfa863000636a0b73692ad"><span>Contatos</span></a></li>
<li><a id="linkMenu15" style="padding-left:35px" link="grupo_email_listar" href="controlador.php?acao=grupo_email_listar&amp;infra_item_menu=15&amp;infra_sistema=100000100&amp;infra_unidade_atual=110000302&amp;infra_hash=25ff76d279508989c15be3b4681b666aa6a469dc2bec59eb19e34c005f2eb4a1"><span>E-Mail</span></a></li>
<li><a id="linkMenu16" style="padding-left:35px" link="grupo_unidade_listar" href="controlador.php?acao=grupo_unidade_listar&amp;infra_item_menu=16&amp;infra_sistema=100000100&amp;infra_unidade_atual=110000302&amp;infra_hash=ceb2646a77205f6f393e1534d92d4ed56c4077b4873aae39e7753f757af25fc8"><span>Envio</span></a></li>
</ul>
</li>
<li><a id="linkMenu17" style="padding-left:5px" link="procedimento_escolher_tipo" href="controlador.php?acao=procedimento_escolher_tipo&amp;infra_item_menu=17&amp;infra_sistema=100000100&amp;infra_unidade_atual=110000302&amp;infra_hash=3255d27d5ace9630d52ca04c4f2d0a2beba057f0b242cfc0a592c51647c300af"><img src="menu/iniciar_processo.svg?4.1.5-2.29.0" width="24" height="24"><span>Iniciar Processo</span></a></li>
<li><a id="linkMenu18" style="padding-left:5px" link="marcador_listar" href="controlador.php?acao=marcador_listar&amp;infra_item_menu=18&amp;infra_sistema=100000100&amp;infra_unidade_atual=110000302&amp;infra_hash=57e712e1fe56e366f4630a67d61ce41d73ac95c3b40d00234eda62e159c38b27"><img src="menu/marcadores.svg?4.1.5-2.29.0" width="24" height="24"><span>Marcadores</span></a></li>
<li><a id="linkMenu19" style="padding-left:5px" link="painel_controle_visualizar" href="controlador.php?acao=painel_controle_visualizar&amp;infra_item_menu=19&amp;infra_sistema=100000100&amp;infra_unidade_atual=110000302&amp;infra_hash=312d9f1ba060976b6203803d04d90cf7c12761329e420519706e3bfd1a6b56a9"><img src="menu/painel_controle.svg?4.1.5-2.29.0" width="24" height="24"><span>Painel de Controle</span></a></li>
<li><a id="linkMenu20" style="padding-left:5px" link="protocolo_pesquisar" href="controlador.php?acao=protocolo_pesquisar&amp;infra_item_menu=20&amp;infra_sistema=100000100&amp;infra_unidade_atual=110000302&amp;infra_hash=43d476c28be9e7e5c15b1fce80d9f91b3b074ce80c0a566d9723b81adac467e3"><img src="menu/pesquisa.svg?4.1.5-2.29.0" width="24" height="24"><span>Pesquisa</span></a></li>
<li><a id="linkMenu21" style="padding-left:5px" link="controle_unidade_gerar" href="controlador.php?acao=controle_unidade_gerar&amp;infra_item_menu=21&amp;infra_sistema=100000100&amp;infra_unidade_atual=110000302&amp;infra_hash=cfbadbf749531d8b54ff1e9b96d4764ae5df81e81ed549f966c38b12a9ded63e"><img src="menu/pontos_controle.svg?4.1.5-2.29.0" width="24" height="24"><span>Pontos de Controle</span></a></li>
<li><a id="linkMenu22" style="padding-left:5px" link="procedimento_sobrestado_listar" href="controlador.php?acao=procedimento_sobrestado_listar&amp;infra_item_menu=22&amp;infra_sistema=100000100&amp;infra_unidade_atual=110000302&amp;infra_hash=c5f5ab7559386540c3b62b00149249e72a88b5ce962ea9f7e25f96dee7751485"><img src="menu/processos_sobrestados.svg?4.1.5-2.29.0" width="24" height="24"><span>Processos Sobrestados</span></a></li>
<li><a id="linkMenu23" style="padding-left:5px" link="reabertura_programada_listar" href="controlador.php?acao=reabertura_programada_listar&amp;infra_item_menu=23&amp;infra_sistema=100000100&amp;infra_unidade_atual=110000302&amp;infra_hash=c4a3d7b11bb127e4fbee8c9bd8b8498b1fd6614624ef4e7e8dd7c6ea363b4e28"><img src="menu/reabertura_programada.svg?4.1.5-2.29.0" width="24" height="24"><span>Reabertura Programada</span></a></li>
<li><a id="linkMenu24" style="padding-left:5px" data-toggle="collapse" class="infraAnchorMenu" href="#submenu24" role="button" aria-expanded="false" aria-controls="collapseMenu"><img src="menu/relatorios.svg?4.1.5-2.29.0" width="24" height="24"><span>Relatórios</span><img src="/infra_css/imagens/menu_seta.png" class="infraImgSetaMenu" style="width:12px;"></a>
<ul class="collapse" id="submenu24">
<li><a id="linkMenu25" style="padding-left:35px" link="atividade_unidade_pesquisar" href="controlador.php?acao=atividade_unidade_pesquisar&amp;infra_item_menu=25&amp;infra_sistema=100000100&amp;infra_unidade_atual=110000302&amp;infra_hash=fa33126c3fa467c1d2dc0a49aec3ef5bd0ebe73bfb6f50a3f1e8008f4ae41e4a"><span>Atividade na Unidade</span></a></li>
<li><a id="linkMenu26" style="padding-left:35px" link="md_pet_adm_vinc_consultar" href="controlador.php?acao=md_pet_adm_vinc_consultar&amp;infra_item_menu=26&amp;infra_sistema=100000100&amp;infra_unidade_atual=110000302&amp;infra_hash=d08e0d304440ad09276b53caeb682ccc9c198fa4b3c900c80e164471ddaa2996"><span>Vinculações e Procurações Eletrônicas</span></a></li>
<li><a id="linkMenu27" style="padding-left:35px" link="md_pet_int_relatorio_listar" href="controlador.php?acao=md_pet_int_relatorio_listar&amp;infra_item_menu=27&amp;infra_sistema=100000100&amp;infra_unidade_atual=110000302&amp;infra_hash=220d0d890a02e0d7c376b744e658f2a7b374dd8ec83ffd94b46518b79024409e"><span>Intimações Eletrônicas</span></a></li>
<li><a id="linkMenu28" style="padding-left:35px" data-toggle="collapse" class="infraAnchorMenu" href="#submenu28" role="button" aria-expanded="false" aria-controls="collapseMenu"><span>Processos Litigiosos</span><img src="/infra_css/imagens/menu_seta.png" class="infraImgSetaMenu" style="width:12px;"></a>
<ul class="collapse" id="submenu28">
<li><a id="linkMenu29" style="padding-left:50px" link="md_lit_relatorio_antecedente" href="controlador.php?acao=md_lit_relatorio_antecedente&amp;infra_item_menu=29&amp;infra_sistema=100000100&amp;infra_unidade_atual=110000302&amp;infra_hash=c35e2e616fc687c789e31ae52820774bcacf6d9e3527e2e25e3ddd42630d84e4"><span>Antecendentes</span></a></li>
<li><a id="linkMenu30" style="padding-left:50px" link="md_lit_relatorio_reincidencia" href="controlador.php?acao=md_lit_relatorio_reincidencia&amp;infra_item_menu=30&amp;infra_sistema=100000100&amp;infra_unidade_atual=110000302&amp;infra_hash=30dc54f91fc1274e816146092a0c6c258623d03cbe8ac74a83084b8f09a8c6f9"><span>Reincidências Específicas</span></a></li>
</ul>
</li>
</ul>
</li>
<li><a id="linkMenu31" style="padding-left:5px" link="retorno_programado_listar" href="controlador.php?acao=retorno_programado_listar&amp;infra_item_menu=31&amp;infra_sistema=100000100&amp;infra_unidade_atual=110000302&amp;infra_hash=24c299f781e3422abd9ca135ced142d6307172b02f0c36e7effca39ad2f78a7a"><img src="menu/retorno_programado.svg?4.1.5-2.29.0" width="24" height="24"><span>Retorno Programado</span></a></li>
<li><a id="linkMenu32" style="padding-left:5px" link="texto_padrao_interno_listar" href="controlador.php?acao=texto_padrao_interno_listar&amp;infra_item_menu=32&amp;infra_sistema=100000100&amp;infra_unidade_atual=110000302&amp;infra_hash=8d2370322436c2bb5e9e38e9f89bd5c67ac521f2a46099cd098d8329f7c9b2f3"><img src="menu/texto_padrao.svg?4.1.5-2.29.0" width="24" height="24"><span>Textos Padrão</span></a></li>
<li><a id="linkMenu33" style="padding-left:5px" link="pen_procedimento_expedido_listar" title="Blocos de Trâmite Externo" data-toggle="collapse" class="infraAnchorMenu" href="#submenu33" role="button" aria-expanded="false" aria-controls="collapseMenu"><img src="modulos/pen/imagens/menu//pen_tramite_externo_lote.svg?4.1.5-2.29.0" width="24" height="24"><span>Tramita GOV.BR</span><img src="/infra_css/imagens/menu_seta.png" class="infraImgSetaMenu" style="width:12px;"></a>
<ul class="collapse" id="submenu33">
<li><a id="linkMenu34" style="padding-left:35px" link="md_pen_tramita_em_bloco" href="controlador.php?acao=md_pen_tramita_em_bloco&amp;infra_item_menu=34&amp;infra_sistema=100000100&amp;infra_unidade_atual=110000302&amp;infra_hash=af4398fb775c78b59c9e7a2c62f7b4d0e28ad773511c728c47f9744587d87494"><span>Blocos de Trâmite Externo</span></a></li>
<li><a id="linkMenu35" style="padding-left:35px" link="pen_procedimento_expedido_listar" href="controlador.php?acao=pen_procedimento_expedido_listar&amp;infra_item_menu=35&amp;infra_sistema=100000100&amp;infra_unidade_atual=110000302&amp;infra_hash=1e7c050f954f6143804d4d16b1722ffc4e059c3fd320532914c2c506ecfff820"><span>Processos em Tramitação Externa</span></a></li>
</ul>
</li>
</ul>
</div>
<script type="text/javascript">infraSetarMenuBootstrap("procedimento_controlar")</script><!--LOGO--><script>document.querySelector("div.infraSidebarMenu").style.overflowY = "visible";</script><div style="font-size: 12px; text-align: center; background-color: #f5f6f7"><div style="height: 12px; margin-bottom: 22px; background-color: var(--color-primary-default);"></div><p style="text-align: left; margin: 15px 5px 5px 5px;"><strong style="font-weight: bolder">Abra o aplicativo do SEI! e faça a leitura do código abaixo para sincronizá-lo com sua conta.</strong></p><img style="margin: 20px auto 6px;" align="center" src="data:image/png;base64, iVBORw0KGgoAAAANSUhEUgAAAFYAAABWAQMAAABvmPO0AAAABlBMVEX///8AAABVwtN+AAAACXBIWXMAAA7EAAAOxAGVKw4bAAABUElEQVQ4jXXTQWoFMQgGYMFtwKsI2Qa8uuA2kKsE3ArW15b2OaVhmPlWifF3AP5ZkiP4XvG8zYyLnNedwM3TccxUc3laXGws++OxVN394dozE+f53v/HkvNrfdbza4ABulnvZ9W/Fo9zjPbY2kzr2oxdpdzmSXgdhpNqMw0zFANmbn59zE8M0uY6BXPfzKqtOckHzy0TmqeickytWprZ1hkmEUebcclZviWdm4k2xazntf+bK4ktYter5nfLAWOUrQbNFHVc5PDLzViXCRCd1dzmCNZ10VY3+JHNOYZ1rzCFqxUdN0u9HNepqJsBDHUpnuDmmkmu0YiF3ZU+Xb/k3j1nJOGo7kIzV6ZMxrYfJsxhKZndVd1ecWcNfbMkUwht527GsbJOuq9M3zx91pBJhacPr2V3Cyg/jSkQWD1/d+XGKtOq8831j8hGCXJo/md9AA+MoDIfjdYaAAAAAElFTkSuQmCC"></div></div>
<div id="divInfraAreaTelaD" class=" flex-grow-1 px-3">




<form id="frmProcedimentoControlar" class="h-100" method="post" action="controlador.php?acao=procedimento_controlar&amp;acao_origem=procedimento_controlar&amp;tipo_filtro=&amp;infra_sistema=100000100&amp;infra_unidade_atual=110000302&amp;infra_hash=31082052d5be67e5985a73f02afe944be6f19ec56b35eedae244d42e793efe71">
  <div id="divControleProcessosConteudo" class="h-100  d-flex flex-column"><div id="divInfraBarraAcesso" class="infraBarraAcesso"><span><a title="Ver últimos acessos" href="controlador.php?acao=infra_acesso_usuario_listar&amp;infra_sistema=100000100&amp;infra_unidade_atual=110000302&amp;infra_hash=f4d59232c985b1fe3063fc3c17d302114f0e02dfa5f0962cef26d4d05c5e411e">Último acesso na quarta-feira, 15 de outubro às 08:55.</a></span></div><div id="divInfraBarraLocalizacao" class="infraBarraLocalizacao" tabindex="450">Controle de Processos</div>

    <div class="barraBotoesSEIMovel">
        <a class="btn d-md-none" data-toggle="collapse" href="#collapseControle" role="button" aria-expanded="true" aria-controls="collapseControle" title="Exibir/Ocultar Ícones" tabindex="451">
          <img src="/infra_css/svg/menu_pontos.svg" width="32" height="32">
        </a>
    </div>

    <div class="collapse d-md-block" id="collapseControle">
        <div id="divBotoesControleProcessos" class="barraBotoesSEI">
          <a href="#" onclick="return acaoControleProcessos('controlador.php?acao=procedimento_enviar&amp;acao_origem=procedimento_controlar&amp;acao_retorno=procedimento_controlar&amp;infra_sistema=100000100&amp;infra_unidade_atual=110000302&amp;infra_hash=95a2d146cda5182b6f74a8a99b8c5d0987f42a9dde4f91f927b6a98502721db5', true, false);" tabindex="452"><img src="svg/processo_enviar.svg?18" alt="Enviar Processo" title="Enviar Processo"></a>
<a href="#" onclick="return acaoControleProcessos('controlador.php?acao=procedimento_atualizar_andamento&amp;acao_origem=procedimento_controlar&amp;acao_retorno=procedimento_controlar&amp;infra_sistema=100000100&amp;infra_unidade_atual=110000302&amp;infra_hash=3dd026f2333dc50f30415f89f7309b980f4de48f2fc1375fedfa861241350348', true, true);" tabindex="452"><img src="svg/processo_atualizar_andamento.svg?18" alt="Atualizar Andamento" title="Atualizar Andamento"></a>
<a href="#" onclick="return acaoControleProcessos('controlador.php?acao=procedimento_atribuicao_cadastrar&amp;acao_origem=procedimento_controlar&amp;acao_retorno=procedimento_controlar&amp;infra_sistema=100000100&amp;infra_unidade_atual=110000302&amp;infra_hash=52578a57aa7981b9c85ebee9d14f81f93c3f2b21769c7bd2949d13a04d160870', true, false);" tabindex="452"><img src="svg/processo_atribuir.svg?18" alt="Atribuição de Processos" title="Atribuição de Processos"></a>
<a href="#" onclick="return acaoBlocoProcessar();" tabindex="452"><img src="svg/bloco_incluir_protocolo.svg?18" alt="Incluir em Bloco" title="Incluir em Bloco"></a>
<a href="#" onclick="return acaoControleProcessos('controlador.php?acao=procedimento_sobrestar&amp;acao_origem=procedimento_controlar&amp;acao_retorno=procedimento_controlar&amp;infra_sistema=100000100&amp;infra_unidade_atual=110000302&amp;infra_hash=ae417f6042c887873af6303021d79c6ed5b3cb0b7223710e05fbf2973a246b5a', true, false);" tabindex="452"><img src="svg/processo_sobrestar.svg?18" alt="Sobrestar Processo" title="Sobrestar Processo"></a>
<a href="#" onclick="return acaoControleProcessos('controlador.php?acao=procedimento_concluir&amp;acao_origem=procedimento_controlar&amp;acao_retorno=procedimento_controlar&amp;infra_sistema=100000100&amp;infra_unidade_atual=110000302&amp;infra_hash=9d7887d1a6127c89204f8064ec68275b32a1a9aa74d07f82fc04e0780c43ad18', true, true);" tabindex="452"><img src="svg/processo_concluir.svg?18" alt="Concluir Processo nesta Unidade" title="Concluir Processo nesta Unidade"></a>
<a href="#" onclick="return acaoControleProcessos('controlador.php?acao=anotacao_registrar&amp;acao_origem=procedimento_controlar&amp;acao_retorno=procedimento_controlar&amp;infra_sistema=100000100&amp;infra_unidade_atual=110000302&amp;infra_hash=a3fe9127148ce616c7c5035a3a3fbe9f53177923b91135896dc302ec6c6d072c', true, true);" tabindex="452"><img src="svg/anotacao_cadastro.svg?18" alt="Anotações" title="Anotações"></a>
<a href="#" onclick="return acaoControleProcessos('controlador.php?acao=acompanhamento_cadastrar&amp;acao_origem=procedimento_controlar&amp;acao_retorno=procedimento_controlar&amp;infra_sistema=100000100&amp;infra_unidade_atual=110000302&amp;infra_hash=c530771212f612b3b9f1f3bc5725a774fb1964848fbb408583ce62734eff6ce7', true, true);" tabindex="452"><img src="svg/acompanhamento_especial_cadastro.svg?18" alt="Acompanhamento Especial" title="Acompanhamento Especial"></a>
<a href="#" onclick="return acaoControleProcessos('controlador.php?acao=documento_gerar_multiplo&amp;acao_origem=procedimento_controlar&amp;acao_retorno=procedimento_controlar&amp;infra_sistema=100000100&amp;infra_unidade_atual=110000302&amp;infra_hash=f7d4bbbf1dc0e783c26e804b96d93cc5b78e18b43829fbaf19a87fce7483f32d', true, true);" tabindex="452"><img src="svg/documento_incluir.svg?18" alt="Incluir Documento" title="Incluir Documento"></a>
<a href="#" onclick="return acaoControleProcessos('controlador.php?acao=andamento_situacao_gerenciar&amp;acao_origem=procedimento_controlar&amp;acao_retorno=procedimento_controlar&amp;infra_sistema=100000100&amp;infra_unidade_atual=110000302&amp;infra_hash=c9a60687ebcda0b834fb8e662894d19b1da105f317cb33998ba76e467641e29f', true, false);" tabindex="452"><img src="svg/situacao_gerenciar.svg?18" alt="Gerenciar Ponto de Controle" title="Gerenciar Ponto de Controle"></a>
<a href="#" onclick="return acaoControleProcessos('controlador.php?acao=andamento_marcador_cadastrar&amp;acao_origem=procedimento_controlar&amp;acao_retorno=procedimento_controlar&amp;infra_sistema=100000100&amp;infra_unidade_atual=110000302&amp;infra_hash=af2219fde6668a0ab1de093591deef96b6fb961d14e16197e2cecfd73cf93d45', true, true);" tabindex="452"><img src="svg/marcador_adicionar.svg?18" alt="Adicionar Marcador" title="Adicionar Marcador"></a>
<a href="#" onclick="return acaoRemoverMarcadorProcessar('controlador.php?acao=andamento_marcador_remover&amp;acao_origem=procedimento_controlar&amp;acao_retorno=procedimento_controlar&amp;infra_sistema=100000100&amp;infra_unidade_atual=110000302&amp;infra_hash=e7849e90b6eacee11cb6882771b61755457530ce99611169f5ecf929513f0b97', true, true);" tabindex="452"><img src="svg/marcador_remover.svg?18" alt="Remover Marcador" title="Remover Marcador"></a>
<a href="#" onclick="return acaoControleProcessos('controlador.php?acao=controle_prazo_definir&amp;acao_origem=procedimento_controlar&amp;acao_retorno=procedimento_controlar&amp;infra_sistema=100000100&amp;infra_unidade_atual=110000302&amp;infra_hash=b219ae77c66abdd18b31d3165f4a58edc5f7113c76d7c1ee665c5ad3fe77eb68', true, true);" tabindex="452"><img src="svg/controle_prazo_gerenciar.svg?18" alt="Controle de Prazos" title="Controle de Prazos"></a>
        </div>
    </div>

    <div id="divFiltro" class="row justify-content-center justify-content-md-start">

<div class=" col-6 p-1 col-md-auto mr-md-3 "><a id="lnkVisualizacaoDetalhada" href="javascript:void(0);" onclick="trocarVisualizacao('D');" class="ancoraPadraoPreta p-0" tabindex="453">Visualização detalhada</a></div>

<div class=" col-6 p-1 col-md-auto mr-md-3  "><a id="lnkAtribuidosMim" href="javascript:void(0);" onclick="verMeusProcessos('M');" class="ancoraPadraoPreta p-0" tabindex="454">Ver atribuídos a mim</a></div>

<div class=" col-6 p-1 col-md-auto mr-md-3 "><a href="controlador.php?acao=procedimento_controlar&amp;acao_origem=procedimento_controlar&amp;tipo_filtro=M&amp;infra_sistema=100000100&amp;infra_unidade_atual=110000302&amp;infra_hash=2a7fae00e173061e957d69e5819547a8f32e5688c7e80918e5e636ebf8cb14e3" class="ancoraPadraoPreta p-0" tabindex="455">Ver por marcadores</a></div>

<div class=" col-6 p-1 col-md-auto mr-md-3  "><a href="controlador.php?acao=procedimento_controlar&amp;acao_origem=procedimento_controlar&amp;tipo_filtro=P&amp;infra_sistema=100000100&amp;infra_unidade_atual=110000302&amp;infra_hash=fb9121b113b3beace1834c6d716ebe2173870832efb1da1be39eb7327eb40853" class="ancoraPadraoPreta p-0" tabindex="456">Ver por tipo</a></div>

<div class=" col-6 p-1 col-md-auto mr-md-3  "><a href="controlador.php?acao=procedimento_controlar&amp;acao_origem=procedimento_controlar&amp;tipo_filtro=R&amp;infra_sistema=100000100&amp;infra_unidade_atual=110000302&amp;infra_hash=667cdaf9f99a8775eede31007a605552a1794daef071e165a08880d65640fdd7" class="ancoraPadraoPreta p-0" tabindex="457">Ver por prioridade</a></div>
    </div>
    <div style="overflow-y: auto;min-height: 200px;margin-top:5px;" class="flex-grow-1 row mx-0 mb-0  d-flex divTabelaProcesso" id="divTabelaProcesso">
        <div class="d-flex justify-content-center w-100 d-md-none" style="height: 25px;">
                <a class="ml-0 mt-1 pl-0 ancoraPadraoAzul   d-md-none mx-auto" href="#" onclick="alterarVisualizacaoTabela('hdnExibirRecebidos','true','hdnExibirGerados')" tabindex="1003">
                  Processos Recebidos
                </a>
                 <a class="ml-0 mt-1 pl-0 ancoraPadraoAzul  d-md-none mx-auto" href="#" onclick="alterarVisualizacaoTabela('hdnExibirGerados','true','hdnExibirRecebidos')" tabindex="1004">
                    Processos Gerados
                </a>
        </div>     <div id="divRecebidos" class="ml-0  pl-0 d-none  d-md-block  col-12 col-md-6">
<div id="divRecebidosAreaPaginacaoSuperior" class="infraAreaPaginacao">
</div>
<div id="divRecebidosAreaTabela" class="infraAreaTabela">
<table id="tblProcessosRecebidos" width="100%" border="0" cellspacing="0" cellpadding="1" class="infraTable tabelaControle" summary="Tabela de Processos Recebidos." tabindex="1001">
<caption class="infraCaption">Processos recebidos (14 registros):</caption><tbody><tr><th class="infraTh" width="5%"><a href="javascript:void(0);" id="lnkInfraCheck" onclick="infraSelecaoMultipla('Recebidos');" tabindex="1001"><img src="/infra_css/svg/check.svg" id="imgRecebidosCheck" title="Selecionar Tudo" alt="Selecionar Tudo" class="infraImg"></a></th>
<th class="infraTh" colspan="3">Recebidos</th>
</tr>
<tr id="P6779498" class="infraTrClara">
<td><a id="lnkRecebidosID-6779498" name="ID-6779498"></a><div class="infraCheckboxDiv"><input class="infraCheckboxInput" id="chkRecebidosItem0" name="chkRecebidosItem0" tabindex="1001" title="00025.001307/2025-14" type="checkbox" value="6779498" aria-label="Tipo Pedidos e informações diversas - Outros / Especificação Alojamento Programa de Intercâmbio SAJ 2025" onclick="infraSelecionarItens(this,'Recebidos');"><label class="infraCheckboxLabel" for="chkRecebidosItem0" title="00025.001307/2025-14"></label></div></td>
<td width="20%"><img src="modulos/peticionamento/imagens/svg/peticionamento_intercorrente.svg?18" onmouseout="return infraTooltipOcultar();" onmouseover="return infraTooltipMostrar(&quot;Intercorrente: 15/10/2025&quot;,&quot;Peticionamento Eletrônico&quot;);" style="width:24px;" tabindex="1001"></td>
<td><a class="processoVisualizado" href="controlador.php?acao=procedimento_trabalhar&amp;acao_origem=procedimento_controlar&amp;acao_retorno=procedimento_controlar&amp;id_procedimento=6779498&amp;infra_sistema=100000100&amp;infra_unidade_atual=110000302&amp;infra_hash=010a5504d639c268ed2042953689774181d90469a4e4a6be1e9e9f73bdebb5dd" aria-label="Pedidos e informações diversas - Outros / Alojamento Programa de Intercâmbio SAJ 2025" onmouseover="return infraTooltipMostrar('Alojamento Programa de Intercâmbio SAJ 2025','Pedidos e informações diversas - Outros');" onmouseout="return infraTooltipOcultar();" tabindex="1001">00025.<wbr>001307/2025-14</a></td>
<td width="10%">(<a href="controlador.php?acao=procedimento_atribuicao_listar&amp;acao_retorno=procedimento_controlar&amp;id_usuario_atribuicao=100014422&amp;id_procedimento=6779498&amp;infra_sistema=100000100&amp;infra_unidade_atual=110000302&amp;infra_hash=5f0e020b144cb0ed86478ae564d35be2152680b53b9df79f0bb5849c09ad7083" title="Atribuído para Emerson Nogueira Santana" class="ancoraSigla" tabindex="1001">emerson.santana</a>)</td>
</tr>
<tr id="P7093872" class="infraTrClara">
<td><a id="lnkRecebidosID-7093872" name="ID-7093872"></a><div class="infraCheckboxDiv"><input class="infraCheckboxInput" id="chkRecebidosItem1" name="chkRecebidosItem1" tabindex="1001" title="00001.006667/2025-72" type="checkbox" value="7093872" aria-label="Tipo Envio de Informações / Especificação OFÍCIO SEI Nº 6266/2025/MPO - Normas legais pendentes de regulamentação. Processo SEI/PR nº 00025.00" onclick="infraSelecionarItens(this,'Recebidos');"><label class="infraCheckboxLabel" for="chkRecebidosItem1" title="00001.006667/2025-72"></label></div></td>
<td width="20%"><img src="modulos/peticionamento/imagens/svg/peticionamento_processo_novo.svg?18" onmouseout="return infraTooltipOcultar();" onmouseover="return infraTooltipMostrar(&quot;Processo Novo: 10/10/2025&quot;,&quot;Peticionamento Eletrônico&quot;);" style="width:24px;" tabindex="1001"></td>
<td><a class="processoVisualizado" href="controlador.php?acao=procedimento_trabalhar&amp;acao_origem=procedimento_controlar&amp;acao_retorno=procedimento_controlar&amp;id_procedimento=7093872&amp;infra_sistema=100000100&amp;infra_unidade_atual=110000302&amp;infra_hash=a83c7a5a1188b9550d7c37b5b36104a2dec9fe51580116154210e251a643575d" aria-label="Envio de Informações / OFÍCIO SEI Nº 6266/2025/MPO - Normas legais pendentes de regulamentação. Processo SEI/PR nº 00025.00" onmouseover="return infraTooltipMostrar('OFÍCIO SEI Nº 6266/2025/MPO - Normas legais pendentes de regulamentação. Processo SEI/PR nº 00025.00','Envio de Informações');" onmouseout="return infraTooltipOcultar();" tabindex="1001">00001.<wbr>006667/2025-72</a></td>
<td width="10%">&nbsp;</td>
</tr>
<tr id="P7096637" class="infraTrClara">
<td><a id="lnkRecebidosID-7096637" name="ID-7096637"></a><div class="infraCheckboxDiv"><input class="infraCheckboxInput" id="chkRecebidosItem2" name="chkRecebidosItem2" tabindex="1001" title="00001.006711/2025-44" type="checkbox" value="7096637" aria-label="Tipo Documentos para a Casa Civil da Presidência da República / Especificação Normas legais pendentes de regulamentação." onclick="infraSelecionarItens(this,'Recebidos');"><label class="infraCheckboxLabel" for="chkRecebidosItem2" title="00001.006711/2025-44"></label></div></td>
<td width="20%"><img src="modulos/peticionamento/imagens/svg/peticionamento_processo_novo.svg?18" onmouseout="return infraTooltipOcultar();" onmouseover="return infraTooltipMostrar(&quot;Processo Novo: 13/10/2025&quot;,&quot;Peticionamento Eletrônico&quot;);" style="width:24px;" tabindex="1001"></td>
<td><a class="processoVisualizado" href="controlador.php?acao=procedimento_trabalhar&amp;acao_origem=procedimento_controlar&amp;acao_retorno=procedimento_controlar&amp;id_procedimento=7096637&amp;infra_sistema=100000100&amp;infra_unidade_atual=110000302&amp;infra_hash=aec00f1910ff86c6e7eb788e67362d813444d44c699b513ee832a8bc2f24022e" aria-label="Documentos para a Casa Civil da Presidência da República / Normas legais pendentes de regulamentação." onmouseover="return infraTooltipMostrar('Normas legais pendentes de regulamentação.','Documentos para a Casa Civil da Presidência da República');" onmouseout="return infraTooltipOcultar();" tabindex="1001">00001.<wbr>006711/2025-44</a></td>
<td width="10%">&nbsp;</td>
</tr>
<tr id="P7045049" class="infraTrClara">
<td><a id="lnkRecebidosID-7045049" name="ID-7045049"></a><div class="infraCheckboxDiv"><input class="infraCheckboxInput" id="chkRecebidosItem3" name="chkRecebidosItem3" tabindex="1001" title="00063.002635/2025-73" type="checkbox" value="7045049" aria-label="Tipo GPPR - Poder Judiciário / Especificação Referência: Medida Cautelar Na Ação Direta De Inconstitucionalidade 7236" onclick="infraSelecionarItens(this,'Recebidos');"><label class="infraCheckboxLabel" for="chkRecebidosItem3" title="00063.002635/2025-73"></label></div></td>
<td width="20%"></td>
<td><a class="processoVisualizado" href="controlador.php?acao=procedimento_trabalhar&amp;acao_origem=procedimento_controlar&amp;acao_retorno=procedimento_controlar&amp;id_procedimento=7045049&amp;infra_sistema=100000100&amp;infra_unidade_atual=110000302&amp;infra_hash=5457b9b6f66c6a0c9419743e6558c33a3c3564f34881c7c180ddc8ce4b798652" aria-label="GPPR - Poder Judiciário / Referência: Medida Cautelar Na Ação Direta De Inconstitucionalidade 7236" onmouseover="return infraTooltipMostrar('Referência: Medida Cautelar Na Ação Direta De Inconstitucionalidade 7236','GPPR - Poder Judiciário');" onmouseout="return infraTooltipOcultar();" tabindex="1001">00063.<wbr>002635/2025-73</a></td>
<td width="10%">(<a href="controlador.php?acao=procedimento_atribuicao_listar&amp;acao_retorno=procedimento_controlar&amp;id_usuario_atribuicao=100002832&amp;id_procedimento=7045049&amp;infra_sistema=100000100&amp;infra_unidade_atual=110000302&amp;infra_hash=7cda2b931bd0de9097e224f447fd35ccbb70c109dc5afcfb100c9e32d8a0a4a9" title="Atribuído para Jussimara Campos Matsumoto de Miranda" class="ancoraSigla" tabindex="1001">jussimaracmm</a>)</td>
</tr>
<tr id="P6824238" class="infraTrClara">
<td><a id="lnkRecebidosID-6824238" name="ID-6824238"></a><div class="infraCheckboxDiv"><input class="infraCheckboxInput" id="chkRecebidosItem4" name="chkRecebidosItem4" tabindex="1001" title="00025.001483/2025-48" type="checkbox" value="6824238" aria-label="Tipo Acordo de Cooperação Técnica" onclick="infraSelecionarItens(this,'Recebidos');"><label class="infraCheckboxLabel" for="chkRecebidosItem4" title="00025.001483/2025-48"></label></div></td>
<td width="20%"></td>
<td><a class="processoVisualizado" href="controlador.php?acao=procedimento_trabalhar&amp;acao_origem=procedimento_controlar&amp;acao_retorno=procedimento_controlar&amp;id_procedimento=6824238&amp;infra_sistema=100000100&amp;infra_unidade_atual=110000302&amp;infra_hash=a213dbd5453025b398b607678f752c686c1b84cb11aff3d41156b82f81a09a63" aria-label="Acordo de Cooperação Técnica" onmouseover="return infraTooltipMostrar('','Acordo de Cooperação Técnica');" onmouseout="return infraTooltipOcultar();" tabindex="1001">00025.<wbr>001483/2025-48</a></td>
<td width="10%">(<a href="controlador.php?acao=procedimento_atribuicao_listar&amp;acao_retorno=procedimento_controlar&amp;id_usuario_atribuicao=100014182&amp;id_procedimento=6824238&amp;infra_sistema=100000100&amp;infra_unidade_atual=110000302&amp;infra_hash=9075a09b117cbe63dae56a6f3969d0d27c36699bb4ea28170df87310f6b53e1a" title="Atribuído para Felipe Augusto Romão" class="ancoraSigla" tabindex="1001">felipe.romao</a>)</td>
</tr>
<tr id="P6641446" class="infraTrClara">
<td><a id="lnkRecebidosID-6641446" name="ID-6641446"></a><div class="infraCheckboxDiv"><input class="infraCheckboxInput" id="chkRecebidosItem5" name="chkRecebidosItem5" tabindex="1001" title="00063.000895/2025-12" type="checkbox" value="6641446" aria-label="Tipo GPPR - Poder Judiciário / Especificação EMB.DECL. NOS EMB.DECL. NA AÇÃO DIRETA DE INCONSTITUCIONALIDADE 2.111 DISTRITO FEDERAL" onclick="infraSelecionarItens(this,'Recebidos');"><label class="infraCheckboxLabel" for="chkRecebidosItem5" title="00063.000895/2025-12"></label></div></td>
<td width="20%"></td>
<td><a class="processoVisualizado" href="controlador.php?acao=procedimento_trabalhar&amp;acao_origem=procedimento_controlar&amp;acao_retorno=procedimento_controlar&amp;id_procedimento=6641446&amp;infra_sistema=100000100&amp;infra_unidade_atual=110000302&amp;infra_hash=a0eb6162fc57b1aab84f527311a85709bff8dde2adb707163230ea22241cc730" aria-label="GPPR - Poder Judiciário / EMB.DECL. NOS EMB.DECL. NA AÇÃO DIRETA DE INCONSTITUCIONALIDADE 2.111 DISTRITO FEDERAL" onmouseover="return infraTooltipMostrar('EMB.DECL. NOS EMB.DECL. NA AÇÃO DIRETA DE INCONSTITUCIONALIDADE 2.111 DISTRITO FEDERAL','GPPR - Poder Judiciário');" onmouseout="return infraTooltipOcultar();" tabindex="1001">00063.<wbr>000895/2025-12</a></td>
<td width="10%">(<a href="controlador.php?acao=procedimento_atribuicao_listar&amp;acao_retorno=procedimento_controlar&amp;id_usuario_atribuicao=100002258&amp;id_procedimento=6641446&amp;infra_sistema=100000100&amp;infra_unidade_atual=110000302&amp;infra_hash=f19494349616784617f2377a58c44ee8ede7b8f862ca2a06071742ac5bf99091" title="Atribuído para Fernanda Rodrigues Saldanha de Azevedo" class="ancoraSigla" tabindex="1001">fernandarsa</a>)</td>
</tr>
<tr id="P6999751" class="infraTrClara">
<td><a id="lnkRecebidosID-6999751" name="ID-6999751"></a><div class="infraCheckboxDiv"><input class="infraCheckboxInput" id="chkRecebidosItem6" name="chkRecebidosItem6" tabindex="1001" title="00063.002465/2025-27" type="checkbox" value="6999751" aria-label="Tipo GPPR - Poder Judiciário / Especificação AÇÃO DIRETA DE INCONSTITUCIONALIDADE 4.245 DISTRITO FEDERAL" onclick="infraSelecionarItens(this,'Recebidos');"><label class="infraCheckboxLabel" for="chkRecebidosItem6" title="00063.002465/2025-27"></label></div></td>
<td width="20%"></td>
<td><a class="processoVisualizado" href="controlador.php?acao=procedimento_trabalhar&amp;acao_origem=procedimento_controlar&amp;acao_retorno=procedimento_controlar&amp;id_procedimento=6999751&amp;infra_sistema=100000100&amp;infra_unidade_atual=110000302&amp;infra_hash=1240d66afec71bff39138dc15fd6e274fa2638bcb84ed540163ca9ef7ec6c4ee" aria-label="GPPR - Poder Judiciário / AÇÃO DIRETA DE INCONSTITUCIONALIDADE 4.245 DISTRITO FEDERAL" onmouseover="return infraTooltipMostrar('AÇÃO DIRETA DE INCONSTITUCIONALIDADE 4.245 DISTRITO FEDERAL','GPPR - Poder Judiciário');" onmouseout="return infraTooltipOcultar();" tabindex="1001">00063.<wbr>002465/2025-27</a></td>
<td width="10%">(<a href="controlador.php?acao=procedimento_atribuicao_listar&amp;acao_retorno=procedimento_controlar&amp;id_usuario_atribuicao=100002258&amp;id_procedimento=6999751&amp;infra_sistema=100000100&amp;infra_unidade_atual=110000302&amp;infra_hash=74062e4e4e73d63ef544cc8005d671b6b67bbfdcffae3ddb7ff1a096d8d0ef9a" title="Atribuído para Fernanda Rodrigues Saldanha de Azevedo" class="ancoraSigla" tabindex="1001">fernandarsa</a>)</td>
</tr>
<tr id="P6928110" class="infraTrClara">
<td><a id="lnkRecebidosID-6928110" name="ID-6928110"></a><div class="infraCheckboxDiv"><input class="infraCheckboxInput" id="chkRecebidosItem7" name="chkRecebidosItem7" tabindex="1001" title="00180.000519/2025-83" type="checkbox" value="6928110" aria-label="Tipo Segurança da Informação - Implementação de Ações" onclick="infraSelecionarItens(this,'Recebidos');"><label class="infraCheckboxLabel" for="chkRecebidosItem7" title="00180.000519/2025-83"></label></div></td>
<td width="20%"><a href="javascript:void(0);" aria-label="Um documento foi incluído ou assinado neste processo" onmouseover="return infraTooltipMostrar('Um documento foi incluído ou assinado neste processo');" onmouseout="return infraTooltipOcultar();" tabindex="1001"><img src="svg/exclamacao.svg?18" class="imagemStatus"></a></td>
<td><a class="processoVisualizado" href="controlador.php?acao=procedimento_trabalhar&amp;acao_origem=procedimento_controlar&amp;acao_retorno=procedimento_controlar&amp;id_procedimento=6928110&amp;infra_sistema=100000100&amp;infra_unidade_atual=110000302&amp;infra_hash=23362120dc2735985581e08056f2300486ad36e0294a010b7101f930dde1c1bd" aria-label="Segurança da Informação - Implementação de Ações" onmouseover="return infraTooltipMostrar('','Segurança da Informação - Implementação de Ações');" onmouseout="return infraTooltipOcultar();" tabindex="1001">00180.<wbr>000519/2025-83</a></td>
<td width="10%">(<a href="controlador.php?acao=procedimento_atribuicao_listar&amp;acao_retorno=procedimento_controlar&amp;id_usuario_atribuicao=100002693&amp;id_procedimento=6928110&amp;infra_sistema=100000100&amp;infra_unidade_atual=110000302&amp;infra_hash=2f7ff5ac9a723127ad7b4d2135d0a7e3cf7797c8e00bccba926a5f8992bbee16" title="Atribuído para Ricardo Brito do Nascimento" class="ancoraSigla" tabindex="1001">ricardobn</a>)</td>
</tr>
<tr id="P2113814" class="infraTrClara">
<td><a id="lnkRecebidosID-2113814" name="ID-2113814"></a><div class="infraCheckboxDiv"><input class="infraCheckboxInput" id="chkRecebidosItem8" name="chkRecebidosItem8" tabindex="1001" title="00025.000498/2020-84" type="checkbox" value="2113814" aria-label="Tipo Acordo de Cooperação Técnica / Especificação Portal da Legislação - C927 e CFSTF" onclick="infraSelecionarItens(this,'Recebidos');"><label class="infraCheckboxLabel" for="chkRecebidosItem8" title="00025.000498/2020-84"></label></div></td>
<td width="20%"><a href="controlador.php?acao=andamento_marcador_gerenciar&amp;acao_origem=procedimento_controlar&amp;acao_retorno=procedimento_controlar&amp;id_procedimento=2113814&amp;infra_sistema=100000100&amp;infra_unidade_atual=110000302&amp;infra_hash=c86222933df91afc7e9fd4a5d984f917bec0b0684614710b0158ea68c5e69170" aria-label="Marcador / Acordos de Cooperação Técnica / STF/CNJ/STJ/ENFAM - Disponibilização de hiperlinks do sistema Corpus927 - Vencimento em 24/05/2025" onmouseover="return infraTooltipMostrar('STF/CNJ/STJ/ENFAM - Disponibilização de hiperlinks do sistema Corpus927 - Vencimento em 24/05/2025','Acordos de Cooperação Técnica');" onmouseout="return infraTooltipOcultar();" tabindex="1001"><img src="svg/marcador_laranja.svg?18" class="imagemStatus"></a><a href="controlador.php?acao=controle_prazo_definir&amp;acao_origem=procedimento_controlar&amp;acao_retorno=procedimento_controlar&amp;id_controle_prazo=1797&amp;id_procedimento=2113814&amp;infra_sistema=100000100&amp;infra_unidade_atual=110000302&amp;infra_hash=eda6cbcd237155ff7f0ffefd3c5a0b481c38776172cf733cac0fb4adbdaca967" aria-label="Controle de Prazo / hansmpf 26/05/2025 (atrasado 142 dias)" onmouseover="return infraTooltipMostrar('hansmpf 26/05/2025 (atrasado 142 dias)','Controle de Prazo');" onmouseout="return infraTooltipOcultar();" tabindex="1001"><img src="svg/controle_prazo3.svg?18" class="imagemStatus"></a></td>
<td><a class="processoVisualizado" href="controlador.php?acao=procedimento_trabalhar&amp;acao_origem=procedimento_controlar&amp;acao_retorno=procedimento_controlar&amp;id_procedimento=2113814&amp;infra_sistema=100000100&amp;infra_unidade_atual=110000302&amp;infra_hash=80004e382b90eb890d2d39123c2a985ed71ae7a15c08a6c0889de00795eb6554" aria-label="Acordo de Cooperação Técnica / Portal da Legislação - C927 e CFSTF" onmouseover="return infraTooltipMostrar('Portal da Legislação - C927 e CFSTF','Acordo de Cooperação Técnica');" onmouseout="return infraTooltipOcultar();" tabindex="1001">00025.<wbr>000498/2020-84</a></td>
<td width="10%">(<a href="controlador.php?acao=procedimento_atribuicao_listar&amp;acao_retorno=procedimento_controlar&amp;id_usuario_atribuicao=100002258&amp;id_procedimento=2113814&amp;infra_sistema=100000100&amp;infra_unidade_atual=110000302&amp;infra_hash=9528f65ab21f127add8b29343813af5bb34c487f00ce463061b7d5eb8e342a29" title="Atribuído para Fernanda Rodrigues Saldanha de Azevedo" class="ancoraSigla" tabindex="1001">fernandarsa</a>)</td>
</tr>
<tr id="P6455190" class="infraTrClara">
<td><a id="lnkRecebidosID-6455190" name="ID-6455190"></a><div class="infraCheckboxDiv"><input class="infraCheckboxInput" id="chkRecebidosItem9" name="chkRecebidosItem9" tabindex="1001" title="00025.000292/2025-69" type="checkbox" value="6455190" aria-label="Tipo Patrimônio - Serviços Gráficos / Especificação Impressão de edição da Revista Jurídica da Presidência - RJP" onclick="infraSelecionarItens(this,'Recebidos');"><label class="infraCheckboxLabel" for="chkRecebidosItem9" title="00025.000292/2025-69"></label></div></td>
<td width="20%"><a href="controlador.php?acao=andamento_marcador_gerenciar&amp;acao_origem=procedimento_controlar&amp;acao_retorno=procedimento_controlar&amp;id_procedimento=6455190&amp;infra_sistema=100000100&amp;infra_unidade_atual=110000302&amp;infra_hash=61a9ee2147ff57b7eec141e25dda8ba9de4a7ef15bbaaff852b4627e43ccf954" aria-label="Marcador / Revista RJP" onmouseover="return infraTooltipMostrar('','Revista RJP');" onmouseout="return infraTooltipOcultar();" tabindex="1001"><img src="svg/marcador_rosa.svg?18" class="imagemStatus"></a></td>
<td><a class="processoVisualizado" href="controlador.php?acao=procedimento_trabalhar&amp;acao_origem=procedimento_controlar&amp;acao_retorno=procedimento_controlar&amp;id_procedimento=6455190&amp;infra_sistema=100000100&amp;infra_unidade_atual=110000302&amp;infra_hash=2af9274bc4973d251b62d1aafcf28ba8066cf1aa6d9c175922a0b33ba78cc2a1" aria-label="Patrimônio - Serviços Gráficos / Impressão de edição da Revista Jurídica da Presidência - RJP" onmouseover="return infraTooltipMostrar('Impressão de edição da Revista Jurídica da Presidência - RJP','Patrimônio - Serviços Gráficos');" onmouseout="return infraTooltipOcultar();" tabindex="1001">00025.<wbr>000292/2025-69</a></td>
<td width="10%">(<a href="controlador.php?acao=procedimento_atribuicao_listar&amp;acao_retorno=procedimento_controlar&amp;id_usuario_atribuicao=100014182&amp;id_procedimento=6455190&amp;infra_sistema=100000100&amp;infra_unidade_atual=110000302&amp;infra_hash=22a8b97f635e5a7c325ffd532c8d74173fe757e3eb4b0d81c2dc5e2ed2ce26af" title="Atribuído para Felipe Augusto Romão" class="ancoraSigla" tabindex="1001">felipe.romao</a>)</td>
</tr>
<tr id="P5357572" class="infraTrClara">
<td><a id="lnkRecebidosID-5357572" name="ID-5357572"></a><div class="infraCheckboxDiv"><input class="infraCheckboxInput" id="chkRecebidosItem10" name="chkRecebidosItem10" tabindex="1001" title="00025.005081/2023-51" type="checkbox" value="5357572" aria-label="Tipo Acordo de Cooperação Técnica / Especificação SAJ/CC-PR e Universidade do Estado do Rio de Janeiro - UERJ" onclick="infraSelecionarItens(this,'Recebidos');"><label class="infraCheckboxLabel" for="chkRecebidosItem10" title="00025.005081/2023-51"></label></div></td>
<td width="20%"><a href="controlador.php?acao=andamento_marcador_gerenciar&amp;acao_origem=procedimento_controlar&amp;acao_retorno=procedimento_controlar&amp;id_procedimento=5357572&amp;infra_sistema=100000100&amp;infra_unidade_atual=110000302&amp;infra_hash=4ebbeb1bcb4f24dc4201a885b0d520f9253ea48271e948389c6745a95b1aee00" aria-label="Marcador / Acordos de Cooperação Técnica / UERJ - Novo ACT" onmouseover="return infraTooltipMostrar('UERJ - Novo ACT','Acordos de Cooperação Técnica');" onmouseout="return infraTooltipOcultar();" tabindex="1001"><img src="svg/marcador_laranja.svg?18" class="imagemStatus"></a></td>
<td><a class="processoVisualizado" href="controlador.php?acao=procedimento_trabalhar&amp;acao_origem=procedimento_controlar&amp;acao_retorno=procedimento_controlar&amp;id_procedimento=5357572&amp;infra_sistema=100000100&amp;infra_unidade_atual=110000302&amp;infra_hash=a95a61bd9a5c448b59bc5b443a5c82819511e3793a113240afa0055d433a4be9" aria-label="Acordo de Cooperação Técnica / SAJ/CC-PR e Universidade do Estado do Rio de Janeiro - UERJ" onmouseover="return infraTooltipMostrar('SAJ/CC-PR e Universidade do Estado do Rio de Janeiro - UERJ','Acordo de Cooperação Técnica');" onmouseout="return infraTooltipOcultar();" tabindex="1001">00025.<wbr>005081/2023-51</a></td>
<td width="10%">(<a href="controlador.php?acao=procedimento_atribuicao_listar&amp;acao_retorno=procedimento_controlar&amp;id_usuario_atribuicao=100013482&amp;id_procedimento=5357572&amp;infra_sistema=100000100&amp;infra_unidade_atual=110000302&amp;infra_hash=c0ab1a4e02c84ed7e03e20a02b5f9c6e90faa394e955621e5eb8f706b0a7b695" title="Atribuído para Betina Stefanello Lima" class="ancoraSigla" tabindex="1001">betina.lima</a>)</td>
</tr>
<tr id="P6606937" class="infraTrClara">
<td><a id="lnkRecebidosID-6606937" name="ID-6606937"></a><div class="infraCheckboxDiv"><input class="infraCheckboxInput" id="chkRecebidosItem11" name="chkRecebidosItem11" tabindex="1001" title="00063.000721/2025-41" type="checkbox" value="6606937" aria-label="Tipo GPPR - Poder Judiciário / Especificação AÇÃO DIRETA DE INCONSTITUCIONALIDADE 5.043 DISTRITO FEDERAL" onclick="infraSelecionarItens(this,'Recebidos');"><label class="infraCheckboxLabel" for="chkRecebidosItem11" title="00063.000721/2025-41"></label></div></td>
<td width="20%"></td>
<td><a class="processoVisualizado" href="controlador.php?acao=procedimento_trabalhar&amp;acao_origem=procedimento_controlar&amp;acao_retorno=procedimento_controlar&amp;id_procedimento=6606937&amp;infra_sistema=100000100&amp;infra_unidade_atual=110000302&amp;infra_hash=ca100417b108099b783bbb86d450c32491cb3096292c8870fbfe6132606be4a4" aria-label="GPPR - Poder Judiciário / AÇÃO DIRETA DE INCONSTITUCIONALIDADE 5.043 DISTRITO FEDERAL" onmouseover="return infraTooltipMostrar('AÇÃO DIRETA DE INCONSTITUCIONALIDADE 5.043 DISTRITO FEDERAL','GPPR - Poder Judiciário');" onmouseout="return infraTooltipOcultar();" tabindex="1001">00063.<wbr>000721/2025-41</a></td>
<td width="10%">(<a href="controlador.php?acao=procedimento_atribuicao_listar&amp;acao_retorno=procedimento_controlar&amp;id_usuario_atribuicao=100002258&amp;id_procedimento=6606937&amp;infra_sistema=100000100&amp;infra_unidade_atual=110000302&amp;infra_hash=fc45cbd3cde8f93692ba83bad3c5f6ba0dbec79e3312686edd1aa8c3da6cf78c" title="Atribuído para Fernanda Rodrigues Saldanha de Azevedo" class="ancoraSigla" tabindex="1001">fernandarsa</a>)</td>
</tr>
<tr id="P6360188" class="infraTrClara">
<td><a id="lnkRecebidosID-6360188" name="ID-6360188"></a><div class="infraCheckboxDiv"><input class="infraCheckboxInput" id="chkRecebidosItem12" name="chkRecebidosItem12" tabindex="1001" title="00025.002883/2024-90" type="checkbox" value="6360188" aria-label="Tipo Consultas - Outros Entes" onclick="infraSelecionarItens(this,'Recebidos');"><label class="infraCheckboxLabel" for="chkRecebidosItem12" title="00025.002883/2024-90"></label></div></td>
<td width="20%"><a href="controlador.php?acao=andamento_marcador_gerenciar&amp;acao_origem=procedimento_controlar&amp;acao_retorno=procedimento_controlar&amp;id_procedimento=6360188&amp;infra_sistema=100000100&amp;infra_unidade_atual=110000302&amp;infra_hash=6a0bf576dc40e8f893d4fd9c6616a57f7c13fd9950ada3ce3edffce0f268b885" aria-label="Marcador / Portal da Legislação" onmouseover="return infraTooltipMostrar('','Portal da Legislação');" onmouseout="return infraTooltipOcultar();" tabindex="1001"><img src="svg/marcador_verde_amazonas.svg?18" class="imagemStatus"></a></td>
<td><a class="processoVisualizado" href="controlador.php?acao=procedimento_trabalhar&amp;acao_origem=procedimento_controlar&amp;acao_retorno=procedimento_controlar&amp;id_procedimento=6360188&amp;infra_sistema=100000100&amp;infra_unidade_atual=110000302&amp;infra_hash=ff4e95f509232d70a3b42653be1302670956026da5b5266a1682a922a023c6bf" aria-label="Consultas - Outros Entes" onmouseover="return infraTooltipMostrar('','Consultas - Outros Entes');" onmouseout="return infraTooltipOcultar();" tabindex="1001">00025.<wbr>002883/2024-90</a></td>
<td width="10%">(<a href="controlador.php?acao=procedimento_atribuicao_listar&amp;acao_retorno=procedimento_controlar&amp;id_usuario_atribuicao=100002832&amp;id_procedimento=6360188&amp;infra_sistema=100000100&amp;infra_unidade_atual=110000302&amp;infra_hash=1cc960ca3c8d384250f5d064062e2b1033096277850a0b8a42adafd268c5b3c2" title="Atribuído para Jussimara Campos Matsumoto de Miranda" class="ancoraSigla" tabindex="1001">jussimaracmm</a>)</td>
</tr>
<tr id="P5806875" class="infraTrClara">
<td><a id="lnkRecebidosID-5806875" name="ID-5806875"></a><div class="infraCheckboxDiv"><input class="infraCheckboxInput" id="chkRecebidosItem13" name="chkRecebidosItem13" tabindex="1001" title="00742.001334/2024-01" type="checkbox" value="5806875" aria-label="Tipo Pedidos e informações diversas - Outros / Especificação CAPACITAÇÃO SOBRE DECRETO 12.002, DE 22/04/2024" onclick="infraSelecionarItens(this,'Recebidos');"><label class="infraCheckboxLabel" for="chkRecebidosItem13" title="00742.001334/2024-01"></label></div></td>
<td width="20%"><a href="controlador.php?acao=andamento_marcador_gerenciar&amp;acao_origem=procedimento_controlar&amp;acao_retorno=procedimento_controlar&amp;id_procedimento=5806875&amp;infra_sistema=100000100&amp;infra_unidade_atual=110000302&amp;infra_hash=42a11f772b90355aa713ba87ff3956939a2d6b6a58937ff85df3ece3f5e31136" aria-label="Marcador / Eventos e Reuniões" onmouseover="return infraTooltipMostrar('','Eventos e Reuniões');" onmouseout="return infraTooltipOcultar();" tabindex="1001"><img src="svg/marcador_ouro.svg?18" class="imagemStatus"></a></td>
<td><a class="processoVisualizado" href="controlador.php?acao=procedimento_trabalhar&amp;acao_origem=procedimento_controlar&amp;acao_retorno=procedimento_controlar&amp;id_procedimento=5806875&amp;infra_sistema=100000100&amp;infra_unidade_atual=110000302&amp;infra_hash=92a667d7d541f858fd45ceacba3a90def255f8a7784bdd2d75e321df2390bad8" aria-label="Pedidos e informações diversas - Outros / CAPACITAÇÃO SOBRE DECRETO 12.002, DE 22/04/2024" onmouseover="return infraTooltipMostrar('CAPACITAÇÃO SOBRE DECRETO 12.002, DE 22/04/2024','Pedidos e informações diversas - Outros');" onmouseout="return infraTooltipOcultar();" tabindex="1001">00742.<wbr>001334/2024-01</a></td>
<td width="10%">(<a href="controlador.php?acao=procedimento_atribuicao_listar&amp;acao_retorno=procedimento_controlar&amp;id_usuario_atribuicao=100002258&amp;id_procedimento=5806875&amp;infra_sistema=100000100&amp;infra_unidade_atual=110000302&amp;infra_hash=aed9fe814a3ecf1e41e09bd3bbf06097c53e674c9146ad45b0de9f652d317b34" title="Atribuído para Fernanda Rodrigues Saldanha de Azevedo" class="ancoraSigla" tabindex="1001">fernandarsa</a>)</td>
</tr>
</tbody></table>
</div>

<input type="hidden" id="hdnRecebidosNroItens" name="hdnRecebidosNroItens" value="14">
<input type="hidden" id="hdnRecebidosItemId" name="hdnRecebidosItemId" value="">
<input type="hidden" id="hdnRecebidosItens" name="hdnRecebidosItens" value="6779498,7093872,7096637,7045049,6824238,6641446,6999751,6928110,2113814,6455190,5357572,6606937,6360188,5806875">
<input type="hidden" id="hdnRecebidosItensHash" name="hdnRecebidosItensHash" value="4c1129f7ca60e19e730d9ca4ce4849ed807f7f50f24f04ee76766438a38b09fd">
<input type="hidden" id="hdnRecebidosItensSelecionados" name="hdnRecebidosItensSelecionados" value="">

<input type="hidden" id="hdnGeradosNroItens" name="hdnGeradosNroItens" value="14">
<input type="hidden" id="hdnGeradosItemId" name="hdnGeradosItemId" value="">
<input type="hidden" id="hdnGeradosItens" name="hdnGeradosItens" value="7052447,6961944,5494260,7073755,7008152,7058253,6961920,6894790,2991883,6430741,6513567,5767955,6299248,4779694">
<input type="hidden" id="hdnGeradosItensHash" name="hdnGeradosItensHash" value="44e1001d678b345d984f65c8fe4092f7d9f91a43a3ff4c478b09ae628d7625f3">
<input type="hidden" id="hdnGeradosItensSelecionados" name="hdnGeradosItensSelecionados" value="">

<input type="hidden" id="hdnInfraSelecoes" name="hdnInfraSelecoes" value="Recebidos,Gerados">
<div id="divRecebidosAreaPaginacaoInferior" class="infraAreaPaginacao">
</div>

<input type="hidden" id="hdnRecebidosPaginaAtual" name="hdnRecebidosPaginaAtual" value="0">
<input type="hidden" id="hdnRecebidosHashCriterios" name="hdnRecebidosHashCriterios" value="78225ad2dec3cc10efae2a8519af7be3">
  </div>
  <div id="divGerados" class=" ml-0 pl-0  d-none d-md-block col-12 col-md-6">
<div id="divGeradosAreaPaginacaoSuperior" class="infraAreaPaginacao">
</div>
<div id="divGeradosAreaTabela" class="infraAreaTabela">
<table id="tblProcessosGerados" width="100%" border="0" cellspacing="0" cellpadding="1" class="infraTable tabelaControle" summary="Tabela de Processos Gerados." tabindex="1002">
<caption class="infraCaption">Processos gerados (14 registros):</caption><tbody><tr><th class="infraTh" width="5%"><a href="javascript:void(0);" id="lnkInfraCheck" onclick="infraSelecaoMultipla('Gerados');" tabindex="1002"><img src="/infra_css/svg/check.svg" id="imgGeradosCheck" title="Selecionar Tudo" alt="Selecionar Tudo" class="infraImg"></a></th>
<th class="infraTh" colspan="3">Gerados</th>
</tr>
<tr id="P7052447" class="infraTrClara">
<td><a id="lnkGeradosID-7052447" name="ID-7052447"></a><div class="infraCheckboxDiv"><input class="infraCheckboxInput" id="chkGeradosItem0" name="chkGeradosItem0" tabindex="1002" title="00025.002226/2025-23" type="checkbox" value="7052447" aria-label="Tipo Pessoal: Processo Seletivo - Edital de Oportunidades / Especificação Programa de Intercambio SAJ (15ª ed) - Termos de compromissos individuais; e outros documentos" onclick="infraSelecionarItens(this,'Gerados');"><label class="infraCheckboxLabel" for="chkGeradosItem0" title="00025.002226/2025-23"></label></div></td>
<td width="20%"><a href="controlador.php?acao=andamento_marcador_gerenciar&amp;acao_origem=procedimento_controlar&amp;acao_retorno=procedimento_controlar&amp;id_procedimento=7052447&amp;infra_sistema=100000100&amp;infra_unidade_atual=110000302&amp;infra_hash=ffa3bca430ee3400e0b46fc64968cfafbebe7af72c35856d4e8f6f2aa47dd42d" aria-label="Marcador / Programa de Intercâmbio / Ate 24/10/2025 23:59
Termos de compromissos individuais; e outros documentos" onmouseover="return infraTooltipMostrar('Ate 24/10/2025 23:59\nTermos de compromissos individuais; e outros documentos','Programa de Intercâmbio');" onmouseout="return infraTooltipOcultar();" tabindex="1002"><img src="svg/marcador_ouro.svg?18" class="imagemStatus"></a></td>
<td><a class="processoVisualizado" href="controlador.php?acao=procedimento_trabalhar&amp;acao_origem=procedimento_controlar&amp;acao_retorno=procedimento_controlar&amp;id_procedimento=7052447&amp;infra_sistema=100000100&amp;infra_unidade_atual=110000302&amp;infra_hash=81b28d7ca6b1cc4cbf011950608e115275556ed8443236556a84d33ec6f31d56" aria-label="Pessoal: Processo Seletivo - Edital de Oportunidades / Programa de Intercambio SAJ (15ª ed) - Termos de compromissos individuais; e outros documentos" onmouseover="return infraTooltipMostrar('Programa de Intercambio SAJ (15ª ed) - Termos de compromissos individuais; e outros documentos','Pessoal: Processo Seletivo - Edital de Oportunidades');" onmouseout="return infraTooltipOcultar();" tabindex="1002">00025.<wbr>002226/2025-23</a></td>
<td width="10%">(<a href="controlador.php?acao=procedimento_atribuicao_listar&amp;acao_retorno=procedimento_controlar&amp;id_usuario_atribuicao=100002693&amp;id_procedimento=7052447&amp;infra_sistema=100000100&amp;infra_unidade_atual=110000302&amp;infra_hash=03eac12dd137ac2bc00b62533cf53e4f66eed5f57778dd4caacb052aeea6a235" title="Atribuído para Ricardo Brito do Nascimento" class="ancoraSigla" tabindex="1002">ricardobn</a>)</td>
</tr>
<tr id="P6961944" class="infraTrClara">
<td><a id="lnkGeradosID-6961944" name="ID-6961944"></a><div class="infraCheckboxDiv"><input class="infraCheckboxInput" id="chkGeradosItem1" name="chkGeradosItem1" tabindex="1002" title="00025.001931/2025-11" type="checkbox" value="6961944" aria-label="Tipo Pedidos e informações diversas - Outros / Especificação Programa Intercâmbio SAJ (15ª ed) -  Solicitação para emissão de crachá personalizado para o evento" onclick="infraSelecionarItens(this,'Gerados');"><label class="infraCheckboxLabel" for="chkGeradosItem1" title="00025.001931/2025-11"></label></div></td>
<td width="20%"><a href="controlador.php?acao=andamento_marcador_gerenciar&amp;acao_origem=procedimento_controlar&amp;acao_retorno=procedimento_controlar&amp;id_procedimento=6961944&amp;infra_sistema=100000100&amp;infra_unidade_atual=110000302&amp;infra_hash=f4fefd0ec931f5b292af0bdb5f5b2c1061e8bb020eb7865326273617fd320277" aria-label="Marcador / Programa de Intercâmbio / Ate 17/10/2025 23:59
Credenciamento" onmouseover="return infraTooltipMostrar('Ate 17/10/2025 23:59\nCredenciamento','Programa de Intercâmbio');" onmouseout="return infraTooltipOcultar();" tabindex="1002"><img src="svg/marcador_ouro.svg?18" class="imagemStatus"></a></td>
<td><a class="processoVisualizado" href="controlador.php?acao=procedimento_trabalhar&amp;acao_origem=procedimento_controlar&amp;acao_retorno=procedimento_controlar&amp;id_procedimento=6961944&amp;infra_sistema=100000100&amp;infra_unidade_atual=110000302&amp;infra_hash=5c4325dd25ffaa34cff3930bfc5e5a6885a9f60d83903dbf082a5d72447c27fb" aria-label="Pedidos e informações diversas - Outros / Programa Intercâmbio SAJ (15ª ed) -  Solicitação para emissão de crachá personalizado para o evento" onmouseover="return infraTooltipMostrar('Programa Intercâmbio SAJ (15ª ed) -  Solicitação para emissão de crachá personalizado para o evento','Pedidos e informações diversas - Outros');" onmouseout="return infraTooltipOcultar();" tabindex="1002">00025.<wbr>001931/2025-11</a></td>
<td width="10%">(<a href="controlador.php?acao=procedimento_atribuicao_listar&amp;acao_retorno=procedimento_controlar&amp;id_usuario_atribuicao=100002693&amp;id_procedimento=6961944&amp;infra_sistema=100000100&amp;infra_unidade_atual=110000302&amp;infra_hash=c7fb0c53189b14ea94bee7b6f499fbb984f064e099b35ab6edb2db4dc20ad34f" title="Atribuído para Ricardo Brito do Nascimento" class="ancoraSigla" tabindex="1002">ricardobn</a>)</td>
</tr>
<tr id="P5494260" class="infraTrClara">
<td><a id="lnkGeradosID-5494260" name="ID-5494260"></a><div class="infraCheckboxDiv"><input class="infraCheckboxInput" id="chkGeradosItem2" name="chkGeradosItem2" tabindex="1002" title="00025.000289/2024-64" type="checkbox" value="5494260" aria-label="Tipo Envio de Informações / Especificação Documentos modelo" onclick="infraSelecionarItens(this,'Gerados');"><label class="infraCheckboxLabel" for="chkGeradosItem2" title="00025.000289/2024-64"></label></div></td>
<td width="20%"><a href="controlador.php?acao=anotacao_registrar&amp;acao_origem=procedimento_controlar&amp;acao_retorno=procedimento_controlar&amp;id_protocolo=5494260&amp;infra_sistema=100000100&amp;infra_unidade_atual=110000302&amp;infra_hash=7703d3e7ff6926d2886ef1a50ba82653fde0c69eb3b8c6b9c8edc92f008efc8e" aria-label="Anotação / Modelos de documentos para processos de novos ACTs 2024 / hansmpf em 22/02/2024 17:29" onmouseover="return infraTooltipMostrar('Modelos de documentos para processos de novos ACTs 2024','hansmpf em 22/02/2024 17:29');" onmouseout="return infraTooltipOcultar();" tabindex="1002"><img src="svg/anotacao1.svg?18" class="imagemStatus"></a></td>
<td><a class="processoVisualizado" href="controlador.php?acao=procedimento_trabalhar&amp;acao_origem=procedimento_controlar&amp;acao_retorno=procedimento_controlar&amp;id_procedimento=5494260&amp;infra_sistema=100000100&amp;infra_unidade_atual=110000302&amp;infra_hash=3b6e4d25c821fa9b4d2f5d2840383733db160abd7982b9837a9a2be8d6c6d99b" aria-label="Envio de Informações / Documentos modelo" onmouseover="return infraTooltipMostrar('Documentos modelo','Envio de Informações');" onmouseout="return infraTooltipOcultar();" tabindex="1002">00025.<wbr>000289/2024-64</a></td>
<td width="10%">(<a href="controlador.php?acao=procedimento_atribuicao_listar&amp;acao_retorno=procedimento_controlar&amp;id_usuario_atribuicao=100013821&amp;id_procedimento=5494260&amp;infra_sistema=100000100&amp;infra_unidade_atual=110000302&amp;infra_hash=50963c5b5f5e3ddf159ea0eb0b02375c9b75104582c71ee2adcea9ab5a7eec91" title="Atribuído para Ana Paula Ferreira Sebastião" class="ancoraSigla" tabindex="1002">ana.sebastiao</a>)</td>
</tr>
<tr id="P7073755" class="infraTrClara">
<td><a id="lnkGeradosID-7073755" name="ID-7073755"></a><div class="infraCheckboxDiv"><input class="infraCheckboxInput" id="chkGeradosItem3" name="chkGeradosItem3" tabindex="1002" title="00025.002284/2025-57" type="checkbox" value="7073755" aria-label="Tipo Pessoal - Comunicação/Orientação / Especificação Exercício de servidores aprovados no CNU - ATPS" onclick="infraSelecionarItens(this,'Gerados');"><label class="infraCheckboxLabel" for="chkGeradosItem3" title="00025.002284/2025-57"></label></div></td>
<td width="20%"></td>
<td><a class="processoVisualizado" href="controlador.php?acao=procedimento_trabalhar&amp;acao_origem=procedimento_controlar&amp;acao_retorno=procedimento_controlar&amp;id_procedimento=7073755&amp;infra_sistema=100000100&amp;infra_unidade_atual=110000302&amp;infra_hash=78795afb60c5464149016f8316060a053f2164383822ddabd4eb99ef1f4e8cad" aria-label="Pessoal - Comunicação/Orientação / Exercício de servidores aprovados no CNU - ATPS" onmouseover="return infraTooltipMostrar('Exercício de servidores aprovados no CNU - ATPS','Pessoal - Comunicação/Orientação');" onmouseout="return infraTooltipOcultar();" tabindex="1002">00025.<wbr>002284/2025-57</a></td>
<td width="10%">(<a href="controlador.php?acao=procedimento_atribuicao_listar&amp;acao_retorno=procedimento_controlar&amp;id_usuario_atribuicao=100002258&amp;id_procedimento=7073755&amp;infra_sistema=100000100&amp;infra_unidade_atual=110000302&amp;infra_hash=be9e7703ea1922151fb85183b846d05cc39cb5b2d2189276011f0e38b3ce787b" title="Atribuído para Fernanda Rodrigues Saldanha de Azevedo" class="ancoraSigla" tabindex="1002">fernandarsa</a>)</td>
</tr>
<tr id="P7008152" class="infraTrClara">
<td><a id="lnkGeradosID-7008152" name="ID-7008152"></a><div class="infraCheckboxDiv"><input class="infraCheckboxInput" id="chkGeradosItem4" name="chkGeradosItem4" tabindex="1002" title="00025.002084/2025-02" type="checkbox" value="7008152" aria-label="Tipo Pessoal: Processo Seletivo - Edital de Oportunidades / Especificação Programa de Estágio em Direito SAJ - Processo Seletivo nº 001/2025" onclick="infraSelecionarItens(this,'Gerados');"><label class="infraCheckboxLabel" for="chkGeradosItem4" title="00025.002084/2025-02"></label></div></td>
<td width="20%"><a href="controlador.php?acao=anotacao_registrar&amp;acao_origem=procedimento_controlar&amp;acao_retorno=procedimento_controlar&amp;id_protocolo=7008152&amp;infra_sistema=100000100&amp;infra_unidade_atual=110000302&amp;infra_hash=cee41296eecc13da3009cfbc39f6d0835a750d4577777253a98f981a9777e21e" aria-label="Anotação / Seleção Programa de Estágio em Direito / ana.sebastiao em 10/09/2025 14:48" onmouseover="return infraTooltipMostrar('Seleção Programa de Estágio em Direito','ana.sebastiao em 10/09/2025 14:48');" onmouseout="return infraTooltipOcultar();" tabindex="1002"><img src="svg/anotacao1.svg?18" class="imagemStatus"></a></td>
<td><a class="processoVisualizado" href="controlador.php?acao=procedimento_trabalhar&amp;acao_origem=procedimento_controlar&amp;acao_retorno=procedimento_controlar&amp;id_procedimento=7008152&amp;infra_sistema=100000100&amp;infra_unidade_atual=110000302&amp;infra_hash=d5d8630ac0e60b4c1cfc0623b6713ad057c9b3c03248978249a9ca293c5a65a0" aria-label="Pessoal: Processo Seletivo - Edital de Oportunidades / Programa de Estágio em Direito SAJ - Processo Seletivo nº 001/2025" onmouseover="return infraTooltipMostrar('Programa de Estágio em Direito SAJ - Processo Seletivo nº 001/2025','Pessoal: Processo Seletivo - Edital de Oportunidades');" onmouseout="return infraTooltipOcultar();" tabindex="1002">00025.<wbr>002084/2025-02</a></td>
<td width="10%">(<a href="controlador.php?acao=procedimento_atribuicao_listar&amp;acao_retorno=procedimento_controlar&amp;id_usuario_atribuicao=100013821&amp;id_procedimento=7008152&amp;infra_sistema=100000100&amp;infra_unidade_atual=110000302&amp;infra_hash=4a871adfd406b5dc4c59b0e7e79da9aaedfae7f13160c931ecbdf926470c3e86" title="Atribuído para Ana Paula Ferreira Sebastião" class="ancoraSigla" tabindex="1002">ana.sebastiao</a>)</td>
</tr>
<tr id="P7058253" class="infraTrClara">
<td><a id="lnkGeradosID-7058253" name="ID-7058253"></a><div class="infraCheckboxDiv"><input class="infraCheckboxInput" id="chkGeradosItem5" name="chkGeradosItem5" tabindex="1002" title="00025.002240/2025-27" type="checkbox" value="7058253" aria-label="Tipo Envio de Informações" onclick="infraSelecionarItens(this,'Gerados');"><label class="infraCheckboxLabel" for="chkGeradosItem5" title="00025.002240/2025-27"></label></div></td>
<td width="20%"><a href="controlador.php?acao=anotacao_registrar&amp;acao_origem=procedimento_controlar&amp;acao_retorno=procedimento_controlar&amp;id_protocolo=7058253&amp;infra_sistema=100000100&amp;infra_unidade_atual=110000302&amp;infra_hash=df31f491bc368d8c10788903f1a93b7696c47cff90deac1aff9afd89bc9fe08b" aria-label="Anotação / oficio - regulamentação de leis ordinárias / ana.sebastiao em 29/09/2025 16:09" onmouseover="return infraTooltipMostrar('oficio - regulamentação de leis ordinárias','ana.sebastiao em 29/09/2025 16:09');" onmouseout="return infraTooltipOcultar();" tabindex="1002"><img src="svg/anotacao1.svg?18" class="imagemStatus"></a></td>
<td><a class="processoVisualizado" href="controlador.php?acao=procedimento_trabalhar&amp;acao_origem=procedimento_controlar&amp;acao_retorno=procedimento_controlar&amp;id_procedimento=7058253&amp;infra_sistema=100000100&amp;infra_unidade_atual=110000302&amp;infra_hash=2be0dbcdad5cb611854b69e18f517dc0179d920f6358a346add31c4b4c92f84a" aria-label="Envio de Informações" onmouseover="return infraTooltipMostrar('','Envio de Informações');" onmouseout="return infraTooltipOcultar();" tabindex="1002">00025.<wbr>002240/2025-27</a></td>
<td width="10%">(<a href="controlador.php?acao=procedimento_atribuicao_listar&amp;acao_retorno=procedimento_controlar&amp;id_usuario_atribuicao=100013821&amp;id_procedimento=7058253&amp;infra_sistema=100000100&amp;infra_unidade_atual=110000302&amp;infra_hash=d9bb444f308d2e0923cf7fed405c9444816318b4fcbc86c1f8ec146dbc8da7db" title="Atribuído para Ana Paula Ferreira Sebastião" class="ancoraSigla" tabindex="1002">ana.sebastiao</a>)</td>
</tr>
<tr id="P6961920" class="infraTrClara">
<td><a id="lnkGeradosID-6961920" name="ID-6961920"></a><div class="infraCheckboxDiv"><input class="infraCheckboxInput" id="chkGeradosItem6" name="chkGeradosItem6" tabindex="1002" title="00025.001930/2025-69" type="checkbox" value="6961920" aria-label="Tipo Pedidos e informações diversas - Outros / Especificação Programa Intercâmbio SAJ (15ª ed) - Solicitação de transporte para os participantes" onclick="infraSelecionarItens(this,'Gerados');"><label class="infraCheckboxLabel" for="chkGeradosItem6" title="00025.001930/2025-69"></label></div></td>
<td width="20%"><a href="controlador.php?acao=andamento_marcador_gerenciar&amp;acao_origem=procedimento_controlar&amp;acao_retorno=procedimento_controlar&amp;id_procedimento=6961920&amp;infra_sistema=100000100&amp;infra_unidade_atual=110000302&amp;infra_hash=1ab813ea555b2d7f3ee11a5da5e936740c41260676f105988bfd309fa433d24f" aria-label="Marcador / Programa de Intercâmbio / Ate 31/10/2025 23:59
Transporte" onmouseover="return infraTooltipMostrar('Ate 31/10/2025 23:59\nTransporte','Programa de Intercâmbio');" onmouseout="return infraTooltipOcultar();" tabindex="1002"><img src="svg/marcador_ouro.svg?18" class="imagemStatus"></a></td>
<td><a class="processoVisualizado" href="controlador.php?acao=procedimento_trabalhar&amp;acao_origem=procedimento_controlar&amp;acao_retorno=procedimento_controlar&amp;id_procedimento=6961920&amp;infra_sistema=100000100&amp;infra_unidade_atual=110000302&amp;infra_hash=ca283c331ce51301090017c838c94272f91d8ec30b89d9f372a41ba00d910baf" aria-label="Pedidos e informações diversas - Outros / Programa Intercâmbio SAJ (15ª ed) - Solicitação de transporte para os participantes" onmouseover="return infraTooltipMostrar('Programa Intercâmbio SAJ (15ª ed) - Solicitação de transporte para os participantes','Pedidos e informações diversas - Outros');" onmouseout="return infraTooltipOcultar();" tabindex="1002">00025.<wbr>001930/2025-69</a></td>
<td width="10%">(<a href="controlador.php?acao=procedimento_atribuicao_listar&amp;acao_retorno=procedimento_controlar&amp;id_usuario_atribuicao=100002693&amp;id_procedimento=6961920&amp;infra_sistema=100000100&amp;infra_unidade_atual=110000302&amp;infra_hash=48953e82ed9b867e23ff6beb7c7f77fcd7138fb75e6bb5ef7d83056c0e6edc50" title="Atribuído para Ricardo Brito do Nascimento" class="ancoraSigla" tabindex="1002">ricardobn</a>)</td>
</tr>
<tr id="P6894790" class="infraTrClara">
<td><a id="lnkGeradosID-6894790" name="ID-6894790"></a><div class="infraCheckboxDiv"><input class="infraCheckboxInput" id="chkGeradosItem7" name="chkGeradosItem7" tabindex="1002" title="00025.001726/2025-48" type="checkbox" value="6894790" aria-label="Tipo Acordo de Cooperação Técnica / Especificação SAJ/CC-PR e Universidade XXX" onclick="infraSelecionarItens(this,'Gerados');"><label class="infraCheckboxLabel" for="chkGeradosItem7" title="00025.001726/2025-48"></label></div></td>
<td width="20%"><a href="controlador.php?acao=anotacao_registrar&amp;acao_origem=procedimento_controlar&amp;acao_retorno=procedimento_controlar&amp;id_protocolo=6894790&amp;infra_sistema=100000100&amp;infra_unidade_atual=110000302&amp;infra_hash=a46202f6262fddf0e3e4a452c1142bc01d59b63a856d52c68ea86077bc4cff15" aria-label="Anotação / modelo em construção / ana.sebastiao em 05/08/2025 13:44" onmouseover="return infraTooltipMostrar('modelo em construção','ana.sebastiao em 05/08/2025 13:44');" onmouseout="return infraTooltipOcultar();" tabindex="1002"><img src="svg/anotacao1.svg?18" class="imagemStatus"></a></td>
<td><a class="processoVisualizado" href="controlador.php?acao=procedimento_trabalhar&amp;acao_origem=procedimento_controlar&amp;acao_retorno=procedimento_controlar&amp;id_procedimento=6894790&amp;infra_sistema=100000100&amp;infra_unidade_atual=110000302&amp;infra_hash=2506dde01181da656bfc3c3118c3220f9eff7b9e51a49352e0bd74ed2f5202e6" aria-label="Acordo de Cooperação Técnica / SAJ/CC-PR e Universidade XXX" onmouseover="return infraTooltipMostrar('SAJ/CC-PR e Universidade XXX','Acordo de Cooperação Técnica');" onmouseout="return infraTooltipOcultar();" tabindex="1002">00025.<wbr>001726/2025-48</a></td>
<td width="10%">&nbsp;</td>
</tr>
<tr id="P2991883" class="infraTrClara">
<td><a id="lnkGeradosID-2991883" name="ID-2991883"></a><div class="infraCheckboxDiv"><input class="infraCheckboxInput" id="chkGeradosItem8" name="chkGeradosItem8" tabindex="1002" title="00025.001060/2021-02" type="checkbox" value="2991883" aria-label="Tipo Tecnologia - Desenvolvimento e Manutenção de Sistemas e Portais" onclick="infraSelecionarItens(this,'Gerados');"><label class="infraCheckboxLabel" for="chkGeradosItem8" title="00025.001060/2021-02"></label></div></td>
<td width="20%"><a href="controlador.php?acao=anotacao_registrar&amp;acao_origem=procedimento_controlar&amp;acao_retorno=procedimento_controlar&amp;id_protocolo=2991883&amp;infra_sistema=100000100&amp;infra_unidade_atual=110000302&amp;infra_hash=d316b5bafdd00b5dd23ec6eac878130ebcd015e1c2e3475a120e1cc1c99a8812" aria-label="Anotação / Verificar se a demanda foi totalmente atendida, caso negativo dar andamento. / fernandarsa em 22/05/2023 17:51" onmouseover="return infraTooltipMostrar('Verificar se a demanda foi totalmente atendida, caso negativo dar andamento.','fernandarsa em 22/05/2023 17:51');" onmouseout="return infraTooltipOcultar();" tabindex="1002"><img src="svg/anotacao1.svg?18" class="imagemStatus"></a><a href="controlador.php?acao=andamento_marcador_gerenciar&amp;acao_origem=procedimento_controlar&amp;acao_retorno=procedimento_controlar&amp;id_procedimento=2991883&amp;infra_sistema=100000100&amp;infra_unidade_atual=110000302&amp;infra_hash=5a7efd9aef7711d3e71c687a8936fdaaebef59b984f425f7e38c79d562aa0ac9" aria-label="Marcador / Solicitações à DITEC" onmouseover="return infraTooltipMostrar('','Solicitações à DITEC');" onmouseout="return infraTooltipOcultar();" tabindex="1002"><img src="svg/marcador_prata.svg?18" class="imagemStatus"></a></td>
<td><a class="processoVisualizado" href="controlador.php?acao=procedimento_trabalhar&amp;acao_origem=procedimento_controlar&amp;acao_retorno=procedimento_controlar&amp;id_procedimento=2991883&amp;infra_sistema=100000100&amp;infra_unidade_atual=110000302&amp;infra_hash=84bbe68fc92dab45f238c09b8ade6deffc3cc4eb30fcb4a643c920b6d650b11f" aria-label="Tecnologia - Desenvolvimento e Manutenção de Sistemas e Portais" onmouseover="return infraTooltipMostrar('','Tecnologia - Desenvolvimento e Manutenção de Sistemas e Portais');" onmouseout="return infraTooltipOcultar();" tabindex="1002">00025.<wbr>001060/2021-02</a></td>
<td width="10%">(<a href="controlador.php?acao=procedimento_atribuicao_listar&amp;acao_retorno=procedimento_controlar&amp;id_usuario_atribuicao=100002258&amp;id_procedimento=2991883&amp;infra_sistema=100000100&amp;infra_unidade_atual=110000302&amp;infra_hash=5ea5191a8315ee036dc392cd71b5667b4469bff29310a924e744b928577b3e65" title="Atribuído para Fernanda Rodrigues Saldanha de Azevedo" class="ancoraSigla" tabindex="1002">fernandarsa</a>)</td>
</tr>
<tr id="P6430741" class="infraTrClara">
<td><a id="lnkGeradosID-6430741" name="ID-6430741"></a><div class="infraCheckboxDiv"><input class="infraCheckboxInput" id="chkGeradosItem9" name="chkGeradosItem9" tabindex="1002" title="00025.000207/2025-62" type="checkbox" value="6430741" aria-label="Tipo Administrativo - Processo Organizacional / Especificação Composição do Conselho Editorial da Revista Jurídica da Presidência - RJP" onclick="infraSelecionarItens(this,'Gerados');"><label class="infraCheckboxLabel" for="chkGeradosItem9" title="00025.000207/2025-62"></label></div></td>
<td width="20%"><a href="controlador.php?acao=andamento_marcador_gerenciar&amp;acao_origem=procedimento_controlar&amp;acao_retorno=procedimento_controlar&amp;id_procedimento=6430741&amp;infra_sistema=100000100&amp;infra_unidade_atual=110000302&amp;infra_hash=20f538ad1f022810716080d72315d6c6c8567e78232572bcc286009e61cf99d4" aria-label="Marcador / Revista RJP" onmouseover="return infraTooltipMostrar('','Revista RJP');" onmouseout="return infraTooltipOcultar();" tabindex="1002"><img src="svg/marcador_rosa.svg?18" class="imagemStatus"></a></td>
<td><a class="processoVisualizado" href="controlador.php?acao=procedimento_trabalhar&amp;acao_origem=procedimento_controlar&amp;acao_retorno=procedimento_controlar&amp;id_procedimento=6430741&amp;infra_sistema=100000100&amp;infra_unidade_atual=110000302&amp;infra_hash=430c85c17c4d13c70804df77baa9e2188030e84aee1af9b9fa3402e212330acb" aria-label="Administrativo - Processo Organizacional / Composição do Conselho Editorial da Revista Jurídica da Presidência - RJP" onmouseover="return infraTooltipMostrar('Composição do Conselho Editorial da Revista Jurídica da Presidência - RJP','Administrativo - Processo Organizacional');" onmouseout="return infraTooltipOcultar();" tabindex="1002">00025.<wbr>000207/2025-62</a></td>
<td width="10%">(<a href="controlador.php?acao=procedimento_atribuicao_listar&amp;acao_retorno=procedimento_controlar&amp;id_usuario_atribuicao=100014182&amp;id_procedimento=6430741&amp;infra_sistema=100000100&amp;infra_unidade_atual=110000302&amp;infra_hash=41778f307f48fd30e3bde5f82837cb90b0b3aaec495cd532252ba071ae8aa6f1" title="Atribuído para Felipe Augusto Romão" class="ancoraSigla" tabindex="1002">felipe.romao</a>)</td>
</tr>
<tr id="P6513567" class="infraTrClara">
<td><a id="lnkGeradosID-6513567" name="ID-6513567"></a><div class="infraCheckboxDiv"><input class="infraCheckboxInput" id="chkGeradosItem10" name="chkGeradosItem10" tabindex="1002" title="00025.000450/2025-81" type="checkbox" value="6513567" aria-label="Tipo Pessoal - Frequência Mensal / Especificação Frequência dos Estagiários - CEJ/SAJ - 2025" onclick="infraSelecionarItens(this,'Gerados');"><label class="infraCheckboxLabel" for="chkGeradosItem10" title="00025.000450/2025-81"></label></div></td>
<td width="20%"></td>
<td><a class="processoVisualizado" href="controlador.php?acao=procedimento_trabalhar&amp;acao_origem=procedimento_controlar&amp;acao_retorno=procedimento_controlar&amp;id_procedimento=6513567&amp;infra_sistema=100000100&amp;infra_unidade_atual=110000302&amp;infra_hash=323906dd92dc0f3b572df1bbcdba1af2786462ed02bb4742742a5b24af5da68a" aria-label="Pessoal - Frequência Mensal / Frequência dos Estagiários - CEJ/SAJ - 2025" onmouseover="return infraTooltipMostrar('Frequência dos Estagiários - CEJ/SAJ - 2025','Pessoal - Frequência Mensal');" onmouseout="return infraTooltipOcultar();" tabindex="1002">00025.<wbr>000450/2025-81</a></td>
<td width="10%">(<a href="controlador.php?acao=procedimento_atribuicao_listar&amp;acao_retorno=procedimento_controlar&amp;id_usuario_atribuicao=100002693&amp;id_procedimento=6513567&amp;infra_sistema=100000100&amp;infra_unidade_atual=110000302&amp;infra_hash=df441d19689d64fa916f05a6c479ed127e378ae3db5f0262ad7d049fc90e75da" title="Atribuído para Ricardo Brito do Nascimento" class="ancoraSigla" tabindex="1002">ricardobn</a>)</td>
</tr>
<tr id="P5767955" class="infraTrClara">
<td><a id="lnkGeradosID-5767955" name="ID-5767955"></a><div class="infraCheckboxDiv"><input class="infraCheckboxInput" id="chkGeradosItem11" name="chkGeradosItem11" tabindex="1002" title="00025.001074/2024-61" type="checkbox" value="5767955" aria-label="Tipo Documentação - Transferência de Acervo para o Arquivo Central e Recolhimento ao Arquivo Nacional / Especificação Centro de Estudos Jurídicos - CEJ/SAJ/CC-PR" onclick="infraSelecionarItens(this,'Gerados');"><label class="infraCheckboxLabel" for="chkGeradosItem11" title="00025.001074/2024-61"></label></div></td>
<td width="20%"><a href="controlador.php?acao=anotacao_registrar&amp;acao_origem=procedimento_controlar&amp;acao_retorno=procedimento_controlar&amp;id_protocolo=5767955&amp;infra_sistema=100000100&amp;infra_unidade_atual=110000302&amp;infra_hash=3ca95e9c49116beb2cb35a9428a1f991f1f88e696d81a780282e471d38f545bb" aria-label="Anotação / O Arquivo Central não está aceitando transferências no momento. Aguardar liberação de espaço físico. / hansmpf em 15/10/2024 17:19" onmouseover="return infraTooltipMostrar('O Arquivo Central não está aceitando transferências no momento. Aguardar liberação de espaço físico.','hansmpf em 15/10/2024 17:19');" onmouseout="return infraTooltipOcultar();" tabindex="1002"><img src="svg/anotacao1.svg?18" class="imagemStatus"></a><a href="controlador.php?acao=andamento_marcador_gerenciar&amp;acao_origem=procedimento_controlar&amp;acao_retorno=procedimento_controlar&amp;id_procedimento=5767955&amp;infra_sistema=100000100&amp;infra_unidade_atual=110000302&amp;infra_hash=c481e7b3c98c6536c40dab0227d5883581e26dd085fc8cb1364e89fe9a3cd433" aria-label="Marcador / Gestão documental" onmouseover="return infraTooltipMostrar('','Gestão documental');" onmouseout="return infraTooltipOcultar();" tabindex="1002"><img src="svg/marcador_bege.svg?18" class="imagemStatus"></a></td>
<td><a class="processoVisualizado" href="controlador.php?acao=procedimento_trabalhar&amp;acao_origem=procedimento_controlar&amp;acao_retorno=procedimento_controlar&amp;id_procedimento=5767955&amp;infra_sistema=100000100&amp;infra_unidade_atual=110000302&amp;infra_hash=71292c7b5ccb985470c8378c104793c343d45da3a51dc1523f6451351d9e8552" aria-label="Documentação - Transferência de Acervo para o Arquivo Central e Recolhimento ao Arquivo Nacional / Centro de Estudos Jurídicos - CEJ/SAJ/CC-PR" onmouseover="return infraTooltipMostrar('Centro de Estudos Jurídicos - CEJ/SAJ/CC-PR','Documentação - Transferência de Acervo para o Arquivo Central e Recolhimento ao Arquivo Nacional');" onmouseout="return infraTooltipOcultar();" tabindex="1002">00025.<wbr>001074/2024-61</a></td>
<td width="10%">(<a href="controlador.php?acao=procedimento_atribuicao_listar&amp;acao_retorno=procedimento_controlar&amp;id_usuario_atribuicao=100002693&amp;id_procedimento=5767955&amp;infra_sistema=100000100&amp;infra_unidade_atual=110000302&amp;infra_hash=e944105bd3c39664a3098907c4d0b576515590b74a3f1861b1f4fabe32b326e2" title="Atribuído para Ricardo Brito do Nascimento" class="ancoraSigla" tabindex="1002">ricardobn</a>)</td>
</tr>
<tr id="P6299248" class="infraTrClara">
<td><a id="lnkGeradosID-6299248" name="ID-6299248"></a><div class="infraCheckboxDiv"><input class="infraCheckboxInput" id="chkGeradosItem12" name="chkGeradosItem12" tabindex="1002" title="00025.002684/2024-81" type="checkbox" value="6299248" aria-label="Tipo Pessoal: Processo Seletivo - Edital de Oportunidades / Especificação Programa de Estágio em Direito SAJ - Processo Seletivo nº 001/2025" onclick="infraSelecionarItens(this,'Gerados');"><label class="infraCheckboxLabel" for="chkGeradosItem12" title="00025.002684/2024-81"></label></div></td>
<td width="20%"><a href="controlador.php?acao=andamento_marcador_gerenciar&amp;acao_origem=procedimento_controlar&amp;acao_retorno=procedimento_controlar&amp;id_procedimento=6299248&amp;infra_sistema=100000100&amp;infra_unidade_atual=110000302&amp;infra_hash=18f756812cfd7c6b521d617717abc444e696bfc727bc6bd695b3d3052b826f16" aria-label="Marcador / Estagiários" onmouseover="return infraTooltipMostrar('','Estagiários');" onmouseout="return infraTooltipOcultar();" tabindex="1002"><img src="svg/marcador_roxo.svg?18" class="imagemStatus"></a></td>
<td><a class="processoVisualizado" href="controlador.php?acao=procedimento_trabalhar&amp;acao_origem=procedimento_controlar&amp;acao_retorno=procedimento_controlar&amp;id_procedimento=6299248&amp;infra_sistema=100000100&amp;infra_unidade_atual=110000302&amp;infra_hash=060a9eabf752eee22ee92636d3441fcfa916b2bb46a82d65f344485bbdfe78bc" aria-label="Pessoal: Processo Seletivo - Edital de Oportunidades / Programa de Estágio em Direito SAJ - Processo Seletivo nº 001/2025" onmouseover="return infraTooltipMostrar('Programa de Estágio em Direito SAJ - Processo Seletivo nº 001/2025','Pessoal: Processo Seletivo - Edital de Oportunidades');" onmouseout="return infraTooltipOcultar();" tabindex="1002">00025.<wbr>002684/2024-81</a></td>
<td width="10%">(<a href="controlador.php?acao=procedimento_atribuicao_listar&amp;acao_retorno=procedimento_controlar&amp;id_usuario_atribuicao=100002258&amp;id_procedimento=6299248&amp;infra_sistema=100000100&amp;infra_unidade_atual=110000302&amp;infra_hash=13bc26213d7d160fb515427cabe1eb1d6a13248e5f08e5d15a2731762a1cb9de" title="Atribuído para Fernanda Rodrigues Saldanha de Azevedo" class="ancoraSigla" tabindex="1002">fernandarsa</a>)</td>
</tr>
<tr id="P4779694" class="infraTrClara">
<td><a id="lnkGeradosID-4779694" name="ID-4779694"></a><div class="infraCheckboxDiv"><input class="infraCheckboxInput" id="chkGeradosItem13" name="chkGeradosItem13" tabindex="1002" title="00025.003480/2023-87" type="checkbox" value="4779694" aria-label="Tipo Envio de Informações / Especificação Inconstitucionalidade do inciso IX do artigo 7º da Lei nº 8.906, de 4 de julho de 1994." onclick="infraSelecionarItens(this,'Gerados');"><label class="infraCheckboxLabel" for="chkGeradosItem13" title="00025.003480/2023-87"></label></div></td>
<td width="20%"><a href="controlador.php?acao=anotacao_registrar&amp;acao_origem=procedimento_controlar&amp;acao_retorno=procedimento_controlar&amp;id_protocolo=4779694&amp;infra_sistema=100000100&amp;infra_unidade_atual=110000302&amp;infra_hash=cf1038aa7676685dc09db59a26cab4124f79ba4fbc79730e52ca590527e79055" aria-label="Anotação / Fernanda fará o encaminhamento devido. / hansmpf em 14/06/2023 18:08" onmouseover="return infraTooltipMostrar('Fernanda fará o encaminhamento devido.','hansmpf em 14/06/2023 18:08');" onmouseout="return infraTooltipOcultar();" tabindex="1002"><img src="svg/anotacao1.svg?18" class="imagemStatus"></a><a href="controlador.php?acao=andamento_marcador_gerenciar&amp;acao_origem=procedimento_controlar&amp;acao_retorno=procedimento_controlar&amp;id_procedimento=4779694&amp;infra_sistema=100000100&amp;infra_unidade_atual=110000302&amp;infra_hash=98bfa7240d962a5f4d450fa0767df51126d0633fa9d26b4e90df68b5d4e8c220" aria-label="Marcador / Portal da Legislação" onmouseover="return infraTooltipMostrar('','Portal da Legislação');" onmouseout="return infraTooltipOcultar();" tabindex="1002"><img src="svg/marcador_verde_amazonas.svg?18" class="imagemStatus"></a></td>
<td><a class="processoVisualizado" href="controlador.php?acao=procedimento_trabalhar&amp;acao_origem=procedimento_controlar&amp;acao_retorno=procedimento_controlar&amp;id_procedimento=4779694&amp;infra_sistema=100000100&amp;infra_unidade_atual=110000302&amp;infra_hash=caf12248394b783fd2433dce72560c5ca7800250a545ea6a5efea409ab7b5fa4" aria-label="Envio de Informações / Inconstitucionalidade do inciso IX do artigo 7º da Lei nº 8.906, de 4 de julho de 1994." onmouseover="return infraTooltipMostrar('Inconstitucionalidade do inciso IX do artigo 7º da Lei nº 8.906, de 4 de julho de 1994.','Envio de Informações');" onmouseout="return infraTooltipOcultar();" tabindex="1002">00025.<wbr>003480/2023-87</a></td>
<td width="10%">(<a href="controlador.php?acao=procedimento_atribuicao_listar&amp;acao_retorno=procedimento_controlar&amp;id_usuario_atribuicao=100002258&amp;id_procedimento=4779694&amp;infra_sistema=100000100&amp;infra_unidade_atual=110000302&amp;infra_hash=e144e2aca357205b6d133c17c4b1a2c7999e63937d87848f12b032836887b81c" title="Atribuído para Fernanda Rodrigues Saldanha de Azevedo" class="ancoraSigla" tabindex="1002">fernandarsa</a>)</td>
</tr>
</tbody></table>
</div>
<div id="divGeradosAreaPaginacaoInferior" class="infraAreaPaginacao">
</div>

<input type="hidden" id="hdnGeradosPaginaAtual" name="hdnGeradosPaginaAtual" value="0">
<input type="hidden" id="hdnGeradosHashCriterios" name="hdnGeradosHashCriterios" value="dca05dbd0d59b1672fab94262d4b57d3">
  </div>
</div>
    <input type="hidden" id="hdnTipoVisualizacao" name="hdnTipoVisualizacao" value="R">
    <input type="hidden" id="hdnExibirRecebidos" name="hdnExibirRecebidos" value="false">
    <input type="hidden" id="hdnExibirGerados" name="hdnExibirGerados" value="false">
    <input type="hidden" id="hdnMeusProcessos" name="hdnMeusProcessos" value="T">
    <input type="hidden" id="hdnIdBloco" name="hdnIdBloco" value="">
    <input type="text" id="txtBloco" name="txtBloco" value="" style="display:none">
    <input type="hidden" id="hdnIdSigilosos" value="">
    <input type="hidden" id="hdnIdComMarcador" value="2113814,6455190,5357572,6360188,5806875,7052447,6961944,6961920,2991883,6430741,5767955,6299248,4779694">
    <input type="hidden" id="hdnIdMarcador110000302" name="hdnIdMarcador110000302" value="">
    <input type="hidden" id="hdnIdTipoProcedimento110000302" name="hdnIdTipoProcedimento110000302" value="">
    <input type="hidden" id="hdnIdTipoPrioridade110000302" name="hdnIdTipoPrioridade110000302" value="">
    <input type="hidden" id="hdnFlagControleProcessos" name="hdnFlagControleProcessos" value="1">
  </div>
</form>

  <script>    divInfraMoverTopo = document.getElementById("divTabelaProcesso");</script>
</div>
</div>
</div>
<input type="hidden" id="hdnInfraPrefixoCookie" name="hdnInfraPrefixoCookie" value="PR_SEI_ricardobn">
<div id="infraDivImpressao" class="infraImpressao"></div>
<div id="infraBs-xs" class="d-none d-xs-block"></div>
<div id="infraBs-sm" class="d-none d-sm-block"></div>
<div id="infraBs-md" class="d-none d-md-block"></div>
<div id="infraBs-lg" class="d-none d-lg-block"></div>


<div id="divInfraTooltip" class="infraTooltip" style="visibility: hidden; left: 1132px; top: 791px; width: auto;"><table id="tabInfraTooltip" border="0" cellspacing="0" style="width:100%;"><tbody><tr><td><div class="infraTooltipTitulo">Portal da Legislação</div></td></tr>
</tbody>
</table>
</div>
</body>
</html>
"""  # noqa: E501


def actions(url: str = '') -> None:
    """Automation here."""
    with sync_playwright() as handler:
        browser = handler.chromium.launch(headless=False)
        ic()
        with browser.new_context() as context:
            page = context.new_page()
            page.goto(url)
            ic()
            expect(
                process_receved := page.locator('#tblProcessosRecebidos'),
            ).to_be_visible()
            ic(process_receved)
            for e in process_receved.get_by_role('row').all():
                ic(e)
            for f in process_receved.get_by_role('link', name='.').all():
                ic(f.get_attribute('name'))
                ic(f.get_attribute('aria-label'))
                ic(f.get_attribute('onmouseover'))

            # FIXME Dont working.
            # href=process_receved.locator('a').get_attribute('href')
            # ic(href)

            for g in process_receved.get_by_role('link').all():
                ic(g.text_content())

            for h in process_receved.locator('//*[@id="P6779498"]/td[3]'):
                ic(h.text_content())
