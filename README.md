# YuanRenXueMatchCollections

**猿人学题解代码----解题进度 6/17**
<p>2021-06-12 记录一波猿人学爬虫题库解题思路</p>

### 第12题 入门级JS
<p>抓包找API,直接看m值,能很容易猜到是Base64编码，解码后为"yuanrenxue"+页数,带着编码后的m值请求即可。</p>
<p>
  <span><a href="http://match.yuanrenxue.com/match/12">题目跳转</a></span>
  <span>/</span>
  <span><a href="https://github.com/YChengLee/YuanRenXueMatchCollections/tree/main/Match12">代码跳转</a></span>
</p>

### 第13题 入门级Cookie
<p>
    用session保持会话，请求一次match13页面，第一次返回的源码里带有yuanrenxue_cookie，正则取出手动放入session里，请求api即可返回正确数据。
</p>
<p>
  <span><a href="http://match.yuanrenxue.com/match/13">题目跳转</a></span>
  <span>/</span>
  <span><a href="https://github.com/YChengLee/YuanRenXueMatchCollections/tree/main/Match13">代码跳转</a></span>
</p>


### Tips
<div>
<p>
能力有限，分享粗糙的代码和简单的解题思路，混个脸熟。
</p>
<p>爬亦有道，数据亦取之有道，与各位爬友共勉。</p>
</div>
