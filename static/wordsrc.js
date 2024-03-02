function processWords(words, bank) {
    // Convert words to uppercase
    words = words.map(word => word.toUpperCase());

    // Reverse words
    let backwords = words.map(word => word.split('').reverse().join(''));

    // Transpose bank
    let transposed = [];
    for (let iter1 = 0; iter1 < bank[0].length; iter1++) {
        let col = [];
        for (let iter2 = 0; iter2 < bank.length; iter2++) {
            col.push(bank[iter2][iter1]);
        }
        transposed.push(col);
    }

    // Diagonalize bank
    let diagonalized = [];
    let diagonalized2 = [];
    let rows = bank.length;
    let cols = bank[0].length;

    for (let i = 0; i < rows + cols - 1; i++) {
        let temp = [];
        for (let j = Math.max(0, i - rows + 1); j < Math.min(cols, i + 1); j++) {
            temp.push(bank[i - j][j]);
        }
        diagonalized.push(temp);
    }

    for (let i = 0; i < rows + cols - 1; i++) {
        let temp = [];
        for (let j = Math.max(0, i - rows + 1); j < Math.min(cols, i + 1); j++) {
            temp.push(bank[i - j][cols - j - 1]);
        }
        diagonalized2.push(temp);
    }

    let locs = [];

    // Create strings for search
    let str1 = bank.flat().join('');
    let str2 = transposed.flat().join('');
    let str3 = diagonalized.flat().join('');
    let str4 = diagonalized2.flat().join('');

    // Find words in strings
    for (let letters of "hi") {
        for (let word of words) {
            let sub = str1.indexOf(word);
            if (sub != -1) {
                locs.push([word, sub, "Horizontal"]);
            }

            sub = str2.indexOf(word);
            if (sub != -1) {
                locs.push([word, sub, "Vertical"]);
            }

            sub = str3.indexOf(word);
            if (sub != -1) {
                locs.push([word, sub, "Diagonall Left to Right"]);
            }

            sub = str4.indexOf(word);
            if (sub != -1) {
                locs.push([word, sub, "Diagonal Right to Left"]);
            }
        }
        words = backwords;
    }

    return locs;
}

function stringTo2DArray(inputString, x, y) {
    if (x * y !== inputString.length) {
        console.error("Invalid dimensions. The product of x and y should be equal to the length of the input string.");
        return null;
    }

    let array2D = [];
    let currentIndex = 0;

    for (let i = 0; i < y; i++) {
        let row = [];
        for (let j = 0; j < x; j++) {
            row.push(inputString[currentIndex]);
            currentIndex++;
        }
        array2D.push(row);
    }

    return array2D;
}
function indexToCoordinate(index, x) {
    let row = Math.floor(index / x); // Calculate the row number
    let col = index % x; // Calculate the column number
    return [col,row]; // Return the coordinate value [column, row]
}



function parse_results(outputArray, words, x){
    words = words.map(word => word.toUpperCase());
    let newarr = [];

    outputArray.forEach(item => {
        let word = item[0]; // Get the word
        let index = indexToCoordinate(item[1], x); // Get the index
        let secondPart = item[2]; // Get the second part
        // Check if the word exists in the comparison array
        if (words.includes(word)) {
            console.log(`${word} exists in the comparison array.`);
            newarr.push([word, index, secondPart]);
        } else {
            console.log(`${word} does not exist in the comparison array.`);
            newarr.push([word.split("").reverse().join(""), index, secondPart]);
        }
    });

    return newarr;
}
function cleanstr(wordArray, list) {
    wordArray.forEach(item => {
        let word = item[0];
        let coordinates = item[1];
        let direction = item[2];
        let parsedString = `Word: ${word}, Coordinates: (${coordinates[0]}, ${coordinates[1]}), Direction: ${direction}`;
        let li = document.createElement('li'); // Create a new list item element
        li.textContent = parsedString; // Set the text content of the list item
        list.appendChild(li); // Append the list item to the list
    });
}



function getVals() {
    let list = document.getElementById('dsp2');
    let letters = document.getElementById("letters").value;
    let words = document.getElementById("Words").value;
    let x = document.getElementById("x").value;
    let y = document.getElementById("y").value;
    words = words.split(',').map(word => word.trim());

    let resultArray = processWords(words, stringTo2DArray(letters, x, y))

    //alert(parse_results(resultArray, words, x));
    //console.log(parse_results(resultArray, words, x))
    //document.getElementById('dsp').innerHTML = 
    cleanstr(parse_results(resultArray, words, x), list);
    console.log(parse_results(resultArray, words, x));
    
  }


function fillex(){
    document.getElementById("letters").value = "OMDUECNARELOTNIMSRRLIEVCDEERCEOIESBBIGOTRYYEEDVAGLIERATICNTTEIMOEAEQTRAVANDETTHEVIOUGULIDARCYWERCREAOOESBFAEREYJLOSLCCDTOMEAOEASEMIIILHENGBNTNDABEGTOODAUTSTUHINNMHYLNGSITHAATIMACTITESRFTRZTQCMRHDQANRJLYYHHYTAPAODMINISTERWNMFY";
    document.getElementById("Words").value = "Activism, Activist, Bigotry, Boycott, Courage, Creed, Desolate, Dignity, Dream, Equality, Freedom, Holiday, Intolerance, January, Legacy, March, Memorial, Minister, Oasis, Reagan, Reverend"
    document.getElementById("x").value = 15
    document.getElementById("y").value = 15
    
}

function clear_all(){
    document.getElementById("letters").value = "";
    document.getElementById("Words").value = ""
    document.getElementById("x").value ="w";
    document.getElementById("y").value = "h";
    document.getElementById('dsp').innerHTML = "";
}