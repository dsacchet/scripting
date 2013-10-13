#!/usr/bin/php
<?php
$cryptedpassword=base64_decode($argv[1]);
$plainpassword=$argv[2];


//echo "password_check( $cryptedpassword, $plainpassword )\n";
if( preg_match( "/{([^}]+)}(.*)/", $cryptedpassword, $cypher ) ) {
$cryptedpassword = $cypher[2];
$_cypher = strtolower($cypher[1]);
} else  {
$_cypher = NULL;
}

$cryptedpassword="a762gwNRQh2A6";

if( crypt($plainpassword, $cryptedpassword ) == $cryptedpassword )
	echo "true\n";
else
	echo "false\n";

?>
