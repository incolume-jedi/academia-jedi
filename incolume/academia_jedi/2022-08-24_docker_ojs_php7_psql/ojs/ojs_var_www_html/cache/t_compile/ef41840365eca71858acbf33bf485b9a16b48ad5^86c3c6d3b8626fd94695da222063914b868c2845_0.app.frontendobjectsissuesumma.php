<?php
/* Smarty version 3.1.34-dev-7, created on 2022-08-25 11:42:08
  from 'app:frontendobjectsissuesumma' */

/* @var Smarty_Internal_Template $_smarty_tpl */
if ($_smarty_tpl->_decodeProperties($_smarty_tpl, array (
  'version' => '3.1.34-dev-7',
  'unifunc' => 'content_63078a40e12198_24489826',
  'has_nocache_code' => false,
  'file_dependency' => 
  array (
    '86c3c6d3b8626fd94695da222063914b868c2845' => 
    array (
      0 => 'app:frontendobjectsissuesumma',
      1 => 1612563690,
      2 => 'app',
    ),
  ),
  'includes' => 
  array (
  ),
),false)) {
function content_63078a40e12198_24489826 (Smarty_Internal_Template $_smarty_tpl) {
if ($_smarty_tpl->tpl_vars['issue']->value->getShowTitle()) {
$_smarty_tpl->_assignInScope('issueTitle', $_smarty_tpl->tpl_vars['issue']->value->getLocalizedTitle());
}
$_smarty_tpl->_assignInScope('issueSeries', $_smarty_tpl->tpl_vars['issue']->value->getIssueSeries());
$_smarty_tpl->_assignInScope('issueCover', $_smarty_tpl->tpl_vars['issue']->value->getLocalizedCoverImageUrl());?>

<div class="obj_issue_summary">

	<?php if ($_smarty_tpl->tpl_vars['issueCover']->value) {?>
		<a class="cover" href="<?php echo call_user_func_array( $_smarty_tpl->smarty->registered_plugins[Smarty::PLUGIN_FUNCTION]['url'][0], array( array('op'=>"view",'path'=>$_smarty_tpl->tpl_vars['issue']->value->getBestIssueId()),$_smarty_tpl ) );?>
">
			<img src="<?php echo call_user_func_array($_smarty_tpl->registered_plugins[ 'modifier' ][ 'escape' ][ 0 ], array( $_smarty_tpl->tpl_vars['issueCover']->value ));?>
" alt="<?php echo (($tmp = @call_user_func_array($_smarty_tpl->registered_plugins[ 'modifier' ][ 'escape' ][ 0 ], array( $_smarty_tpl->tpl_vars['issue']->value->getLocalizedCoverImageAltText() )))===null||$tmp==='' ? '' : $tmp);?>
">
		</a>
	<?php }?>

	<h2>
		<a class="title" href="<?php echo call_user_func_array( $_smarty_tpl->smarty->registered_plugins[Smarty::PLUGIN_FUNCTION]['url'][0], array( array('op'=>"view",'path'=>$_smarty_tpl->tpl_vars['issue']->value->getBestIssueId()),$_smarty_tpl ) );?>
">
			<?php if ($_smarty_tpl->tpl_vars['issueTitle']->value) {?>
				<?php echo call_user_func_array($_smarty_tpl->registered_plugins[ 'modifier' ][ 'escape' ][ 0 ], array( $_smarty_tpl->tpl_vars['issueTitle']->value ));?>

			<?php } else { ?>
				<?php echo call_user_func_array($_smarty_tpl->registered_plugins[ 'modifier' ][ 'escape' ][ 0 ], array( $_smarty_tpl->tpl_vars['issueSeries']->value ));?>

			<?php }?>
		</a>
		<?php if ($_smarty_tpl->tpl_vars['issueTitle']->value && $_smarty_tpl->tpl_vars['issueSeries']->value) {?>
			<div class="series">
				<?php echo call_user_func_array($_smarty_tpl->registered_plugins[ 'modifier' ][ 'escape' ][ 0 ], array( $_smarty_tpl->tpl_vars['issueSeries']->value ));?>

			</div>
		<?php }?>
	</h2>

	<div class="description">
		<?php echo call_user_func_array($_smarty_tpl->registered_plugins[ 'modifier' ][ 'strip_unsafe_html' ][ 0 ], array( $_smarty_tpl->tpl_vars['issue']->value->getLocalizedDescription() ));?>

	</div>
</div><!-- .obj_issue_summary -->
<?php }
}
