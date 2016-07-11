#package.installcall
#The function installs and calls a package if not available else just calls a package 
#@ packages is parameter for the installation package 


package.installcall <-  function (packages = c("")){ 
  
  new_packages <- packages[!(packages %in% installed.packages()[,"Package"])]
  
  if(length(new_packages)> 0) {
    install.packages(packages); 
    sapply(packages, require, character.only = TRUE)
  } else {
    sapply(packages, require, character.only = TRUE)
    }
}
