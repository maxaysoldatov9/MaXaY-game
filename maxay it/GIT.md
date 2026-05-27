Основные команды
[[git status]]
[[git add .]]
[[git commit -m]]
[[git log --oneline]]
[[git checkout]]
[[git branch]]


```dataviewjs
const pages = dv.pages()
    .sort(p => p.file.name)

dv.table(
    ["Заметка", "Создана"],
    pages.map(p => [
        p.file.link,
        p.file.ctime
    ])
)
```

# Git Roadmap

- [x] git init
- [x] git status
- [x] git add
- [x] git commit
- [x] git log
- [x] git checkout

- [x] git branch
- [ ] git merge
- [ ] git push
- [ ] git pull
- [ ] GitHub
- [ ] SSH keys
- [ ] .gitignore

