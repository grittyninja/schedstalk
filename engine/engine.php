<?php
session_start();
if (isset($_POST['csrf_token']) && $_POST['csrf_token'] === $_SESSION['csrf_token']) {
    if(isset($_POST['q'])){
		$query = $_POST['q'];
		// logging
		$timezone  = 7; 
		$time = gmdate("Y/m/j H:i:s", time() + 3600*($timezone+date("I"))); 
		$client_ip = $_SERVER['HTTP_X_FORWARDED_FOR'];
		$log = $time."\t".$client_ip."\t\t".$query."\n";

		$file = fopen("schedstalk-logging.log","a");
		fwrite($file,$log);
		fclose($file);
		
		
		// time cleaning
		preg_match( '/([01]?[0-9]|2[0-3]):[0-5][0-9]/', $query, $match );
		if($match){
		$time = explode(":", $match[0]);
		$timenew = intval($time[0]) % 12;
		$timenew = strval($timenew)." lebih ".$time[1];
		$query = str_replace($match, $timenew, $query);
		}
		// remove unused character
		$query = preg_replace('/[^a-zA-Z0-9 "]/', '', $query);
		$query = str_replace("  ","",$query);
		
		// run program
		$output = shell_exec("python engine.py '".$query."'");
		echo $output;
}
}
die();

?>