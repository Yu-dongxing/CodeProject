<template>
    <!-- v-loading.fullscreen.lock="fullscreenLoading"   v-for="item in reversedItems" :key="item.id" @click="getData()"-->
    <div  v-loading.fullscreen.lock="isLoading"  element-loading-text="Loading...">
        <!-- <div >
            <Search_App/>
        </div> -->
        <!-- <div class="devOrpro">
            <el-switch v-model="isDev" />
        </div> -->
        <!-- 自己设计的卡片布局 -->
        <div class="main-index" v-if="isDev">
            <div class="item" v-for="item in reversedItems" :key="item.id">
                <div class="item-img">
                    <div class="iimg">
                        <el-image :src="item.img" fit="cover" />
                    </div>
                    <!-- <img :src="item.img" alt="depng"> -->
                    
                </div>
                <div class="item-right" >
                    <div class="item-right-title">
                        <!-- <p><el-text size="large" truncated>{{ item.name }}</el-text></p> -->
                        <p>{{ item.name }}</p>
                        <!-- <el-text size="large" truncated>{{ item.name }}</el-text> -->
                    </div>
                    <div class="contion-tags">
                            <el-tag>
                                <img ref="img" src="@/assets/time/time.svg"  />
                                {{ item.updateTime }} | 
                                <img ref="img" src="@/assets/user/user.svg"/>
                                {{ item.author }} | 
                                <img ref="img" src="@/assets/tab/tab.svg"/>
                                {{ item.tab }}</el-tag> 
                    </div>
                    <div class="item-right-button">
                        <!-- <a class="button" :href="item.url" target="_blank">
                            <img src="@/assets/info/info.svg" alt="info">
                            查看
                        </a> -->

                        <el-button class="button"  @click="goDetail(item.id)"><img src="@/assets/info/info.svg" alt="info">查看</el-button>
                    </div>
                </div>
            </div>
        </div>
        <!-- el框架的卡片布局 -->
        <div class="main-index"  v-if="!isDev">
            <el-card shadow="always"  class="card"  v-for="item in reversedItems" :key="item.id">
                <div class="card-lift">
                    <el-image :src="item.img" alt="" class="lift-img"></el-image>
                </div>
                <div class="card-right">
                    <div class="right-contion">
                        <div class="contion-title">
                            <span class="text">{{ item.name }}</span>
                        </div>
                        <div class="contion-tags">
                            <el-tag>
                                <img ref="img" src="@/assets/time/time.svg"  />
                                {{ item.updateTime }} | 
                                <img ref="img" src="@/assets/user/user.svg"/>
                                {{ item.author }} | 
                                <img ref="img" src="@/assets/tab/tab.svg"/>
                                {{ item.tab }}</el-tag> 
                        </div>
                    </div>
                </div>
                <template #footer>
                    <div class="card-button">
                            <el-link class="bu" :underline="false" :href="item.url" target="_blank">
                                <span><img src="@/assets/info/info.svg" alt="info"></span>
                                <span>查看</span>
                            </el-link>
                            <!-- <el-button type="primary" @click="goDetail(item.id)">查看</el-button> -->
                        
                    </div>
                </template>
            </el-card>
        </div>
    </div>
</template>
<script>
import { resourceApi } from '@/api/resource'
import Search_App from '@/components/Search_App/index.vue'
export default {
  name: 'MainIndex',
  components: {
    Search_App
  },
  data () {
    return {
        isDev:true,
        isLoading: true,
        tme:null,
        zyk: [],
    }
  },
  methods: {
    async getData() {
      try {
        this.isLoading = true
        const res = await resourceApi.getResources()
        this.zyk = res.data
      } catch (error) {
        console.error('获取资源列表失败:', error)
      } finally {
        this.isLoading = false
      }
    },
    setisloading(){ // 设置isLoading状态
        this.isLoading = !this.isLoading; // 切换isLoading状态
        this.zyk.p // 访问zyk数组的p属性（注意：这里可能存在错误，因为zyk是一个数组，没有p属性）
    },
    // 资源详情跳转
    goDetail(id) {
        this.$router.push({ path: '/detail', query:  { id: id } }) // 跳转到资源详情页面，并传递资源ID参数
    },
  },
  computed: {
    //通过计算属性实现倒序
    reversedItems() {
    //   return this.zyk.slice().reverse(); // 返回zyk数组的倒序副本
      return this.zyk; // 返回zyk数组的倒序副本
    }
  },
  mounted () {
      this.getData(); // 组件挂载完成后，调用getData方法获取数据
  },
}
</script>

