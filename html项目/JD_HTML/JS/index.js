

moves();
setInterval(time_h_s_m,1);


function SetClass(){
    var CLA = document.getElementById("My_JD");
    CLA.style.display="block";
    console.log(CLA);
}
function moves(){
    // 获取特定id和class的元素
    const elementWithId = document.getElementById("My_jd");
    if (elementWithId) {
      elementWithId.addEventListener('mouseenter', function(event) {
        SetClass();
         console.log('Mouse entered an element with id:', this.id);
      });
    }
  }

  function time_h_s_m(){
    var myDate = new Date();
    //获取当前小时数(0-23)
    //获取当前分钟数(0-59)
    //获取当前秒数(0-59)
    document.getElementById("houer").innerText=myDate.getHours().toString().padStart(2, '0');
    document.getElementById("minute").innerText=myDate.getMinutes().toString().padStart(2, '0');
    document.getElementById("second").innerText=myDate.getSeconds().toString().padStart(2, '0');
  }

