import pandas as pd
df = pd.read_csv("county_facts.csv")
df = df[["area_name", "state_abbreviation", "LFE305213", "HSG445213", "INC110213", "POP010210", "EDU685213"]]
df.columns = ["county", "state", "com", "home", "inc", "pop", "edu"]

df = df.dropna() # drop null values

print("correlation between happiness and the rate of higher education in counties")
print("============")
#  (income * homeownership) / commute
df["rating"] = df.apply(lambda row: (row["inc"] * row["home"]) / row["com"] , axis=1)

avg = df["rating"].mean()

uh = df[df["rating"] < avg]
vh = df[df["rating"] >= avg]

uhavg = uh["edu"].mean()
vhavg = vh["edu"].mean()

diff = vhavg - uhavg

if diff >= 20:
    print("Happy counties have significantly more college graduates")
elif diff >= 5:
    print("Happy counties have slightly more college graduates")
elif diff <= -5:
    print("Unhappy counties have slightly more college graduates")
elif diff <= -20:
    print("Unhappy counties have significantly more college graduates")
else:
    print("no correlation")


print("Similar Counties")
print("==============")

def sim(a, b):
    return abs((a - b) / b) <= 0.02

for i in range(len(df)):
    county = df.iloc[i]["county"]
    state =  df.iloc[i]["state"]
    # remove this country from df
    ff = df[(df["state"] != state) | (df["county"] != county)]
    filters = ["pop", "edu", "com", "inc", "home"]
    
    for f in filters:
        target = df.iloc[i][f]
        ff = ff[sim(ff[f], target)]
        
    if len(ff) > 0:
        print ("Similar counties to", county, state, ":")
        print(ff)































