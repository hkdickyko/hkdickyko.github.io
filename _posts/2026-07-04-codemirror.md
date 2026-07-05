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
## 查找和搜索

如果编辑器画布之外构建自己的 UI 按钮，则可以通过导入特定的命令函数并将 EditorView 实例直接传递给它们来切换内置的搜索/替换面板如下：

- 文件 **main.js**

```js
import { EditorView, basicSetup } from "@codemirror/basic-setup";
import { javascript } from "@codemirror/lang-javascript";
import { EditorState } from "@codemirror/state";
import { search, searchKeymap } from "@codemirror/search";
import { openSearchPanel, closeSearchPanel } from "@codemirror/search";
import { keymap } from "@codemirror/view";

// 将设置导出为一个函数，以便在 HTML 中调用
export function createEditor(element) {
  return new EditorView({
    state: EditorState.create({
      extensions: [basicSetup, javascript(), search({ top: true }), keymap.of(searchKeymap)]
    }),
    parent: element
  });
}

export function openSearch(view){
  return openSearchPanel(view);
}

export function closeSearch(view){
  return closeSearchPanel(view);
}
```

- 执行打包

```sh
npx rollup -c --bundleConfigAsCjs
```

- 文件 **index.html**

```html
<!doctype html>
<html>
  <head>
    <title>CodeMirror 6 IIFE Example</title>
  </head>
  <body>
    <button id="open-find" type="button">Open Search</button>
    <button id="close-find" type="button">Close Search</button>
    <div id="editor-container"></div>
    <script src="dist/codemirror-bundle.js"></script>
    <script>
      // 调用 main.js 中导出的函数
      const container = document.getElementById("editor-container");
      const editor = CodeMirrorBundle.createEditor(container);
      document.getElementById("open-find").addEventListener("click", () => {
        CodeMirrorBundle.openSearch(editor);
      });
      document.getElementById("close-find").addEventListener("click", () => {
        CodeMirrorBundle.closeSearch(editor);
      });
    </script>
  </body>
</html>
```

## 安装 replit/codemirror-css-color-picker 额外插件

 - 安装 CodeMirror 模块

```sh
npm install @codemirror/lang-css
npm install -save @replit/codemirror-css-color-picker
```

- npm install --save <包名> 命令用于在项目中安装指定模块。还会把该模块的名称及版本号自动记录到项目的 package.json 文件中的 dependencies（生产环境依赖）字段内。即使省略 --save 也会默认保存，但显式使用该标志可确保代码向后兼容。

- 更新文件 **main.js**

```js
import { basicSetup } from 'codemirror';
import { EditorState } from '@codemirror/state';
import { EditorView } from '@codemirror/view';
import { css } from '@codemirror/lang-css';
import { colorPicker, wrapperClassName } from '@replit/codemirror-css-color-picker';

export function createEditor(idName) {
  return new EditorView({
    parent: document.querySelector('#' + idName),
    state: EditorState.create({
      doc: '.wow {\n  color: #fff;\n}',
      extensions: [
        basicSetup,
        css(),
        colorPicker,
        EditorView.theme({
          [`.${wrapperClassName}`]: {
            outlineColor: 'transparent',
          },
        }),
      ],
    }),
  });
}
```

- 执行打包

```sh
npx rollup -c --bundleConfigAsCjs
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
      const editor = CodeMirrorBundle.createEditor("editor-container");
    </script>
  </body>
</html>
```

## GFM 

CodeMirror 的 GFM（GitHub Flavored Markdown）模式是其专门用于处理 GitHub 扩展 Markdown 语法的扩展包

 - 扩展语法支持：全面支持删除线（~~text~~）、任务列表（[ ]）、Emoji 表情符号（如 :smile:）等 GitHub 特有语法。
 - 代码高亮：支持带有语言标识的围栏代码块（Fenced Code Blocks），并可针对其中的代码进行语法高亮。
 - 智能链接：支持 URL 自动识别链接以及 SHA 提交哈希引用（如 User/Project@SHA）。

CodeMirror 6：作为 @codemirror/lang-markdown 包的一部分，在 CM6 中 GFM 模式已被集成并常被称为 markdownLanguage，可以通过设置基础语言来无缝支持这些扩展。

 - 安装 CodeMirror 模块

```js
npm install @codemirror/lang-markdown 
npm install @codemirror/language-data
npm install @lezer/markdown
```

 - 更新文件 **main.js**

```js
import { basicSetup } from 'codemirror';
import { EditorState } from "@codemirror/state";
import { EditorView } from "@codemirror/view";
import { markdown, markdownLanguage } from "@codemirror/lang-markdown";
import { languages } from "@codemirror/language-data";

export function createEditor(idName) {

  const startState = EditorState.create({
    doc: "# GFM 測試\n\n- [x] 任務列表\n- ~~刪除線~~\n\n```javascript\nconst a = 1;\n```",
    extensions: [
      basicSetup,
      // 啟用 Markdown 語言支援
      markdown({
        base: markdownLanguage,   // 基礎為 Markdown
        codeLanguages: languages, // 允許圍欄程式碼塊自動匹配高亮語言（如 js, python 等）
        addExtensions: []         // 如果需要進一步自訂，可在此處加入額外的 Markdown 語法擴充
      })
    ]
  });

  return new EditorView({
    state: startState,
    parent: document.getElementById("#" + idName) // DOM 節點
  });
}
```

- 文件 **rollup.config.js**

