# Git Workflow Documentation

## 1. Repository Initialization

The project was initialized as a Git repository using:

```bash
git init
```

The initial project files were then added and committed.

## 2. Initial Commit
The initial project setup was committed using:
```bash
git add .
git commit -m "Initial Project Setup"
```

## 3. Branching
The following branches were created:
- `main`
- `dev`
- `feature/replay-option`

The `main` branch represents the stable version of the project.
The `dev` branch is used for development.
The `feature/replay-option` branch was used to develop the replay functionality.

## 4. Feature Development
The replay option was developed on:
`feature/replay-option`

The feature was committed with:
`Add replay option to Tic-Tac-Toe`

## 5. Pull Request #1
The feature branch was merged into the development branch through a Pull Request:
`feature/replay-option` → `dev`

## 6. Pull Request #2
After the feature was merged into `dev`, the development branch was merged into the stable branch through another Pull Request:
`dev` → `main`

## 7. Git Tag
The stable version was tagged:
`v1.0.0`

The tag was pushed to GitHub using:
```bash
git push origin v1.0.0
```

## 8. Git Stash
Git stash was demonstrated by temporarily storing uncommitted changes:
```bash
git stash
```

The changes were restored using:
```bash
git stash pop
```

## 9. Merge Conflict
A controlled merge conflict was created by modifying the same line of `README.md` differently on two branches.
Git reported the conflict during the merge.
The conflicting section was manually edited to the desired final content, after which the file was staged and committed.

## Final Git Workflow

```text
feature/replay-option
          |
          | Pull Request #1
          v
         dev
          |
          | Pull Request #2
          v
         main
          |
          v
       v1.0.0
```

## Conclusion
This project demonstrates the basic Git and GitHub workflow used to manage a version-controlled DevOps project.