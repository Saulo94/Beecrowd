var input = require('fs').readFileSync('/dev/stdin', 'utf8');
var lines = input.split('\n');

if (lines[0].length <= 80)
    console.log('YES');
else
    console.log('NO');
