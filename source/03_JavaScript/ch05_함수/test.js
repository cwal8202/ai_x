function sumAll(){
    if(arguments.length == 0){ 
        console.log(sum);
    } else if(arguments.length>=1){
        result = 0;
        for(item in arguments) {
            result += item;
            console.log(result);
        }
    }
}