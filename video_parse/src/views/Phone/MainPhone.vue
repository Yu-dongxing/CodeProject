<template>
    <!-- 联系模块 -->
  <div class="MainPhone">
    <div class="P_L">
      <!-- 子模块 -->
      <div class="L_M M_backgroud_img">
        <div class="M_H">
          <div class="H_A close"></div>
          <div class="H_B"></div>
          <div class="H_C"></div>
        </div>
        <div class="M_B">
          <div class="B_A">
              <div class="A_I"></div>
              <div class="A_N">
                <div class="N_P">
                  <p>YUXS</p>
                </div>
              </div>
              <div class="A_D">
                <div class="D_P">
                  <p>000100110111001101000101101011010110101</p>
                  <p>100110110101010110111000101010101101101</p>
                  <p>100110111111010111101111011101010101110</p>
                  <p>001001111101110001010100111001011010111</p>
                  <p>100110001000100111101101011101000101001</p>
                  <p>100010000010000000101010101000101010011</p>
                  <p>111011111100001111010101001011001101001</p>
                  <p>100111011010100110111101110100101010010</p>
                  <router-link :to="{path:'/MainPhone/CwXt'}"  @click="changeDisplay()" >
                      <span>财务系统</span>
                  </router-link>
                </div>
              </div>
            </div>
        </div>
        <div class="M_F"></div>
      </div>
    </div>
    <router-view></router-view>
  </div>
</template>

<script>
export default {
    name:'MainPhone',
    methods:{
      changeDisplay() {
        // 使用querySelector选择第一个具有指定类名的元素
        var element = document.querySelector(".P_L");
        if (element) {
          // 修改元素的display属性
          element.style.display = "none";
        } else {
          console.log('没有找到指定类名的元素');
        }
      }
    }
}
</script>

<style lang="less" >
.M_backgroud_img{
        background:url("/public/backgroundimg/20240426im6d2d.webp");
        background-repeat: no-repeat;  /* 不重复背景图像 */  
        background-size: cover;        /* 使背景图像覆盖整个元素 */  
        background-position: center;   /* 将背景图像居中放置 */ 
    }
.MainPhone{
  --desc-img-name:rgba(255, 255, 255, 0.075);
  
  width: 100%;
  height: 100%;
  display: flex;
  justify-content: center;
  margin-top:10px;
  /* background-color: aqua; */
  .P_L{
    margin-top: 10px;
    display: block;
    // text-align: -webkit-center;
    
    .L_M{
      width: 500px;
      height: 450px;
      background-color: #1e4155;
      box-shadow: 0px 0px 15px 5px #1e4155;
      align-content: center;
      .M_H,.M_B,.M_F{
        width: 500px;
      }
      .M_H{
        display: flex;
        justify-content: space-around;
        align-items: center;
        height: 30px;
        width: 100px;
        background-color: #2a4d62;
        .H_A,.H_B,.H_C{
          width: 20px;
          height: 20px;
        }
        .H_A{
          background-color: rgb(255, 136, 0);
        }
        .H_B{
          background-color: rgb(238, 255, 0);
          
        }
        .H_C{
          background-color: rgb(0, 255, 26);
        }
      }
      .M_B{
        height: 370px;
        .B_A{
          // 设置弹性布局
          display: flex;
          // 水平居中
          justify-content: center;
          // 垂直居中
          align-items: center;
          // 垂直排列
          flex-direction: column;
            .A_I{
              width: 100px;
              height: 100px;
              background-color: var(--desc-img-name);
              border: 1px solid #ffffff;
              box-shadow: 0px 0px 10px 1px #ffffff;
            }
            .A_N{
              margin-top: 10px;
              height: 50px;
              width: 500px;
              // background-color: var(--desc-img-name);
              .N_P{
                p{
                  color: aliceblue;
                  font-size: 40px;
                  line-height: 50px;
                  width: 115px;
                  margin: 0 auto;
                }
              }
            }
            .A_D{
              margin-top: 10px;
              width: 500px;
              height: 200px;
              // background-color: var(--desc-img-name);    
              .D_P{
                padding: 5px;
                p{
                  width: 500px;
                  // unicode-bidi:embed;
                  color:rgb(86, 250, 80);
                  font-size: 20px;
                  // p标签换行
                  word-break: break-all;
                }
              }     
            }
          }
      }
      .M_F{
        height: 50px;
      }
    }
  }
}
@keyframes color {
  from{
    background-color: red;
  }
  to{
    background-color: rgb(89, 255, 0);
  }
}
.ccpp,.H_A{
    /* 设置动画持续时间为3秒 */
    animation-duration: 3s;
    /* 设置动画名称为color */
    animation-name: color;
    /* 设置动画循环次数为无限次 */
    animation-iteration-count: infinite;
    /* 设置动画方向为交替 */
    animation-direction: alternate;
}
p{
  
}
</style>