import json
from typing import Dict, List

t = """
| 名前      | 色     | 大きさ     |コメント|
|---------- | :----------: | -----------: |-----------: |
| シェパード | 茶色   | でかい    |    |
|  チワワ    |  白            | ちいさい    |アイフル    |
"""


def mrkd2json(inp: str) -> List[Dict[str, str]]:
    lines = inp.split('\n')
    lines = list(filter(lambda x: x.strip() != "", lines))
    keys = [s.strip() for s in lines[0].split('|')]
    ret: List[Dict[str, str]] = []
    for l in lines[2:]:
        line_data = l.split('|')
        if len(line_data) != len(keys):
            raise Exception(f"line is invalid, line={l}")
        k = {keys[i+1]: v.strip() for i, v in enumerate(line_data[1:-1])}
        ret.append(k)
    return ret


print(json.dumps(mrkd2json(t)))
