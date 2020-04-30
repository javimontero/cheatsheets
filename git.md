## Branching to github
Create a new branch  
```
git branch develop
git checkout develop
```
Shorcut  
`git checkout -b develop`

Push to remote repo  
`git push -u origin develop`

## Comparing branches
View branches in local repo  
`git branch`
View both remote and local branches  
`git branch -a` 

## Delete
`git branch -d develop`

## Replace local branch from remote
Assuming origin/develop is the remote branch you want to reset to
`git reset --hard origin/develop`
