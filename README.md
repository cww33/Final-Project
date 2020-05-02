# Final-Project#

## Setup

### Repo Setup

Use Github.com online interface a new remote repository such as *Subscription_Tracking*. Ensure you add a "README.md" file.

After creating the remote repo, use the Github.com online interface and click on the green button that says Clone or Download and click on the option that says Open in Desktop. Once this is done you will be promted on your web browser asking if you want to open the repository on your Github desktop software, click on the option that says Open GitHubDesktop.exe.

After you finish that, navigate to the repo from the command line:

```
cd ~/Desktop/Subscriptions
```

### Environment Setup

We need to create and activate a new Anaconda virtual environment. Do this by first placing in the command line:

```
conda create -n allowance-env python=3.7
```
This will only be done when setting up the project for the first time. Run it and then place in the command line:

```
conda activate allowance-env
```
This will activate the virtual environment. From within the virtual environment, demonstrate your ability to run the Python script from the command line:
```
python subscription.py
```

### Program Output

This program will produce a output similar to:

```
Your Current Subscriptions are:
______________________________________________
Netflix  $9.99
Hulu  $4.99
Amazon  $5.99
Spotify  $4.99
Les_mills  $14.99
LinkedIn  $59.99
----------------------------------
Total:  $100.94
______________________________________________
Allowance left $399.06
______________________________________________
Storing data to CSV file


Hope this application helped! Have a nice day!

```


## Disclaimers 

#### Allowance

An allowance is given to the user regarding the salary the user makes monthly and the percentage of salary the user chooses that he/she wants to allocate towards monthly subscriptions. These numbers are decided by the users and the application is **NOT** designed to be a budgeting tool.

#### How the Allowance is Calculated

The allowance is calculated by multiplying the salary the user inputs he/she makes monthly to the percentage of salary the user chooses that he/she wants to allocate towards monthly subscriptions. This application calculates said allowance and allows the users to input subscriptions that they already have with new subscriptions to see whether or not they can afford the new subscriptions.




