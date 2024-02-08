# v1.0

>使用[联机许可证]

[联机许可证]:http://license.rosmontis.com

使用域名txt解析获取授权状态

使用wmi获取设备信息

# v1.1

>使用脱机临时许可证 ~~(暂时方案)~~


使用ntp在线授时校验脱机许可证有效性

# feature-v1.1-2way_auth  **分支版本**

>使用脱机临时许可证 ~~(暂时方案)~~

"*使用ntp在线授时校验脱机许可证有效性*"

使用RSA+AES混合加密保存脱机证书

|server||client|
|-|-|-|
|*RSA_Pu*|-->||
||<--|**RSA_Pu(** *AES* **)** + **AES(** *id* **)**
|**AES(** *id+license* **)**|-->||

# v1.2

更新GUI，可在GUI内完成授权配置

新增文件/文件夹链接

# v1.3

支持授权校验

# v1.4

规范文件格式

使用 [Fluent Design](https://github.com/zhiyiYo/PyQt-Fluent-Widgets) 设计

支持文件拖拽

支持自动搜索与自定义编译器

# v1.5(todo)

规范界面设计，更改多选项卡样式

使用双引擎，可选 `nutika` 和 `pyinstaller`