<style lang="less" scopd>
a {
    // 不需要下划线
    text-decoration: none; // 移除链接的下划线装饰

}
.main-index {
    transition: all 3s ease; /* 设置所有属性的过渡效果，持续时间为3秒，使用ease缓动函数 */
    margin-top: 4px; /* 设置顶部外边距为4px */
    box-sizing: border-box; /* 设置盒模型为border-box，即宽度和高度包含边框和内边距 */
    padding: 5px; /* 设置内边距为5px */
    width: 100%; /* 设置宽度为100% */
    background-color: var(--bg-100); /* 设置背景颜色，使用CSS变量--bg-100 */
    display: grid; /* 设置为网格布局 */
    gap: 10px; /* 使用 gap 替代 grid-gap */
    grid-template-columns: repeat(auto-fill, minmax(464px, 1fr)); /* 定义网格布局的列，使用 repeat 函数自动填充，每列的最小宽度为 500px，最大宽度为 1fr（剩余空间的一份） */
    grid-template-rows: repeat(auto-fill, minmax(100px, 1fr)); /* 定义网格布局的行，使用 repeat 函数自动填充，每行的最小高度为 100px，最大高度为 1fr
    （剩余空间的一份） */
    // aspect-ratio: 4 / 3;
    .el-card__body{
        padding: 10px;
        display: flex;
    }
    // el自定义卡片布局
    .card{
        height: auto;
        min-height: 100px;
        .card-lift{
            // border: 0.1px solid #000000;
            .lift-img{
                // aspect-ratio: 6/5;
                width: 100px;
                height: 100px;
                border-radius: 25px;
                margin-right: 5px;
            }
        }
        .card-right{
            // border: 0.1px solid #000000;
            width: 100%;
            .right-contion{
                .contion-title{
                    margin-bottom: 10px;
                    .text{
                        font-size: 18px;
                        font-weight: bold;
                    }
                }
                .contion-tags{
                    .el-tag__content{
                        display: flex;
                        align-items: center; /* 垂直居中 */
                        img{
                            width: 15px;
                            height: 15px;
                        }
                    }
                }
            }
        }
        .card-button{
            display: flex;
            align-items: center;
            justify-content: flex-end;
            .el-link__inner {
                display: inline-flex;
                justify-content: center;
                align-items: stretch;

            }
            .bu{
                float:right;
                transition: all 0.3s ease;
                width: 100px;
                height: 30px;
                border-radius: var(--border-radius-de);
                border: 1.5px solid var(--primary-200); /* 简化 border */
                background-color: transparent;
                color: var(--text-100);
                font-size: 14px;
                font-weight: 600;
                display: flex;
                align-items: center;
                justify-content: center;
                img{
                    width: 20px;
                    height: 20px;
                    margin-right: 5px;
                }
            }
        }
    }
    // 自定义卡片布局
    .item{
        // margin: 15px 0 5px 0; /* 合并 margin */
        width: 100%; 
        height: auto; /* 设置元素的高度为自动，根据内容调整高度 */
        border-radius: 15px; /* 设置元素的边框圆角为10像素 */
        box-sizing: border-box;
        padding: 5px; /* 设置元素的内边距为5像素 */
        display: flex; /* 设置元素的显示方式为flex，启用Flexbox布局 */
        box-shadow: var(--box-shadow-de); /* 设置元素的阴影效果，使用CSS变量--box-shadow-de定义的阴影样式 */
        background-image: linear-gradient(to right, var(--bg-100), var(--bg-200));
        .item-img {
            
            // border-radius: var(--border-radius-de);
            // border-radius: 25px;
            margin-right: 5px;
            .iimg{
                display: flex;
                align-items: center;
                justify-content: center;
                width: 60px;
                height: 60px;
                img {
                width: 100%;
                height: 100%;
                object-fit: cover; /* 确保图片填充 */
                border-radius: 15px;
                }
            }
        }
        .item-right{
            flex: 1;
            margin-left: 10px;
            box-sizing: border-box;
            .item-right-title{
                padding: 10px;
                padding-left: 0;
                p{
                    min-width: 200px;
                    font-size: 18px;
                    font-weight: bold;
                    color: var(--text-100);
                    margin: 0;
                }
            } 
            .contion-tags{
                    .el-tag__content{
                        display: flex;
                        align-items: center; /* 垂直居中 */
                        img{
                            width: 15px;
                            height: 15px;
                        }
                    }
                }
            .item-right-button{
                float: right;
                .button{
                    transition: all 0.3s ease;
                    width: 100px;
                    height: 30px;
                    border-radius: var(--border-radius-de);
                    border: 1.5px solid var(--primary-200); /* 简化 border */
                    background-color: transparent;
                    color: var(--text-100);
                    font-size: 14px;
                    font-weight: 600;
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    img{
                        width: 20px;
                        height: 20px;
                        margin-right: 5px;
                    }
                }
                .button:hover{
                    background-color: var(--primary-100);
                    color: var(--text-200);
                }
            }
        }
    }
}
/* 当屏幕宽度小于500px */
@media screen and (max-width: 600px) {
  .item-img,.card-lift{
    display: none;
  }
  .main-index{
    grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  }
}
.devOrpro{
    position: absolute;
    right: 10px;
    background-color: var(--bg-100);
}
</style>
