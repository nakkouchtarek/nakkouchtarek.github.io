 <!DOCTYPE html>
<html>
<head>
<link rel="stylesheet" href="main.css">
<link rel="stylesheet" href="header.css">
<link rel="stylesheet" href="index.css">

<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Bebas+Neue&display=swap" rel="stylesheet">

<title>Portfolio</title>
</head>

<body>

<div id="header">
	<img src="./logo.png" onclick="location.href='./index.php';" id="header_icon"/>

	<ul id="main_links">
		<li>
			<a href="./skills.php">Skills</a>
		</li>

		<li>
			<a href="./career.php">Career</a>
		</li>

		<li>
			<a href="./work.php">Work</a>
		</li>

		<li>
			<a href="./projects.php">Projects</a>
		</li>

		<li>
			<a href="./contact.php">Contact</a>
		</li>
	</ul>

</div>

<div id="main_home">
	
	<div id="main_home_1">
		<h1>
			Hello, 
			<br>
			My name is Tarek Nakkouch
		</h1>
		
		<h2>
			I'm a computer science student
		</h2>
		
		 <button type="button" onclick="location.href='./contact.php';" >Get in touch</button> 

		<br>

		<img class="icon" src="./github.png" onclick="location.href='https://github.com';" style="margin-left: 20%"/>
		<img class="icon" src="./credly.svg" onclick="location.href='https://credly.com';" />
		<img class="icon" src="./linkedin.png" onclick="location.href='https://linkedin.com';"/>

	</div>

	<img src="./profile.jpg" id="profile" />

</div>

</body>

</html> 

<?php
	/*
	Get repos
	curl https://api.github.com/users/nakkouchtarek/repos
	Fetch file
	curl https://api.github.com/repos/nakkouchtarek/TriviaGame/contents/README.md
	Get readme content
	curl https://raw.githubusercontent.com/nakkouchtarek/TriviaGame/master/README.md
	
	*/
?>