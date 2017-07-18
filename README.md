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
