This is a Word Hunt bot that solves any board for you!

Word Hunt is a game on Game Pigeon where players compete to find words in a 4x4 grid of letters.

Words are formed by forming strings of letters, where each subsequent letter is adjacent form the previous.

tiles can not be reused.

To use the program, run main.py and input the 16 characters from left to right, top to bottom.

The program will tell you the list of all possible words that can be made from longest (highest points) to shortest (lowest points).

Here are examples of a Word Hunt Board:

Board 1:

I T T A
H A E O
U S P N
R I W N

Board 2:

F G H O
A D H T
N S M I
A N T M

Here is an example of an actual game:

N Z P R
C S H C
N I I O
O S T T

Input:
nzprcshcniioostt

Output:

['PHOTINOS', 'COITIONS', 'STICHIC', 'CHITINS', 'PHOTINO', 'PHOTICS', 'HOISINS', 'TOISONS', 'COITION', 'NOSTOC', 'CHINOS', 'NOSTOI', 'RHOTIC', 'CHOTTS', 'RHINOS', 'HOISIN', 'STICHS', 'PSIONS', 'SCIONS', 'PHOTIC', 'OTITIC', 'OTITIS', 'CISTIC', 'TOISON', 'CHITIN', 'INSIST', 'SHOTTS', 'SONICS', 'SHINS', 'STOIC', 'TOITS', 'SHISO', 'CHICS', 'CHINS', 'SHOTS', 'PHOTS', 'SNITS', 'COTTS', 'PSION', 'HOIST', 'CHINO', 'RHINO', 'SHOTT', 'STICH', 'SCION', 'SONIC', 'COITS', 'CHOTT', 'CHITS', 'SHITS', 'SHIST', 'TITIS', 'STOIT', 'CIONS', 'HITS', 'SHIN', 'CHIN', 'ONST', 'SICH', 'SNIT', 'IONS', 'COTT', 'TICS', 'CIST', 'CITO', 'SONS', 'HOTS', 'NITS', 'STOT', 'HOIS', 'ICHS', 'PHOT', 'ISIT', 'HIST', 'TOTS', 'CHIS', 'COIT', 'COTS', 'HINS', 'SICS', 'PSIS', 'CITS', 'CION', 'SHOT', 'CHIT', 'SIST', 'TITI', 'HISN', 'SINS', 'OTIC', 'TITS', 'NISH', 'TOIT', 'NISI', 'SHIT', 'PHIS', 'TICH', 'CHIC', 'TINS', 'SITS', 'SHO', 'TIT', 'HOC', 'CIS', 'HOI', 'PHI', 'OCH', 'OIS', 'SIT', 'IOS', 'HIT', 'COT', 'RHO', 'ICH', 'SIS', 'TIC', 'TIN', 'HIN', 'INS', 'SIC', 'CHI', 'NOS', 'ZHO', 'HOT', 'NIS', 'SIN', 'TIS', 'ISH', 'SON', 'TOC', 'OHS', 'ITS', 'HIS', 'ION', 'CIT', 'TOT', 'ONS', 'PHO', 'ISO', 'HIC', 'PSI', 'NIT']


