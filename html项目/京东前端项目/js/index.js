//实现模糊查询
var keyword = document.querySelector('.keyword'); //获取输入框
var searchhelper = document.querySelector('.search-helper');

//定义数组，搜索内容
var searchArr = ['小米手机', '华为手机', '苹果手机', '小米电视', '小米平板', '苹果12', '苹果书包'];

//给输入框绑定内容改变事件
keyword.oninput = function() {

   searchhelper.innerHTML = ''; // 清空之前的查询结果
   searchhelper.style.display = 'none'; // 先将查询结果隐藏

   for (let i = 0; i < searchArr.length; i++) {

       if (searchArr[i].indexOf(keyword.value) != -1) {
           searchhelper.innerHTML += '<p>' + searchArr[i] + '</p>';
           searchhelper.style.display = 'block';
       }
   }
};


