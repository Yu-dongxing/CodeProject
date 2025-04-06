// 链接跳转函数
function openNewTab(url, istrue = false) {
    window.open(url, istrue ? '_blank' : '_self');
}
