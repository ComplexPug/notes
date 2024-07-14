# JavaScript
## Ajax
XHR(XmlHttpRequest)
Ajax（Asynchronous JavaScript and XML）是一种在Web开发中使用的技术，它允许网页在不重新加载整个页面的情况下与服务器交换数据并更新部分网页内容。Ajax的核心是JavaScript的`XMLHttpRequest`对象，它可以在后台与服务器进行异步数据交换。

Ajax的关键特点包括：

1. **异步通信**：可以在不影响用户界面和用户体验的情况下，与服务器进行数据交换。
2. **JavaScript和DOM操作**：使用JavaScript处理从服务器返回的数据，并通过DOM操作更新页面内容。
3. **支持多种数据格式**：虽然名称中包含XML，但Ajax可以处理多种数据格式，包括JSON、HTML和纯文本。
4. **提高用户体验**：由于无需重新加载整个页面，因此能显著提高应用程序的响应速度和用户体验。
5. **与后端语言无关**：Ajax技术与后端实现语言无关，可以与任何服务器端技术（如Java, PHP, .NET等）结合使用。

Ajax在现代Web应用程序中广泛使用，特别是在需要快速响应和动态内容更新的应用场景中。例如，社交媒体的实时更新、搜索引擎的自动补全功能等都是Ajax技术的典型应用。

# Axios
Axios 是一个流行的 JavaScript HTTP 客户端，用于在浏览器和 node.js 环境中发送 HTTP 请求。它是基于 Promise 的，因此它允许你以异步方式处理 HTTP 响应，并提供了一种简洁且强大的方式来进行网络请求。

以下是 Axios 的一些主要特点：

1. 从浏览器中创建 XMLHttpRequests。
2. 从 node.js 创建 http 请求。
3. 支持 Promise API。
4. 拦截请求和响应。
5. 转换请求和响应数据。
6. 取消请求。
7. 自动转换 JSON 数据。
8. 客户端支持防御 XSRF。

使用 Axios 之前，你需要先将其安装到你的项目中。如果你在使用 Node.js，可以使用 npm 来安装：

```bash
npm install axios
```

以下是一个使用 Axios 发送 GET 请求的基本示例：

```javascript
const axios = require('axios');

axios.get('https://api.example.com/data')
  .then(function (response) {
    // 处理成功情况
    console.log(response.data);
  })
  .catch(function (error) {
    // 处理错误情况
    console.log(error);
  })
  .then(function () {
    // 总是会执行
  });
```

Axios 的优点是易用且功能丰富，但也要注意处理好错误和异常情况，确保应用的稳定性。

## YApi
接口Api测试生成