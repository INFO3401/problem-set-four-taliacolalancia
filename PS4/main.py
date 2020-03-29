from utils import *
from pollingData import *
import pandas as pd
import matplotlib.pyplot as plt
import math
import numpy as np

#df = loadAndCleanData("2020pres.csv")
df = loadAndCleanData("2020PostSuperTues.csv")

#print(df)

#6
normalizeData(df)

#print(plotCandidate)

#7
for candidate in df.columns:
    if candidate not in ["Poll", "Date", "Sample", "Spread", "Undecided"]:
        plotCandidate(candidate, df)

#9
myCandidate = []
for candidate in df.columns:
    if candidate not in ["Poll", "Date", "Sample", "Spread", "Undecided"]:
        myCandidate.append(candidate)
        print(candidate.statsPerCandidate(candidate, df))
#print(statsPerCandidate)


#11
df = cleanSample(df)
print(cleanSample)

#14
weightedStatsPerCandidate("Biden", df)
weightedStatsPerCandidate("Warren", df)
weightedStatsPerCandidate("Sanders", df)
weightedStatsPerCandidate("Biden", df)

#16
repeatList = []

for candidate1 in myCandidate:
    for candidate2 in myCandidate:
        if candidate1 != candidate2:
            if [candidate1, candidate2] not in repeatList and [canidate1, candidate2] not in repeatList:
                print(candidate1 + "vs " + candidate2 + ": " + computerCorrelation(candidate1, candidate2, df))
                repeatList.append([candidate1, candidate2])

#18
superTuesday(df, myCandidate)
print("Biden Mean: " + df["BidenST"].mean())
print("Sanders Mean: " + df["SandersST"].mean())
print("Biden Weighted Mean: " + weightedStatsPerCandidate("BidenST", df))
print("Sanders Weighted Mean: " + weightedStatsPerCandidate("SandersST", df))

#19
getConfidenceInterval(df["BidenST"])
getConfidenceInterval(df["SandersST"])

#20
print("Numbers: " + runTTest(df["Biden"], df["Sanders"]))
print("Aggregated Numbers: " + runTTest(df["BidenST"], df["SandersST"]))
