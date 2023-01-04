import sys
import tkinter as tk
import matplotlib
matplotlib.use('Agg')
import pandas
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt


def write_to_csv(age, experience, position, nationality):
    df = pandas.DataFrame({'Age': age, 'Experience': experience,'Position': position, 'Nationality': nationality, 'Go': 1}, index=[0])
    df.to_csv('data.csv', mode='a', header=False, index=False, columns=['Age', 'Experience','Position', 'Nationality', 'Go'])


def get_and_write_data():
    age = int(age_var.get())
    experience = int(experience_var.get())
    position = position_var.get()
    nationality = nationality_var.get()
    write_to_csv(age, experience, position, nationality)


def agaciCiz():
    df = pandas.read_csv("data.csv")
    print(df)
    d = {'UK': 0, 'USA': 1, 'TR': 2}
    df['Nationality'] = df['Nationality'].map(d)
    d = {'YES': 1, 'NO': 0}
    df['Go'] = df['Go'].map(d)

    features = ['Age', 'Experience', 'Position', 'Nationality']

    X = df[features]
    y = df['Go']

    dtree = DecisionTreeClassifier()
    dtree = dtree.fit(X, y)

    tree.plot_tree(dtree, feature_names=features)

    plt.savefig(sys.stdout.buffer)
    sys.stdout.flush()

def create_ui():
    root = tk.Tk()
    root.title("Decision Tree")

    global age_var, experience_var, position_var, nationality_var
    age_var = tk.StringVar()
    experience_var = tk.StringVar()
    position_var = tk.StringVar()
    nationality_var = tk.StringVar()

    tk.Label(root, text="Yaş:").grid(row=0, column=0)
    tk.Radiobutton(root, text="20", variable=age_var, value=20).grid(row=0, column=1)
    tk.Radiobutton(root, text="30", variable=age_var, value=30).grid(row=0, column=2)
    tk.Radiobutton(root, text="40", variable=age_var, value=40).grid(row=0, column=3)

    tk.Label(root, text="Deneyim Yılı:").grid(row=1, column=0)
    tk.Radiobutton(root, text="1", variable=experience_var, value=1).grid(row=1, column=1)
    tk.Radiobutton(root, text="5", variable=experience_var, value=5).grid(row=1, column=2)
    tk.Radiobutton(root, text="10", variable=experience_var, value=10).grid(row=1, column=3)

    tk.Label(root, text="Pozisyon:").grid(row=2, column=0)
    tk.Radiobutton(root, text="Junior", variable=position_var, value="Junior").grid(row=2, column=1)
    tk.Radiobutton(root, text="Mid", variable=position_var, value="Mid").grid(row=2, column=2)
    tk.Radiobutton(root, text="Senior", variable=position_var, value="Senior").grid(row=2, column=3)

    tk.Label(root, text="Uyruk:").grid(row=3, column=0)
    tk.Radiobutton(root, text="UK", variable=nationality_var, value="UK").grid(row=3, column=1)
    tk.Radiobutton(root, text="USA", variable=nationality_var, value="USA").grid(row=3, column=2)
    tk.Radiobutton(root, text="TR", variable=nationality_var, value="TR").grid(row=3, column=3)

    tk.Button(root, text="Gönder", command=get_and_write_data).grid(row=4, column=0)
    tk.Button(root, text="Decision Tree Çiz", command=agaciCiz).grid(row=4, column=1)
    tk.Button(root, text="Çıkış", command=root.destroy).grid(row=4, column=2)

    root.mainloop()

create_ui()

