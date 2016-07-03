#multiply.seq
#The function
#@ x is a parameter for the starting number of the interval
#@ y is a paramater for the ending number of the interval
#@ z is a paramater for the interval

multiply.seq <- function(x=from,y=to,z=by){
  a <- seq(x,y,z)
  d <- a[1]
  for(i in 1:length(a[-1])){
    b <- a[i]
    c <- a[!a %in% b]
    rm(b)
    d <- d*c[i]
  }
  return(d)
}