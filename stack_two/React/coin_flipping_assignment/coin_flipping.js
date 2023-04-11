//function that waits for heads to be flipped 5 times.

function tossCoin() {
    return Math.random() > 0.5 ? "heads" : "tails";
};

const fiveHeads = () => {
    return new Promise((resolve, reject) => {
        let headsCount = 0;
        let attempts = 0;
        while (headsCount < 5) {
            attempts++;
            let result = tossCoin();
            console.log(`${result} was flipped`);
            if(result === "heads") {
                headsCount++;
            } else {
                headsCount = 0;
            }
        }
        if(headsCount === 5) {
            resolve(`5 heads were flipped in a row in ${attempts} attempts.`)
        }
        else {
            reject(`Process failed at ${attempts} attempts... Try again.`)
        }
    });
};

fiveHeads().then(result => console.log(result)).catch(error => console.log(error));