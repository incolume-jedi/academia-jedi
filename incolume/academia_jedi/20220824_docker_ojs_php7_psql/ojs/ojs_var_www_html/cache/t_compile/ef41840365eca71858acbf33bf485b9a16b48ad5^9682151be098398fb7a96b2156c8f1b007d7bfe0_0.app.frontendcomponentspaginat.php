<?php
/* Smarty version 3.1.34-dev-7, created on 2022-08-25 11:42:08
  from 'app:frontendcomponentspaginat' */

/* @var Smarty_Internal_Template $_smarty_tpl */
if ($_smarty_tpl->_decodeProperties($_smarty_tpl, array (
  'version' => '3.1.34-dev-7',
  'unifunc' => 'content_63078a40e31ae0_30750839',
  'has_nocache_code' => false,
  'file_dependency' => 
  array (
    '9682151be098398fb7a96b2156c8f1b007d7bfe0' => 
    array (
      0 => 'app:frontendcomponentspaginat',
      1 => 1612563758,
      2 => 'app',
    ),
  ),
  'includes' => 
  array (
  ),
),false)) {
function content_63078a40e31ae0_30750839 (Smarty_Internal_Template $_smarty_tpl) {
if ($_smarty_tpl->tpl_vars['prevUrl']->value || $_smarty_tpl->tpl_vars['nextUrl']->value) {?>
	<div class="cmp_pagination" aria-label="<?php echo call_user_func_array($_smarty_tpl->registered_plugins[ 'modifier' ][ 'escape' ][ 0 ], array( call_user_func_array( $_smarty_tpl->smarty->registered_plugins[Smarty::PLUGIN_FUNCTION]['translate'][0], array( array('key'=>"common.pagination.label"),$_smarty_tpl ) ) ));?>
">
		<?php if ($_smarty_tpl->tpl_vars['prevUrl']->value) {?>
			<a class="prev" href="<?php echo $_smarty_tpl->tpl_vars['prevUrl']->value;?>
"><?php echo call_user_func_array( $_smarty_tpl->smarty->registered_plugins[Smarty::PLUGIN_FUNCTION]['translate'][0], array( array('key'=>"help.previous"),$_smarty_tpl ) );?>
</a>
		<?php }?>
		<span class="current">
			<?php echo call_user_func_array( $_smarty_tpl->smarty->registered_plugins[Smarty::PLUGIN_FUNCTION]['translate'][0], array( array('key'=>"common.pagination",'start'=>$_smarty_tpl->tpl_vars['showingStart']->value,'end'=>$_smarty_tpl->tpl_vars['showingEnd']->value,'total'=>$_smarty_tpl->tpl_vars['total']->value),$_smarty_tpl ) );?>

		</span>
		<?php if ($_smarty_tpl->tpl_vars['nextUrl']->value) {?>
			<a class="next" href="<?php echo $_smarty_tpl->tpl_vars['nextUrl']->value;?>
"><?php echo call_user_func_array( $_smarty_tpl->smarty->registered_plugins[Smarty::PLUGIN_FUNCTION]['translate'][0], array( array('key'=>"help.next"),$_smarty_tpl ) );?>
</a>
		<?php }?>
	</div>
<?php }
}
}
