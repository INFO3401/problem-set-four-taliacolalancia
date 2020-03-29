import matplotlib.pyplot as plt

#5
def normalizeData(df):
    x = df.copy()
    sumList = []

    for i, row in x.iterrows():
        row.drop(labels = ["Poll", "Date", "Sample", "Spread"], inplace = True)
        print(row)
        sumList.append(100-sum(row))

    x["Undecided"] = sumList

    print(x)

#7
def plotCandidate(candidate, df):
    plt.scatter(y = df[candidate], x = df["Poll"]) #variables no quotes
    plt.title(candidate + "Polling")
    plt.ylim(0) #bottom is 0
    plt.show()

#8
def statsPerCandidate(candidate, df):
    return df[candidate].mean()

#10
def cleanSample(df):
    sampleType = []
    sampleSize = []

    for i in df["Sample"]:
        sampleType.append(i[-2:])
        sampleSize.append(i[-2:])

    df["Sample Type"] = sampleType
    df["Sample Size"] = sampleSize
    return df

#12
def computePollWeight(df, poll):
    x = df["Poll"] == poll
    xSum = sum(x["Sample Size"])
    y = sum(df["Sample Size"])
    return xSum/y

#13
def weightedStatsPerCandidate(candidate, df):
    weightedAverages = []
    for poll in df["Poll"].unique():
        x = sum(df[df["Poll"] == poll][candidate])
        y = computePollWeight(df, poll)
        weightedAverages.append(x*y)
    return sum(weightedAverages)/len(weightedAverages)

#15
def computerCorrelation(candidate1, candidate2, df):
    return df[candidate1].corr(df[candidate2])

#17
def superTuesday(df, candidates):
    BidenST = []
    SandersST = []

    for i, row in df.iterrows():
        BidenCount = row["Biden"]
        SandersCount = row["Sanders"]
        for candidate in candidates:
            if candidate != "Biden" and candidate != "Sanders":
                BidenCorr = computerCorrelation("Biden", candidate, df)
                SandersCorr = computerCorrelation("Sanders", candidate, df)
                if abs(BidenCorr) > abs(SandersCorr):
                    BidenCount += row[candidate]
                else:
                    SandersCount += row[candidate]
        BidenST.append(BidenCount)
        SandersST.append(SandersCount)

    df["BidenST"] = BidenST
    df["SandersST"] = SandersST
