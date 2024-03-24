function calculateDemeritPoints (speed){
    const speedlimit = 70;
    const kmperpoint = 5;

    if(speed <=speedlimit){
        console.log("okay");
        return 0;
    } else {
        const points = Math.floor((speed -speedlimit)/kmperpint);
        if (points >=12) {
            console.log ("license suspended");
        }else {
            console.log ("points:" , points);







            
        }
    }
}