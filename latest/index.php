<?php
echo "<h1> Kueri terbaru yang sukses dieksekusi</h1>";
$output = shell_exec('tac ../engine/_latest_query_.txt | head -n 20 | nl');
echo "<pre>$output</pre>";
?>