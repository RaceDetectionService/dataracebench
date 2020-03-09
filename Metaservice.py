import json
import re
import sys

file = open(sys.argv[1],"r")
Lines = file.readlines()
content = [line.strip() for line in Lines]
ArcherVote = 0
ArcherVoteNeg = 0
ArcherVotePos = 0
Voteflag = 0
for i in range(len(content)):
    if content[i] == {}:
        ArcherVoteNeg += 1
    else:
        ArcherVotePos += 1

if ArcherVoteNeg > ArcherVotePos:
    ArcherVote == 0
else:
    ArcherVote == 1
    Voteflag += 1

file = open(sys.argv[2],"r")
Lines = file.readlines()
content = [line.strip() for line in Lines]
InspectorVote = 0
InspectorVoteNeg = 0
InspectorVotePos = 0
for i in range(len(content)):
    if content[i] == {}:
        InspectorVoteNeg += 1
    else:
        InspectorVotePos += 1

if InspectorVoteNeg > InspectorVotePos:
    InspectorVote == 0
else:
    InspectorVote == 1
    Voteflag += 1
    
file = open(sys.argv[3],"r")
Lines = file.readlines()
content = [line.strip() for line in Lines]
RompVote = 0
RompVoteNeg = 0
RompVotePos = 0
for i in range(len(content)):
    if content[i] == {}:
        RompVoteNeg += 1
    else:
        RompVotePos += 1
        
if RompVoteNeg > RompVoteNeg:
    RompVote == 0
else:
    RompVote == 1
    Voteflag += 1

file = open(sys.argv[4],"r")
Lines = file.readlines()
content = [line.strip() for line in Lines]
TsanVote = 0
TsanVoteNeg = 0
TsanVotePos = 0
for i in range(len(content)):
    if content[i] == {}:
        TsanVoteNeg += 1
    else:
        TsanVotePos += 1

if TsanVoteNeg > TsanVotePos:
    TsanVote == 0
else:
    TsanVote == 1
    Voteflag += 1
    
if Voteflag >= 2:
    print("RDS detected a data race!")

###information need to dispaly
