<?php
     	
     	$name = $_REQUEST['name'];
     	$addr1 = $_REQUEST['addr1'];
     	$addr2 = $_REQUEST['addr2'];
     	$email = $_REQUEST['email'];
        
        $con = mysqli_connect("localhost","root","","test") or die('Could not connect');
        
        if (mysqli_query($con,"INSERT into student values('$name','$addr1','$addr2','$email')"))
        {
                echo "Data inserted successfully!";
        }
       
        mysqli_close($con);
?>