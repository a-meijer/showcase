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
The rating algorithm saves files as it processes tournaments. If a tournament is processed erroneously or in the wrong chronological order, the algorithm must be reset back from 2022. To reset the algorithm, delete all files in /data/2022/players and delete the matchlist.csv and output.csv files in /data/. Delete the contents of tdata.csv and save it as a blank file. Then run 2022Tournaments.py. All of the 2022 tournaments are hard-coded in there to be processed in order. This will create a matchlist.csv file which shows in order all the matches that have been processed, and it will create output.csv which is the player rankings. tdata.csv shows the winners of each of the tournaments and has running stats including the total number of matches, total number of players, player ID with most matches, and player ID with most wins. It will also populate /data/2022/players with files for each of the players. The data in these files can be queried with search.py by searching for player IDs on the command line. To get the ID for the player you want, search by name, and search.py will print their ID. You may need to change search.py so it points to the right folder containing player files. It points to /data/2026/players by default. To process the 2023 tournaments, copy the contents of /data/2022/players into /data/2023/players and then run 2023Tournaments.py. Repeat this process for 2024, 2025, and 2026, copying the player data to the next year's folder and running 20XXTournaments.py. To see the results in a markdown format, run CSVToMD_Rankings.py and CSVToMD_Winners.py.

### Previous Years
The rankings for previous years, starting from 2022, are saved to separate Markdown files in the /data subfolders.

### Previous Versions
After the prototype versions, I made the first full version of my rankings project in 2025.
For that version, I only used tournaments that affected Provincial Rankings.

### More Information
For more information, summary, and analysis of the rankings see the relevant blog post on andrewmeijer.substack.com.
These rankings are for Summer 2026, so all tournaments that took place since August 1, 2026 do not affect the rankings.
See data/2026/2026ranking.md for the full list of rankings. 
Inactive players are unranked. Players with zero wins are unranked. As of Summer 2026, there are 195 ranked players.
Ranking is subject to change as new features and upgrades are added to the ranking algorithm.

