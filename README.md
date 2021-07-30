# openstack-nova-mining-exercise

These instructions will get you a copy of the project to run on your local machine.
### Python Prerequisites

You need Python 3.7 or above to run this program.
Then, you need to install the following libraries.
```
pip install numpy
pip install pandas
pip install matplotlib
```

### Getting a GitHub Authorization token
If you already have a GitHub Authorization token, you can reuse it in later parts.

Otherwise, follow this tutorial to obtain a developer token.
https://docs.github.com/en/github/authenticating-to-github/keeping-your-account-and-data-secure/creating-a-personal-access-token

## Running the Project

Clone the repo.
```
git clone https://github.com/NimmiW/openstack-nova-mining-exercise.git
```

Open a command prompt in the root directory of the project.

Then, run the main.py file.

```html
D:\...\openstack-nova-mining-exercise>python main.py
```

Then you get the following:
```
Enter your Authorization token:
```
Enter the Autorization token you have and hit Enter key.

Then, you will see a result like follows:

```
Downloading...
Downloading...
Downloading...
Downloading...
Downloading...
588  dounloaded succesfully.
====================================================================================================
Time Period:  2021-02-01  to present
The most active commit authors and the number of commits in openstack/nova project are listed below:
====================================================================================================
Zuul 295
Stephen Finucane 116
Lee Yarwood 43
Balazs Gibizer 35
melanie witt 18
Artom Lifshitz 10
Sean Mooney 10
Sylvain Bauza 10
Kashyap Chamarthy 6
Ghanshyam Mann 4
Johannes Kulik 4
Dan Smith 3
Lucas Alvares Gomes 3
Takashi Natsume 3
Belmiro Moreira 2
====================================================================================================
Time Period:  2021-02-01  to present
The Distribution of the number of commits from a user
====================================================================================================
A summary on the number of commits by an author
count     40.000000
mean      14.700000
std       49.526579
min        1.000000
25%        1.000000
50%        1.000000
75%        4.000000
max      295.000000
Name: commit_count, dtype: float64
Number of commit Authors  40
Once the Zuul's data was removed from the datase, the statistics are ad follows:
count     39.000000
mean       7.512821
std       19.920727
min        1.000000
25%        1.000000
50%        1.000000
75%        3.500000
max      116.000000
Name: commit_count, dtype: float64

```

