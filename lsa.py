################################################################
# This script provides LSA cosine similarity values.
#
# We will use RPy2, which needs to be installed (pip install rpy2)
# We will use the lsa library in R, which needs to be installed.
# 
# The data comes from this open directory:
# http://www.lingexp.uni-tuebingen.de/z2/LSAspaces/
#
# It holds the following other data files:
# TASA.rda                21-May-2014 11:37  168M  
# TASA_RP.rda             07-Jul-2014 10:23   30M  
# blogs.rda               24-Feb-2014 16:29  214M  
# blogs_en.rda            25-Apr-2014 15:19   62M  
# blogs_nl.rda            21-May-2014 11:41  261M  
# blogs_stem.rda          21-May-2014 11:43  187M  
# literature.rda          24-Feb-2014 16:37  162M  
# newspapers.rda          24-Feb-2014 16:35  239M 
#
# TASA.r is a small script that 
# - loads TASA.rda
# - imports the lsa library
# - provides a cosine similarity function for the TASA model
# - deals with out-of-bound errors if a word is not in the model
#   ==> if this happens, get_cos returns a value of 999.0 (an absurdly high value)

import rpy2
import rpy2.robjects as robjects

robjects.r("source('TASA.r')")
r_getcos = robjects.globalenv['get_cos']

def get_cos(x,y):
    return(r_getcos(x,y)[0])

