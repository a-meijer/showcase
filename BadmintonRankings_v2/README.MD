## ReadMe
### Purpose
The purpose of this project is to maintain a Provincial rating system for Men's Singles badminton players based on match results from events hosted in BC on tournamentsoftware.com

### Introduction
For more information on how the ELO rating system works, see the initial prototype: [github.com](https://github.com/a-meijer/showcase/tree/master/ELO)

The 2022 and 2023 rankings have been created, and the 2024 rankings are in development. For more information on the ongoing development process, see devlog.txt.

For a demonstration of the accuracy of the rankings compared to the official rankings, see the previous version from 2025: [github.com](https://github.com/a-meijer/showcase/tree/master/BadmintonRankings_v1)

The match data for each tournament is in CSV files in the tournaments directory.

Match data is also available on Google Drive:
https://drive.google.com/drive/folders/1GX5JPSUZaMUrkilviBPgyZCzfP7bpef-?usp=sharing

Summary and analysis of each year's ranking is available on my blog: https://andrewmeijer.substack.com

### The Validity And Accuracy of the Ratings
The theory behind what makes this rating system more accurate than the official rankings is that it depends on match results rather than tournament placement.
The results of individual matches affect rating points, not the results of tournaments. For example, if you lost in the first round of a tournament to a high rank opponent, that wouldn't affect your rating as much as losing to a low rank opponent.

### The First Tournament
There were no provincial ranking tournaments in 2020 or 2021, and since tournaments only affect the official rankings for two years, the official rankings were reset in 2022.
Therefore, it is fitting to start this ratings project from the first tournament of 2022, when the provincial rankings were reset.

### About The Initial Prototype
The initial prototype for this project is called "ELO": [github.com/a-meijer/showcase](https://github.com/a-meijer/showcase/tree/master/ELO)
At the time of the initial prototype, in the Summer of 2024, it was easy to copy and past the match results from each tournament into spreadsheets to use for the ELO ratings algorithm.
Unfortunately, due to a reformatting of the website, it is no longer as easy to copy the match data from the match pages. Henceforth I will manually copy the match data into spreadsheets.
The silver lining of this is that manually copying the match data into spreadsheets makes it is easier to avoid copying the consolation matches which should not affect rating points.

### How To Use The Rating System
The rating algorithm saves files as it processes tournaments. If a tournament is processed erroneously or in the wrong chronological order, the algorithm must be reset back from 2022. To reset the algorithm, delete all files in /data/2022/ and delete the matchlist, output, and tdata files in /data/. Then run 2022Tournaments.py. All of the 2022 tournaments are hard-coded in there.

### Previous Years
The rankings for previous years, starting from 2022, are saved to separate Markdown files.

### Previous Versions
After the prototype versions, I made the first full version of my rankings project in 2025.
For that version, I only used tournaments that affected Provincial Rankings.



## 2024 Top 100 Rankings
See data/2024/2024Ranking.md for the full list of rankings.
Ranking is subject to change as new features and upgrades are added to the ranking algorithm.

|Rank|Rating|Name|ID|Wins|Losses|Previous Rank|Previous Rating|
|---|---|---|---|---|---|---|---|
|1|1654|Antonio Li|BC7414|14|1|2|1519|
|2|1615|Victor Lai|ON13010|9|1|10|1335|
|3|1606|Saurabh Pandiar|BC17070|80|10|3|1491|
|4|1601|Joshua Nguyen|ON13127|14|1|1|1627|
|5|1559|Yu-Yuan Chang|U20020423|11|2|21|1242|
|6|1497|Joshua Liu|BC1815|13|3|5|1469|
|7|1458|Anish Jojula|BC18940|28|7|101|1048|
|8|1449|Gurbaksh Saini|ON41508|46|13|6|1450|
|9|1445|Lyem Fedoretz|BC13763|45|11|4|1481|
|10|1397|Zachary Desjardins|QC11074|6|2|74|1077|
|11|1393|Ricky Lo|X980302|6|2|NR|1000|
|12|1390|Jackson Yang|BC10895|22|6|8|1355|
|13|1370|Kevin Luo|BC8266|28|9|11|1332|
|14|1350|Matt Downton|BC1418|5|0|9|1350|
|15|1345|Wenjun Ouyang|BC8870|5|2|70|1088|
|16|1333|Ryan Liu|BC10841|24|13|7|1364|
|17|1329|Nicholas Chiu|USA00021|7|2|12|1329|
|18|1328|Harrison Hsu|BC4245|4|0|13|1328|
|19|1309|Peike Xu|BC15886|16|6|15|1305|
|20|1286|Jaden Thom|BC15336|20|8|16|1260|
|21|1273|Jack Chen|BC10265|27|15|29|1208|
|22|1270|Alexis Duval|BC6020|9|2|27|1213|
|23|1259|Nik Cruz|BC3960|12|4|20|1245|
|24|1253|Roger Quach|BC17133|24|11|38|1165|
|25|1252|Lai Yin Chung|BC17060|7|4|37|1168|
|26|1248|Connor Chin|AB03249|5|2|18|1248|
|26|1248|David Purnomo|BC17159|6|2|17|1248|
|28|1246|Neil Ward|BC0435|7|2|19|1246|
|29|1235|Jadon Tsang|BC7711|3|1|22|1235|
|30|1226|Fengjie Hu|BC16226|9|5|212|927|
|31|1220|Victor Ho|MB09472|17|11|46|1148|
|32|1218|David Yang|BC9870|10|5|52|1131|
|33|1216|Simar Singh|BC18188|15|8|NR|1000|
|34|1212|Robert Foster|BC6881|9|4|23|1235|
|34|1212|Guillaume Blais|QC10468|2|1|NR|1000|
|36|1208|Imran Wadia|AB07299|3|1|28|1208|
|37|1205|Nicholas Poon|BC14114|14|10|114|1033|
|38|1200|Daniel Jieru Zhou|AB21350|3|1|31|1200|
|38|1200|Connor Louie|BC10576|29|20|26|1214|
|40|1199|Jasper Kong|BC16320|12|6|33|1191|
|41|1194|Kwun Ho So|BC12748|27|15|24|1220|
|42|1192|Kiren Deraj|MB1631|4|3|63|1100|
|43|1188|Mitchell Purnomo|BC17160|4|2|34|1188|
|44|1178|Miklos Kanyasi|NS1999456|3|2|113|1035|
|45|1170|Uday Bharti|BC15951|14|9|55|1122|
|45|1170|Joshua R Yan|BC9134|9|5|25|1219|
|47|1167|Nathan Lee|BC16181|6|5|30|1206|
|48|1164|Shingchun (Kevin) Wu|BC14906|14|11|56|1117|
|49|1160|Ruixi Zhang|BC14918|18|15|58|1115|
|50|1159|Albert Liang|BC11047|4|2|40|1159|
|51|1158|David Crawford|BC4189|5|2|41|1158|
|52|1154|Anthony Wong|AB09514|4|2|43|1154|
|53|1152|Kyi Nichols|MB0064|2|2|66|1092|
|54|1150|Nguyen Phan|BC19242|3|1|45|1150|
|55|1148|Justin L Li|ON14222|5|2|54|1124|
|55|1148|Robert Ruobei Xu|BC13987|3|3|NR|1000|
|57|1147|Connor O'Reilly|BC16854|8|5|48|1147|
|58|1146|Manmeet Singh|BC16926|8|3|49|1146|
|59|1145|Eden Dewei Liang|BC14809|3|3|NR|1000|
|60|1140|Ethan Yen|BC14739|13|11|47|1147|
|61|1139|Ayden Travis Lee|BC16117|5|2|14|1320|
|62|1137|Andrew Zhuang|ON9302|2|1|NR|1000|
|62|1137|Reven Liu|BC9635|3|1|NR|1000|
|64|1135|Evan Chen|BC18670|3|3|68|1092|
|65|1132|Anton Menzel|AB09146|3|2|36|1172|
|65|1132|Austin Flannigan|ON10357|2|1|NR|1000|
|65|1132|Raunak Sandhu|AB20272|4|2|NR|968|
|68|1131|Dale Kinley|MB0044|3|3|44|1152|
|69|1120|Luo Kai Wen|X21695129|2|1|NR|1000|
|70|1119|Ethan Ao|U1020508|2|1|NR|1000|
|71|1117|Hossein Ahmadi|BC17717|8|6|32|1194|
|71|1117|Mitash Jain|BC17537|3|3|163|995|
|73|1112|Hailegebriel Kebede|BC12752|10|7|59|1112|
|74|1111|Adrian Unruh|U158261|3|2|NR|1000|
|75|1107|Stephen Dee|BC0389|6|3|NR|1000|
|76|1105|Daniel Leung|ON13705|2|1|NR|1000|
|77|1103|Jalil Waiz|BC7562|20|19|118|1031|
|78|1102|Jason Too|BC19055|2|1|NR|1000|
|78|1102|Charlton Li|ON31174|3|2|91|1061|
|78|1102|Jack Saunders|AB10192|9|7|129|1020|
|81|1100|Youwei Zhang|BC15945|2|1|62|1100|
|82|1098|Jordan Sipos|BC6054|2|1|64|1098|
|83|1097|Louis N Thai|BC14680|3|2|57|1117|
|84|1096|Kevin Aissa|BC19253|5|3|135|1013|
|85|1093|William Ma|BC15972|7|7|42|1155|
|86|1091|Angus Li|BC3939|4|2|39|1165|
|86|1091|David Zuo|X1019625|2|1|69|1091|
|88|1090|Nathan Quach|AB22070|2|2|85|1063|
|88|1090|Liam Zhang|ON30018|1|1|NR|1000|
|90|1088|Franklin Chen|BC17865|8|7|120|1028|
|91|1087|Alex Anlai Song|X1019779|3|3|137|1010|
|92|1086|Zheng Fang|QC10585|2|1|71|1086|
|93|1085|Cyrus Lau|BC15982|4|3|103|1046|
|93|1085|Anirudh Rajesh|U1021461|2|1|NR|1000|
|95|1083|Chris Wiebe|MB1371|3|3|35|1175|
|95|1083|Brian McBay|BC14400|1|1|73|1083|
|97|1081|Sahil Aggarwal|BC16091|11|12|181|982|
|98|1080|Eason Wong|AB09702|2|2|96|1059|
|99|1077|Harrison Guo|X00217|4|4|124|1024|
|100|1076|Colin Wang|BC12492|6|4|88|1061|

### Tournaments
See the file TournamentWinners.md for the full list of tournaments and winners.

### Author
Andrew Meijer