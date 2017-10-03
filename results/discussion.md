## Discussion of the results
### What are the results?
Using some python scripts and other methods I managed to compile the information about __De-Novo proteins in CATH__ into [one big csv](https://github.com/CATH-summer-2017/De-Novo/blob/master/results/superfam_info.csv). The most important column in the csv is the first two - they show which superfamilies have whoich proportion of De-Novo proteins. My research shows the 166 De-Novo proteins in CATH are spread across 47 different superfamilies. However only 10 superfamilies have De-Novo that contribute to more than 5% of all domains. They are listed in the __table below:__

***


| superfam id | de-novo proportion | number of domains | number of de-novo | example domain id | description |
| ------------| --------- | --- | ------- | ----- | ------------------- |
| [1.20.1480.30](http://cathdb.info/version/v4_1_0/superfamily/1.20.1480.30/) | 100.00% | 2 | 2 | 1p68A00 | Designed four-helix bundle protein | 
| [3.30.1710.10](http://cathdb.info/version/v4_1_0/superfamily/3.30.1710.10/) | 100.00% | 5 | 5 | 1qysA00 | "top7 |  de novo designed protein" | 
| [1.20.1270.70](http://cathdb.info/version/v4_1_0/superfamily/1.20.1270.70/) | 50.00% | 2 | 1 | 2zxqA06 | Designed single chain three-helix bundle | 
| [4.10.860.20](http://cathdb.info/version/v4_1_0/superfamily/4.10.860.20/) | 33.33% | 18 | 6 | 3v1aA00 | "rabenosyn (458-503) |  rab4 binding domain " | 
| [1.10.8.40](http://cathdb.info/version/v4_1_0/superfamily/1.10.8.40/) | 23.08% | 13 | 3 | 2j5yA00 | Albumin-binding domain | 
| [1.20.5.420](http://cathdb.info/version/v4_1_0/superfamily/1.20.5.420/) | 10.00% | 120 | 12 | 4npdA00 | "Immunoglobulin FC |  subunit C" | 
| [3.30.980.10](http://cathdb.info/version/v4_1_0/superfamily/3.30.980.10/) | 7.41% | 27 | 2 | 1v4pA01 | "Threonyl-trna Synthetase; Chain A |  domain 2" | 
| [3.90.960.10](http://cathdb.info/version/v4_1_0/superfamily/3.90.960.10/) | 7.41% | 27 | 2 | 2dxaA00 | YbaK/ProRS associated domain | 
| [3.30.70.340](http://cathdb.info/version/v4_1_0/superfamily/3.30.70.340/) | 6.90% | 29 | 2 | 1kwmA01 |  | 
| [1.25.40.20](http://cathdb.info/version/v4_1_0/superfamily/1.25.40.20/) | 6.83% | 293 | 20 | 4duiA00 |  | 

***
### Discussion

As we can in these superfamilies domains from De-Novo proteins make up quite a significant proportion, in some more than in others. Quite an intersting example is the 1.20.1270.70 superfamily, consisting of only 2 domains, one of them De-Novo and one of them 6th domain of endo-alpha-N-acetylgalactosaminidase. 2 superfamilies that consist of only De-Novo proteins are suspicious as well.

### Issues

I plan to rewrite the code in /scripts directory so it would do more check and in general be more defensive, which may result in appearance of a couple of other De-Novo proteins that I might have missed before. 
