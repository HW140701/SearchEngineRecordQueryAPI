# SearchEngineRecordQueryAPI

用于获取各大搜索引擎对站点某一个页面的收录状态。该项目基于flask框架搭建。

## 1 百度收录查询
**接口描述**：用于获取百度对某个页面的收录状态。

**接口调用**： 

 - 请求地址：http://127.0.0.1:5000/api/BaiduRecordQuery/?url=www.stubbornhuang.com/503/
 - 请求方法：Get
 - 请求参数： 
     - url : 需要查询的页面链接

**接口响应**:
响应示例：

```python
{
	"url": "www.stubbornhuang.com/503/",
	"isRecord": true
}
```

响应参数：

 - url : 需要查询的页面链接
 - isRecord：表示搜索引擎收录状态，true表示该搜素引擎已收录，false表示该搜索引擎未收录

	


