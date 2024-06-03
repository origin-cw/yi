
[Word排版基础教程](https://www.bilibili.com/video/BV1YQ4y1M73G/?spm_id_from=333.1007.top_right_bar_window_custom_collection.content.click&vd_source=9b0f22ba38b29446d9922bddebde1c5d)

---
### 1.设置样式
可以在首行先设置好需要的格式，然后一一对应填上去。F4是快捷键，将光标所在的段落样式设置为上一个。
### 2. 设置多级列表
* 先设置好标题的样式，然后在使用多级列表时，选中该级别列表要连接到什么样式，然后直接应用就行了。  
* 多级列表可以用来插入章节号，所以标题不需要手动写入章节号。    
* 只有设置好了多级列表，在插入图片时才能按照章节号进行引用。  


当牵扯到第一级列表是中文时候，可以这么[解决](https://blog.csdn.net/qq_42191914/article/details/105936695)。  
即第一级使用大写数字，但是后续章节选中“正规形式编号”；或者第一章使用阿拉伯数字，但是要选中隐藏，然后在“文件-选项-显示”里面把文字给隐藏掉即可。    


### 3.题注和引用
在 **引用**里找到**插入题注**，然后设置好需要的格式，之后插入就可以；引用的时候，在同样的位置有一个交叉引用，在这里设置引用。
题注的样式设置和第一部分一样，先设置题注的格式，再引用就可以了。
> Tips：当删除图片或者表格的时候，需要更新其他图片的序号，先ctrl+A选中全文，然后按 F9/Fn+F9 就可以更新序号了。
### 4.制作三线表
先根据需要创建一个？行？列的表格；
选中表格后，会出来一个表设计，进去之后提供了很多表格的样式；也可以自己设置，新建一个表格类型，可以调节表格线宽、字体格式等。
最常见的是三线表，先设置**整个表格**，设置线宽，然后添加到上边框和下边框；再设置**标题行**,添加到下边框就可以。

当我们需要在某个单元行的上下添加边框时，就选中该单元行，然后**右击鼠标**，点击**表格属性**，点击**边框和底纹**，在这里就可以添加上下边框。
### 5. 插入参考文献
使用[Endnote](./Endnote.md)插入
### 6.生成目录
前提是先设置多级列表；然后把光标定位到目录处，在 引用 里面的 目录 下，可以添加目录，或者自定义目录，在设置里面还可以添加超链接；
当后续修改标题时，点击更新目录即可更新。
### 7.设置页码
当想在中间某一页重新排序时，将光标放在这一页的前端，选中布局--分隔符--下一页，然后选择插入--页码，可以选择插入的样式；
之后修改页码，比如删掉第一页的页码，或者想从第2页重新排序，那么插入下一页分隔符后，先选中第2页的页码，然后取消 链接到前一条页眉 ，之后再删掉第一页的页码就可以了，或者在 页码格式 里面选择 起始页码 重新排序即可；
如果想设置全都是奇数的页码或者全都是偶数的页码，可以在插入分隔符阶段，不选择下一页，而是 奇数页 或者 偶数页。

### 8.导出pdf
可以在布局里面设置纸张大小和页边距，然后在开始里面导出为PDF


---

### 额外补充
* 三个“-”加回车可以快速添加一条直线，类似的还有三个“*”、“=”、“~”
* 选中文字段落后后，`Ctrl+2`可以快速调整双倍行距，`Ctrl+1`可以快速调整单倍行距
* 选中文字段落后，使用替换功能，查找“空格”，替换那里不填写，确定之后就可以快速删除段落里面的空格
* 打上2610/2611/2612后，然后选中，再`Alt+x`，就会形成特殊符号。
* [双栏排版里面插入图片只显示底部一小部分](https://blog.csdn.net/weixin_57242009/article/details/126029034?utm_medium=distribute.pc_relevant.none-task-blog-2~default~baidujs_baidulandingword~default-0-126029034-blog-106399018.235^v43^control&spm=1001.2101.3001.4242.1&utm_relevant_index=3)
* [双栏格式下插入单栏图片](https://blog.csdn.net/weixin_46902019/article/details/131234418?spm=1001.2101.3001.6650.5&utm_medium=distribute.pc_relevant.none-task-blog-2%7Edefault%7EBlogCommendFromBaidu%7ERate-5-131234418-blog-125625885.235%5Ev43%5Econtrol&depth_1-utm_source=distribute.pc_relevant.none-task-blog-2%7Edefault%7EBlogCommendFromBaidu%7ERate-5-131234418-blog-125625885.235%5Ev43%5Econtrol&utm_relevant_index=7)
* [修改endnote插入word的参考文献格式（现代制造工程）](https://blog.csdn.net/weixin_42616244/article/details/103539129)
* [页眉页码设置在同一行](https://zhidao.baidu.com/question/342895711.html#:~:text=%E6%96%B9%E6%B3%95%E6%AD%A5%E9%AA%A4%E5%A6%82%E4%B8%8B%EF%BC%9A%201%E3%80%81%E6%89%93%E5%BC%80%E9%9C%80%E8%A6%81%E6%93%8D%E4%BD%9C%E7%9A%84WORD%E6%96%87%E6%A1%A3%EF%BC%8C%E5%9C%A8%E6%8F%92%E5%85%A5%E9%80%89%E9%A1%B9%E5%8D%A1%E4%B8%AD%E7%82%B9%E5%87%BB%E2%80%9C%E9%A1%B5%E7%9C%89%E2%80%9D%EF%BC%8C%E5%B9%B6%E6%A0%B9%E6%8D%AE%E9%9C%80%E8%A6%81%E5%8F%AF%E9%80%89%E6%8B%A9%E4%B8%89%E6%A0%8F%E6%A0%B7%E5%BC%8F%E7%9A%84%E9%A1%B5%E7%9C%89%E6%8F%92%E5%85%A5%E3%80%82%20%E3%80%90%E6%96%B9%E4%BE%BF%E5%9C%A8%E5%90%8E%E9%9D%A2,%E4%B8%80%E6%A0%8F%E6%8F%92%E5%85%A5%E9%A1%B5%E7%A0%81%E3%80%91%202%E3%80%81%E8%BE%93%E5%85%A5%E9%A1%B5%E7%9C%89%E7%9B%B8%E5%85%B3%E6%96%87%E6%9C%AC%E5%86%85%E5%AE%B9%EF%BC%8C%E7%84%B6%E5%90%8E%E5%B0%86%E5%85%89%E6%A0%87%E5%81%9C%E5%9C%A8%E5%90%8E%E9%9D%A2%E4%B8%80%E6%A0%8F%E4%B8%8A%EF%BC%8C%E7%82%B9%E5%87%BB%E6%8F%92%E5%85%A5%E9%80%89%E9%A1%B9%E5%8D%A1%E4%B8%AD%E7%9A%84%E2%80%9C%E6%96%87%E6%A1%A3%E9%83%A8%E4%BB%B6%E2%80%9D%3E%E2%80%9C%E5%9F%9F%E2%80%9D%E3%80%82%203%E3%80%81%E5%9C%A8%E5%9F%9F%E5%90%8D%E4%B8%AD%E6%89%BE%E5%88%B0%E5%B9%B6%E7%82%B9%E5%87%BB%E2%80%9Cpage%E2%80%9D%EF%BC%8C%E7%84%B6%E5%90%8E%E5%9C%A8%E5%8F%B3%E4%BE%A7%E9%80%89%E6%8B%A9%E9%A1%B5%E7%A0%81%E6%A0%BC%E5%BC%8F%EF%BC%8C%E7%82%B9%E5%87%BB%E7%A1%AE%E5%AE%9A%E5%8D%B3%E5%8F%AF%E3%80%82%204%E3%80%81%E8%BF%94%E5%9B%9E%E4%B8%BB%E6%96%87%E6%A1%A3%EF%BC%8C%E5%8F%91%E7%8E%B0%E5%9C%A8word2007%E4%B8%AD%EF%BC%8C%E5%9C%A8%E9%A1%B6%E7%AB%AF%E6%8A%8A%E9%A1%B5%E7%9C%89%E9%A1%B5%E7%A0%81%E5%90%8C%E6%97%B6%E8%AE%BE%E7%BD%AE%E5%9C%A8%E5%90%8C%E4%B8%80%E8%A1%8C%E6%93%8D%E4%BD%9C%E5%AE%8C%E6%88%90%E3%80%82)
* [双栏格式中，最后一页的两栏对齐](https://zhidao.baidu.com/question/468801604.html#:~:text=%E7%AC%AC%E4%B8%80%E6%AD%A5%EF%BC%9A%E9%80%89%E4%BD%8F%E6%9C%80%E5%90%8E%E4%B8%80%E9%A1%B5%E6%89%80%E6%9C%89%E5%86%85%E5%AE%B9%EF%BC%8C%E9%A1%B5%E9%9D%A2%E5%B8%83%E5%B1%80%EF%BC%8C%E5%88%86%E6%A0%8F%EF%BC%8C%E4%B8%80%E6%A0%8F%EF%BC%9B,%E7%AC%AC%E4%BA%8C%E6%AD%A5%EF%BC%9A%E5%9C%A8%E6%9C%80%E5%90%8E%E4%B8%80%E9%A1%B5%E7%9A%84%E6%9C%80%E5%90%8E%E4%B8%80%E8%A1%8C%E5%9B%9E%E8%BD%A6%EF%BC%8C%E5%86%8D%E9%80%89%E4%BD%8F%E6%9C%80%E5%90%8E%E4%B8%80%E9%A1%B5%E6%89%80%E6%9C%89%E5%86%85%E5%AE%B9%EF%BC%88%E4%B8%8D%E5%8C%85%E6%8B%AC%E6%9C%80%E5%90%8E%E5%A2%9E%E5%8A%A0%E7%9A%84%E7%A9%BA%E8%A1%8C%EF%BC%89%EF%BC%8C%E9%A1%B5%E9%9D%A2%E5%B8%83%E5%B1%80%EF%BC%8C%E5%88%86%E6%A0%8F%EF%BC%8C%E4%BA%8C%E6%A0%8F%EF%BC%8C%E5%8D%B3%E5%8F%AF%E5%AE%8C%E6%88%90%E3%80%82)，还有一个[方法二](https://blog.csdn.net/qq_15255077/article/details/106941858)
* `Ctrl + shift + s` :新建样式
* `Ctrl + shift + 8(Ctrl + *)` :显示/隐藏 标记和内容
* [修改word中mathtype插入的公式字体大小](https://www.mathtype.cn/jiqiao/piliang-xiugai-zitidaxiao.html)
* [使用Mathtype的“插入下一章”导致整个自动生成的目录出现难看的章节号](https://blog.csdn.net/a_cherry_blossoms/article/details/129119339)

---
**针对同一行部分文字居中，部分文字居右**：
方法一：
在“视图”里面打开“标尺”，然后在左上角可以选中居中居右，在标尺的位置上可以插入居中居右，如下图所示
![sdfa](./image/Word排版/制表符.jpg)
然后在文字前按一下tab键就可以了。

方法二：
把光标放置在那一行，然后鼠标右击，选择“段落-制表符”；    
在制表符里面可以设置tab键的缩进字符数，原理和方法一是一样的，只不过更精确。
然后再按tab键就可以了

---