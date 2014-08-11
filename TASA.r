library(lsa)

load('./resources/TASA_RP.rda')

get_cos <- function(x,y) {
    out <- tryCatch(
        {
        cosine(TASA[x,],TASA[y,])[1][1]    
        },
        error=function(cond) {
#            message("Got an error:")
#            message(cond)
#            message('', appendLF = TRUE)
#            message("Don't worry! It's all taken care of ;)")
#
#            Return value in case of error:
            return(999)
        },
        warning=function(cond) {
                    #
        },
        finally={
                    #
        }
    )    
    return(out)
}
