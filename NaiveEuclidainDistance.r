#My short project to calculate the euclidian distance between two strings using a naive approach
#function to transform names into a binary matrix based on letters
transNameDist <- function(x,y){
    alphabets <- data.frame(letters,number=seq_along(letters))
    name1 <- x
    name2 <- y
    a <- ifelse(
               is.na(
                    merge(x = alphabets,y = 
                                      subset(alphabets,alphabets$letters %in% strsplit(name1,"")[[1]]),by = c("letters"), all.x = TRUE)$number.y),0,1)
    b <- ifelse(
               is.na(
                    merge(x = alphabets,y = 
                                       subset(alphabets,alphabets$letters %in% strsplit(name2,"")[[1]]),by = c("letters"), all.x = TRUE)$number.y),0,1)
    print ("call x as a data.frame from global")
    return(data.frame(a = a, b = b))
    x <<- data.frame(a = a, b = b)
    
} 
transNameDist(x = "umair", y = "obaid")

#function to calculate euclidian distance
euclidDist <- function(x,y){
    x <- matrix(x)
    y <- matrix(y)
    z <- (x-y)^2
    d <- 0
    for (i in z[,1]){
        d <- d + (i)
    }
    return (sqrt(d))
}
euclidDist(x = x$a,y = x$b)