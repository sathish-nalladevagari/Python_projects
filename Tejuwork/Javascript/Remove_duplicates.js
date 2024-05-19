function remove_duplicates(arr){
    if (arr.length == 0){
        console.log("Array is Empty")
    }
    else{
        const unique = [... new Set(arr)]
        console.log(unique)
        
    }
}

remove_duplicates([1,2,2,3,4,5,5,5,6])