```js
import { nodeResolve } from "@rollup/plugin-node-resolve";
export default {
  input: "main.js", // 编写打包入口文件
  output: {
    file: "dist/codemirror-bundle.js",
    format: "iife", // 这会将代码转换为 IIFE
    name: "cm",     // 全局变量名称为 cm
    inlineDynamicImports: true, // 添加此行强制 Rollup 将所有内容打包到一个文件中
  },
  plugins: [
    nodeResolve({
      dedupe: ["@codemirror/state", "@codemirror/view"],
    }),
  ],
};
```

如果严格要求使用 iife 格式，可以通过设置 **inlineDynamicImports: true** 来强制 Rollup 将所有内容打包到一个文件中。

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
      const editor = CodeMirrorBundle.createEditor("editor-container");
    </script>
  </body>
</html>
```

## 直接输出 CodeMirror

将 codemirror 函数打开为 **IIFE**

- 更新文件 **main.js**

```js
import { EditorView, basicSetup } from "codemirror";
import { javascript } from "@codemirror/lang-javascript";

export { EditorView, basicSetup, javascript };
```

- 文件 **rollup.config.js**

```js
import { nodeResolve } from "@rollup/plugin-node-resolve";
export default {
  input: "main.js", // 编写打包入口文件
  output: {
    file: "dist/codemirror-bundle.js",
    format: "iife", // 这会将代码转换为 IIFE
    name: "cm",     // 全局变量名称为 cm
  },
  plugins: [
    nodeResolve({
      dedupe: ["@codemirror/state", "@codemirror/view"],
    }),
  ],
};
```

- 文件 **index.html**

```html
<!doctype html>
<meta charset="utf8" />
<div id="editor"></div>

<script src="dist/codemirror-bundle.js"></script>
<script>
  const { EditorView, basicSetup, javascript } = cm;
  new EditorView({
    extensions: [basicSetup, javascript()],
    parent: document.getElementById("editor"),
  });
</script>
```


# CodeMirror v6 的核心設計理念

CodeMirror v6 的核心設計理念是「一切皆為擴展 (Everything is an extension)」。v6 的核心（@codemirror/state 與 @codemirror/view）只負責最基礎的數據和渲染，其餘所有功能（如行號、語法高亮、快捷鍵、主題）全部以擴展（Extensions）的形式注入。

## 官方核心擴展介紹 (Core Extensions)

官方將常用功能分散在不同的模組套件中，可以依需求自由組合：

界面與外觀 (@codemirror/view)
 - lineNumbers()：在編輯器左側添加行號邊欄。
 - highlightActiveLine()：高亮當前游標所在行的背景色。
 - EditorView.theme(spec)：定義自定義主題與 CSS 樣式。
 
文本操作與歷史 (@codemirror/commands)
 - history()：啟用復原 (Undo) 與 重做 (Redo) 的歷史記錄功能（通常搭配快捷鍵使用）。
 - 快捷鍵綁定 (keymap.of(Array))：將鍵盤操作（如 Ctrl-Z）對應到特定的編輯器命令（Commands）。
 
語言與語法高亮 (@codemirror/language 及各語言套件)
 - foldGutter()：在邊欄顯示代碼摺疊按鈕（如摺疊函式、大括號）。
 - syntaxHighlighting(highlighter)：啟用語法高亮引擎。
 - 語言包（如 @codemirror/lang-javascript）：提供特定語言的語法解析器（基於 Lezer Tree-sitter 概念）和代碼結構識別。
 
編輯輔助 (@codemirror/autocomplete & @codemirror/search)
 - autocompletion()：啟用代碼自動補全彈出視窗與提示。
 - search()：啟用內建的搜尋與取代功能面版（支援快捷鍵 Ctrl-F）。
 - closeBrackets()：自動補全成對的括號或引號（如輸入 ( 自動產生 )）。



## Markdown 实时预览

在 CodeMirror 中实现 Markdown 实时预览，核心逻辑是监听编辑器内容变化，然后将内容传递给 Markdown 解析器（如 marked 或 markdown-it）转化为 HTML，最后渲染到预览区域。

 - 安装 CodeMirror 模块

```js
npm install @codemirror/view 
npm install @codemirror/state @codemirror/lang-markdown 
npm install @codemirror/theme-one-dark 
npm install marked
```

- 更新文件 **main.js**

```js
import { EditorView, basicSetup } from "codemirror";
import { EditorState } from "@codemirror/state";
import { markdown } from "@codemirror/lang-markdown";
import { oneDark } from "@codemirror/theme-one-dark";
import { marked } from "marked";

export {EditorState, EditorView, basicSetup};
export {markdown, oneDark, marked};
```

- 文件 **index.html**

```html
<!doctype html>
<html>
  <head>
    <title>CodeMirror 6 IIFE Example</title>
  </head>
  <body>
    <div id="editor"></div>
    <div id="preview"></div>
    <script src="dist/codemirror-bundle.js"></script>
    <script>
      const { EditorState, EditorView, basicSetup } = cm;
      const { markdown, oneDark, marked } = cm;
      const previewEl = document.getElementById("preview");
      // 監聽器：當編輯器內容更新時觸發
      const updateListener = EditorView.updateListener.of((update) => {
        if (update.docChanged) {
          const docText = update.state.doc.toString();
          // 使用 marked 解析並渲染到預覽區
          previewEl.innerHTML = marked.parse(docText);
        }
      });
      // 初始化編輯器
      const view = new EditorView({
        state: EditorState.create({
          doc: "# 歡迎使用 Markdown 編輯器\n\n在這裡輸入內容...",
          extensions: [
            basicSetup,
            markdown(), // 啟用 Markdown 語法高亮
            oneDark, // 選擇性加入主題
            updateListener,
          ],
        }),
        parent: document.getElementById("editor"),
      });
      // 初始渲染一次預覽
      previewEl.innerHTML = marked.parse(view.state.doc.toString());
    </script>
  </body>
</html>
```