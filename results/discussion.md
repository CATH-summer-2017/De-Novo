## Discussion of the results
### What are the results?
Using some python scripts and other methods I managed to compile the information about __De-Novo proteins in CATH__ into [one big csv](https://github.com/CATH-summer-2017/De-Novo/blob/master/results/final_results.csv).

My research shows the 463 De-Novo proteins in CATH are spread across 65 different superfamilies. However only 20 superfamilies have enough De-Novo domains, contributing to more than 5% of all domains. They are listed in the __table below:__

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
