## ReadMe
### Purpose
The purpose of this project is to maintain a Provincial rating system for Men's Singles badminton players based on the official ranking system for British Columbia, using the tournaments that award points towards the official rankings.

### Introduction
For more information on how the ELO rating system works, see the initial prototype: [github.com/a-meijer/showcase](https://github.com/a-meijer/showcase/tree/master/ELO)

For more information on the ongoing development process, see devlog.txt.

Match data is available on Google Drive:
https://drive.google.com/drive/folders/1GX5JPSUZaMUrkilviBPgyZCzfP7bpef-?usp=sharing

The match data for each tournament is in CSV files in the tournaments directory.

### 2026 Ranking


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
To use the rating algorithm, run the program: main.py. By default, the program selects "Ratings.csv" as the input data file, but you may opt for a different filename.
You can also change the output filename; just be careful not to overwrite anything.
You will need to enter the filename for the tournament match data you are processing. multiTourneyProcessing.py is used to hard-code filenames and process multiple tournaments at once.

### Tournaments
    Mar 11, 2022:   Campbell River Badminton Championship
    May  6, 2022:   Victoria Closed Club Championship
    May 27, 2022:   Provincial Championship
    Aug  5, 2022:   New Era Open Blue&Yellow
    Oct  8, 2022:   Nanaimo Open
    Oct  8, 2022:   C1 Thanksgiving Tournament
    Nov 19, 2022:   Island Open

    Jan  1, 2023:   C1 New Year's Tournament
    Jan  6, 2023:   BC Senior Elite
    Jan 13, 2023:   Campbell River Badminton Championship
    Jan 15, 2023:   Kelowna Adult Open
    Feb 25, 2023:   Wing's-GHS Tournament
    Mar 31, 2023:   Jack Underhill Open A&B
    Apr  7, 2023:   Easter Open 15+
    Apr 22, 2023:   Provincial Championship
    May 26, 2023:   12.2 O-Go-PoCo Open
    Jun  2, 2023:   Victoria Closed Club Championship
    Jun 23, 2023:   White Rock Tournament
    Sep 22, 2023:   Nanaimo Open
    Sep 23, 2023:   12.2 POCOmon GO Open
    Oct  7, 2023:   C1 Thanksgiving Tournament
    Nov 17, 2023:   BC Senior Elite
    Nov 24, 2023:   Island Open
    Dec  2, 2023:   Kelowna Open

    Jan  1, 2024:   New Year's Tournament
    Jan 12, 2024:   Campbell River
    Jan 31, 2024:   Canadian Senior Championships
    Feb 17, 2024:   Jack Underhill
    Mar 29, 2024:   Easter Open
    Apr 19, 2024:   Sunshine Tournament - https://badmintoncanada.tournamentsoftware.com/tournament/BAB8ED58-E9F6-4653-A872-7B8FFDCFA771
    Apr 26, 2024:   Provincial Championship - done
    May 24, 2024:   Victoria Club - https://www.tournamentsoftware.com/tournament/53D4A72D-8101-457A-B1A2-EFF35297C7D3
    Jun 22, 2024:   White Rock Tournament - https://www.tournamentsoftware.com/tournament/1CE02EB5-8EB6-4FF2-87EA-2C329C2E052B
    Sep 27, 2024:   Nanaimo Open - https://badmintoncanada.tournamentsoftware.com/tournament/4D9D9ABC-0EEA-43E2-AD6B-E60009A500FB
    Oct 12, 2024:   Thanksgiving Tournament - https://www.tournamentsoftware.com/tournament/4091C614-9206-4F14-B3FC-C4EFB5FC3D08
    Nov 15, 2024:   Vancouver Island Open - https://www.tournamentsoftware.com/tournament/AF23D1A8-56E6-4C34-B592-F5A68DB9D712
    Nov 29, 2024:   Wing's Open - done
    Dec 12, 2024:   Shuttlesport Open Series #2 - done
    Dec 27, 2024:   Boxing Week Tournament - https://www.tournamentsoftware.com/tournament/D12FB96F-D490-4422-B369-0985D12C504E

    Jan  3, 2025:   Kelowna Open - https://www.tournamentsoftware.com/tournament/D8141B44-BE16-4FD5-9D87-0AA07DF1EF7D
    Jan 10, 2025:   Campbell River - https://badmintoncanada.tournamentsoftware.com/tournament/6B4EE983-4635-4828-83EB-3117140640DA
    Feb  7, 2025:   Jack Underhill - done
    Apr  4, 2025:   Provincial Championship - done
    Apr 18, 2025:   Easter Open - https://www.tournamentsoftware.com/tournament/1A4B87CA-8734-4781-9793-1AC0892DCBA1
    Apr 21, 2025:   VRC Club - https://www.tournamentsoftware.com/tournament/326D1266-AAAD-461C-9366-8F2CB38FAFC8
    Jun  6, 2025:   Victoria Club - https://badmintoncanada.tournamentsoftware.com/tournament/B0D1C7C7-20BF-4DE3-902B-FBB127970033
    Jun 21, 2025:   White Rock Tournament - https://www.tournamentsoftware.com/tournament/7868E502-491B-4CDE-A7C8-E588CF7438AF
    Aug  2, 2025:   Smash Champs Grand Opening - https://www.tournamentsoftware.com/tournament/FC3D01C9-BD3D-4675-A62B-0264BBF039D7
    Oct  3, 2025:   Nanaimo Open - https://badmintoncanada.tournamentsoftware.com/tournament/B38511A2-46FE-4297-A4AA-EF18ADD5504F
    Oct 11, 2025:   Thanksgiving Tournament - https://www.tournamentsoftware.com/tournament/D4D45938-FFD1-4E55-806E-FA09FE9F7E8B
    Nov 14, 2025:   Vancouver Island Open - https://badmintoncanada.tournamentsoftware.com/tournament/C1694DAE-19AB-4053-BD85-267029754E39
    Nov 21, 2025:   Kelowna Fall Open - https://www.tournamentsoftware.com/tournament/F9BF7D30-45E8-4099-8FCC-45F22D46CD8C
    Nov 29, 2025:   Surrey Open - https://www.tournamentsoftware.com/tournament/553C4ADE-D607-4ACF-8DE8-AA9107E10C11
    Dec 26, 2025:   Boxing Week Tournament - https://www.tournamentsoftware.com/tournament/7E5F1132-A24D-495F-AE0E-1531F59CC426

    Jan  9, 2026:   Cindy Simpson Memorial - https://badmintoncanada.tournamentsoftware.com/tournament/8D69A67F-8CCA-490C-8AC7-46CBB195F1CC
    Jan 23, 2026:   Kelowna Winter Open - https://www.tournamentsoftware.com/tournament/D16CC9D8-94E4-495F-B270-0B5F5CF1A13F
    Feb  6, 2026:   Jack Underhill - https://badmintoncanada.tournamentsoftware.com/tournament/ADA2BB34-1F57-40A4-9743-81F79D81D658
    Mar 20, 2026:   Kamloops Open in Kelowna - https://www.tournamentsoftware.com/tournament/89F64C51-9E00-4411-B847-5529F3B1CF06
    Apr  3, 2026:   Easter Open - https://www.tournamentsoftware.com/tournament/696C1080-72AE-44DA-8CB9-3EC6E10EA0A4
    Apr 10, 2026:   Provincial Championship - https://badmintoncanada.tournamentsoftware.com/tournament/25725E4A-CF6A-4B3F-A7A4-918C1A01BD79
    Apr 13, 2026:   VRC Club - https://www.tournamentsoftware.com/tournament/DB920DB7-2D46-4F3E-85BD-C8C408C45752
    May 29, 2026:   Victoria Club - https://www.tournamentsoftware.com/tournament/64CF707D-3318-4918-926C-F2172C716E48

    Jun 20, 2026:   White Rock Tournament - https://www.tournamentsoftware.com/sport/event.aspx?id=C0E36D5D-C989-49AD-9FDB-197222EB17CE&event=20

### Previous Versions
After the prototype versions, I made the first full version of my rankings project in 2025.
For that version, I only used tournaments from 2022 that affected Provincial Rankings.

### 2025 Rankings
|Rank|Rating|Name                           |ID     |Wins|Losses|
|----|------|-------------------------------|-------|----|------|
|1   |1530  |ANISH Chandra Jojula           |BC18940|14  |1     |
|2   |1518  |Saurabh Pandiar                |BC17070|23  |3     |
|3   |1406  |Lyem Fedoretz                  |BC13763|9   |1     |
|4   |1319  |Joshua Liu                     |BC1815 |6   |1     |
|5   |1306  |Victor Ho                      |MB09472|12  |5     |
|6   |1303  |Ziyi Yang Jackson              |BC10895|4   |0     |
|7   |1274  |Connor Nicholas Louie          |BC10576|10  |6     |
|8   |1247  |Peike Xu                       |BC15886|4   |1     |
|8   |1247  |Rickey Ruixi Zhang             |BC14918|7   |4     |
|10  |1240  |Gurbaksh Singh Saini           |ON41508|6   |2     |
|11  |1211  |Kevin Luo                      |BC8266 |5   |2     |
|11  |1211  |Ryan Liu                       |BC10841|4   |2     |
|13  |1209  |Jack Chen                      |BC10265|7   |6     |
|14  |1193  |Jadon Tsang                    |BC7711 |3   |1     |
|15  |1171  |Raunak Sandhu                  |AB20272|4   |1     |
|16  |1163  |Uday pratap Bharti             |BC15951|9   |5     |
|17  |1151  |Jalil Waiz                     |BC7562 |10  |8     |
|18  |1150  |Jasper Kong                    |BC16320|4   |2     |
|19  |1122  |Joshua R Yan                   |BC9134 |2   |1     |
|20  |1119  |simar singh                    |BC18188|9   |5     |
|21  |1115  |Ratnesh Rao Ippili             |BC17071|7   |6     |
|22  |1095  |Tai-Yu (Harrison) LIU          |BC17354|2   |1     |
|23  |1090  |Shingchun (Kevin) Wu           |BC14906|3   |2     |
|24  |1081  |Connor O'Reilly                |BC16854|2   |1     |
|25  |1076  |YiYang Jiang                   |ON13537|2   |1     |
|26  |1074  |Kwun Ho So                     |BC12748|3   |2     |
|27  |1070  |Nicholas Poon                  |BC14114|4   |4     |
|28  |1066  |Sarabpreet Singh Sodhi         |BC17850|4   |3     |
|29  |1052  |Allan Crawford                 |BC15210|1   |1     |
|29  |1052  |Daniel-Kyle Tan                |BC16232|1   |1     |
|31  |1050  |Roger Quach                    |BC17133|2   |2     |
|32  |1048  |Brian McBay                    |BC14400|1   |1     |
|33  |1043  |Simon Wu                       |BC17274|2   |2     |
|34  |1039  |Robert Zhongjia Shi            |BC13617|6   |5     |
|35  |1034  |William Ka wang Ma             |BC15972|1   |1     |
|36  |1026  |Paul Cho                       |BC3748 |2   |2     |
|37  |1025  |Manmeet Singh                  |BC16926|1   |1     |
|37  |1025  |Mahdi Ahmadi                   |BC15814|1   |1     |
|37  |1025  |Trevor Tak Sing Chun           |BC15986|1   |1     |
|37  |1025  |ZeLin Shan                     |BC16166|1   |1     |
|41  |1021  |Kelsey Liang                   |BC13170|1   |1     |
|42  |1013  |Van Long Nguyen                |BC16173|2   |2     |
|43  |1010  |Ayush Ayush                    |BC18578|1   |2     |
|44  |1009  |Ethan Yen                      |BC14739|1   |1     |
|45  |1007  |Franklin Chen                  |BC17865|2   |2     |
|46  |1003  |Michael Poon                   |BC9740 |1   |1     |
|46  |1003  |Luke Lee                       |BC8269 |1   |1     |
|46  |1003  |Will Bui                       |BC13605|1   |1     |
|46  |1003  |Colin Wang                     |BC12492|1   |1     |
|46  |1003  |Maurice Li                     |BC18471|1   |1     |
|51  |1000  |Angus Li                       |BC3939 |1   |1     |
|52  |993   |Stephen Dee                    |BC0389 |2   |2     |
|52  |993   |Jaden Thom                     |BC15336|1   |3     |
|54  |992   |Aakar Chatha                   |BC17063|5   |6     |
|54  |992   |Jason Too                      |BC19055|0   |1     |
|54  |992   |Colt Love                      |BC12636|2   |4     |
|57  |986   |Daniel Huang                   |BC14954|1   |1     |
|58  |976   |Barry Xie                      |BC17273|1   |2     |
|59  |974   |Rinesh Dilshan Hetti Arachchige|BC20039|1   |1     |
|60  |968   |Brandon Robert Myrbo           |BC16273|1   |2     |
|61  |967   |Sahil Rajesh Aggarwal          |BC16091|1   |2     |
|62  |966   |Ryan Chee Khun Chung           |BC14991|0   |1     |
|63  |948   |THOMAS GEORGE                  |BC19905|1   |3     |
|64  |947   |Eddie Huang                    |BC17311|0   |1     |
|65  |946   |Andrew Meijer                  |BC6030 |2   |4     |
|66  |940   |Renjie Xiong                   |BC18391|1   |2     |
|67  |935   |Loki Fung                      |BC17229|2   |3     |
|67  |935   |Roy Hung                       |BC11052|1   |3     |
|69  |933   |John Ou                        |BC16127|1   |2     |
|70  |932   |Nghia Tuan Nguyen              |BC20030|0   |1     |
|70  |932   |Aadharsh Hariharan             |BC19780|0   |1     |
|72  |929   |Laurence Kao                   |BC3829 |0   |1     |
|73  |928   |Nicholas Lee                   |SK01305|0   |1     |
|73  |928   |Raymond Wu                     |BC16114|0   |1     |
|73  |928   |Robert Stephen Foster          |BC6881 |0   |1     |
|73  |928   |Bangjian (James) Geng          |BC13109|0   |1     |
|73  |928   |Oliver Long                    |BC13904|0   |1     |
|78  |927   |Josemaria (JM) Teleg           |BC16122|2   |4     |
|79  |926   |Dwayne da Silva                |BC18335|0   |1     |
|80  |925   |Brian Liu                      |BC18365|0   |1     |
|81  |921   |Peter Tran                     |BC5824 |0   |1     |
|82  |919   |Ev Haus                        |BC19123|0   |2     |
|82  |919   |Andy Le                        |BC17175|1   |3     |
|84  |908   |Jithin Prakash                 |BC15890|1   |2     |
|85  |907   |Zhengheng Bao                  |BC18926|0   |1     |
|86  |900   |Fong-Ming Chow                 |BC16012|0   |1     |
|86  |900   |Adrian KH Wong                 |BC12183|0   |1     |
|86  |900   |Nelson Oi Sang Chan            |BC16318|0   |1     |
|86  |900   |Lai Yin Chung                  |BC17060|0   |1     |
|86  |900   |Anjie Wang                     |BC17891|0   |1     |
|86  |900   |Dan MacDonald                  |BC0474 |0   |1     |
|86  |900   |Frank Nguyen                   |BC17406|0   |1     |
|86  |900   |Volodymyr Zubariev             |BC17770|0   |1     |
|86  |900   |Rahi Kumar                     |BC17795|0   |1     |
|86  |900   |Hayden Lam                     |BC16882|0   |1     |
|86  |900   |Zhijing Liu                    |BC14515|0   |1     |
|86  |900   |John McWalter Keith            |BC17576|0   |1     |
|86  |900   |Markus Weilmeier               |BC10033|0   |1     |
|86  |900   |Leo Shen                       |BC15094|0   |1     |
|86  |900   |Nusorn Krachangtoy             |BC8364 |0   |1     |
|86  |900   |David Yang                     |BC9870 |0   |1     |
|86  |900   |Jack Saunders                  |AB10192|0   |1     |
|86  |900   |Eugene Kwok                    |BC17953|0   |1     |
|86  |900   |Shukang Wang                   |BC16808|0   |1     |
|86  |900   |Hossein Ahmadi                 |BC17717|0   |1     |
|86  |900   |Yichen Li                      |BC18977|0   |1     |
|86  |900   |Marcus James Tseng             |BC16125|0   |1     |
|86  |900   |Ayden Travis Lee               |BC16117|0   |1     |
|86  |900   |Yancong Li                     |BC19032|0   |1     |
|86  |900   |Justin Lam                     |BC14897|0   |1     |
|86  |900   |Keshav Jheeta                  |BC17169|0   |1     |
|86  |900   |Digby Johannson-Miller         |BC15083|0   |1     |
|113 |898   |Benson Wong                    |BC16112|0   |1     |
|114 |877   |Yigit Kirsan                   |BC19455|0   |1     |
|115 |871   |Marcus Chan                    |BC16107|0   |1     |
|115 |871   |Quinn Lawler                   |AB22569|0   |1     |
|115 |871   |Chi-Kin Chan                   |BC15989|0   |1     |
|115 |871   |Dayton Se                      |BC13042|0   |1     |
|119 |870   |Soham Ghugal                   |BC19017|0   |3     |
|120 |867   |Shen Wei Lai                   |BC8302 |0   |2     |
|121 |865   |Brendon Kwan                   |BC9351 |0   |2     |
|122 |863   |Clayton A Miller               |BC4316 |0   |1     |
|123 |857   |Arseny Shestakov               |BC17183|0   |2     |
|124 |855   |Justin Phuong                  |BC11051|0   |2     |
|125 |850   |Luca Ferretti                  |ON35979|0   |2     |
|126 |847   |Gilbert Limarta                |BC19167|0   |2     |
|127 |838   |Rohail Mir                     |BC19034|0   |3     |
|128 |825   |Samuel Ha                      |BC17845|0   |2     |
|129 |824   |Jesse Guo                      |BC19644|0   |3     |
|130 |823   |Gurnishan Singh Sidhu          |BC19528|0   |3     |
|131 |776   |Isaac Fu                       |BC18369|0   |3     |

### Tournaments Affecting 2025 Rankings
     
    
### Author
Andrew Meijer