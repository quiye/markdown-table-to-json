# markdown-table-to-json

```json
vscode ➜ /workspaces/markdown-table-to-json $ python main.py  | jq .
[
  {
    "名前": "シェパード",
    "色": "茶色",
    "大きさ": "でかい",
    "コメント": ""
  },
  {
    "名前": "チワワ",
    "色": "白",
    "大きさ": "ちいさい",
    "コメント": "アイフル"
  }
]
```