/* 
    Given an array of objects / dictionaries to represent new inventory,
    and an array of objects / dictionaries to represent current inventory,
    update the quantities of the current inventory
    
    if the item doesn't exist in current inventory, add it to the inventory
    return the current inventory after updating it.
*/

const newInv1 = [
    { name: "Grain of Rice", quantity: 9000 },
    { name: "Peanut Butter", quantity: 50 },
    { name: "Royal Jelly", quantity: 20 },
];
const currInv1 = [
    { name: "Peanut Butter", quantity: 20 },
    { name: "Grain of Rice", quantity: 1 },
];
const expected1 = [
    { name: "Peanut Butter", quantity: 70 },
    { name: "Grain of Rice", quantity: 9001 },
    { name: "Royal Jelly", quantity: 20 },
];




const newInv2 = [];
const currInv2 = [{ name: "Peanut Butter", quantity: 20 }];
const expected2 = [{ name: "Peanut Butter", quantity: 20 }];




const newInv3 = [{ name: "Peanut Butter", quantity: 20 }];
const currInv3 = [];
const expected3 = [{ name: "Peanut Butter", quantity: 20 }];

/**
 * @typedef {Object} Inventory
 * @property {string} Inventory.name The name of the item.
 * @property {number} Inventory.quantity The quantity of the item.
 */

/**
 * Updates the current inventory based on the new inventory.
 * - Time: O(?).
 * - Space: O(?).
 * @param {Array<Inventory>} newInv A shipment of new inventory.
 *    An array of inventory objects.
 * @param {Array<Inventory>} currInv
 * @return The currInv after being updated.
 */
// -----Spencer solution-----
function updateInventory(newInv, currInv) {
    for (let newEntry of newInv) { //iterate over items to be added into inventory
        let match = false; //set a flag to keep track of if we find a matching item in our currInv
        for (let currEntry of currInv) { //inner loop: iterating over existing items in inventory
            if (currEntry['name'] == newEntry['name']) { //if we find a matching entry
                match = true; //set match to true
                currEntry['quantity'] += newEntry['quantity']; //update quantities in our inventory
                break; //stop the loop since we've found our match
            }
        }
        if (!match) { //item didn't exist in our currInv
            currInv.push(newEntry) //so we add it
        }
    }
    return currInv;
}

// -----Spencer solution 2-----
//   function updateInventory(newInv, currentInv) {
//     const currInvTable = {};

//     for (let i = 0; i < currentInv.length; i++) {
//       // save a reference to this currentInv item into our hash table object
//       // so we can look it up with O(1) constant time
//       currInvTable[currentInv[i].name] = currentInv[i];
//     }

//     for (let i = 0; i < newInv.length; i++) {
//       const item = newInv[i];

//       if (currInvTable.hasOwnProperty(item.name)) {
//         // retrieve the currentInv obj reference
//         let currentInvItem = currInvTable[item.name];

//         // update the obj by reference
//         currentInvItem.quantity += item.quantity;
//       } else {
//         currentInv.push(item);
//       }
//     }
//     return currentInv;
//   }

// -----My solution-----(almost works)
// function updateInventory(newInv, currInv) {
//     for (let i = 0; i < newInv.length; i++){
//         for (let j = 0; j < currInv.length; j++){
//             if (newInv[i].name == currInv[j].name){
//                 currInv[j].quantity += newInv[i].quantity;
//                 break;
//             }
//             else if (newInv[i].name != currInv[j].name){
//                 currInv.push(newInv[i]);
//             }
//         }
//     }
//     return currInv;
// }

console.log(updateInventory(newInv1, currInv1))
console.log(updateInventory(newInv2, currInv2))
console.log(updateInventory(newInv3, currInv3))