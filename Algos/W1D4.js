/* 
    Given in an alumni interview in 2021.
    String Encode
    You are given a string that may contain sequences of consecutive characters.
    Create a function to shorten a string by including the character,
    then the number of times it appears. 
    
    
    If final result is not shorter (such as "bb" => "b2" ),
    return the original string.
  */

const str1 = "aaaabbcddd";
const expected1 = "a4b2c1d3";

const str2 = "";
const expected2 = "";

const str3 = "a";
const expected3 = "a";

const str4 = "bbcc";
const expected4 = "bbcc";

/**
 * Encodes the given string such that duplicate characters appear once followed
 * by a number representing how many times the char occurs. Only encode strings
 * when the result yields a shorter length.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str The string to encode.
 * @returns {string} The given string encoded.
 */
function encodeStr(str) {
    let compress = '';
    let count = 1;
    for (let i = 0; i < str.length; i++) {
        if (str[i] === str[i + 1]) {
            count++;
        } else {
            compress += str[i] + String(count);
            count = 1;
        }
    }
    return compress.length < str.length ? compress : str;
}
console.log(encodeStr(str1)); // "a4b2c1d3"
console.log(encodeStr(str2)); // ""
console.log(encodeStr(str3)); // "a"
console.log(encodeStr(str4)); // "bbcc"

/*****************************************************************************/


const strA = "a3b2c1d3";
const expectedA = "aaabbcddd";

const strB = "a3b2c12d10";
const expectedB = "aaabbccccccccccccdddddddddd";

/**
 * Decodes the given string by duplicating each character by the following int
 * amount if there is an int after the character.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str An encoded string with characters that may have an int
 *    after indicating how many times the character occurs.
 * @returns {string} The given str decoded / expanded.
 */
//helpful built-ins : isNaN() .repeat() parseInt() 
function encodeStr(str) {
    let encoded = "";

    for (let i = 0; i < str.length; i++) {
        let currChar = str[i];
        let dupeCount = 1;

        while (str[i + 1] === currChar) {
            dupeCount++;
            i++;
        }

        if (dupeCount == 1) {
            encoded += currChar
        }
        if (dupeCount == 2) {
            encoded += currChar + currChar
        }
        else {
            encoded += currChar + dupeCount;
        }
    }
    return encoded;
}





function decodeStr(str = "") {
    let decoded = "";
    let i = 0;

    while (i < str.length) {
        // Retrieve letter at current index then increment the idx (post increment)
        // to get to the num that comes after the char.
        let char = str[i++];

        //a23b3
        // the num is a string so multiple digits need to be concatenated before
        // converted to a number. '1' + '1' => '11'. 1 + 1 => 2
        let numStr = "";
        /* 
        parseInt returns NaN if it fails to parse. NaN is a weird special value
        that requires using isNaN to check b/c NaN === NaN => false.
        */
        let isNumber = isNaN(parseInt(str[i])) === false;

        /* 
        Iterate over all the nums that come after this string until the next
        non-number.
        */
        while (i < str.length && isNumber) {
            // concatenate the string-num digit then increment.
            numStr += str[i++];
            isNumber = isNaN(parseInt(str[i])) === false;
        }

        // .repeat will automatically convert numStr to a number if it can.
        decoded += char.repeat(numStr);
    }
    return decoded;
}

console.log(decodeStr(strA)) // Expected: aaabbcddd
console.log(decodeStr(strB)) // Expected: aaabbccccccccccccdddddddddd

