import tkinter as tk
from tkinter import ttk
from tkinter import messagebox 
from  DecisionTree import *

def retrieve_input_text(textbox):
    value = textbox.get("1.0", 'end-1c')
    return value


def retrieve_combobox(combobox):
    return combobox.get()


def main():

    def retrieve_values():
        example = dict()
        columns = ['age','sex','cp','trestbps','chol','fbs','restecg','thalach','exang','oldpeak','slope','ca','thal','num']
        
        # Age
        val_age = int(retrieve_input_text(text_age))
        if val_age >=60:
            example['age'] = 2.0
        elif val_age >=40:
            example['age'] = 1.0
        else:
            example['age'] = 0.0
        # Gender
        val_sex = retrieve_combobox(combobox_sex)
        if val_sex == 'Male':
            example['sex'] = 1.0
        elif val_sex == 'Female':
            example['sex'] = 0.0
        # Chest Pain Type
        val_ches_pain = retrieve_combobox(combobox_chest_pain)
        if val_ches_pain == 'Typical Angina':
            example['cp'] = 1.0
        elif val_ches_pain == 'Atypical Angina':
            example['cp'] = 2.0
        elif val_ches_pain == 'Non-Anginal Pain':
            example['cp'] = 3.0
        else:
            example['cp'] = 4.0
        # Blood Pressure

        """
            Systolic Blood Pressure :-
            -- Value 0 : <120
            -- Value 1 : 120 - 129
            -- Value 2 : 130 - 139
            -- Value 3 : 140 - 179
            -- Value 4 : >180
            """
        val_resting_bp = int(retrieve_input_text(text_resting_bp))
        if val_resting_bp>=180:
            example['trestbps'] = 4.0
        elif val_resting_bp>=140 :
            example['trestbps'] = 3.0
        elif val_resting_bp>=130:
            example['trestbps'] = 2.0
        elif val_resting_bp>=120:
            example['trestbps'] = 1.0
        else:
            example['trestbps'] = 0.0
        # Cholestrol
        val_cholestrol = int(retrieve_input_text(text_cholestrol))
        if val_cholestrol>=180:
            example['chol'] = 0.0
        else:
            example['chol'] = 1.0
        # Fasting Blood Sugar
        val_fasting_sugar = retrieve_combobox(combobox_fasting_sugar)

        if val_fasting_sugar == 'Less than 120 mg/dl':
            example['fbs'] = 0.0
        else:
            example['fbs'] = 1.0

        # Rest ECG
        val_resting_cardiac = retrieve_combobox(combobox_resting_cardiac)

        if val_resting_cardiac == "Normal":
            example['restecg'] = 0.0
        elif val_resting_cardiac == 'Having ST-T wave abnormality':
            example['restecg'] = 1.0
        else:
            example['restecg'] = 2.0

        # thalach
        val_max_heart = int(retrieve_input_text(text_max_heart_rate))

        if val_max_heart >=150:
            example['thalach'] = 2.0
        elif val_max_heart>=100:
            example['thalach'] = 1.0
        else:
            example['thalach'] = 0.0


        # Exang
        val_induced_angina = retrieve_combobox(combobox_induced_angina)
        
        if val_induced_angina == 'Yes':
            example['exang'] = 1.0
        else:
            example['exang'] = 0.0

        # Old Peak
        val_old_peak = float(retrieve_input_text(text_old_peak))

        if val_old_peak>=4:
            example['oldpeak'] = 2.0
        elif val_old_peak>=2:
            example['oldpeak'] = 1.0
        else:
            example['oldpeak'] = 0.0

        # Slope
        """
        -- Value 1 : upsloping 
        -- Value 2 : flat
        -- Value 3 : downsloping
        """
        val_slope = retrieve_combobox(combobox_slope)

        if val_slope == "Upsloping":
            example['slope'] = 1.0
        elif val_slope == "Downsloping":
            example['slope'] = 3.0
        else:
            example['slope'] = 2.0
        
        val_ca = retrieve_combobox(combobox_ca)
        example['ca'] = float(val_ca)

        val_thallium_test = retrieve_combobox(combobox_thallium_test)
        if val_thallium_test == "Normal":
            example['thal'] = 3.0
        elif val_thallium_test == "Fixed Defect":
            example['thal'] = 6.0
        else:
            example['thal'] = 7.0
        print(example)

        df_ex= pd.DataFrame([example])
        df_ex['classification'] = df_ex.apply(classify_example,axis=1,args=(tree,))
        print(df_ex.classification)
        if int(df_ex.classification) == 1:
        
            messagebox.showwarning("Warning", "Patient is at a risk of Cardiac Arrest. System Accuracy is " + str(round((accuracy)*100,2))+"%. Please refer to a cardiologist on urgent basis.") 
        else:
            messagebox.showinfo("Information", "Patient is not a risk of Cardiac Arrest. System Accurary is " + str(round((accuracy)*100,2))+"%.") 

        
        
        
       
       

       
        

    root = tk.Tk()
    root.geometry('850x420')
    root.title(" Predict ")
    root.configure(bg='grey11')

    header = tk.Label(root, text="Habib Heart Diseases Prediction System", font='Helvetica 20 bold',
                      fg='tan1', bg='grey11')
    header.place(x=170, y=10)

    age = tk.Label(root, text="Age (Years) ", font='Helvetica 10 bold',
                   fg='tan1', bg='grey11')  # Numerical
    age.place(x=30, y=60)

    sex = tk.Label(root, text=" Gender ", font='Helvetica 10 bold',
                   fg='tan1', bg='grey11')  # Categorical
    sex.place(x=30, y=100)

    chest_pain = tk.Label(root, text="Chest Pain Type",
                          font='Helvetica 10 bold', fg='tan1', bg='grey11')  # Categorical
    chest_pain.place(x=30, y=140)

    resting_bp = tk.Label(
        root, text="Systolic Blood Pressure", font='Helvetica 10 bold', fg='tan1', bg='grey11')  # Numerical
    resting_bp.place(x=30, y=180)

    cholestrol = tk.Label(root, text="Serum Cholestrol",
                          font='Helvetica 10 bold', fg='tan1', bg='grey11')   # Numerical
    cholestrol.place(x=30, y=220)

    fasting_sugar = tk.Label(
        root, text="Fasting Blood Sugar", font='Helvetica 10 bold', fg='tan1', bg='grey11')  # Categorical
    fasting_sugar.place(x=30, y=260)

    thallium_test = tk.Label(root, text="Thallium Test",
                             font='Helvetica 10 bold', fg='tan1', bg='grey11')  # Categorical
    thallium_test.place(x=30, y=300)

    resting_cardiac = tk.Label(
        root, text="Resting Electocardiographic Results", font='Helvetica 10 bold', fg='tan1', bg='grey11')  # Categorical
    resting_cardiac.place(x=400, y=60)

    max_heart_rate = tk.Label(
        root, text="Max Heart Rate during Thallium Test", font='Helvetica 10 bold', fg='tan1', bg='grey11')  # Numerical
    max_heart_rate.place(x=400, y=110)

    induced_angina = tk.Label(
        root, text="Exercise Induced Angina", font='Helvetica 10 bold', fg='tan1', bg='grey11')  # Categorical
    induced_angina.place(x=400, y=160)

    old_peak = tk.Label(root, text="ST depression induced by\nexercise relative to rest", font='Helvetica 10 bold',
                        fg='tan1', bg='grey11')  # Numerical
    old_peak.place(x=400, y=210)

    slope = tk.Label(root, text="Slope of the peak exercise \nST segment", font='Helvetica 10 bold',
                     fg='tan1', bg='grey11')  # Categorical
    slope.place(x=400, y=260)

    ca = tk.Label(
        root, text="CA : Number of major vessels (0-3)", font='Helvetica 10 bold', fg='tan1', bg='grey11')  # Categorical
    ca.place(x=400, y=300)

    text_age = tk.Text(root, height=1, width=20, bd=3)
    text_age.place(x=200, y=60)

    combobox_sex = ttk.Combobox(
        root, width=24, values=['Female', 'Male'], state="readonly")
    combobox_sex.current(0)
    combobox_sex.place(x=200, y=100)

    combobox_chest_pain = ttk.Combobox(
        root, width=24, values=['Typical Angina', 'Atypical Angina', 'Non-Anginal Pain', 'Asymptomatic'], state="readonly")
    combobox_chest_pain.current(0)
    combobox_chest_pain.place(x=200, y=140)

    text_resting_bp = tk.Text(root, height=1, width=20, bd=3)
    text_resting_bp.place(x=200, y=180)

    text_cholestrol = tk.Text(root, height=1, width=20, bd=3)
    text_cholestrol.place(x=200, y=220)

    combobox_fasting_sugar = ttk.Combobox(
        root, width=24, values=['Less than 120 mg/dl', 'Greater than 120 mg/dl'], state="readonly")
    combobox_fasting_sugar.current(0)
    combobox_fasting_sugar.place(x=200, y=260)

    combobox_thallium_test = ttk.Combobox(
        root, width=24, values=['Normal', 'Fixed Defect', 'Reversable Defect'], state="readonly")
    combobox_thallium_test.current(0)
    combobox_thallium_test.place(x=200, y=300)

    combobox_resting_cardiac = ttk.Combobox(
        root, width=24, values=['Normal', 'Having ST-T wave abnormality', 'Showing probable or definite left ventricular hypertrophy by Estes criteria'], state="readonly")
    combobox_resting_cardiac.current(0)
    combobox_resting_cardiac.place(x=650, y=60)

    text_max_heart_rate = tk.Text(root, height=1, width=20, bd=3)
    text_max_heart_rate.place(x=650, y=110)

    combobox_induced_angina = ttk.Combobox(
        root, width=24, values=['No', 'Yes'], state="readonly")
    combobox_induced_angina.current(0)
    combobox_induced_angina.place(x=650, y=160)

    text_old_peak = tk.Text(root, height=1, width=20, bd=3)
    text_old_peak.place(x=650, y=210)

    combobox_slope = ttk.Combobox(
        root, width=24, values=['Upsloping', 'Flat', 'Downsloping'], state="readonly")
    combobox_slope.current(0)
    combobox_slope.place(x=650, y=260)

    combobox_ca = ttk.Combobox(
        root, width=24, values=['0', '1', '2', '3'], state="readonly")
    combobox_ca.current(0)
    combobox_ca.place(x=650, y=300)

    photo = tk.PhotoImage(file=r"predict.png")
    btn_predict = tk.Button(root, image=photo, bd=5,
                            bg='tan1', command=retrieve_values)
    btn_predict.place(x=670, y=340)

    root.mainloop()


