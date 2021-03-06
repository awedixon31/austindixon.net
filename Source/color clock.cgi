<!DOCTYPE html>
<html>
<head>
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<meta name="apple-mobile-web-app-capable" content="yes">
  
	<title>Nightscout</title>
  
	<link href="/images/round1.png" rel="icon" id="favicon" type="image/png" />
	<link rel="apple-touch-icon" sizes="57x57" href="/images/apple-touch-icon-57x57.png">
	<link rel="apple-touch-icon" sizes="60x60" href="/images/apple-touch-icon-60x60.png">
	<link rel="apple-touch-icon" sizes="72x72" href="/images/apple-touch-icon-72x72.png">
	<link rel="apple-touch-icon" sizes="76x76" href="/images/apple-touch-icon-76x76.png">
	<link rel="apple-touch-icon" sizes="114x114" href="/images/apple-touch-icon-114x114.png">
	<link rel="apple-touch-icon" sizes="120x120" href="/images/apple-touch-icon-120x120.png">
	<link rel="apple-touch-icon" sizes="144x144" href="/images/apple-touch-icon-144x144.png">
	<link rel="apple-touch-icon" sizes="152x152" href="/images/apple-touch-icon-152x152.png">
	<link rel="apple-touch-icon" sizes="180x180" href="/images/apple-touch-icon-180x180.png">
  
	<style type="text/css">
		@import url("//fonts.googleapis.com/css?family=Open+Sans:700");
  
		body {
			text-align: center;
			margin: 0 0;
			padding: 0;
			overflow: hidden;
			font-family: 'Open Sans';
			color: white;
			background-color: white;
		}
		main {
			display: -webkit-box;
			display: -ms-flexbox;
			display: -webkit-flex;
			display: flex;
			-webkit-box-align: center;
			-ms-flex-align: center;
			-webkit-align-items: center;
			align-items: center;
			height: 100vh;
		}
		.inner {
			width: 100%;
			-webkit-transform: translateY(-5%);
		}
		#bgnow {
			font-weight: 700;
			font-size: 40vmin;
		}
		#trend {
			display: -ms-flexbox;
			display: -webkit-flex;
			display: flex;
			-ms-flex-align: center;
			-webkit-align-items: center;
			-webkit-transform: translateX(1%);
			align-items: center;
			justify-content: center;
			-webkit-flex-direction: column;
			flex-direction: column;
		}
		#arrowDiv {
			flex-grow: 1;
			text-align: center;
		}
		img#arrow {
			height: 30vmin;
		}
		#staleTime {
			flex-grow: 1;
			font-size: 6vmin;
			display: none;
		}
	</style>
</head>

<body>

	<main>
		<div class="inner">
			<div id="bgnow"></div>
			<div id="trend">
				<div id="arrowDiv"><img id="arrow" src=""/></div>
				<div id="staleTime"></div>
			</div>
		</div>
	</main>
  
	<script src="https://seeaustinssugar.herokuapp.com/api/v1/status.js"></script>
	<script src="https://seeaustinssugar.herokuapp.com/js/bundle.js?v=%3C%=%20locals.cachebuster%20%%3E"></script>
	<script src="http://seeaustinssugar.herokuapp.com/api/v1/entries.json?count=1"></script>
  
	<script type="text/javascript">
	
		function query ( ) {
			console.log('query');
			$.ajax('https://seeaustinssugar.herokuapp.com/api/v1/entries/current.json', { success: render });
		}
		function render (xhr) {,.
			console.log('xhr', xhr);
			
			var rec = xhr[0];
			var last = new Date(rec.date);
			var now = new Date( );
			var elapsedMins = Math.round(((now - last) / 1000) / 60);
			
			var bgHigh = sgv > 180;
			var bgLow = sgv < 80;
			var bgTargetBottom = 90;
			var bgTargetTop = 180;
			// Convert BG to mmol/L if necessary.
			if (window.serverSettings.settings.units == 'mmol') {
				rec.sgv = Nightscout.units.mgdlToMMOL(rec.sgv);
				bgHigh = Nightscout.units.mgdlToMMOL(bgHigh);
				bgLow = Nightscout.units.mgdlToMMOL(bgLow);
				bgTargetBottom = Nightscout.units.mgdlToMMOL(bgTargetBottom);
				bgTargetTop = Nightscout.units.mgdlToMMOL(bgTargetTop);
			}
			
			var bgNum = parseFloat(rec.sgv);
			// These are the particular shades of red, yellow, green, and blue.
			var red = 'rgba(213,9,21,1)';
			var yellow = 'rgba(234,168,0,1)';
			var green = 'rgba(134,207,70,1)';
			var blue = 'rgba(78,143,207,1)';
			var direction = rec.direction;
			
			// Insert the trend arrow.
			$('#arrow').attr('src', 'images/'+direction+'.svg');
			// Insert the BG value text.
			$('#bgnow').text(rec.sgv);
			
			// Insert the BG stale time text.
			$('#staleTime').text(elapsedMins+' minutes ago');
			// Threshold background coloring.
			if (bgNum < bgLow) {
				$('body').css('background-color', red);
			}
			if ((bgLow <= bgNum) && (bgNum < bgTargetBottom)) {
				$('body').css('background-color', blue);
			}
			if ((bgTargetBottom <= bgNum) && (bgNum < bgTargetTop)) {
				$('body').css('background-color', green);
			}
			if ((bgTargetTop <= bgNum) && (bgNum < bgHigh)) {
				$('body').css('background-color', yellow);
			}
			if (bgNum >= bgHigh) {
				$('body').css('background-color', red);
			}
			
			// Time before data considered stale.
			var staleMinutes = 13;										
			var threshold = 1000 * 60 * staleMinutes;			
			
			// Restyle body bg, and make the "x minutes ago" visible too.
			if (now - last > threshold) {
				$('body').css('background-color', 'grey');
				$('body').css('color', 'black');
				$('#staleTime').css('display', 'block');
			} else {
				$('#staleTime').css('display', 'none');
				$('body').css('color', 'white');
			}
		}
		function init ( ) {
			console.log('init');
			query( );
			setInterval(query, 1 * 60 * 1000);
		}
		init( );
	</script>
</body>
</html>