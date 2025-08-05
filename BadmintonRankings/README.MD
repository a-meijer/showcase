## ReadMe
### Purpose
The purpose of this project is to maintain a Provincial rating system for Men's Singles badminton players based on the official ranking system for British Columbia, using the tournaments that award points towards the official rankings.

### Introduction
For more information on how the ELO rating system works, see the initial prototype: [github.com/a-meijer/showcase](https://github.com/a-meijer/showcase/tree/master/ELO)
For more information on the ongoing development process, see devlog.txt.
Match data is available on Google Drive:
https://drive.google.com/drive/folders/1GX5JPSUZaMUrkilviBPgyZCzfP7bpef-?usp=sharing

The match data for each tournament is in CSV files in the tournaments directory.

### The Validity And Accuracy of the Ratings
The theory behind what makes this rating system more accurate than the official rankings is that it depends on match results rather than tournament placement.
The results of individual matches affect rating points, not the results of tournaments. For example, if you lost in the first round of a tournament to a high rank opponent, that wouldn't affect your rating as much as losing to a low rank oppoent.
To reconcile these ratings with the official provincial rankings, I will only use the results from tournaments that affect the official rankings.

### The First Tournament
There were no provincial ranking tournaments in 2020 or 2021, and since tournaments only affect the official rankings for two years, the official rankings were reset in 2022.
Therefore, it is fitting to start this ratings project from the first provincial ranking tournament in 2022, when the provincial rankings were reset. 
The Provincial Ratings will be aligned with the official rankings in this way.
As new tournament results are incorporated into the official rankings, they will also be incorporated into these ratings according to the purpose of this project.

### About The Initial Prototype
The initial prototype for this project is called "ELO": [github.com/a-meijer/showcase](https://github.com/a-meijer/showcase/tree/master/ELO)
At the time of the initial prototype, in the Summer of 2024, it was easy to copy and past the match results from each tournament into spreadsheets to use for the ELO ratings algorithm.
Unfortunately, due to a reformatting of the website, it is no longer as easy to copy the match data from the match pages. Henceforth I will manually copy the match data into spreadsheets.
The silver lining of this is that manually copying the match data into spreadsheets makes it is easier to avoid copying the consolation matches which should not affect rating points.

### How To Use The Rating System
To use the rating algorithm, run the program: src/main.py
By default, the program selects "Ratings.csv" as the input data file, but you may opt for a different filename.
The program selects "RatingsOutput.csv" as the default output data file, but you may change the filename; just be careful not to overwrite anything.
You will need to enter the filename for the tournament match data you are processing. You will need to approve the initial rankings for new players.
Now RankingsOutput.csv should be used as the input data file for the next tournament.
You can run printRankings.py RankingsOutput.csv to display the new rankings.

### Ratings
|Rating|Name                           |ID     |Wins|Losses|
|------|-------------------------------|-------|----|------|
|1530  |ANISH Chandra Jojula           |BC18940|14  |1     |
|1518  |Saurabh Pandiar                |BC17070|23  |3     |
|1406  |Lyem Fedoretz                  |BC13763|9   |1     |
|1319  |Joshua Liu                     |BC1815 |6   |1     |
|1306  |Victor Ho                      |MB09472|12  |5     |
|1303  |Ziyi Yang Jackson              |BC10895|4   |0     |
|1274  |Connor Nicholas Louie          |BC10576|10  |6     |
|1247  |Peike Xu                       |BC15886|4   |1     |
|1247  |Rickey Ruixi Zhang             |BC14918|7   |4     |
|1240  |Gurbaksh Singh Saini           |ON41508|6   |2     |
|1211  |Kevin Luo                      |BC8266 |5   |2     |
|1211  |Ryan Liu                       |BC10841|4   |2     |
|1209  |Jack Chen                      |BC10265|7   |6     |
|1193  |Jadon Tsang                    |BC7711 |3   |1     |
|1171  |Raunak Sandhu                  |AB20272|4   |1     |
|1163  |Uday pratap Bharti             |BC15951|9   |5     |
|1151  |Jalil Waiz                     |BC7562 |10  |8     |
|1150  |Jasper Kong                    |BC16320|4   |2     |
|1122  |Joshua R Yan                   |BC9134 |2   |1     |
|1119  |simar singh                    |BC18188|9   |5     |
|1115  |Ratnesh Rao Ippili             |BC17071|7   |6     |
|1095  |Tai-Yu (Harrison) LIU          |BC17354|2   |1     |
|1090  |Shingchun (Kevin) Wu           |BC14906|3   |2     |
|1081  |Connor O'Reilly                |BC16854|2   |1     |
|1076  |YiYang Jiang                   |ON13537|2   |1     |
|1074  |Kwun Ho So                     |BC12748|3   |2     |
|1070  |Nicholas Poon                  |BC14114|4   |4     |
|1066  |Sarabpreet Singh Sodhi         |BC17850|4   |3     |
|1052  |Allan Crawford                 |BC15210|1   |1     |
|1052  |Daniel-Kyle Tan                |BC16232|1   |1     |
|1050  |Roger Quach                    |BC17133|2   |2     |
|1048  |Brian McBay                    |BC14400|1   |1     |
|1043  |Simon Wu                       |BC17274|2   |2     |
|1039  |Robert Zhongjia Shi            |BC13617|6   |5     |
|1034  |William Ka wang Ma             |BC15972|1   |1     |
|1026  |Paul Cho                       |BC3748 |2   |2     |
|1025  |Manmeet Singh                  |BC16926|1   |1     |
|1025  |Mahdi Ahmadi                   |BC15814|1   |1     |
|1025  |Trevor Tak Sing Chun           |BC15986|1   |1     |
|1025  |ZeLin Shan                     |BC16166|1   |1     |
|1021  |Kelsey Liang                   |BC13170|1   |1     |
|1013  |Van Long Nguyen                |BC16173|2   |2     |
|1010  |Ayush Ayush                    |BC18578|1   |2     |
|1009  |Ethan Yen                      |BC14739|1   |1     |
|1007  |Franklin Chen                  |BC17865|2   |2     |
|1003  |Michael Poon                   |BC9740 |1   |1     |
|1003  |Luke Lee                       |BC8269 |1   |1     |
|1003  |Will Bui                       |BC13605|1   |1     |
|1003  |Colin Wang                     |BC12492|1   |1     |
|1003  |Maurice Li                     |BC18471|1   |1     |
|1000  |Angus Li                       |BC3939 |1   |1     |
|993   |Stephen Dee                    |BC0389 |2   |2     |
|993   |Jaden Thom                     |BC15336|1   |3     |
|992   |Aakar Chatha                   |BC17063|5   |6     |
|992   |Jason Too                      |BC19055|0   |1     |
|992   |Colt Love                      |BC12636|2   |4     |
|986   |Daniel Huang                   |BC14954|1   |1     |
|976   |Barry Xie                      |BC17273|1   |2     |
|974   |Rinesh Dilshan Hetti Arachchige|BC20039|1   |1     |
|968   |Brandon Robert Myrbo           |BC16273|1   |2     |
|967   |Sahil Rajesh Aggarwal          |BC16091|1   |2     |
|966   |Ryan Chee Khun Chung           |BC14991|0   |1     |
|948   |THOMAS GEORGE                  |BC19905|1   |3     |
|947   |Eddie Huang                    |BC17311|0   |1     |
|946   |Andrew Meijer                  |BC6030 |2   |4     |
|940   |Renjie Xiong                   |BC18391|1   |2     |
|935   |Loki Fung                      |BC17229|2   |3     |
|935   |Roy Hung                       |BC11052|1   |3     |
|933   |John Ou                        |BC16127|1   |2     |
|932   |Nghia Tuan Nguyen              |BC20030|0   |1     |
|932   |Aadharsh Hariharan             |BC19780|0   |1     |
|929   |Laurence Kao                   |BC3829 |0   |1     |
|928   |Nicholas Lee                   |SK01305|0   |1     |
|928   |Raymond Wu                     |BC16114|0   |1     |
|928   |Robert Stephen Foster          |BC6881 |0   |1     |
|928   |Bangjian (James) Geng          |BC13109|0   |1     |
|928   |Oliver Long                    |BC13904|0   |1     |
|927   |Josemaria (JM) Teleg           |BC16122|2   |4     |
|926   |Dwayne da Silva                |BC18335|0   |1     |
|925   |Brian Liu                      |BC18365|0   |1     |
|921   |Peter Tran                     |BC5824 |0   |1     |
|919   |Ev Haus                        |BC19123|0   |2     |
|919   |Andy Le                        |BC17175|1   |3     |
|908   |Jithin Prakash                 |BC15890|1   |2     |
|907   |Zhengheng Bao                  |BC18926|0   |1     |
|900   |Fong-Ming Chow                 |BC16012|0   |1     |
|900   |Adrian KH Wong                 |BC12183|0   |1     |
|900   |Nelson Oi Sang Chan            |BC16318|0   |1     |
|900   |Lai Yin Chung                  |BC17060|0   |1     |
|900   |Anjie Wang                     |BC17891|0   |1     |
|900   |Dan MacDonald                  |BC0474 |0   |1     |
|900   |Frank Nguyen                   |BC17406|0   |1     |
|900   |Volodymyr Zubariev             |BC17770|0   |1     |
|900   |Rahi Kumar                     |BC17795|0   |1     |
|900   |Hayden Lam                     |BC16882|0   |1     |
|900   |Zhijing Liu                    |BC14515|0   |1     |
|900   |John McWalter Keith            |BC17576|0   |1     |
|900   |Markus Weilmeier               |BC10033|0   |1     |
|900   |Leo Shen                       |BC15094|0   |1     |
|900   |Nusorn Krachangtoy             |BC8364 |0   |1     |
|900   |David Yang                     |BC9870 |0   |1     |
|900   |Jack Saunders                  |AB10192|0   |1     |
|900   |Eugene Kwok                    |BC17953|0   |1     |
|900   |Shukang Wang                   |BC16808|0   |1     |
|900   |Hossein Ahmadi                 |BC17717|0   |1     |
|900   |Yichen Li                      |BC18977|0   |1     |
|900   |Marcus James Tseng             |BC16125|0   |1     |
|900   |Ayden Travis Lee               |BC16117|0   |1     |
|900   |Yancong Li                     |BC19032|0   |1     |
|900   |Justin Lam                     |BC14897|0   |1     |
|900   |Keshav Jheeta                  |BC17169|0   |1     |
|900   |Digby Johannson-Miller         |BC15083|0   |1     |
|898   |Benson Wong                    |BC16112|0   |1     |
|877   |Yigit Kirsan                   |BC19455|0   |1     |
|871   |Marcus Chan                    |BC16107|0   |1     |
|871   |Quinn Lawler                   |AB22569|0   |1     |
|871   |Chi-Kin Chan                   |BC15989|0   |1     |
|871   |Dayton Se                      |BC13042|0   |1     |
|870   |Soham Ghugal                   |BC19017|0   |3     |
|867   |Shen Wei Lai                   |BC8302 |0   |2     |
|865   |Brendon Kwan                   |BC9351 |0   |2     |
|863   |Clayton A Miller               |BC4316 |0   |1     |
|857   |Arseny Shestakov               |BC17183|0   |2     |
|855   |Justin Phuong                  |BC11051|0   |2     |
|850   |Luca Ferretti                  |ON35979|0   |2     |
|847   |Gilbert Limarta                |BC19167|0   |2     |
|838   |Rohail Mir                     |BC19034|0   |3     |
|825   |Samuel Ha                      |BC17845|0   |2     |
|824   |Jesse Guo                      |BC19644|0   |3     |
|823   |Gurnishan Singh Sidhu          |BC19528|0   |3     |
|776   |Isaac Fu                       |BC18369|0   |3     |

### Tournaments
2022 BC OPEN AND U-23 PROVINCIAL CHAMPIONSHIP

2023 Jack Underhill Open

2023 BC Junior A, U23 and Open Provincial Championship

2024 VRC Jack Underhill Open A and B Tournament

2024 BC Junior A and Open Provincial Championship (U15,U17,U23, Open A & B)

Wing’s Open Badminton Tournament

Shuttlesport Open Series #2

2025 VRC Jack Underhill Open A & B Tournament

2025 BC Junior A, Open A and Open B Provincial Championships


### Author
Andrew Meijer