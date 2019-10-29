# 抓取动物农场
1. 需求描述
    实现[动物农场](https://www.kanunu8.com/book3/6879/)的抓取
2. 实现步骤
    - 分析页面拿到当前页面的子链接
    - 封装每章数据的写入
    - 使用多线程抓取数据
3. 具体实现

4. 总结：
    - 注意```from multiprocessing.dummy import Pool```的使用
        ```
            pool = Pool(3)
            pool.map(funName,paraList)#多个线程调用funName函数，参数是paraList列表中的元素 
       ```
    - 注意os.path.join相当于不同操作系统的目录之间的连接符
        ```os.path.join('dir','a.txt')#在dir目录下的a.txt ```
