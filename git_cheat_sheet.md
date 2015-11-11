# Git Usage

> Carlson have the following assumtions for the readers of this file
> 1. They have their git correctly installed
> 2. The version of their git is greater than 1.8
> 3. They do not have any configuration for their git

### Single Branching - Working With Only Yourself

>Single Branching in this chapter means, only one branch locally, and one branch
remotely.

>That means, no commands like merge, rebase, fork, or something else that
related to Branching will be introduced in this chapter


>Suppose we have only one branch on the remote repo, and nothing locally.
With the content in this chapter, you can understand how to use git in the most
basic manner. You can play around it, and have your code uploaded to any git
server like Github or Bitbucket.

>However, with only the following skills/information, you can hardly cooperate
with your teammates, since there is only one branch locally and remotely.

With git installed, we can have git init on any dir

```bash
git init
# create a .git dir in the current dir
git remote add <remote-repo-name> <remote-repo-url>
# bind a name with a url. The <remote-repo-name> do not have to be consistent
# with the real repo name in the remote server (like Github)
git remote
# This will show the known remote repo name. See if your repo is added correctly
```

Sample output:
```bash
carlson@machine:~/testbed$ git init
Initialized empty Git repository in /home/carlson/testbed/.git/
carlson@machine:~/testbed$ git remote add webappdemo https://github.com/CarlsonZhuo/WebAppDemo.git
carlson@machine:~/testbed$ git remote
webappdemo
```

Now pull the data in the remote repo to local.
```bash
carlson@machine:~/testbed$ git pull webappdemo master
# Now we still don't have any branch locally.
# In the remote repo, there is also only one branch, called master
# Therefore, I pull the master branch from webappdemo.
# And now I have a master branch lcoally
remote: Counting objects: 23, done.
remote: Compressing objects: 100% (6/6), done.
remote: Total 23 (delta 2), reused 0 (delta 0), pack-reused 16
Unpacking objects: 100% (23/23), done.
From https://github.com/CarlsonZhuo/WebAppDemo
 * branch            master     -> FETCH_HEAD
 * [new branch]      master     -> webappdemo/master

```

Suppose now you have some changes on your local files. To see what files you've
change, use the following git command

```bash
git status
```

To see exactly what modication you've made, use the following git command

```bash
git diff
```

And you want to push
the changes to the remote server like Github, so that your talented work can be
shared with others, we need to do the following.

```bash
git add -A
# This will add all the modification/file-delete/file-add to index
# Notice the terminology, index. The how git works.png may help in understanding
git commit -m 'some comment here'
# Now the change is added to local repo
git push <remote-branch-name> <local-branch-name>
# Before doing this, the repo on the server like Github is not affected.
```

### Single Branching - Basic Cooperation
>Single Branching in this chapter means only one branch remotely, but multiple
branch locally. This makes cooperation among 2-5 people possible.

The git commands involved in this chapter will be:
```bash
git branch <branch name>
# create a new branch locally based on your current branch
git checkout <branch name>
# switch to the <branch name>
git rebase <branch name>
# re-base the current branch on the <branch name> branch
```

example



### Multi-branching

After reading the two single branching chapter above, I believe that you've
already got your thing running. By now, it is still hard to convince you that
git is indeed better that SVN or other version control tools.

Indeed, git is much more than single branching, since it
provides fork, merge, and a lot of other powerful tools.

Since this cheat sheet is just the most basic cheat sheet, and aim at having
thing running without too much background knowledge. I believe that, there are
already countless good tutorial introducing the Multi-branching functionality
of git. :-D

### Roll Back

Assuming you did not commit the file, or add it to the index, then:
```bash
git checkout filename
```
Assuming you added it to the index, but did not commit it, then:
```bash
git reset HEAD filename
git checkout filename
```
Assuming you did commit it, then:
```
git checkout origin/master filename
```
Assuming you want to blow away all commits from your branch (VERY DESTRUCTIVE):
```
git reset --hard origin/master
```

### Diff Branch, Fork, Fetch, Merge, Rebase and Clone

reference:

[1] http://stackoverflow.com/questions/3329943/git-branch-fork-fetch-merge-rebase-and-clone-what-are-the-differences

### Delete a remote branch

```bash
git push <remote-branch-name> --delete <branch-name>
```

reference:

[1] http://stackoverflow.com/questions/2003505/delete-a-git-branch-both-locally-and-remotely
