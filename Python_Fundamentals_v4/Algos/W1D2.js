/* 
  String: Reverse
  Given a string,
  return a new string that is the given string reversed
*/

const str1 = "creature";
const expected1 = "erutaerc";

const str2 = "dog";
const expected2 = "god";

const str3 = "hello";
const expected3 = "olleh";

const str4 = "";
const expected4 = "";


/**
 * Reverses the given str.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str String to be reversed.
 * @returns {string} The given str reversed.
 */
function reverseString(str) {
    var temp = "'";
    for(var i = str.length - 1; i >= 0; i--){
        temp += str[i];
    }
    temp += "'"
    return temp
    // var temp = "";
    // for(var i = 0; i < str.length/2; i++){
    //     temp = str[i];
    //     str[i] = str[str.length - 1 - i];
    //     str[str.length - 1 - i] = temp;
    // }
    // return str
}

console.log(reverseString(str1)); // "erutaerc"
console.log(reverseString(str2)); // "god"
console.log(reverseString(str3)); // "olleh"
console.log(reverseString(str4)); // ""

/*****************************************************************************/