## Top 100 Rankings
|Rank|Rating|Name|ID|Wins|Losses|Previous Rank|Previous Rating|Latest Tournament|
|---|---|---|---|---|---|---|---|---|
|1|1771|Jason Ho-Shue|ON10935|11|0|5|1559|2026-04-03|
|2|1613|Anish Jojula|BC18940|48|9|4|1567|2026-04-03|
|3|1586|Jadon Tsang|BC7711|11|2|3|1586|2025-11-14|
|4|1578|Saurabh Pandiar|BC17070|93|14|1|1619|2026-04-03|
|5|1532|Imran Wadia|AB07299|9|3|17|1354|2026-04-03|
|6|1521|Ethan Ao|U1020508|7|1|6|1521|2025-12-26|
|7|1520|Ricky Lo|X980302|10|2|NR|1413|2026-06-20|
|8|1508|Antonio Li|BC7414|15|3|2|1587|2026-04-03|
|9|1497|Lyem Fedoretz|BC13763|56|13|8|1482|2026-06-20|
|10|1487|Digby Johannson-Miller|BC15083|15|6|14|1393|2026-01-23|
|11|1472|Nik Cruz|BC3960|24|5|9|1472|2025-11-14|
|12|1434|Kevin Luo|BC8266|32|11|11|1431|2026-04-03|
|13|1414|Aadharsh Hariharan|BC19780|14|6|58|1159|2026-05-29|
|14|1400|Wenjun Ouyang|BC8870|8|4|18|1352|2026-04-03|
|15|1394|Roger Quach|BC17133|32|13|13|1394|2025-11-14|
|16|1389|Raunak Sandhu|AB20272|8|4|15|1389|2025-08-02|
|17|1384|Yu-Yuan Chang|U20020423|11|4|16|1384|2025-06-21|
|18|1364|Lap Hang Hugo Pong|BC20238|7|2|12|1429|2026-04-03|
|19|1347|Lai Yin Chung|BC17060|11|6|21|1324|2026-04-03|
|20|1340|Pratham Sangwan|X24191232|4|0|19|1340|2025-11-29|
|21|1335|David Yang|BC9870|21|7|28|1289|2026-06-20|
|22|1324|Stephen Smith|AB23228SS|4|0|NR|1000|2026-03-20|
|23|1317|Fengjie Hu|BC16226|12|6|22|1317|2025-11-14|
|24|1313|Alex Anlai Song|X1019779|7|4|23|1313|2025-12-26|
|25|1298|Nguyen Phan|BC19242|7|2|26|1298|2025-11-21|
|26|1296|Ryan Liu|BC10841|29|16|20|1337|2026-06-20|
|27|1295|Jaden Thom|BC15336|33|16|24|1311|2026-05-29|
|28|1290|Connor Louie|BC10576|41|25|32|1273|2026-04-10|
|29|1284|Felix Zhen|BC15340|13|8|95|1045|2026-06-20|
|30|1281|Alexis Duval|BC6020|12|3|31|1281|2025-11-14|
|31|1279|Keyu Zhou|ON34750|4|3|99|1039|2026-04-03|
|32|1277|Troy Morgan|BC16699|8|4|105|1025|2026-01-23|
|33|1276|Harry Ng|BC15958|5|3|67|1124|2026-06-20|
|34|1273|Eden Dewei Liang|BC14809|7|5|33|1273|2025-08-02|
|35|1257|Nicholas Poon|BC14114|31|19|38|1256|2026-06-20|
|36|1256|Neil Ward|BC0435|13|4|39|1256|2025-11-21|
|37|1254|Daniel-Kyle Tan|BC16232|3|2|78|1080|2026-06-20|
|38|1251|David Crawford|BC4189|8|3|NR|1164|2026-03-20|
|39|1246|Tang Cheuk Man Edmond|XX24685822|2|1|NR|1000|2026-04-03|
|40|1242|Sarabpreet Sodhi|BC17850|8|6|42|1242|2025-11-29|
|41|1240|Joseph Lu|ON14211|3|1|43|1240|2025-11-14|
|42|1239|Victor Ho|MB09472|22|15|27|1293|2026-04-10|
|43|1236|Brendan KC Wong|BC14055|12|9|45|1207|2026-06-20|
|44|1229|Shingchun (Kevin) Wu|BC14906|21|15|35|1264|2026-04-10|
|45|1216|Uday Bharti|BC15951|22|15|41|1244|2026-04-03|
|46|1216|Jackson Lachance|AB10071|3|3|NR|1013|2026-04-03|
|47|1204|Kwun Ho So|BC12748|30|17|46|1204|2025-11-14|
|48|1204|Hector Devesa|BC13264|12|7|111|1010|2026-03-20|
|49|1200|Arseny Shestakov|BC17183|9|10|113|1010|2026-06-20|
|50|1199|Abdelrahman Abdelhakim|BC20972|3|2|NR|1000|2026-04-03|
|51|1193|Ratnesh Ippili|BC17071|26|20|59|1153|2026-04-10|
|52|1192|Angus Li|BC3939|9|4|47|1192|2025-11-14|
|53|1185|Shourya Joshi|BC17705|5|4|50|1185|2025-06-21|
|54|1175|Simar Singh|BC18188|23|14|62|1142|2026-04-03|
|55|1168|Colt Love|BC12636|27|23|60|1151|2026-05-29|
|56|1165|Peter Wong|BC7367|3|2|NR|1048|2026-06-20|
|57|1154|Jalil Waiz|BC7562|29|27|54|1170|2026-04-10|
|58|1145|Tony Dawkins|BC21016|4|2|101|1038|2026-01-23|
|59|1141|Colin Wang|BC12492|10|6|63|1141|2025-11-14|
|60|1140|Ryder Persson|AB21652|5|4|175|908|2026-01-09|
|61|1135|Aaron Lin|BC12213|5|3|64|1135|2025-11-14|
|62|1132|Hailegebriel Kebede|BC12752|15|10|55|1167|2026-05-29|
|63|1130|Evan Zhang|BC12220|3|2|65|1130|2025-08-02|
|64|1127|Jason Carlson|X22114996|4|2|66|1127|2025-11-21|
|65|1123|Robert Foster|BC6881|10|5|68|1123|2025-10-03|
|66|1120|Yun Chi Lo|X22575070|3|2|44|1209|2026-04-03|
|67|1113|Max Smith|AB22287|3|1|NR|1000|2026-03-20|
|68|1111|Hardeep Singh|BC13447|2|2|69|1111|2025-11-14|
|69|1108|Andrew Meijer|BC6030|19|26|61|1148|2026-05-29|
|70|1105|David D Dryden|BC1641|2|1|NR|1000|2026-06-20|
|71|1102|Tymmond Thai|BC12178|3|2|NR|1061|2026-06-20|
|72|1099|Jack Saunders|AB10192|11|9|72|1099|2025-11-21|
|73|1089|Brandon Myrbo|BC16273|6|12|195|821|2026-05-29|
|74|1086|Victor Chang|BC16223|14|15|49|1186|2026-05-29|
|75|1082|Andrew Gu|MB36006|4|4|77|1082|2025-11-29|
|76|1081|Hendra Triwardani|AB25184|1|1|NR|1000|2026-04-03|
|77|1074|Nathan Quach|AB22070|2|3|NR|1097|2026-04-03|
|78|1074|Mark Kitts|BC14477|2|1|80|1074|2025-11-21|
|79|1070|Aakar Chatha|BC17063|19|23|81|1073|2026-04-03|
|80|1069|Zhenghao (Hao) Cui|BC13992|2|1|83|1069|2025-08-02|
|81|1067|Nathaniel Volfbeyn|U1022176|1|1|84|1067|2025-12-26|
|82|1066|Peter Tran|BC5824|6|6|48|1188|2026-04-10|
|83|1064|Jack Jiang|BC20429|2|1|NR|1000|2026-04-10|
|84|1062|Baolin Zhao|BC12035|2|2|53|1171|2026-04-03|
|85|1061|Van Long Nguyen|BC16173|16|19|87|1061|2025-11-14|
|86|1057|Ayden Travis Lee|BC16117|8|4|NR|1116|2026-03-20|
|87|1053|Kai Yang|BC12746|2|1|91|1053|2025-06-21|
|88|1051|Sunil Wadhwa|BC18927|2|2|92|1051|2025-06-21|
|89|1051|Hayden Ostrom|BC8161|3|2|93|1051|2025-11-21|
|90|1051|Tyler Kunz|BC4275|3|2|NR|1000|2026-03-20|
|91|1050|Andrew Li|BC3800|2|2|NR|976|2026-04-03|
|92|1047|Luke Peter Evans|X23347624|1|1|94|1047|2025-08-02|
|93|1043|Johnathan Chi|BC14691|1|2|96|1043|2025-12-26|
|94|1041|Jason Chiu|AB22318|3|4|70|1108|2026-04-03|
|95|1041|Cory Kunz|BC3915|2|1|NR|1000|2026-03-20|
|96|1040|Nicholas Volfbeyn|X1022178|4|4|98|1040|2025-12-26|
|97|1039|Allen George|U47084|1|1|100|1039|2025-12-26|
|98|1035|Krishan Kumar|X24248443|1|1|103|1035|2025-11-29|
|99|1033|Stephen Atherton|BC0834|2|2|NR|1019|2026-03-20|
|100|1029|Luke Lee|BC8269|7|11|115|1005|2026-04-13|

