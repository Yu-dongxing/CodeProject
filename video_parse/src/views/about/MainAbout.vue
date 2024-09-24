<template>
  <!-- 关于模块 -->
  <div class="About radius">
    <!-- 关于模块中的内容模块 -->
    <div class="about_L radius">
      <div class="L_a radius er">
        <div class="box blur_color radius" v-for="(item) in zh_xw " :key="item.id">
          <!-- 文章列表 -->
          <div class="her">
            <!-- 文章主题 -->
            <div class="her_p">
              <p class="text-ellipsis-2 ">{{ item.title }}</p>
            </div>
            <!-- 文章图片 -->
            <div class="her_img ">
              <img class="radius" :src="item.pic" :alt="item.id">
            </div>
          </div>
          <div class="desc radius">
            <!-- 列表文章 -->
            <div class="d_m">
              <div class="m_p">
                <p>{{ item.desc }}</p>
              </div>
            </div>
            <!-- 列表点击模块 -->
            <div class="d_f">
              <div class="f_a transition_color_bkcolor">
                <img src="../../../public/anxin.svg" alt="">
                <span>点赞</span>
              </div>
              <div class="f_b transition_color_bkcolor">
                <img src="../../../public/anxin.svg" alt="">
                <span>喜欢</span>
              </div>
              <div class="f_c transition_color_bkcolor aw">
                <img src="../../../public/anxin.svg" alt="">
                <span>收藏</span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <!-- 关于模块中的用户模块 -->
    <div class="about_R ">
      <!-- 用户个人信息模块 -->
      <div class="R_a">
        <!-- 用户头像和id模块 -->
        <div class="a_a">
          <div class="a_img">
            <img class="radius transition_color_bkcolor" :src="User.Tx_url" :alt="User.id">
            <p class="p_w_text-indent">UID: 
              <span style="color: #ff0000;">{{ User.id }}</span>
            </p>
          </div>
          <!-- 用户名称模块 -->
          <div class="a_Name">
            <p class="a_Name_p p_w_text-indent">欢迎"<span style="color: #ff0000;">{{ User.name }}</span>"的到来 !!!</p>
          </div>
          <div class="a_Bu ">
            <div class="Bu_a transition_color_bkcolor">
              <p class="transition_color_bkcolor">写文章</p>
            </div>
            <div class="Bu_b transition_color_bkcolor">
              <p class="transition_color_bkcolor">写文章</p>
            </div>
            <div class="Bu_c transition_color_bkcolor">
              <p class="transition_color_bkcolor">写文章</p>
            </div>
          </div>
        </div>
        <div class="a_b">
        </div>
      </div>
      <div class="R_b">
        <p style="color: #ffffff;">内容占用框</p>
      </div>
      <div class="R_c">
        <p style="color: #ffffff;">内容占用框</p>
      </div>
      <!-- <div class="R_d"></div> -->
    </div>
  </div>
</template>