#main()
df = pd.read_csv("Data/HeartData.csv")

train_df,test_df = train_test_split(df,test_size=0.3)
tree = decision_tree_algorithm(train_df,max_depth=3,use_entropy=False)
accuracy,precision,recall = evaluate(test_df,tree)
pprint(tree,width=50)
main()

"""
1. Age -- Numerical  *
2. Sex -- Categorical
-- Value 0 : Female
-- Value 1 : Male
3. Chest Pain Type -- Categorical
-- Value 1 : typical angina
-- Value 2 : atypical angina
-- Value 3 : non-anginal pain
-- Value 4 : asymptomatic
4. Resting Blood Pressure -- Numerical *
5. Cholestrol : serum cholestrol in mg/dl -- Numerical *
6. Fasting Blood Sugar : -- Categorical Data
-- Value 0 : Fasting Blood Sugar < 120 mg/dl
-- Value 1 : Fasting Blood Sugar > 120 mg/dl
7. Resting Electocardiographic Results -- Categorical.
-- Value 0 : Normal
-- Value 1 : Having ST-T wave abnormality
-- Value 2 : showing probable or definite left ventricular hypertrophy by Estes' criteria
8. Maximum Heart Rate During a Thallium Test -- Numerical    *
9. Excercise Induced Angina -- Categorical
-- Value 0: No
-- Value 1: Yes
10. Old Peak : ST depression induced by exercise relative to rest -- Numerical  *
11. Slope : The slope of the peak excercise ST segment. -- Categorical
-- Value 1 : upsloping
-- Value 2 : flat
-- Value 3 : downsloping
12. CA : Number of major vessels (0-3) colored by flourosopy -- Categorical
13. Thallium Test -- Categorical
-- Value  3 : Normal
-- Value  6 : Fixed Defect
-- Value  7 : Reversable Defect
14. Num :  diagnosis of heart disease (angiographic disease status) -- Categorical
-- Value 0: < 50% diameter narrowing
-- Value 1: > 50% diameter narrowing
"""
