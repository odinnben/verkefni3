<!DOCTYPE html>
<html>
<head>
	<title>{{Header}}</title>
	<meta charset="utf-8">
	<link rel="stylesheet" type="text/css" href="/css/style.css">
</head>
<body>
	% include("header.tpl")

	<section>
		<div class="oki">
			<h2>{{Header}}</h2>
			<img src="/myndir/{{Image}}">
		</div>
		<div class="frettir">
			<p>{{Content}}</p>
			<p>{{Reporter}}</p>
			<br>
			<a href="/b">Til baka</a>
		</div>
	</section>

	% include("footer.tpl")
</body>
</html>
