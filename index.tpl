<!DOCTYPE html>
<html>
<head>
	<title>Fréttasíðan mín</title>
	<meta charset="utf-8">
	<link rel="stylesheet" type="text/css" href="css/style.css">
</head>
<body>
	% include("header.tpl")

	<section>
		<div class="oki">
			<h2>{{frettir[0]['Header']}}</h2>
			<img src="/myndir/{{frettir[0]['Image']}}">
		</div>
		<div class="frettir">
			<ul>
				<li><a href="/frett/0">Frétt 1</a></li>
				<li><a href="/frett/1">Frétt 2</a></li>
				<li><a href="/frett/2">Frétt 3</a></li>
				<li><a href="/frett/3">Frétt 4</a></li>
			</ul>
		</div>
	</section>

	% include("footer.tpl")
</body>
</html>


