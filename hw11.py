import pandas as pddef chickenpox_by_sex():
    data = {'sex': ['male', 'female', 'male', 'female', 'male', 'female', 'male', 'female'],            'chickenpox': [True, False, True, True, False, False, True, False],
            'vaccinated': [True, True, False, True, True, False, True, True]}    df = pd.DataFrame(data)
    vaccinated_with_chickenpox_male = len(df[(df['sex'] == 'male') & (df['chickenpox'] == True) & (df['vaccinated'] == True)])
    vaccinated_no_chickenpox_male = len(df[(df['sex'] == 'male') & (df['chickenpox'] == False) & (df['vaccinated'] == True)])
    vaccinated_with_chickenpox_female = len(df[(df['sex'] == 'female') & (df['chickenpox'] == True) & (df['vaccinated'] == True)])    vaccinated_no_chickenpox_female = len(df[(df['sex'] == 'female') & (df['chickenpox'] == False) & (df['vaccinated'] == True)])
    male_ratio = vaccinated_with_chickenpox_male / vaccinated_no_chickenpox_male if vaccinated_no_chickenpox_male >0 else 0
    female_ratio = vaccinated_with_chickenpox_female / vaccinated_no_chickenpox_female if vaccinated_no_chickenpox_female > 0 else 0    return {"Мужчины": male_ratio, "Женщины": female_ratio}
print(chickenpox_by_sex())
