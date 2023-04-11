var fs = require('fs');
const path = require('path');
const express = require('express');

const app = express();

const fileLocation = path.join(__dirname, 'colors.txt');

app.get('/', (req, res) => {
	fs.readFile(fileLocation, 'utf8', function (err, data) {
		if (err) throw err;
		console.log(data);
		console.log(JSON.stringify(data));
		res.json(data);
	});
});

app.listen(3000, (req, res) => {
	console.log('server started');
});
