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
 TASA.rda         168M  English LSA Space, 300 dimensions
 TASA_RP.rda      30M   English, built with Random Projection using the package SemanticVectors
 blogs.rda        214M  German LSA Space, 300 dimensions
 blogs_en.rda     62M   English LSA Space, 300 dimensions
 blogs_nl.rda     261M  Dutch LSA Space, 300 dimensions
 blogs_stem.rda   187M  German LSA Space, 300 dimensions
 literature.rda   162M  German LSA space, 300 dimensions
 newspapers.rda   239M  German LSA space, 300 dimensions
```

I just chose to distribute this space for its size. Some other space might be more suitable for your needs.