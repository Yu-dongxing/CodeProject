<template>
  <div>
    <div class="addResource">
      <el-card>
        <!-- style="min-width: 100px;max-width: 300px;" -->
          <el-form  label-position="top" label-width="80px" :model="form">
            <!-- 需要添加文件类型资源，请点击 --> 
            <el-link @click="this.$router.push('/addresourcefile')" type="primary">添加文件类型资源</el-link>
            
          <el-form-item label="资源名称:">
            <el-input v-model="from.name" placeholder="请输入资源名称" />
          </el-form-item>
          <!-- <el-switch v-model="isFile" active-text="文件类型" inactive-text="链接类型" /> -->

          <el-form-item label="资源地址:" >
            <el-input @change="extractDomain" v-model="from.url" placeholder="请输入资源地址" />
          </el-form-item>

          <el-form-item label="资源说明:" >
            <!-- <el-input type="textarea" autosize  v-model="from.desc" placeholder="请输入资源说明" /> -->
            <wangeditor v-model="from.desc"></wangeditor>
          </el-form-item>


          <el-form-item label="资源图标(资源地址输入完成后点击图标输入框自动获取网站图标):">
            <el-input v-model="from.img" placeholder="请输入资源展示图标" />
          </el-form-item>


          <el-form-item label="标签:">
            <el-input-tag v-model="from.tag" placeholder="请输入标签" tag-type="success"/>
          </el-form-item>



          <el-form-item>
            <el-button type="primary" @click="onSubmit">提交</el-button>
            <el-button  @click="resetSubmit">重置</el-button>
          </el-form-item>
        </el-form>
        <!-- <el-card> -->
          <!-- <el-text style="color: var(--text-200);"><el-icon><InfoFilled /></el-icon>提交后资源将进入审核阶段，审核通过后资源将展示在首页</el-text> -->
          <el-alert class="board-rids-10" title="提交后资源将进入审核阶段，审核通过后资源将展示在首页" type="info" show-icon />
        <!-- </el-card> -->
        
      </el-card>
      
    </div>
  </div>
</template>

<script>
import { resourceApi } from '@/api/resource'
import { ElMessage } from 'element-plus'
import wangeditor from '@/components/wangeditor.vue'

export default {
    name: 'AddResouce',
    components:{wangeditor},
    data() {
      return {
        from: {
          name: '',
          url: '',
          tag: ['文章'],
          author: 'Guest', // 默认作者
          desc:"",
          img: 'https://mdn.alipayobjects.com/huamei_0prmtq/afts/img/A*PXAJTYXseTsAAAAAAAAAAAAADvuFAQ/original' // 默认图片
          // img:this.extractDomain(url)  // 默认图片
        },
        isFile: false,
      }
    },
    methods:{
      async onSubmit() {
        try {
          if(this.validateForm()){
              const submitData = {
              ...this.from,
              tab: this.from.tag.join(',') // 将标签数组转换为字符串
            }
            await resourceApi.addResource(submitData)
            ElMessage.success('添加成功,等待审核！！！')
            this.$router.push('/')
          }
        } catch (error) {
          ElMessage.error('添加失败')
          console.error('添加资源失败:', error)
        }
      },
      extractDomainurl(url) {
        // 使用URL构造函数解析URL
        const parsedUrl = new URL(url);
        this.from.img = 'https://api.akams.cn/favicon/'+parsedUrl.hostname;
        // 返回域名
        return 'https://api.akams.cn/favicon/'+parsedUrl.hostname;
      },


      extractDomain() {
        this.from.img = this.from.url ? this.extractDomainurl(this.from.url) : '';
      },
      extractDomainFromUrl(url) {
        try {
          const parsedUrl = new URL(url);
          return parsedUrl.hostname;
        } catch (error) {
          console.error('Invalid URL:', url);
          return ''; // 或者返回一个默认的域名或错误信息
        }
      },
      //表单较验，如果为空则提示
      validateForm() {
        const requiredFields = {
          name: '名称不能为空',
          url: '链接不能为空',
          tag: '标签不能为空',
          img: '图片不能为空',
        };
        let errorMessage = '';
        for (const field in requiredFields) {
          if (!this.from[field]) {
            errorMessage += `${requiredFields[field]}\n`;
          }
        }
        if (errorMessage) {
          ElMessage.error(errorMessage.trim());
          return false;
        }
        return true;
      },
      resetSubmit(){
        this.from = {
          name: '',
          url: '',
          tag: ['文章'],
          author: 'Guest', // 默认作者
          img: 'https://mdn.alipayobjects.com/huamei_0prmtq/afts/img/A*PXAJTYXseTsAAAAAAAAAAAAADvuFAQ/original' // 默认图片
        }
      }
    }

}
</script>

<style>
.board-rids-10{
  border-radius: 10px;
}
</style>