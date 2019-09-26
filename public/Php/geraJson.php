<?php
$server = "localhost";
$usuario  = "root";
$senha    = "";

$conn = mysql_connect($servidor, $usuario, $senha);

$SQL = "SELECT id_usuario, nome, email, status FROM tb_usuarios";

$table = mysql_query($SQL) or die(mysql_error());

while ($row = mysql_fetch_array($table))  
{

    $i=0;
                
    foreach($row as $key => $value)    
    {

        if (is_string($key)) 
        {
         $fields[mysql_field_name($table,$i++)] = $value;
        }

    }

    $json_result["bindings"] [ ] =  $fields;

}

$JSON = json_encode($json_result);


?>