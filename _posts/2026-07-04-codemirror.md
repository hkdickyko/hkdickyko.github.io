---
category: [软件]
tags: [Linux, 系统]
title: CodeMirror
date: 2026-07-03 00:00:01
---

# CodeMirror 6

CodeMirror 6 是以独立的 ES Modules (**ESM**) 原生模块形式发布的，无法直接像 CodeMirror 5 那样直接用 **script** 引入 **IIFE** 格式的文件。为了能在浏览器中直接通过 **script** 标签以 **IIFE**（立即调用函数表达式）全局变量的方式使用它，需要借助构建工具将其打包并导出为全局对象。CodeMirror 6 采用了高度模块化的设计，按功能被拆分成了多个 **npm** 包（如 @codemirror/state、@codemirror/view、@codemirror/lang-javascript 等）。它依赖 **ESM** 进行 Tree-shaking 以减小体积，因此官方并没有提供预编译好的单文件 **IIFE** 版本。

## 构建工具转换

将 **ESM** 转换为 **IIFE** 如果希望将代码完全下载至本地以保证加载速度与离线运行，建议使用 Rollup 这类打包工具进行转换。

创建一个项目文件夹。在该文件夹内，通过以下方式安装 CodeMirror 6 软件包和 Rollup 如下所示：

- 安装工具： 在项目目录中安装 Rollup 及需要的 CodeMirror 模块：
  - npm init -y 指令，意思是自动同意所有设定提示并跳过互动问。
  - npm install -D <package-name> 的意思是將指定的套件下載並安裝為「開發時依賴項」（Development Dependency）。

```sh
mkdir cm6-iife
cd cm6-iife
npm init -y
npm install -D rollup 
npm install -D @rollup/plugin-node-resolve 
npm install -D @rollup/plugin-commonjs
npm install @codemirror/state @codemirror/view
npm install @codemirror/basic-setup
npm install @codemirror/language
npm install @codemirror/lang-javascript
```

- 编写打包入口文件 **main.js** 如下

```sh
touch main.js
```

- 文件 **main.js**

```js
import { EditorView, basicSetup } from "@codemirror/basic-setup";
import { javascript } from "@codemirror/lang-javascript";
import { EditorState } from "@codemirror/state";

// 将设置导出为一个函数，以便在 HTML 中调用
export function createEditor(element) {
  return new EditorView({
    state: EditorState.create({
      extensions: [basicSetup, javascript()],
    }),
    parent: element
  });
}
```

- 配置打包工具 **rollup.config.js** 如下，设置输出格式为 **IIFE**，并指定全局变量映射名称

```sh
touch rollup.config.js
```

- 文件 **rollup.config.js**

```js
import { nodeResolve } from "@rollup/plugin-node-resolve";
export default {
  input: "main.js", // 编写打包入口文件
  output: {
    file: "dist/codemirror-bundle.js",
    format: "iife", // 这会将代码转换为 IIFE
    name: "CodeMirrorBundle", // 全局变量名称
    sourcemap: true,
  },
  plugins: [
    nodeResolve({
      dedupe: ["@codemirror/state", "@codemirror/view"],
    }),
  ],
};
```

 - @rollup/plugin-node-resolve 外掛的 dedupe 功能：
   - 強制單一化（De-duplication）
      - 它會告訴打包工具：「不論在任何套件或路徑中看到 @codemirror/state 及 @codemirror/view，都只能將它解析（resolve）為同一個本機複本。」
   - 預防衝突
      - 這能確保整個應用程式在執行時，所有使用的都是同一個實例，從而徹底解決 instanceof 失效的問題。


- 执行打包：运行 Rollup 后，就会在 dist/ 目录下生成一个 **codemirror-bundle.js** 的 IIFE 包。
  - npx rollup -c --bundleConfigAsCjs 是一个用于执行 Rollup 打包的指令。其主要功能是强制将 ES 模组（ESM）格式的 rollup.config.js 设定档，在载入时先编译为 CommonJS（CJS）格式再执行
  - 指令参数拆解
    - npx：免安装直接执行或调用本地 node_modules/.bin 中的指令。
    - rollup：呼叫 Rollup 打包工具。
    - -c（或 --config）：使用专案根目录下的 rollup.config.js 设定档。
    - --bundleConfigAsCjs：强制将设定档本身及其相依模组，预先打包编译成 CJS 格式后再供 Rollup 读取。

```sh
npx rollup -c --bundleConfigAsCjs
```

将生成的 codemirror-bundle.js 文件包含到 HTML 页面中。可以使用全局的 CodeMirrorBundle 将编辑器附加到任何 HTML 元素。

```sh
touch index.html
```

- 文件 **index.html**

```html
<!DOCTYPE html>
<html>
  <head>
    <title>CodeMirror 6 IIFE Example</title>
  </head>
  <body>
    <div id="editor-container"></div>
    <script src="dist/codemirror-bundle.js"></script>
    <script>
      // 调用 main.js 中导出的函数
      const container = document.getElementById("editor-container");
      const editor = CodeMirrorBundle.createEditor(container);
    </script>
  </body>
</html>
```

## 安装额外插件

```sh
npm install @codemirror/lang-markdown 
npm install @codemirror/language-data
npm install --save @babel/runtime
npm install @uiw/codemirror-extensions-color
```

  - npm install --save <包名> 命令用于在项目中安装指定模块。还会把该模块的名称及版本号自动记录到项目的 package.json 文件中的 dependencies（生产环境依赖）字段内。即使省略 --save 也会默认保存，但显式使用该标志可确保代码向后兼容。


- 更新文件 **main.js**

```js
import { EditorView, basicSetup } from "@codemirror/basic-setup";
import { javascript } from "@codemirror/lang-javascript";
import { EditorState } from "@codemirror/state";
import { color } from '@uiw/codemirror-extensions-color';
// 将设置导出为一个函数，以便在 HTML 中调用
export function createEditor(element) {
  return new EditorView({
    state: EditorState.create({
      extensions: [basicSetup, javascript(), color],
    }),
    parent: element
  });
}
```

- 执行打包

```sh
npx rollup -c --bundleConfigAsCjs
```