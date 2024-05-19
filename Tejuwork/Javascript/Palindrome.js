function palindrome(string){
    if (string == ""){
        console.log("String is Empty")
        console.log("")
    }
    else{
        const reversed = string.split("").reverse().join("")
        if (reversed == string){
            console.log("string is palindrome")
        }
        else{
            console.log("not a palindrome")
        }

    }
}

palindrome("racecar")