```dataviewjs
const command = "git checkout 4cdd9dd"

const description = `
Git покажет проект таким, каким он был в этом коммите.
Ты буквально перемещаешься во времени между версиями проекта.
`

const warning = `
Ты находишься в режиме detached HEAD.
Это не ошибка — просто временный просмотр старой версии.
`

const back = "git checkout master"

const box = dv.el("div", "", {
    cls: "git-card"
})

box.innerHTML = `
<div class="git-top">
    <div class="git-badge">GIT</div>
    <div class="git-status">ACTIVE</div>
</div>

<div class="git-title">
🔄 Перемещение между версиями
</div>

<div class="git-subtitle">
Перейти к старому коммиту
</div>

<pre class="git-code">${command}</pre>

<div class="git-desc">
${description}
</div>

<div class="git-warning">
⚠️ ${warning}
</div>

<div class="git-section">
<div class="git-small-title">
↩️ Вернуться обратно
</div>

<pre class="git-code">${back}</pre>
</div>

<div class="git-footer">
HEAD → 4cdd9dd
</div>
`
```
