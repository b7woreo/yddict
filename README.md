# yddict

## 介绍
有道翻译命令行工具 Python3 版本

## 1.安装
``` bash
git clone https://github.com/chrnie27/yddict
```

## 2.配置
0. 到[有道翻译API](http://fanyi.youdao.com/openapi?path=data-mode)申请一个 key
0. 修改 yddict目录下的 config.json
``` json
{
    "keyfrom": "your keyfrom",
    "key": "your key"
}
```

## 3.使用
``` bash
./yddict.py Hello,world

翻译：
	你好,世界

```
