# zsh  |  oh-my-zsh  |  terminal utilities

## git plugin ([Full git plugin reference](https://github.com/robbyrussell/oh-my-zsh/wiki/Plugin:git))  
`gaa` - git add --all  
`gcam` - git commit -a -m (include "message")  
`ggp` - git push origin master  

## utilities
`mdcat` - render markdown files in terminal (`brew install mdcat`)  

## git
### Clear git history
```
rm -rf .git # Remove the history from 

# recreate the repos from the current content only
git init
git add .
git commit -m "Initial commit"

push to the github remote repos ensuring you overwrite history
git remote add origin <repo address>
git push -u --force origin master
```
Compact version w/ oh-my-zsh
```
repo=`git config --get remote.origin.url`
rm -rf .git
g init; gaa; gcam "Initial commit"; gra origin $repo; ggf
```
## tmux
Start new session: `tmux`  
New session w/ name: `tmux new -s name`  
List sessions: `tmux ls`  
Attach: `tmux a`, `tmux at`, `tmux attach` or `tmux a -t name`  


