<?php
if(isset($_GET['pass']) && $_GET['pass']=='letupdatebegin'){
    shell_exec("./update.sh &> schedstalk-update.log &");
}
?>