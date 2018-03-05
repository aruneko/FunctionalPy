# FunctionalPy
## これなに
関数型的なPythonを実現するためのライブラリ

## 実装済み具象クラス
### Seq
List相当のクラス。標準パッケージのtypingにあるListと被るのを防ぐため苦肉の策でSeqクラスと命名。

### Maybe
おなじみ。

## 実装済み型クラス
### Functor
mapできるやつ

### Applicative
Functorであり、apできるやつ

### Monad
Applicativeであり、flat_mapできるやつ

### Foldable
要するにたたみ込めるやつ

## 既知の問題
- 一部のメソッドで型検査時に`incompatible with supertype`が発生する
    - あるインターフェースに含まれるメソッドを実装したとき、型ヒントを具象クラスのものにしてしまうと発生する
    - [GithubのIssue](https://github.com/python/typing/issues/241)に上がっている
    - 一応[解決のための提案](https://github.com/python/mypy/issues/4432)はあるらしい