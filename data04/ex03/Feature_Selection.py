import pandas as pd
from sklearn.preprocessing import StandardScaler
from statsmodels.stats.outliers_influence import variance_inflation_factor

# Multicolinealidad: cuando dos o mas variables independientes son altamente correlacionadas entre si
# VIF: Variance Inflation Factor: sirve para medir cuanta varianza de un coeficiente de regresion se debe a la multicolinealidad
# VIF = 1: no hay multicolinealidad
# 1 < VIF < 5: multicolinealidad moderada
# VIF > 5: multicolinealidad alta
# VIF > 10: multicolinealidad severa
def feature_selection():
    csv_path = "../Train_knight.csv"

    df = pd.read_csv(csv_path)
    df['knight'] = df['knight'].map({'Sith': 1, 'Jedi': 0})

    scaler = StandardScaler()
    data_scaled = scaler.fit_transform(df)
    df_scaled = pd.DataFrame(data_scaled, columns=df.columns)

    def calculate(df_scaled):
        vif_data = pd.DataFrame()
        vif_data["Feature"] = df_scaled.columns
        vif_data["VIF"] = [variance_inflation_factor(df_scaled.values, i) for i in range(df_scaled.shape[1])]
        vif_data["Tolerance"] = 1 / vif_data["VIF"]
        return vif_data

    vif_data = calculate(df_scaled)
    vif_start = vif_data.copy()

    while vif_data['VIF'].max() > 5:
        remove = vif_data.sort_values('VIF', ascending=False).iloc[0]['Feature']
        df_scaled = df_scaled.drop(columns=[remove])
        vif_data = calculate(df_scaled)

    vif_final = vif_data.copy()
    # print("VIF Start:")
    # print(vif_start)
    print("VIF Final:")
    print(vif_final)

if __name__ == "__main__":
    feature_selection()