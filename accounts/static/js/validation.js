/*************************************************************************\

The MIT License (MIT)

Copyright (c) 2011-2015 Mark Rogaski

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

\*************************************************************************/

Array.prototype.unique = function() {
    var tmp = this.sort();
    if (tmp.length == 0) { 
        return tmp;
    }
    else {
        var ret = [tmp[0]];
        for (var i = 1; i < tmp.length; i += 1) {
            if (tmp[i] != tmp[i - 1])
                ret.push(tmp[i]);
        }
        return ret;
    }
}

String.prototype.count = function(c) {
    return (this.match(new RegExp(c,"g"))).length;
}

function calculateEntropy(form) {
    var str = form.inputbox.value;
    var sym = str.split("").unique();
    var i, m = str.length, n = sym.length, entropy = 0;
    for (i = 0; i < n; i += 1) {
        var p = str.count(sym[i]) / m;
        entropy -= (p * Math.log(p) / Math.log(2));
    };
    return entropy;
}


