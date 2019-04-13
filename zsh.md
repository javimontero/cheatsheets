# zsh  |  oh-my-zsh  |  terminal utilities

## git plugin ([Full git plugin reference](https://github.com/robbyrussell/oh-my-zsh/wiki/Plugin:git))  
`gaa` - git add --all  
`gcam` - git commit -a -m (include "message")  
`ggp` - git push origin master  

## utilities
`mdcat` - render markdown files in terminal (`brew install mdcat`)  

## git
### Clear git history
-- Remove the history from 
rm -rf .git

-- recreate the repos from the current content only
git init
git add .
git commit -m "Initial commit"

-- push to the github remote repos ensuring you overwrite history
git remote add origin git@github.com:<YOUR ACCOUNT>/<YOUR REPOS>.git
git push -u --force origin master


