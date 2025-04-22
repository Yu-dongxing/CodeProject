<template>
    <!-- v-loading.fullscreen.lock="fullscreenLoading"   v-for="item in reversedItems" :key="item.id" @click="getData()"-->
    <div  v-loading.fullscreen.lock="isLoading"  element-loading-text="Loading...">
        
        <!-- 自己设计的卡片布局 -->
        <div class="main-index" v-if="isDev">
            <div class="item main-index-hover" v-for="item in reversedItems" :key="item.id" @click="goDetail(item.id)">
                <div class="item-img">
                    <div class="iimg">
                        <el-image :src="item.img" fit="cover" />
                    </div>
                </div>
                <div class="item-right" >
                    <div class="item-right-title">
                        <p>{{ item.name }}</p>
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
                        <el-button class="button"  @click="goDetail(item.id)"><img src="@/assets/info/info.svg" alt="info">查看</el-button>
                    </div>
                </div>
            </div>
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
    },
    // 资源详情跳转
    goDetail(id) {
        this.$router.push({ path: '/detail', query:  { id: id } }) // 跳转到资源详情页面，并传递资源ID参数
    },
  },
  computed: {
    //通过计算属性实现倒序
    reversedItems() {
      return this.zyk; 
    }
  },
  mounted () {
      this.getData(); 
  },
}
</script>

<style lang="less" scopd>
a {
    // 不需要下划线
    text-decoration: none; // 移除链接的下划线装饰

}
.main-index-hover{
    transition: all 0.3s ease; /* 设置所有属性的过渡效果，持续时间为0.3秒，使用ease缓动函数 */
    border: 1px solid #0051ff00;
    &:hover {
        //指针
        cursor: pointer;
        // transform: scale(1.01); /* 鼠标悬停时，元素放大1.05倍 */
        border: 1px solid #0051ff;
    }
}
.main-index {
    transition: all 3s ease; 
    margin-top: 4px; 
    box-sizing: border-box; 
    padding: 5px; 
    width: 100%; 
    background-color: var(--bg-100); 
    display: grid; 
    gap: 10px; 
    grid-template-columns: repeat(auto-fill, minmax(464px, 1fr)); 
    grid-template-rows: repeat(auto-fill, minmax(100px, 1fr)); 
    .el-card__body{
        padding: 10px;
        display: flex;
    }
    .item{
        width: 100%; 
        height: auto; 
        border-radius: 15px; 
        box-sizing: border-box;
        padding: 5px; 
        display: flex; 
        box-shadow: var(--box-shadow-de);
        background-image: linear-gradient(to right, var(--bg-100), var(--bg-200));
        .item-img {
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
                display: none;
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
