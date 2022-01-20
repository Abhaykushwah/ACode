<?php

//single variable array
$year= array('january','february', 'march','april');

echo "this month is $year[1]<br>";
echo "this month is $month[3]";

//multiple variable array
$month[] = 'jan';
$month[] = 'fab';
$month[] = 'mar';
$month[] = 'apr';

//range array in single variable
$alpha = range('a','z');
echo "<br><br> Seventeenth alphabet in English language is $alpha[16]";

//key pair values in array
//also known as associative array
$mon = array(
    '1' =>'jan',
    '2' => 'fab',
    '3' => 'mar',
    '4' => 'apr',
    '5' => 'may',
    '6' => 'jun',
    '7' => 'jul',
    '8' => 'aug',
    '9' => 'sep',
    '10' => 'oct',
    '11' => 'nov',
    '12' => 'dec'
);

echo "<br>$mon[1]";
echo "<br>$mon[11]";


//foreach array call
foreach ($mon as $value ) {
    // code....
    echo "<br>Months respectively numbering as follow :  $key $value";
}
?>