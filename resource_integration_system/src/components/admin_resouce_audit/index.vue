<template>
  <el-table :data="resouce_data" height="250" style="width: 100%">
      <el-table-column prop="name" label="资源名称" width="180" />
      <el-table-column prop="author" label="作者" width="180" />
      <el-table-column prop="img" label="资源图片">
        <template #default="scope">
          <el-image :src="scope.row.img" fit="cover" style="width: 100px; height: 100px"></el-image>
        </template>
      </el-table-column>
      <el-table-column prop="tab" label="资源标签" >
        <template #default="scope">
              <el-tag>{{ scope.row.tab }}</el-tag>
        </template>
      </el-table-column>
      <el-table-column prop="url" label="资源地址" >
        <template #default="scope">
          <el-link :href="scope.row.url" target="_blank">
            <el-button>点击跳转</el-button>
          </el-link>
        </template>
      </el-table-column>
      <el-table-column prop="updateTime" label="更新时间" />
      <el-table-column prop="id" label="操作">
        <template #default="scope">
          <el-button
            size="small"
            type="danger"
            @click="handleDelete(scope.row.id)"
          >
            审核通过
          </el-button>
          <el-button
            size="small"
            @click="ResourceFileById(scope.row.id)"
          >
            查看详情
          </el-button>
        </template>
      </el-table-column>
    </el-table>
    <el-dialog v-model="dialogVisible" title="查看待审核资源" >
      <el-form :model="resourse_info" label-position="top">
        <el-form-item label="资源名">
          <el-input  v-model="resourse_info.name" autocomplete="off" />
        </el-form-item>
        <el-form-item label="资源地址">
          <el-input v-model="resourse_info.url" autocomplete="off" />
        </el-form-item>
        <el-form-item label="资源说明">
          <!-- <el-input v-model="resouce_from.desc" autocomplete="off" /> -->
          <el-input type="textarea" autosize  v-model="resourse_info.desc" placeholder="请输入资源说明" />
        </el-form-item>
        <el-form-item label="资源图片">
          <el-input v-model="resourse_info.img" autocomplete="off" />
        </el-form-item>
        <el-form-item label="资源标签">
          <el-input v-model="resourse_info.tab" autocomplete="off" />
        </el-form-item>
        
        <el-card>
          <FileUpload :resourceid="resourse_info.resourceFileId"></FileUpload>
        </el-card>

        <el-table :data="resourse_info.fileData" height="250" style="width: 100%">
          <el-table-column prop="fileName" label="资源文件名称" />
          <el-table-column prop="fileUrl" label="资源文件地址"></el-table-column>
          <el-table-column prop="id" label="操作">
            <template #default="scope">
              <el-button size="small" type="danger" @click="deleteFile(scope.row.id)" >删除</el-button>
            </template>
          </el-table-column>
        </el-table>
      </el-form>
      <template #footer>
        <div class="dialog-footer">
          <el-button @click="dialogVisible = false">取消</el-button>
          <el-button type="primary" @click="updateResource(this.resouce_from,this.resouce_update_id)">
            提交
          </el-button>
        </div>
      </template>
    </el-dialog>
</template>

<script>
import { resourceApi } from '@/api/resource'
import FileUpload from '@/components/FileUpload.vue'
export default {
    name:'admin_resouce_audit',
    components:{FileUpload},
    data(){
        return{
          dialogVisible: false,
            resouce_data:[],
            resourse_info:{},
            
        }
    },
    methods:{
        async getData(){
            try{
                const res = await resourceApi.ResourceAudit()
                this.resouce_data = res.data
                
                console.log(res.data);
            } catch(e){
                console.log(e)
            }
        },
        async ResourceAuditById(id){
            try{
                await resourceApi.ResourceAuditById(id)
            } catch(e){
                console.log(e)
            }
            this.getData()
        },
        //根据id获取文件类型资源
        async ResourceFileById(id){
          this.dialogVisible=true
            try{
                const info = await resourceApi.getResourceById(id)
                this.resourse_info = info.data
                
            } catch(e){
                console.log(e)
            }
        },
         // 根据id删除资源 deleteResource(id)
        async deleteResource(id){
          try{
            const res = await resourceApi.deleteResource(id)
            if(res.code === 200){
              console.log('删除资源成功',res)
            }else{
              console.log('删除资源失败',res)
            }
          } catch(erro) {

          }
          this.getData()
        },
        handleDelete(id){
            console.log('审核',id)
            this.$confirm('此操作将该资源展示到主页中, 是否继续?', '提示', {
                confirmButtonText: '通过',
                cancelButtonText: '取消',
                type: 'warning'
            }).then(() => {
                this.ResourceAuditById(id)
                this.$message({
                type: 'success',
                message: '审核成功!'
                });
                this.time()
            }).catch(() => {
                this.$message
            });
            this.time()
        },
        // 定时器3秒后调用请求
        // async getData(){
        //     try{
        //         const res = await resourceApi.ResourceAudit()
        //         this.resouce_data = res.data
        //     } catch(e){
        //         console.log(e)
        //     }
        //     setTimeout(() => {
        //         this.getData()
        //     }, 3000);
        // }
        time(){
            setTimeout(() => {
                this.getData()
            }, 30);
        }
    },
    created(){
        this.getData()
    },
    mounted(){

    }

}
</script>

<style>

</style>