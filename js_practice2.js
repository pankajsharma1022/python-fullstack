// empty array created
let roster = [];
 
// create a function for the task


// Add a new student

// create a function called addNew that takes in a name
// and uses .push to add a ne student to the array
function addyNew() {
    let newName = prompt("what name would you like to add? ")
    roster.push(newName)
}

// Remove student
function remove() {
    let removeName = prompt("what name would you like to remove?")
    let index= roster.indexof(removeName);
    roster.splice(index,1);
}

// display roster
function display() {
    console.log(roster);
}

let start = prompt("would you like to start the roster web app? y/n")
var request = "empty";
if (start === 'y') {
    while (request !== "quit") {
        request = prompt("please select an action: add,remove,display, or quit.")
        if(request=='add'){
            addNew();
        }
        else if (request === 'display'){
            display();
        }
        else if (request == 'remove'){
            remove();
        }
        else {
            alert("Not recognized")
            request = "quit"
        }  
    }
}
alert("Thanks for using the weeb App! Please refersh to start over!")