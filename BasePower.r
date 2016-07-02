#base power - function
#num is number you are trying to find the x for where x is some power to the base 10
#e.g. 100 == 10^x the function should return 2, here 100 is num and x is what we are trying to find

findNum<- function(num){
    x <- seq(1,100000,0.01)
    for(i in x){
        y <- as.integer(10^i)
        y <- y[!is.na(y)]
        if(y == num){
            print(i)
        } 
    }
}
findNum(100)