<script>
import axios from 'axios';
export default {
    name:'MainAbout',
    data(){
        return{
          texxt:[
            {
              id:1,
              title:'【推动高质量发展系列主题新闻发布会'  ,
              desc:"6月4日，嫦娥六号完成月背“挖土”，携带的由玄武岩纤维制成的“石头版”五星红旗，在月球背面成功展开。阳光照射下，五星红旗光彩夺目，闪耀着鲜艳的中国红。"
            },
            {id:2,title:'测试2'      ,desc:"央视网消息（新闻联播）：国务院新闻办公室6月6日举行“推动高质量发展”系列主题新闻发布会，陕西省有关负责人介绍了相关情况。" },
            {id:3,title:'测试3'      ,desc:"十年来，陕西省地区生产总值年均增长6.4%，去年达到3.38万亿元，连续跨越两个万亿元台阶。培育形成航空工业、集成电路、先进结构材料3个国家级产业集群，光伏电池转换效率屡破世界纪录，超导、特高压输电、新型显示等领域技术达到国际先进水平，钛加工产业规模、重卡变速器产量全球第一，创新驱动发展驶入快车道。" },
            {id:4,title:'男生保送北大物理“卓越计划”，来考了唯一一门语文！“挑战我最弱的语文”'      ,desc:"潮新闻讯  如果把高考看作一场比赛，提前“上岸”的保送生，就是“神”一样的存在。每年高考，杭州第二中学（滨江校区）考点门口，由保送生组成的“学霸助考天团”，总能引来家长和同学们的羡慕惊叹。保送生来给同学送考加油，已经成为杭二中的传统，这是好运的加持，也是拼搏的传承。" },
            {id:5,title:'外交部：中吉乌铁路项目彰显三国谋合作、促发展的共同心愿'      ,desc:"新华社北京6月7日电（记者冯歆然）中国－吉尔吉斯斯坦－乌兹别克斯坦铁路项目三国政府间协定签字仪式6日在北京举行。外交部发言人毛宁7日在例行记者会上答问时表示，中吉乌铁路项目彰显了三国谋合作、促发展的共同心愿。中方期待同各方紧密合作，齐心协力，早日建成这条符合地区人民共同利益的发展之路、友谊之路和幸福之路。毛宁说，1996年，乌兹别克斯坦第一个提出中国－吉尔吉斯斯坦－乌兹别克斯坦铁路的设想。在近30年时间内，三国就项目举行了很多轮磋商和谈判，充分、深入沟通工作思路。去年5月，中吉乌铁路项目可研基本完成，项目推进工作驶入快车道。短短一年时间内，三方通力协作、加紧商谈，在有关重大问题上不断缩小分歧、累积共识，最终于6日签署了中吉乌铁路三国政府间协定。" },
            {id:6,title:'中国海警局新闻发言人就日方炒作我钓鱼岛维权巡航发表谈话'      ,desc:"中国海警局新闻发言人甘羽表示，6月7日，中国海警2501编队在我钓鱼岛领海内依法开展维权巡航活动，这是我维护国家主权、安全和海洋权益的例行性行动，是我维护地区和平稳定、反制日方近期一系列消极举动的必要举措。钓鱼岛及其附属岛屿是中国固有领土，我们奉劝日方谨言慎行、反躬自省、停止挑衅，中国海警将依法加强在中国管辖海域的巡航执法力度，坚决挫败一切侵权挑衅图谋。来源：中国海警局网站" },
          ],
          zh_xw:[
            {id:1,title:'加载中！！！'  ,desc:"加载中！！！" ,pic:"https://ts1.cn.mm.bing.net/th/id/R-C.91f8e62c0ed7b5deeb4cbc7b6874e57b?rik=RjFU3f6mxkcyaw&riu=http%3a%2f%2fimg95.699pic.com%2fphoto%2f40168%2f4380.jpg_wh860.jpg&ehk=cN0vXYFpp1JOnXYGYAE6oGd0%2fj06SIjQodY0HfgzaVo%3d&risl=&pid=ImgRaw&r=0" },
          ],
          User:{
            id:10023,
            name:'admin_yuxs',
            Tx_url:'https://ts1.cn.mm.bing.net/th/id/R-C.fd81516a06ce33c15b194494272fa6e9?rik=XAfnJ6A9NFvAyA&riu=http%3a%2f%2fimg.touxiangwu.com%2fuploads%2fallimg%2f2022053117%2fivhiashhpu1.jpg&ehk=Yi2aDhWvd0rnBKl1xloJy8F1RfGd8%2bcC75k4ff8dVXk%3d&risl=&pid=ImgRaw&r=0',

          }
        }
    },
    methods:{
      async  zhxw() { 
            // if(!id){
            //     id=1;
            // } 
            try {  
                const response = await axios.get(  
                    'https://api.pearktrue.cn/api/social/hotlist.php?type=%E7%9F%A5%E4%B9%8E',  
                ); 
                if (Array.isArray(response.data.data)) {    
                        this.zh_xw = []; // 初始化this.video 数组    
                        response.data.data.forEach(item => {    
                            this.zh_xw.push(
                                { 
                                    id: item.index  , 
                                    title: item.title ,
                                    desc:item.desc,
                                    pic:item.pic
                                });    
                        });
                        console.log(this.zh_xw);
                        } else {  
                        console.error('data is not an array');  
                    }   
            } catch (error) {  
                console.error(error);  
            }  
        },
    },
    // updated(){
    // this.zhxw();
    // },
    beforeMount(){
      this.zhxw();
    },
    // mounted() {  
    //   this.zhxw();
    // },
}
</script>

