# amis-demo
amis与iframe之间的通信
amis父页面和iframe子页面为独立的页面，通过src连接，src指向flask后端的子页面的api

一：
amis给iframe发送数据：amis父页面发送格式： 
window.frames[0].postMessage(
            {
            },
        );
iframe子页面要设置监听器：
window.addEventListener('message', e => {
            // e.data 获取当前数据域数据，进行使用
        });
        
发送的数据可以是自定义的，也可以是amis form表单里的数据（包括后端发回来的数据）
可以通过 amisScoped.getComponentByName('page1.form1').getValues() 来获取到所有表单的值，需要注意 page 和 form 都需要有 name 属性
发送的数据只能是data和value的值
(也可以发送自定义数据到子页面，子页面验证后通过jquery与flask后端通信得到数据显示在子页面里)

二：
iframe给amis发送数据：iframe子页面发送格式：
window.parent.postMessage(
            {
            },
        );
amis父页面要设置监听器：
window.addEventListener('message', e => {
            // e.data 获取当前数据域数据，进行使用
        });

-----------------------------------------------------------
目前amis发送给iframe的数据暂时显示在了iframe子页面的script里，没有放到子页面的amis框架里，子页面主要是threejs的显示，所以显示在script里更方便threejs提取。

使用说明：
发送的为输入框里的value值，所以在输入框里输入后，可将value值发送到子页面，发送的其他信息通过 console.log()显示在控制台里，可通过开发者工具查看。
