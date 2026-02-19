# ================================================================
#  Kaggle - Feature Engineering
#  Creating Features
# ================================================================

# ----------------------------------------------------------------
#  Q1 - Mathematical Transforms
# ----------------------------------------------------------------

# YOUR CODE HERE
X_1 = pd.DataFrame()  # dataframe to hold new features

X_1["LivLotRatio"] = df.GrLivArea / df.LotArea
X_1["Spaciousness"] = (df.FirstFlrSF + df.SecondFlrSF) / df.TotRmsAbvGrd
X_1["TotalOutsideSF"] = df.WoodDeckSF + df.OpenPorchSF + df.EnclosedPorch + df.Threeseasonporch + df.ScreenPorch
# Check your answer
q_1.check()


# ----------------------------------------------------------------
#  Q2 - Interaction Features
# ----------------------------------------------------------------

# YOUR CODE HERE
# One-hot encode BldgType. Use `prefix="Bldg"` in `get_dummies`
X_2 = pd.get_dummies(df.BldgType, prefix="Bldg")
X_2 = X_2.mul(df.GrLivArea, axis=0)

# Check your answer
q_2.check()


# ----------------------------------------------------------------
#  Q3 - Count Features
# ----------------------------------------------------------------

X_3 = pd.DataFrame()

X_3["PorchTypes"] = df[[
    "WoodDeckSF",
    "OpenPorchSF",
    "EnclosedPorch",
    "Threeseasonporch",
    "ScreenPorch",
]].gt(0.0).sum(axis=1)

# Check your answer
q_3.check()


# ----------------------------------------------------------------
#  Q4 - Break Down a Categorical Feature
# ----------------------------------------------------------------

X_4 = pd.DataFrame()

X_4["MSClass"] = df.MSSubClass.str.split("_", n=1, expand=True)[0]
# Check your answer
q_4.check()


# ----------------------------------------------------------------
#  Q5 - Use a Grouped Transform
# ----------------------------------------------------------------

X_5 = pd.DataFrame()

X_5["MedNhbdArea"] = df.groupby("Neighborhood")["GrLivArea"].transform("median")
# Check your answer
q_5.check()
