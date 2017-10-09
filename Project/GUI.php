
<?php

    $db = new PDO('sqlite:renturo.db');
    $db->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

?>

<html>
<head>
<title>Renturo</title>
<style type = "text/css">
    body 
    {
      font-family:Arial, Helvetica, sans-serif;
      font-size:14px;
    }
       
    label 
    {
      font-weight:bold;
      width:100px;
      font-size:14px;
    }
       
    .box 
    {
      border:#666666 solid 1px;
    }
    a:link {
      color: red;
    }

/* visited link */
    a:visited {
      color: green;
    }

/* mouse over link */
    a:hover {
      color: hotpink;
      font-weight:bold;
      width:100px;
      font-size:14px;
    }
table {
    border-collapse: collapse;
    width: 75%;
}

th, td {
    text-align: left;
    padding: 8px;
}

tr:nth-child(even){background-color: #f2f2f2}

th {
    background-color: #4CAF50;
    color: white;
}
</style>
</head>
<body bgcolor = "#FFFFFF">
  
    <div align = "center">
        <div style = "width:550px; border: solid 1px #333333; " align = "left">
            <div style = "background-color:#333333; color:#FFFFFF; padding:3px;"><div align = "center"><h1>RenTuro</h1></div></div>
                <div style = "margin:30px">
                <form action="" method="POST">
              
                 <div style = "font-size:11px; color:#cc0000; margin-top:10px">



<form action="" method="post">
<label> Select City :</label>
<select name="state">
<?php

    $result = $db->query('SELECT DISTINCT City FROM data');


    foreach($result as $row)

    {


        print "<option>".$row['City']."</option>";

    }

?>
</select><br><br>

<label> Select Car Type :</label>
<select name="cartype">
<?php

    $result = $db->query('SELECT DISTINCT car_type FROM data');


    foreach($result as $row)

    {


        print "<option>".$row['car_type']."</option>";


    }


?>
</select><br><br>
<label>Number Of Recommendations : </label>
<select name="output">
 <option value ="1">1</option>
 <option value ="2">2</option>
 <option value ="3">3</option>
 <option value ="4">4</option>
 <option value ="5">5</option>   
</select><br><br>
<div align = "center">
<input type="submit" name="submit">
</form>
            

<?php
    if (isset($_POST['submit'])) 
                {

                    $city = $_POST['state'];
             

                    $cartype = $_POST['cartype'];
       
                    
                    $number = $_POST['output'];
            



            echo "<br><br><table id ='example' align='center'>
                                <thead>
                                <tr>
                                <th>Make</th>
                                <th>Model</th>
                                <th>Year</th>
                                </tr></thead>";

            $result = $db->query("SELECT City, State FROM data WHERE City ='$city' LIMIT '1'");


            foreach($result as $row)

            {

                $state=$row['State'];
      

            }


            $result = $db->query("SELECT Make, Model, Year FROM data WHERE State ='$state' AND car_type='$cartype' ORDER BY RANK DESC LIMIT '$number'");


            foreach($result as $row)

            {


            echo "<tr>";    
            echo "<td>".$row['Make']."</td>";
            echo "<td>".$row['Model']."</td>";
            echo "<td>".$row['Year']."</td>";
            echo "</tr>";


            }


                }


?>


            </div>
         
            </div>
        
         </div>
      
      </div>



   </body>
</html>