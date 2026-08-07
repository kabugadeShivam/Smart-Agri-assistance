from utils.scheme_matcher import match_schemes

results = match_schemes(
    state="Maharashtra",
    crop="Sugarcane",
    land_area=5,
    age=30,
    gender="All"
)

print("Matched Schemes:", len(results))

for scheme in results[:5]:
    print("-" * 50)
    print("Scheme :", scheme["Scheme_Name"])
    print("Benefit:", scheme["Benefit"])
    print("Subsidy:", scheme["Subsidy"])