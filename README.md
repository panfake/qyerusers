# qyerusers
###一个上午写出来的多线程网页抓取程序。

通过枚举用户ID抓取qyer上用户评论数。并单独列出评论数超过500的用户。

调用了beautifulsoup进行过滤，当然也可以用自带的。
多线程通过multiprocessing的map函数完成。

###使用方法：
* Windows
  ```user.py ```
* Linux
  ```python user.py ```
* 然后输入最大用户ID(从1开始枚举)。

###已知BUG：
在VPS(Ubuntu 14 X32)上用100线程跑。数据量在10000左右的时候会崩毁。
提示```Exception in thread Thread-X (most likely raised during interpreter shutdown) ``` 如果你知道为什么请帮助我提高！

非常感谢！
