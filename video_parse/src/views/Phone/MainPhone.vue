<template>
    <!-- 联系 -->
  <div class="MainPhone">
    <div class="P_L">
      <div class="L_M">
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
                </div>
              </div>
            </div>
        </div>
        <div class="M_F"></div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
    name:'MainPhone',
}
</script>

<style lang="less" scoped>
.MainPhone{
  --desc-img-name:rgba(255, 255, 255, 0.075);
  
  width: 100%;
  height: 100%;
  /* background-color: aqua; */
  .P_L{
    margin-top: 10px;
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
          display: flex;
          justify-content: center;
          align-items: center;
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
  animation-duration: 3s;
  animation-name: color;
  animation-iteration-count: infinite;
  animation-direction: alternate;
}
p{
  
}
</style>