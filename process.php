<?php
  $a = escapeshellarg($_GET['a']);
  $b = escapeshellarg($_GET['b']);
  $c = escapeshellarg($_GET['c']);
  $d = escapeshellarg($_GET['d']);
  $e = escapeshellarg($_GET['e']);

  $command = "python3 data_management.py $a $b $c $d $e";
  $result = shell_exec($command);

  echo $result;
?>
