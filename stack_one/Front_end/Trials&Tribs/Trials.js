function counter(startNum) {    //The function is expecting some PARAMETER in order to run
        for (var num = startNum ; num >= 0 ; num--) {        
            console.log(num);    
        }
    }
    counter(6);    // Passing in an ARGUMENT of 6, the console would display: 6, 5, 4, 3, 2, 1, 0
    counter(3);    // Passing in an ARGUMENT of 3, the console would display: 3, 2, 1, 0
                    // syntax

    function createArray(num) {        
            var newArray = [];       
            for (var i = 0; i <= num; i++) {                
                newArray.push(i);        
            }
        }
        createArray(5);
        // The newArray only exists inside of the function.  Out here it no longer exists!
        // syntax
        function createArray(num) {        
                var newArray = [];        
                for (var i = 0; i <= num; i++) {                
                    newArray.push(i);        
                }        
                return newArray;        // added the return statement
            }
            var y = createArray(5);        // now y is the variable that is calling on createArray
            // syntax