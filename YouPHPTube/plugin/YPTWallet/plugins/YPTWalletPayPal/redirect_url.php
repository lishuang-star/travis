<?php

header('Content-Type: application/json');

if (empty($global['systemRootPath'])) {
    $global['systemRootPath'] = '../../../../';
}
require_once $global['systemRootPath'] . 'videos/configuration.php';
require_once $global['systemRootPath'] . 'objects/user.php';

$plugin = YouPHPTubePlugin::loadPluginIfEnabled("YPTWallet");
$paypal = YouPHPTubePlugin::loadPluginIfEnabled("PayPalYPT");
$users_id = User::getId();
        
$invoiceNumber = uniqid();
$redirect_url = "plugin/SupportAuthor/redirect_url.php";
$cancel_url = "plugin/SupportAuthor/cancel_url.php";

$payment = $paypal->executePayment();
//var_dump($amount);
$obj= new stdClass();
$obj->error = true;
if (!empty($payment)) {
    $amount = PayPalYPT::getAmountFromPayment($payment);
    $plugin->addBalance($users_id, $amount->total, "Paypal payment", json_encode($payment));
    $obj->error = false;
    header("Location: plugin/YPTWallet/view/addFunds.php?status=success");
}else{
    header("Location: plugin/YPTWallet/view/addFunds.php?status=fail");
}
error_log(json_encode($obj));


?>