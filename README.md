框架简介
---
  	框架组成：Python + SeleniumLibrary + Robotframework
  	框架说明：使用的Robotframework框架，该框架有丰富的测试工具三方库，例如我们此次使用的SeleniumLibrary就是在selenium的基础上做了封装，当然我们还是需要对其做一些自定义的修改，Robotframework可以自动生成日志、Fail页面截图、自动生成报告、还有suite和test级别的setup和teardown等等，基本上你可以想到的一个测试框架应该具备的需求，他都已经支持了，只需要我们来逐步的把这些功能找出来使用就可以了，同时还支持使用中文定义关键名称，用例我们完全可以使用中文来进行编写了，使测试用例一目了然。
    被测对象是在tools下面的learning_log,这个web系统是我们自定义的网站，如果想运行已经编写好的测试用例或者还想再自己编写一下用例练习的话，请解压后执行“RunLearningLog.bat”，使该web系统在本地启动，这样就可以使用这个项目下的测试用例了。


环境依赖
---
    Chrome和chromedriver的版本只要对应好就行了
  	Python 3.7.3
   	Chrome 53.0
   	chromedriver

目录结构描述
---
  	├── lib                      
  	│    ├── CommonLib.py        // 使用python编写的公共关键字库，存放与Selenium事务性操作无关的关键字
  	│    ├── SeleniumLib.py        // 使用python编写的Selenium事务性关键字，继承自SeleniumLibrary，对其原有的关键字做自定义修改，并将关键字名指定为中文
  	│    └── SysLib.py        // 使用python编写的工具类函数，不直接作为关键字使用，函数主要用于数据处理
  	├── log        // 放置生成的测试报告、日志、截图
  	├── resources                    
  	│    └── SeleniumResources.txt        // 对已有的Selenium事务性操作进行再封装，例如：将点击和检查，放到一起封装为“点击并检查页面跳转”
  	├── suite                      
  	│    ├── _config        // 配置文件放置的地址，使用“_”为开头是为了使用RIDE打开时，不显示该目录
  	│    ├── ProjectResources       // 测试对象业务步骤关键存放的目录，使用txt编写
  	│    └── TestCases        // 测试用例存放的目录，使用txt编写测试用例
  	├── tools                      
  	│    └── learning_log.zip        // web系统文件，需要解压后再点击“RunLearningLog.bat”来在本地启动
  	├── tools                      
  	│    ├── HTMLTestRunner.py        // html测试报告生成，支持用例失败重试，错误用例截图
  	│    ├── CreatePY.py        // python脚本生成，读取Excel中的测试用例生成py测试文件
  	│    └── AllTestRun.py        // 批量执行
  	├── varibles                      
  	│    └── locator.py        // 被测系统的locator统一存放在此文件
  	└── Readme.md        // help

执行参数说明
---
    -P C:\workspaces\SeleniumTest -V C:\workspaces\SeleniumTest\suite\_config\config.py  -d C:\workspaces\SeleniumTest\log 
    -P C:\workspaces\SeleniumTest：将-P后的路径临时加入path变量中，指定项目文件所在目录
    -V C:\workspaces\SeleniumTest\suite\_config\config.py：指定config文件所在目录
    -d C:\workspaces\SeleniumTest\log：指定输出文件的路径包括：日志、报告
    --extension txt:robot：使用测试文件可以使用txt格式
  
