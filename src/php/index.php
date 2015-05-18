<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
<title>Welcome page</title>
<style type="text/css" media="screen">
body { background: #e7e7e7; font-family: Verdana, sans-serif; font-size: 11pt; }
#page { background: #ffffff; margin: 50px; border: 2px solid #c0c0c0; padding: 10px; }
#header { background: #4b6983; border: 2px solid #7590ae; text-align: center; padding: 10px; color: #ffffff; }
#header h1 { color: #ffffff; }
#body { padding: 10px; }
span.tt { font-family: monospace; }
span.bold { font-weight: bold; }
a:link { text-decoration: none; font-weight: bold; color: #C00; background: #ffc; }
a:visited { text-decoration: none; font-weight: bold; color: #999; background: #ffc; }
a:active { text-decoration: none; font-weight: bold; color: #F00; background: #FC0; }
a:hover { text-decoration: none; color: #C00; background: #FC0; }
</style>
</head>
<body>
<div id="page">
 <div id="header">
 <h1> Network Setup </h1>
  SELECT AN SSID
 </div>

<p>
<form action="delete.php" method="post">

<?php
	$file = fopen("/home/pi/LeCubeMedia/src/network-update/listssidfromfile", "r") or die ("ERROR");
	$file2 = fread($file, filesize("/home/pi/LeCubeMedia/src/network-update/listssidfromfile"));

	$ssid = explode("\n", $file2);
	$l = count($ssid);
	$i = 0;
	while ($i < $l-1){
		echo "<input type='radio' name='delete' value='$ssid[$i]'> $ssid[$i] <br> ";
		$i++;
	}

?>
<input type="submit" value="Delete">
</form>
</p>

<form action="add.php" method="post">
	<select name="add">

<?php
	$file = fopen("/home/pi/LeCubeMedia/src/network-update/listssidfromscanfin", "r") or die ("ERROR");
	$file2 = fread($file, filesize("/home/pi/LeCubeMedia/src/network-update/listssidfromscanfin"));

	$ssid = explode("\n", $file2);
	$l = count($ssid);
	$i = 0;
	while ($i < $l){
		echo "<option value='$ssid[$i]' > $ssid[$i] </option>";
		$i++;
	}

?>
	</select>
	<br>
	Password: <input type="text" name="password">
	<br>
	<input type="submit" value="Add">

</form>


</div>
<!-- s:853e9a42efca88ae0dd1a83aeb215047 -->
</body>
</html>
