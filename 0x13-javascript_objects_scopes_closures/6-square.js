#!/usr/bin/node
module.exports = class Square extends require('./5-square.js') {
    chartPrint(c) {
        if (c === undefined) {
            this.print();
        }
        else {
            for (let i = 0; i < this.height; i++) {
                console.log('X'.repeat(this.width));
            }
        }
    }
};
