<template>
  <!-- 开发日志 -->
  <div class="MainVlog er">
    <div class="M_V" v-for="item in log " :key="item.id">
      <div class="V_L">
        <div class="L_Img"></div>
      </div>
      <div class="V_F">
        <div class="F_Title">
          <div class="T_a">
            <p><b>{{item.title}}</b></p>
          </div>
          <div class="T_b">
            <p>{{ item.date }}</p>
          </div>
        </div>
        <div class="F_Desc">
          <p>{{ item.desc }}</p>
        </div>
      </div>
    </div>

  </div>
</template>
<script>
export default {
    name:'MainVlog',
    data(){
      return{
        log:[
          {id:1,title:"开发1",date:"2024/2/3",desc:"优化代码框架，修改代码错误，添加模块框架代码"},
          {id:2,title:"开发2",date:"2024/1/3",desc:"优化代码框架，修改代码错误，添加模块框架代码"},
          {id:3,title:"开发3",date:"2024/5/3",desc:"优化代码框架，修改代码错误，添加模块框架代码"},
        ]
      }
    },
}
</script>

<style>
.MainVlog{
  width: 100%;
  height: 100%;
  /* background-color: aqua; */
  overflow: scroll;
}
.MainVlog .M_V{
  margin-top: 10px;
  margin-left: 2.5%;
  width: 95%;
  height: 150px;
  /* background-color: rgb(20, 26, 26); */
  display: flex;
}
.MainVlog .M_V .V_L{
  width: 10%;
  height: 100%;
  /* background-color: rgb(133, 133, 133); */
}
.MainVlog .M_V .V_F{
  width: 90%;
  height: 100%;
  /* background-color: rgba(172, 237, 50, 0.466); */
}
.MainVlog .M_V .V_F .F_Title{
  width: 100%;
  height: 25%;
  background-color: #ffffff;
}
.MainVlog .M_V .V_F .F_Title .T_a{
  width: 50%;
  height:100%;
  /* background-color: burlywood; */
  float: left;
}
.MainVlog .M_V .V_F .F_Title .T_a p,
.MainVlog .M_V .V_F .F_Title .T_b p
{
  width: 80%;
  height: 35px;
  /* background-color: cornsilk; */
  line-height: 35px;
}
.MainVlog .M_V .V_F .F_Title .T_b{
  width: 50%;
  height:100%;
  /* background-color: rgb(69, 62, 52); */
  float: right;
}
.MainVlog .M_V .V_F .F_Title .T_b p{
  color: red;
}
.MainVlog .M_V .V_F  .F_Desc{
  width: 100%;
  height: 75%;
  /* background-color: blue; */
}
</style>