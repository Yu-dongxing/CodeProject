<template>
    <div class="main-index">
        <div class="item" v-for="item in zyk" :key="item.id">
            <!-- v-for="item in 10" :key="item" -->
            <div class="item-img">
                <img src="@/assets/depng/png.svg" alt="depng">
            </div>
            <div class="item-right" >
                <div class="item-right-title">
                    <p>{{ item.name }}</p>
                </div>
                <div class="item-right-content">
                    <div class="content-time" title="创建时间">
                        <img ref="img" src="@/assets/time/time.svg"/>
                        <p>{{ item.createTime }}</p>
                    </div>
                    <div class="content-user" title="作者">
                        <img ref="img" src="@/assets/user/user.svg"/>
                        <p>{{ item.author }}</p>
                    </div>
                    <div class="content-tab" title="分类">
                        <img ref="img" src="@/assets/tab/tab.svg"/>
                        <p>{{ item.tab }}</p>
                    </div>
                </div>
                <div class="item-right-button">
                    <a class="button" :href="item.url" target="_blank">
                        <img src="@/assets/info/info.svg" alt="info">
                        查看
                    </a>
                </div>
            </div>
        </div>
    </div>
</template>
<script>
export default {
  name: 'MainIndex',
  data () {
    return {
      zyk: [
        { id: 1, name: '《移动应用设计开发（UI设计）》', url: 'https://www.yuque.com/tianfangyetan-3iytl/vs9n8l/wkr05l7ya6popqsl?singleDoc# 《移动应用设计开发（UI设计）》', createTime: '2024-12-21', author: 'Admin', tab: '文章' },
        { id: 2, name: '《移动应用开发（开发设计）》', url: 'https://www.yuque.com/tianfangyetan-3iytl/vs9n8l/min9mvv0lnh99xz1?singleDoc# 《移动应用开发（开发设计）》', createTime: '2024-12-22', author: 'Admin', tab: '文章' },
        { id: 3, name: 'Java 全栈知识体系', url: 'https://www.pdai.tech/md/java/basic/java-basic-oop.html', createTime: '2024-12-21', author: 'Admin', tab: '网站' },
        { id: 4, name: '《学习路线图》', url: 'https://www.yuque.com/tianfangyetan-3iytl/tyqp3d/wvqb03npyns8gpsn?singleDoc# 《学习路线图》', createTime: '2024-12-21', author: 'Admin', tab: '文章' },
        { id: 5, name: '《Git常用命令参考手册》', url: 'https://www.yuque.com/tianfangyetan-3iytl/gowu5g/readme?singleDoc# 《Git常用命令参考手册》', createTime: '2024-12-21', author: 'Admin', tab: '文章' },
        { id: 6, name: '《CSS 属性的速查列表》', url: 'https://www.yuque.com/tianfangyetan-3iytl/vs9n8l/alqinr2im2okntna?singleDoc# 《CSS 属性的速查列表》', createTime: '2024-12-21', author: 'Admin', tab: '文章' }
      ]
    }
  }
}
</script>

<style lang="less" scopd>
a {
    // 不需要下划线
    text-decoration: none;

}
.main-index {
    transition: all 3s ease;
    margin-top: 10px;
    box-sizing: border-box;
    padding: 10px;
    height: calc(100vh - 70px - 40px - 10px);
    width: 100%;
    background-color: var(--bg-100);
    // border: 1px solid #000000;
    overflow: auto;
    .item{
        margin-top: 15px;
        margin-bottom: 5px;
        margin-left: 2.5%;
        width: 95% ;
        height: auto;
        // background-color: var(--bg-100);
        background-image:
        -webkit-gradient(linear, left top, right top, from(var(--bg-100)), to(var(--bg-200))),
        linear-gradient(to right, var(--bg-100), var(--bg-200));
        border-radius: 10px;
        box-sizing: border-box;
        padding: 10px;
        display: flex;
        box-shadow: var(--box-shadow-de);
        .item-img{
            width: 100px;
            height: 100px;
            // background-color: var(--primary-100);
            border-radius: var(--border-radius-de);
            img{
                width: 100%;
                height: 100%;
            }
        }
        .item-right{
            flex: 1;
            margin-left: 10px;
            box-sizing: border-box;
            padding: 10px;
            .item-right-title{
                box-sizing: border-box;
                padding: 10px;
                padding-left: 0;
                border-bottom: 1px solid var(--primary-200);
                p{
                    min-width: 200px;
                    font-size: 18px;
                    font-weight: 600;
                    color: var(--text-100);
                    margin: 0;
                }
            }
            .item-right-content{
                display: flex;
                .content-time,.content-user,.content-tab{
                    display: flex;
                    align-items: center;
                    img{
                        width: 20px;
                        height: 20px;
                    }
                    p{
                        margin-left:0;
                        // margin: 10px;
                        font-size: 14px;
                        font-weight: 100;
                        color: rgb(92, 125, 171);
                    }
                }
                .content-user,.content-tab{
                    margin-left: 10px;
                }

            }
            .item-right-button{
                float: right;
                .button{
                    transition: all 0.3s ease;
                    width: 100px;
                    height: 30px;
                    border-radius: var(--border-radius-de);
                    background-color: #ffffff00;
                    border-bottom: 3px solid var(--primary-200);
                    border-top: 0px solid var(--primary-200);
                    border-left: 0px solid var(--primary-200);
                    border-right: 0px solid var(--primary-200);
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
@media screen and (max-width: 500px) {
  .item-img{
    display: none;
  }
}
</style>
