import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#https://stackoverflow.com/questions/6170246/how-do-i-use-matplotlib-autopct
def make_autopct(values):
    def my_autopct(pct):
        total = sum(values)
        val = int(round(pct * total / 100.0))
        return '{p:.2f}%  ({v:d})'.format(p=pct, v=val)

    return my_autopct


def prepare_data(since, author_commit_list):
    df = pd.DataFrame([x for x in author_commit_list])
    print("A summary on the number of commits by an author")
    print(df["commit_count"].describe())
    print("Number of commit Authors ", str(len(df)))
    return df


def draw_graphs(since, author_commit_list):
    print("====================================================================================================")
    print("Time Period: ", since, " to present")
    print("The Distribution of the number of commits from a user")
    print("====================================================================================================")
    df = prepare_data(since, author_commit_list)

    plt.title("The number of commits since " + since + " \n by the commit authors")
    plt.xlabel("Number of commits")
    plt.ylabel("Number of commit authors")
    hist = df["commit_count"].hist(bins=40)
    plt.show()

    filtered_df = df[df["commit_count"] < 100]["commit_count"].hist(bins=50)
    removed_users = df[df["commit_count"] >= 100]

    plt.title("The number of commits since " + since + " \n by the commit authors\n (zoomed in version)")
    plt.xlabel("Number of commits")
    plt.ylabel("Number of commit authors")
    plt.show()

    other_users_commits = df[df["commit_count"] < 100]["commit_count"].sum()
    values = np.append(removed_users["commit_count"].values, other_users_commits)
    labels = np.append(removed_users["author"].values, "Other authors")
    plt.title("The percentage of the number of commit by commit authors",
              bbox={'facecolor': '0.8', 'pad': 5})
    plt.pie(values, labels=labels, autopct=make_autopct(values))
    plt.show()

    print("Once the Zuul's data was removed from the datase, the statistics are ad follows:")
    print(df[df["author"] != 'Zuul']['commit_count'].describe())
