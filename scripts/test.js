// 等待 DOM 内容加载完毕后再运行代码
document.addEventListener("DOMContentLoaded", function() {

    /****************** create variables ******************/
    /* create variables to hold the values for modelName and duration */

    // Set the initial model name to "XYZ" and duration to 0
    let modelName = "XYZ";
    let duration = 0;

    /****************** helper function ******************/
    /* create a function called recalculate() which will
        - create a variable to represent the calculated-cost span element. That will look something like:
            // let costLabel = document.getElementById("calculated-cost");
        - check the value of the modelName variable, and use that to calculate the new total cost:
            e.g. if modelName is currently "XYZ", duration * 100 gives us the new total cost.
            if modelName is currently "CPRG", duration * 213 gives us the new total cost.
        - set the value of the calculated-cost element's innerHTML to this new value
    */

    // Function to recalculate the total cost based on model and duration
    function recalculate() {
        let costLabel = document.getElementById("calculated-cost");
        
        // Calculate cost based on model
        let cost = 0;
        if (modelName === "XYZ") {
            cost = duration * 100;
        } else if (modelName === "CPRG") {
            cost = duration * 213;
        }

        // Update the calculated cost display
        costLabel.innerHTML = cost.toFixed(2); // Ensure it's displayed as a number with 2 decimal places
    }

    /****************** model button logic ******************/
    /* 
    - first, create a variable to represent the "Switch Model" pseudo-button (hint: can use getElementById)
    - second, create a function called changeModel() which checks the value of the model name variable. This function will:
        - create a variable to represent the model-text span element
        - if modelName is currently "XYZ", change the value of modelName to "CPRG", and change the innerHTML of the model-text span element to "Model CPRG"
        - if modelName is currently "CPRG", change the value of modelName to "XYZ", and change the innerHTML of the model-text span element to "Model XYZ"
        - then, recalculate() the total cost.
    - finally, uncomment the following line of JavaScript to have this function run automatically whenever the pseudo-button is clicked: */
        
    // Create a variable to represent the "Switch Model" button
    let modelButton = document.getElementById("model-button");

    // Function to switch model and recalculate cost
    function changeModel() {
        let modelText = document.getElementById("model-text");
        
        // Switch model and update model-text
        if (modelName === "XYZ") {
            modelName = "CPRG";
            modelText.innerHTML = "Model CPRG";
        } else if (modelName === "CPRG") {
            modelName = "XYZ";
            modelText.innerHTML = "Model XYZ";
        }
        
        // Recalculate the total cost
        recalculate();
    }

    // Attach the changeModel function to the "Switch Model" button
    modelButton.addEventListener("click", changeModel);

    /****************** duration button logic ******************/
    /*  - first, create a variable to represent the "Change Duration" pseudo-button.
        - then, create a function called changeDuration() that will
            - create a variable to represent the duration-text span element
            - prompt() the user for a new duration
            - save the result of the prompt() to the duration variable
            - change the innerHTML of the duration-text span element to this new value
            - recalculate() the total cost/
        - finally, attach this function to the "Change Duration" pseudo-button, so it runs whenever the button is clicked.
    */

    // Create a variable to represent the "Change Duration" button
    let durationButton = document.getElementById("duration-button");

    // Function to change duration and recalculate cost
    function changeDuration() {
        let durationText = document.getElementById("duration-text");
        
        // Prompt user for new duration
        let newDuration = prompt("Enter new duration (in days):");
        
        // Check if the input is a valid number
        if (newDuration && !isNaN(newDuration)) {
            duration = parseInt(newDuration);
            durationText.innerHTML = duration;
            
            // Recalculate the total cost
            recalculate();
        } else {
            alert("Please enter a valid number for the duration.");
        }
    }

    // Attach the changeDuration function to the "Change Duration" button
    durationButton.addEventListener("click", changeDuration);

});
