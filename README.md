# De Novo Proteins in CATH?

## Background info
De Novo protein design is a branch of computational biology that is focused on creating new protein structures, quite often from scratch, that have never existed before. Some of the De Novo designed proteins try to repeat the structure of proteins that already exist in nature ([1](http://www.rcsb.org/pdb/explore/explore.do?structureId=5CW9), [2](http://www.rcsb.org/pdb/explore/explore.do?structureId=5UN5)), some try to design proteins that have specific functions ([1](http://www.rcsb.org/pdb/explore/explore.do?structureId=5VBT), [2](http://www.rcsb.org/pdb/explore/explore.do?structureId=5U9T)) and some of them are designed completely from scratch, without any functions planned for them, usually to see if structures like that are even possible ([1](http://www.rcsb.org/pdb/explore/explore.do?structureId=5H78), [2](http://www.rcsb.org/pdb/explore/explore.do?structureId=5K7V), [3](http://www.rcsb.org/pdb/explore.do?structureId=4HXT)).

These structures are uploaded in the PDB and classified as "De Novo Protein". Additionally, these structures usually have "synthetic construct" in the "organism" line. There are currently ~4000 proteins that are tagged with "synthetic construct" and only ~700 pdb structures that are classified as De Novo proteins. This happens because De Novo proteins that are designed to have a specific function are usually labelled by their function and not by the fact that they are designed.

## What is the issue?

One of the main features of CATH is the classification of proteins by their Homology - how closely evolutionally related are proteins. However De Novo designed proteins can interfere with this process foe obvious reasons - they are not evolutionally related to any proteins. For this reason I think it is important to separate the De Novo protein in CATH into a dedicated superfamily or at least take a look on how the superfamilies would form without them in CATH.

## Solutions?

We need to check how CATH already processed the De Novo proteins and how did it classify them. Right now there are ~13000 domains that are tagged as "De Novo" in CATH, however some of them are not from De Novo proteins. This may be the hard part of this research, because the tagging is not very accurate sometimes. It might be a good idea to find a couple of relatively small superfamilies that contain a significant amount of De Novo designed proteins and look at them, excluding the De Novo proteins.

Based on the results of that it is important to make a decision about the further processing of De Novo proteins. If it turns out that De Novo proteins have a negative effect on how CATH "creates" superfamilies, it may be necessary to remove them from CATH or create a separate superfamily. Another solution may be to not assign them to a particular superfamily.

However, if it turns out that the negative effect is negligible, we can just tag them as "De Novo designed protein" to remind users of the origins of this protein.

# Results

## Discussion of the results

### What are the results?
Using some python scripts and other methods I managed to compile the information about __De-Novo proteins in CATH__ into [one big csv](https://github.com/CATH-summer-2017/De-Novo/blob/master/results/final_results.csv). My research shows the 463 De-Novo proteins in CATH are spread across 65 different superfamilies. However only 20 superfamilies have De-Novo that contribute to more than 5% of all domains. They are listed in the __table below:__

***


|                |                   |                           |                       | 
|----------------|-------------------|---------------------------|-----------------------| 
| __Superfamily ID__ | __Number of Domains__ | __Number of De-Novo Domains__ | __Proportion of De-Novo__ | 
| [3.30.1710.10](http://cathdb.info/version/v4_1_0/superfamily/3.30.1710.10/)   | 5                 | 5                         | 100.00%               | 
| [1.20.1480.30](http://cathdb.info/version/v4_1_0/superfamily/1.20.1480.30/)   | 2                 | 2                         | 100.00%               | 
| [1.20.120.660](http://cathdb.info/version/v4_1_0/superfamily/1.20.120.660/)   | 1                 | 1                         | 100.00%               | 
| [4.10.860.20](http://cathdb.info/version/v4_1_0/superfamily/4.10.860.20/)    | 18                | 17                        | 94.40%                | 
| [1.10.340.20](http://cathdb.info/version/v4_1_0/superfamily/1.10.340.20/)    | 2                 | 1                         | 50.00%                | 
| [1.20.1270.70](http://cathdb.info/version/v4_1_0/superfamily/1.20.1270.70/)   | 2                 | 1                         | 50.00%                | 
| [1.20.5.420](http://cathdb.info/version/v4_1_0/superfamily/1.20.5.420/)     | 120               | 46                        | 38.30%                | 
| [1.20.91.10](http://cathdb.info/version/v4_1_0/superfamily/1.20.91.10/)    | 44                | 15                        | 34.10%                | 
| [1.10.10.180](http://cathdb.info/version/v4_1_0/superfamily/1.10.10.180/)   | 45                | 15                        | 33.30%                | 
| [1.10.8.40](http://cathdb.info/version/v4_1_0/superfamily/1.10.8.40/)      | 13                | 3                         | 23.10%                | 
| [3.90.960.10](http://cathdb.info/version/v4_1_0/superfamily/3.90.960.10/)    | 27                | 6                         | 22.20%                | 
| [3.30.54.20](http://cathdb.info/version/v4_1_0/superfamily/3.30.54.20/)    | 18                | 3                         | 16.70%                | 
| [1.25.40.20](http://cathdb.info/version/v4_1_0/superfamily/1.25.40.20/)     | 293               | 46                        | 15.70%                | 
| [3.30.70.340](http://cathdb.info/version/v4_1_0/superfamily/3.30.70.340/)    | 29                | 4                         | 13.80%                | 
| [3.30.980.10](http://cathdb.info/version/v4_1_0/superfamily/3.30.980.10/)    | 27                | 3                         | 11.10%                | 
| [3.90.930.1](http://cathdb.info/version/v4_1_0/superfamily/3.90.930.1/)     | 20                | 2                         | 10.00%                | 
| [2.30.30.220](http://cathdb.info/version/v4_1_0/superfamily/2.30.30.220/)    | 33                | 3                         | 9.10%                 | 
| [3.10.20.10](http://cathdb.info/version/v4_1_0/superfamily/3.10.20.10/)    | 212               | 19                        | 9.00%                 | 
| [2.60.40.230](http://cathdb.info/version/v4_1_0/superfamily/2.60.40.230/)    | 27                | 2                         | 7.40%                 | 
| [1.25.10.10](http://cathdb.info/version/v4_1_0/superfamily/1.25.10.10/)     | 313               | 16                        | 5.10%                 | 
| [3.40.220.10](http://cathdb.info/version/v4_1_0/superfamily/3.40.220.10/)    | 198               | 10                        | 5.10%                 | 


***
### Discussion

As we can see from the table above, among the 20 superfamilies with over 5% De-Novo content, 6 have an over 50% De-Novo content, while having only 27 domains. It seems to me that these superfamilies might not belong in CATH, escpecially since some of them are very small ([1.20.120.660](http://cathdb.info/version/v4_1_0/superfamily/1.20.120.660/) is a good example, having only 1 domain). However I am still unsure about the general idea of De-Novo proteins in CATH



