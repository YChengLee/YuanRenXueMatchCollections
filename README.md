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

### 第15题 备周则意怠-常见则不疑
<div>
    <p>抓包，发现请求需要参数m值，看调用栈，发现m值由3个字段用‘|’拼接生成。</p>
    <ul>
        <li>1.时间戳整除2</li>
        <li>2.时间戳整除2 再减去一个随机数(直接减个固定值即可）</li>
        <li>3.拿上面两个参数用一个不知名的加密搞出个新值。</li>
    </ul>
    <p>这个不知名参数是啥玩意呢？</p>
    <p>分析源码可以发现调用了一个wasm.main的文件，我就去搜了一波！</p>
    <p><a href="https://zhuanlan.zhihu.com/p/338265761">啥是wasm?</a>我个人理解为算是一个能够被浏览器编译的一个插件。</p>
    <p>源码中调用了这个插件的encode方法，舒服的是python也有执行这类代码的第三方库<a href="https://pypi.org/project/pywasm/">pywasm</a>。</p>
    <p>所以直接可以生成参数m,然后请求接口返回正确的值了。</p>
</div>
<p>
  <span><a href="http://match.yuanrenxue.com/match/15">题目跳转</a></span>
  <span>/</span>
  <span><a href="https://github.com/YChengLee/YuanRenXueMatchCollections/tree/main/Match15">代码跳转</a></span>
</p>

### Tips
<div>
<p>
能力有限，分享粗糙的代码和简单的解题思路，混个脸熟。
</p>
<p>爬亦有道，数据亦取之有道，与各位爬友共勉。</p>
</div>
