function factorial(num){
    if (factorial < 0){
        console.log("number should be positive")
    }
    if (num ==0 || num ==1){
        return 1
    }
    else{
        return num * factorial(num-1)
    }
}

console.log(factorial(5))