<style>
.About{
  width: 100%;
  height: 100%; 
  display: flex;
  position: relative;
  /* background-color: aqua; */

}
.About .about_L{
  width: 80%;
  height: 100%;
  /* background-color: aqua; */
  margin-right: 5px;
}
.About .about_L .L_a{
  width: 95%;
  height: 100%;
  margin-left: 2.5%;
  /* background-color: rgb(134, 194, 31); */
  overflow: scroll;
}
.About .about_L .L_a .box{
  width: 90%;
  height: 170px;
  margin-left: 5%;
  /* background-color: black; */
  margin-top: 10px;
  margin-bottom: 10px;
  display:flex;

}
.About .about_L .L_a .box .her{
    display: flex;
    flex-direction: column;
    padding: 5px;
    align-items: center;
    width: 200px;
}
.About .about_L .L_a .box  .desc{
  width: 100%;
  height: 170px;
  /* background-color: rgba(168, 254, 236, 0.747); */
  /* transition: width .2s ease; */

}
.About .about_L .L_a .box  .desc .d_m{
  width: 100%;
  height: 100px;
  margin-top: 20px;
}
.About .about_L .L_a .box  .desc .d_m .m_p{
  padding: 5px;
  overflow: hidden;
  -webkit-line-clamp: 4;
  text-overflow: ellipsis;
  display: -webkit-box;
  -webkit-box-orient: vertical;
  height: 80px;
}
.About .about_L .L_a .box  .desc .d_f{
  display: flex;
  justify-content: space-between;
  align-items: center;
  height: 50px;
}
.About .about_L .L_a .box  .desc .d_f .f_a,
.About .about_L .L_a .box  .desc .d_f .f_b,
.About .about_L .L_a .box  .desc .d_f .f_c{
  width: 100px;
  height: 35px;
  background-color: rgb(255, 255, 255);
  margin-left: 5px;
  margin-right: 5px;
  display: flex;
  align-items: center;
  justify-content: center;
}
.About .about_L .L_a .box  .desc .d_f .f_a:hover,
.About .about_L .L_a .box  .desc .d_f .f_b:hover,
.About .about_L .L_a .box  .desc .d_f .f_c:hover{
  background-color: rgb(255, 0, 0);
  cursor: pointer;
}
.aw:active{
  background-color: black;
}
.About .about_L .L_a .box  .desc .d_f .f_a img,
.About .about_L .L_a .box  .desc .d_f .f_b img,
.About .about_L .L_a .box  .desc .d_f .f_c img{
  width: 20px;
  height: 20px;
  margin-left: 5px;
  margin-right: 5px;
}
.About .about_L .L_a .box  .desc .d_f .f_a{}
.About .about_L .L_a .box  .desc .d_f .f_b{}
.About .about_L .L_a .box  .desc .d_f .f_c{}
/* .About .about_L .L_a .box  .desc:hover{
  width: 180px;
} */
.About .about_L .L_a .box .her .her_p{
  width: 135px;
}
.About .about_L .L_a .box .her .her_p p{
  /* color: #000000d6; */
  font-weight: bolder;
}
.About .about_L .L_a .box .her .her_img img{
    width: 135px;
    height: 120px;
    transition: width .2s ease,height .2s ease;
}
.About .about_L .L_a .box .her .her_img img:hover{
    width: 138px;
    height: 123px;

}

.About .about_R{
  /* position: relative; */
  float:right;
  width: 20%;
  height: 100%;
  /* background-color: rgb(173, 255, 255); */
  
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}
.About .about_R .R_a,
.About .about_R .R_b,
.About .about_R .R_c,
.About .about_R .R_d{
    width: 100%;
    height: 24%;
    /* background-color: black; */
    /* margin-top: 6px; */
    /* margin-bottom: 6px; */
}

.About .about_R .R_a{
  height: 50%;
}
.About .about_R .R_a .a_a{
  margin-top:10px;
  width: 100%;
  height: auto;
  background-color: rgb(255, 255, 255);
}
.About .about_R .R_a .a_a .a_img{
  width: 100%;
  height: 110px;
  /* background-color: rgba(170, 255, 113, 0.452); */
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
  color: #1900ff;
}
.About .about_R .R_a .a_a .a_img img{
  width: 80px;
  height: 80px;
  border: 2px solid #ffffff;
  margin-top: 5px;
}
.About .about_R .R_a .a_a .a_img img:hover{
  border: 2px solid #ff0000;
  box-shadow:1px 1px 3px 1px #ff0000;
}
.About .about_R .R_a .a_a .a_Name{
  width: 100%;
  height: auto;
  /* overflow: hidden; */
}
.About .about_R .R_a .a_a .a_Name p{
  text-align: center;
  font-size: 25px;
  color: #026a97;
  height: auto;
  width: 100%;
}
.About .about_R .R_a .a_a .a_Bu{
  width: 100%;
  height: 80px;
  background-color: #72efff;
  /* display: flex; */
  display: none;
  justify-content: center;
  /* justify-content: space-between; */
  align-items: center;
  
}
.About .about_R .R_a .a_a .a_Bu .Bu_a,
.About .about_R .R_a .a_a .a_Bu .Bu_b,
.About .about_R .R_a .a_a .a_Bu .Bu_c{
  width: 100px;
  height: 50px;
  background-color: #9dff4d9e;
  margin-left: 5px;
  margin-right: 5px;
}
.About .about_R .R_a .a_a .a_Bu .Bu_a:hover,
.About .about_R .R_a .a_a .a_Bu .Bu_b:hover,
.About .about_R .R_a .a_a .a_Bu .Bu_c:hover{
  background-color: #ffffff;
  cursor: pointer;
}
.About .about_R .R_a .a_a .a_Bu .Bu_a :hover,
.About .about_R .R_a .a_a .a_Bu .Bu_b :hover,
.About .about_R .R_a .a_a .a_Bu .Bu_c :hover{
  color: #000;
}
.About .about_R .R_a .a_a .a_Bu .Bu_a{
  display: flex;
  /* justify-content: center; */

}
.About .about_R .R_a .a_a .a_Bu .Bu_a p,
.About .about_R .R_a .a_a .a_Bu .Bu_b p,
.About .about_R .R_a .a_a .a_Bu .Bu_c p{
  width: 70px;
  height: 50px;
  line-height: 50px;
  color: #ffffff;
  margin:  0 auto;
}
.About .about_R .R_a .a_a .a_Bu .Bu_b{}
.About .about_R .R_a .a_a .a_Bu .Bu_c{}

.About .about_R .R_b{
  display: none;
}
.About .about_R .R_c{
  display: none;
}
/* .About .about_R .R_d{
  height: 24%;
} */
</style>