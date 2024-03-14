

moves();


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