<?php
$result = 5+5;
function square()
{
    $result = 5*5;
    echo "Local Square Result = $result<br>";
}
function cube()
{
    $result =5*5*5;
    echo "Local Cube Result = $result<br>";
}

echo "The Global Sum Result = $resulte<br>";
square();
cube();
?>