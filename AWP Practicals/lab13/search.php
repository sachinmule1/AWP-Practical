<html>
     <h2>Search Result</h2>
		<table border=1>
    		<tr>
    			<th>Name</th><th>Address Line 1</th><th>Address Line 2</th><th>Email-ID</th>
    		</tr>
               		<?php
     			$name = $_REQUEST['name'];
     			$con = mysqli_connect("localhost","root","","test") or die('Could not connect');
     			$result = mysqli_query($con,"SELECT * FROM student WHERE name='$name'");
     			
     			while ($row = mysqli_fetch_array($result))	
                    {
                    
                    echo "<tr>";
                    echo "<td>".$row['name']."</td>";
                    echo "<td>".$row['addr1']."</td>";
	          	    echo "<td>".$row['addr2']."</td>";
          	     	echo "<td>".$row['email']."</td>";
          	     	echo "</tr>";
          		}
          		mysqli_close($con);
          	?>    
          
     	</table>
</html>