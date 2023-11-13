#!/usr/bin/node
sizeSquare = Math.floor(Number(process.argv[2]));
if (isNaN(sizeSquare)) {
    console.log('Missing size');
} else {
    for (i = 1; i <= sizeSquare; i++) {
        let strRow = '';
        for (j = 1; j <= sizeSquare; j++) {
            strRow += 'X';
        }
        console.log(strRow);
    }
}
