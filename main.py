# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


from itertools import groupby
from github.get import download_commits, read_commits
from graphs import distribution_of_commits_per_author
import os


def group_commit_authors_by_count(commits):
    commits_dicts = list(map(lambda x: dict(x), commits))
    commits_dicts.sort(key=lambda x: x['commit']['author']["name"])
    groups = groupby(commits_dicts, lambda content: content['commit']['author']["name"])
    author_commit_list = []
    for author, group in groups:
        count = 0
        for commit in group:
            count = count + 1
        author_commit_list.append(
            {"author": author,
             "commit_count": count}
        )
    author_commit_list.sort(key=lambda x: x["commit_count"], reverse=True)
    return author_commit_list


def print_active_commit_authors(since, author_commit_list, number_of_commit_authors):
    print("====================================================================================================")
    print("Time Period: ", since, " to present")
    print("The most active commit authors and the number of commits in openstack/nova project are listed below:")
    print("====================================================================================================")
    for author in author_commit_list[:number_of_commit_authors]:
        print(author["author"], author["commit_count"])


def main():
    token = input('Enter your Authorization token:')
    token = os.getenv('GITHUB_TOKEN', token)

    since = "2021-02-01"
    data_file_path = "./data/commits.json"
    download_commits(token,since=since, per_page=100, page=1, file_path=data_file_path,
                     download_directory="./data/json_files/")
    commits = read_commits(data_file_path)
    print(str(len(commits)), " dounloaded succesfully.")
    author_commit_list = group_commit_authors_by_count(commits)

    print_active_commit_authors(since, author_commit_list, number_of_commit_authors=15)
    distribution_of_commits_per_author.draw_graphs(since, author_commit_list)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