### Tournaments
|Start Date|Name|Champion|
|---|---|---|
|Mar 11, 2022|2022 Campbell River|Manmeet Singh|
|May 6, 2022|2022 Victoria Closed|Joshua R Yan|
|May 27, 2022|2022 Provincial Championships|Jackson Yang|
|Aug 5, 2022|2022 New Era Open|Lyem Fedoretz|
|Oct 8, 2022|2022 Nanaimo Open|Nik Cruz|
|Oct 8, 2022|2022 C1 Thanksgiving Tournament|Jackson Yang|
|Nov 19, 2022|2022 Island Open|Saurabh Pandiar|
|Jan 1, 2023|2023 New Year's Tournament|Lyem Fedoretz|
|Jan 6, 2023|2022-2023 BC Senior Elite|Joshua Nguyen|
|Jan 13, 2023|2023 Campbell River|Saurabh Pandiar|
|Jan 15, 2023|2023 Kelowna Adult Open|Matt Downton|
|Feb 25, 2023|2023 Wing's-GHS Tournament|Peike Xu|
|Mar 31, 2023|2023 Jack Underhill|Lyem Fedoretz|
|Apr 7, 2023|2023 Easter Open|Antonio Li|
|Apr 22, 2023|2023 Provincials|Joshua Liu|
|Jun 2, 2023|2023 Victoria Closed|Jaden Thom|
|Jun 23, 2023|2023 White Rock Tournament|Ryan Liu|
|Sep 22, 2023|2023 Nanaimo Open|Roger Quach|
|Sep 23, 2023|2023 POCOmon GO Open|Gurbaksh Saini|
|Oct 7, 2023|2023 C1 Thanksgiving Tournament|Saurabh Pandiar|
|Nov 17, 2023|2023-2024 BC Senior Elite|Joshua Nguyen|
|Nov 24, 2023|2023 Island Open|Connor Louie|
|Dec 2, 2023|2023 Kelowna Open|Harrison Hsu|
|Jan 1, 2024|2024 New Year's Tournament|Saurabh Pandiar|
|Jan 12, 2024|2024 Campbell River|Saurabh Pandiar|
|Jan 31, 2024|2024 National Championships|Victor Lai|
|Feb 17, 2024|2024 Jack Underhill|Saurabh Pandiar|
|Mar 29, 2024|2024 Easter Open|Antonio Li|
|Apr 19, 2024|2024 Sunshine Tournament|Jaden Thom|
|Apr 26, 2024|2024 Provincials|Saurabh Pandiar|
|May 24, 2024|2024 Victoria Closed|Roger Quach|
|Jun 22, 2024|2024 White Rock Tournament|Saurabh Pandiar|
|Sep 27, 2024|2024 Nanaimo Open|Anish Jojula|
|Oct 12, 2024|2024 C1 Thanksgiving Tournament|Yu-Yuan Chang|
|Nov 15, 2024|2024 Island Open|Roger Quach|
|Nov 29, 2024|2024 Wing's Open|Saurabh Pandiar|
|Dec 12, 2024|2024 Shuttlesport Open|Anish Jojula|
|Dec 27, 2024|2024 Boxing Week Tournament|Kevin Luo|
|Jan 3, 2025|2025 Kelowna Open|Harrison Liu|
|Jan 10, 2025|2025 Campbell River Open|David Yang|
|Feb 7, 2025|2025 Jack Underhill|Anish Jojula|
|Apr 4, 2025|2025 Provincial Championships|Connor Louie|
|Apr 18, 2025|2025 Easter Open|Jason Ho-Shue|
|Apr 21, 2025|2025 VRC Club Championships|Nicholas Poon|
|Jun 6, 2025|2025 Victoria Closed|Nik Cruz|
|Jun 21, 2025|2025 White Rock Tournament|Lyem Fedoretz|
|Aug 2, 2025|2025 Smash Champs Grand Opening|Anish Jojula|
|Oct 3, 2025|2025 Nanaimo Open|Nik Cruz|
|Oct 11, 2025|2025 Thanksgiving Tournament|Saurabh Pandiar|
|Nov 14, 2025|2025 Island Open|Jadon Tsang|
|Nov 21, 2025|2025 Kelowna Fall Open|Digby Johannson-Miller|
|Nov 29, 2025|2025 Surrey Open|Pratham Sangwan|
|Dec 26, 2025|2025 Boxing Week Tournament|Ethan Ao|
|Jan 9, 2026|2026 Cindy Simpson Memorial|David Yang|
|Jan 23, 2026|2026 Kelowna Winter Open|Digby Johannson-Miller|
|Feb 6, 2026|2026 Jack Underhill|Anish Jojula|
|Mar 20, 2026|2026 Kamloops Open in Kelowna|Stephen Smith|
|Apr 3, 2026|2026 Easter Open|Jason Ho-Shue|
|Apr 10, 2026|2026 Provincial Championships|Connor Louie|
|Apr 13, 2026|2026 VRC Club Championships|Nicholas Poon|
|May 29, 2026|2026 Victoria Closed|Aadharsh Hariharan|
|Jun 20, 2026|2026 Canada Winter Games Trial|Lyem Fedoretz|
|Jun 20, 2026|2026 White Rock Tournament|Ricky Lo|

### Author
Andrew Meijer