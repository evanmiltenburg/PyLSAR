###PyLSAR: a script to interact with LSA spaces built in R
------------

PyLSAR uses the RPy2 module to load an R script that provides a cosine similarity function. It is very basic, and at some point I will try to expand the functions one can use.


#### Dependencies
The script depends on two different modules:
  
  - RPy2
  - The R-package *lsa*

If you want to expand the script, also have a look at the R-package *LSAfun*.


#### Resources
The `./resources` folder contains one example space, TASA_RP.rda, which comes from [this open directory](http://www.lingexp.uni-tuebingen.de/z2/LSAspaces/). The following other LSA spaces are publically available there as well.

```
 TASA.rda                21-May-2014 11:37  168M  
 TASA_RP.rda             07-Jul-2014 10:23   30M  
 blogs.rda               24-Feb-2014 16:29  214M  
 blogs_en.rda            25-Apr-2014 15:19   62M  
 blogs_nl.rda            21-May-2014 11:41  261M  
 blogs_stem.rda          21-May-2014 11:43  187M  
 literature.rda          24-Feb-2014 16:37  162M  
 newspapers.rda          24-Feb-2014 16:35  239M
```

I just chose to distribute this space for its size. Some other space might be more suitable for your needs. Check out the file descriptions [here](http://www.lingexp.uni-tuebingen.de/z2/LSAspaces/Descriptions.txt).