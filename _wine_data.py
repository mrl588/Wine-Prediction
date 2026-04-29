from ucimlrepo import fetch_ucirepo 
  
# fetch dataset 
wine_quality = fetch_ucirepo(id=186) 
  
# data (as pandas dataframes) 
X = wine_quality.data.features 
y = wine_quality.data.targets 

df = X.join(y)
df.columns = df.columns.str.strip().str.replace(" ", "_")

if "Id" in df.columns:
    df = df.drop(columns=["Id"])

X = df.drop(columns=["quality"])
y = df[["quality"]]
 
# metadata 
print(wine_quality.metadata) 
  
# variable information 
print(wine_quality.variables) 
