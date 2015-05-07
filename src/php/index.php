<html>
<head>
<meta charset="UTF-8">
<title>TEST</title>
</head>

<body>

<h1> NETWORK SETUP </h1>
<p> Select an SSID. </p>

<?php
            	
			

									                                       
?>


<form action="process.php" method="post">        
        <select name="ssidnama">
        		
<?php
		//take the SSID list 
		$file = fopen("/home/pi/ssidlistfin", "r") or die ("Unable to open file!");
		$file2 = fread($file, filesize("/home/pi/listssid"));
	
		$ssid = explode("\n", $file2);
		$l = count($ssid);
		$i = 0;
		while ($i < $l){
		echo "<option value='$ssid[$i]'> $ssid[$i] </option>";
		$i++;
		}
		
?>
            
        </select>
	<input type="submit" value="submit">
        
</form>

</body>

</html>

