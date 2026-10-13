## ReadMe
### Purpose
The purpose of this project is to maintain a Provincial rating system for Men's Singles badminton players based on match results from events hosted in BC on tournamentsoftware.com and badmintoncanada.tournamentsoftware.com.

### Introduction
For more information on how the ELO rating system works, see the initial prototype: [github.com](https://github.com/a-meijer/showcase/tree/master/ELO)

For a demonstration of the accuracy of the rankings compared to the official rankings, see the previous version from 2025: [github.com](https://github.com/a-meijer/showcase/tree/master/BadmintonRankings_v1)

The match data for each tournament is in CSV files in the tournaments directory.

Tournament match data is also on Google Drive:
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
The rating algorithm saves files as it processes tournaments. If a tournament is processed erroneously or in the wrong chronological order, the algorithm must be reset back from 2022. To reset the algorithm, delete all files in /data/2022/ and delete the matchlist, output, and tdata files in /data/. Then run 2022Tournaments.py. All of the 2022 tournaments are hard-coded in there. Initializing the algorithm may require an empty 2022/players folder and an blank tdata.csv file.

### Previous Years
The rankings for previous years, starting from 2022, are saved to separate Markdown files.

### Previous Versions
After the prototype versions, I made the first full version of my rankings project in 2025.
For that version, I only used tournaments that affected Provincial Rankings.


## 2025 Top 100 Rankings
See data/2025/2025ranking.md for the full list of rankings.
Ranking is subject to change as new features and upgrades are added to the ranking algorithm.
|Rank|Rating|Name|ID|Wins|Losses|Previous Rank|Previous Rating|Latest Tournament|
|---|---|---|---|---|---|---|---|---|
|1|1619|Saurabh Pandiar|BC17070|90|12|3|1640|2025-12-26|
|2|1587|Antonio Li|BC7414|14|2|1|1722|2025-04-18|
|3|1586|Jadon Tsang|BC7711|11|2|NR|1244|2025-11-14|
|4|1567|Anish Jojula|BC18940|41|8|7|1516|2025-08-02|
|5|1559|Jason Ho-Shue|ON10935|6|0|NR|1000|2025-04-18|
|6|1521|Ethan Ao|U1020508|7|1|58|1124|2025-12-26|
|7|1516|Nicholas Chiu|USA00021|12|3|NR|1333|2025-04-18|
|8|1482|Lyem Fedoretz|BC13763|50|12|8|1473|2025-06-21|
|9|1472|Nik Cruz|BC3960|24|5|25|1265|2025-11-14|
|10|1470|Gurbaksh Saini|ON41508|50|15|9|1471|2025-04-18|
|11|1431|Kevin Luo|BC8266|30|10|11|1436|2025-04-18|
|12|1429|Lap Hang Hugo Pong|BC20238|5|1|NR|1000|2025-04-18|
|13|1394|Roger Quach|BC17133|32|13|16|1344|2025-11-14|
|14|1393|Digby Johannson-Miller|BC15083|11|6|NR|781|2025-11-21|
|15|1389|Raunak Sandhu|AB20272|8|4|40|1164|2025-08-02|
|16|1384|Yu-Yuan Chang|U20020423|11|4|5|1629|2025-06-21|
|17|1354|Imran Wadia|AB07299|5|2|NR|1207|2025-04-18|
|18|1352|Wenjun Ouyang|BC8870|6|3|14|1386|2025-04-18|
|19|1340|Pratham Sangwan|X24191232|4|0|NR|1000|2025-11-29|
|20|1337|Ryan Liu|BC10841|26|14|15|1352|2025-08-02|
|21|1324|Lai Yin Chung|BC17060|9|5|22|1284|2025-04-18|
|22|1317|Fengjie Hu|BC16226|12|6|21|1285|2025-11-14|
|23|1313|Alex Anlai Song|X1019779|7|4|63|1117|2025-12-26|
|24|1311|Jaden Thom|BC15336|32|15|19|1324|2025-12-26|
|25|1302|Harrison Liu|BC17354|7|1|NR|1000|2025-02-07|
|26|1298|Nguyen Phan|BC19242|7|2|NR|1151|2025-11-21|
|27|1293|Victor Ho|MB09472|21|13|24|1281|2025-04-18|
|28|1289|David Yang|BC9870|16|6|26|1260|2025-04-21|
|29|1289|Jack Chen|BC10265|27|16|18|1325|2025-04-18|
|30|1285|Lasitha Menaka|USA00081|3|1|NR|1000|2025-04-18|
|31|1281|Alexis Duval|BC6020|12|3|20|1309|2025-11-14|
|32|1273|Connor Louie|BC10576|37|23|27|1220|2025-08-02|
|33|1273|Eden Dewei Liang|BC14809|7|5|43|1161|2025-08-02|
|34|1264|Peike Xu|BC15886|17|7|17|1340|2025-04-18|
|35|1264|Shingchun (Kevin) Wu|BC14906|20|14|37|1185|2025-08-02|
|36|1260|Ruixi Zhang|BC14918|24|17|33|1211|2025-04-18|
|37|1257|Anton Menzel|AB09146|5|3|59|1122|2025-04-18|
|38|1256|Nicholas Poon|BC14114|24|16|23|1284|2025-11-29|
|39|1256|Neil Ward|BC0435|13|4|NR|1248|2025-11-21|
|40|1250|Miklos Kanyasi|NS1999456|5|3|34|1207|2025-04-18|
|41|1244|Uday Bharti|BC15951|22|14|35|1198|2025-11-29|
|42|1242|Sarabpreet Sodhi|BC17850|8|6|157|971|2025-11-29|
|43|1240|Joseph Lu|ON14211|3|1|NR|1000|2025-11-14|
|44|1209|Yun Chi Lo|X22575070|3|1|NR|1000|2025-04-18|
|45|1207|Brendan KC Wong|BC14055|10|7|193|887|2025-12-26|
|46|1204|Kwun Ho So|BC12748|30|17|30|1213|2025-11-14|
|47|1192|Angus Li|BC3939|9|4|86|1072|2025-11-14|
|48|1188|Peter Tran|BC5824|5|4|NR|1000|2025-12-26|
|49|1186|Victor Chang|BC16223|12|13|141|991|2025-11-14|
|50|1185|Shourya Joshi|BC17705|5|4|171|938|2025-06-21|
|51|1180|Son Do Trieu Phan|BC19243|4|1|NR|1000|2025-01-03|
|52|1172|Kiren Deraj|MB1631|4|4|28|1218|2025-04-18|
|53|1171|Baolin Zhao|BC12035|2|1|NR|1000|2025-10-11|
|54|1170|Jalil Waiz|BC7562|27|25|42|1163|2025-11-29|
|55|1167|Hailegebriel Kebede|BC12752|14|9|55|1132|2025-11-14|
|56|1164|Joshua R Yan|BC9134|9|5|41|1164|2024-12-27|
|57|1161|Robert Ruobei Xu|BC13987|3|3|44|1161|2024-12-27|
|58|1159|Aadharsh Hariharan|BC19780|7|5|NR|1000|2025-11-14|
|59|1153|Ratnesh Ippili|BC17071|20|18|79|1084|2025-11-29|
|60|1151|Colt Love|BC12636|24|22|123|1010|2025-11-14|
|61|1148|Andrew Meijer|BC6030|14|22|206|744|2025-12-26|
|62|1142|Simar Singh|BC18188|19|12|29|1215|2025-12-26|
|63|1141|Colin Wang|BC12492|10|6|93|1058|2025-11-14|
|64|1135|Aaron Lin|BC12213|5|3|101|1042|2025-11-14|
|65|1130|Evan Zhang|BC12220|3|2|139|994|2025-08-02|
|66|1127|Jason Carlson|X22114996|4|2|NR|1000|2025-11-21|
|67|1124|Harry Ng|BC15958|2|2|NR|963|2025-12-26|
|68|1123|Robert Foster|BC6881|10|5|31|1212|2025-10-03|
|69|1111|Hardeep Singh|BC13447|2|2|NR|1025|2025-11-14|
|70|1108|Jason Chiu|AB22318|3|3|191|896|2025-04-18|
|71|1107|Adrian Unruh|U158261|3|2|67|1107|2024-12-27|
|72|1099|Jack Saunders|AB10192|11|9|48|1151|2025-11-21|
|73|1097|Jason Too|BC19055|2|2|68|1106|2025-02-07|
|74|1096|Charlton Li|ON31174|4|3|57|1124|2025-06-06|
|75|1094|Anirudh Rajesh|U1021461|2|1|72|1094|2024-12-27|
|76|1086|Nathan Lee|BC16181|6|6|38|1182|2025-04-18|
|77|1082|Andrew Gu|MB36006|4|4|NR|925|2025-11-29|
|78|1080|Daniel-Kyle Tan|BC16232|1|1|NR|1000|2025-02-07|
|79|1074|Vincent Chen|U1019469|2|1|85|1074|2024-12-27|
|80|1074|Mark Kitts|BC14477|2|1|NR|1000|2025-11-21|
|81|1073|Aakar Chatha|BC17063|19|22|61|1117|2025-10-11|
|82|1072|Jason Yang|BC12317|8|6|88|1072|2024-12-27|
|83|1069|Zhenghao (Hao) Cui|BC13992|2|1|NR|1000|2025-08-02|
|84|1067|Nathaniel Volfbeyn|U1022176|1|1|NR|1000|2025-12-26|
|85|1063|Carlos Chan|BC17072|3|3|NR|1034|2025-04-18|
|86|1063|Jacob Chuhua Zhang|BC12208|1|1|NR|1000|2025-04-18|
|87|1061|Van Long Nguyen|BC16173|16|19|127|1005|2025-11-14|
|88|1060|Saqib Talewad|BC17557|2|1|NR|1000|2025-01-10|
|89|1055|Robert Shi|BC13617|11|9|83|1076|2025-04-04|
|90|1054|Stephen Dee|BC0389|7|5|62|1117|2025-11-14|
|91|1053|Kai Yang|BC12746|2|1|NR|1000|2025-06-21|
|92|1051|Sunil Wadhwa|BC18927|2|2|NR|977|2025-06-21|
|93|1051|Hayden Ostrom|BC8161|3|2|NR|1002|2025-11-21|
|94|1047|Luke Peter Evans|X23347624|1|1|NR|1000|2025-08-02|
|95|1045|Felix Zhen|BC15340|7|6|90|1067|2025-12-26|
|96|1043|Johnathan Chi|BC14691|1|2|NR|1000|2025-12-26|
|97|1041|Job Babu|BC20274|2|2|NR|941|2025-01-03|
|98|1040|Nicholas Volfbeyn|X1022178|4|4|130|1002|2025-12-26|
|99|1039|Keyu Zhou|ON34750|1|1|NR|1000|2025-04-18|
|100|1039|Allen George|U47084|1|1|NR|1000|2025-12-26|

### Tournaments
See the file data/2025/2025tournaments.md for the full list of tournaments and winners.

### Author
Andrew Meijer