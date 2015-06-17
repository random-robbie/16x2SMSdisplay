<?php
$username = "";
$password = "";
$dbname = "";
$tablename = "";
$hostname = ""; 
 
//##################### POST settings & MYSQL Connections #############
 
//POST, this is the code that receives new texts
$sender = $_REQUEST['sender'];
$content = $_REQUEST['content'];
$inNumber = $_REQUEST['inNumber'];
$email = $_REQUEST['email'];
$credits = $_REQUEST['credits'];
 
//establish a connection to the database
$dbhandle = mysql_connect($hostname, $username, $password)
 or die("Unable to connect to MySQL". mysql_error());
 
//select a database to work with
$selected = mysql_select_db($dbname,$dbhandle)
  or die(mysql_error());
 
// inserts POST'd text messages from txtlocal api
  $insertsms = mysql_query("INSERT INTO ".$tablename." (sender,content,inNumber,email,credits) VALUES ('".$sender."', '".$content."', '".$inNumber."', '".$email."', '".$credits."')");

// Delete older SMS
mysql_query("DELETE FROM `texts` WHERE `datereceived` < \'NOW() - INTERVAL 1 DAY\'\n". "");

// execute on local machine  
//shell_exec ('sudo python sms.py'); 

// execute sms.py on remote pi via hamachi
$connection = ssh2_connect('25.61.133.224', 2222);
ssh2_auth_password($connection, 'root', 'raspberry');

$stream = ssh2_exec($connection, 'sudo python /var/www/sms/sms.py&');

?>
