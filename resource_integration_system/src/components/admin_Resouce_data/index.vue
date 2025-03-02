<template>
  <div class="resouce-data-admin">
    <el-table :data="resouce_data" height="250" style="width: 100%">
      <el-table-column prop="name" label="资源名称" width="180" />
      <el-table-column prop="author" label="作者" width="180" />
      <el-table-column prop="img" label="资源图片">
        <template #default="scope">
          <!-- <el-link :href="scope.row.img" target="_blank">
              <el-button>点击跳转</el-button>
          </el-link> -->
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
          <el-button size="small" @click="handleEdit(scope.row.id)" >
            编辑
          </el-button>
          <el-button
            size="small"
            type="danger"
            @click="handleDelete(scope.row.id)"
          >
            删除
          </el-button>
        </template>
      </el-table-column>
    </el-table>
    <el-dialog v-model="dialogFormVisible" title="资源编辑" width="80%">
      <el-form :model="resouce_from" label-position="top">
        <el-form-item label="资源名">
          <el-input  v-model="resouce_from.name" autocomplete="off" />
        </el-form-item>
        <el-form-item label="资源地址">
          <el-input v-model="resouce_from.url" autocomplete="off" />
        </el-form-item>
        <el-form-item label="资源说明">
          <!-- <el-input v-model="resouce_from.desc" autocomplete="off" /> -->
          <!-- <el-input type="textarea" autosize  v-model="resouce_from.desc" placeholder="请输入资源说明" /> -->
          <wangeditor  v-model="resouce_from.desc"></wangeditor>
        </el-form-item>
        <el-form-item label="资源图片">
          <el-input v-model="resouce_from.img" autocomplete="off" />
        </el-form-item>
        <el-form-item label="资源标签">
          <el-input v-model="resouce_from.tab" autocomplete="off" />
        </el-form-item>
        
        <el-card v-if="file_list != ''">
          <FileUpload :resourceid="resourceFileId"></FileUpload>
        </el-card>

        <el-table :data="file_list" height="250" style="width: 100%" v-if="file_list != ''">
          <el-table-column prop="fileName" label="资源文件名称" />
          <el-table-column prop="id" label="操作">
        <template #default="scope">
          <el-button size="small" type="danger" @click="deleteFile(scope.row.id)" >删除</el-button>
        </template>
      </el-table-column>
        </el-table>
      </el-form>
      <template #footer>
        <div class="dialog-footer">
          <el-button @click="dialogFormVisible = false">取消</el-button>
          <el-button type="primary" @click="updateResource(this.resouce_from,this.resouce_update_id)">
            提交
          </el-button>
        </div>
      </template>
    </el-dialog>
    <!-- <el-dialog v-model="dialogdelentVisible" title="是否删除" width="500">
      <template #footer>
        <div class="dialog-footer">
          <el-button @click="dialogdelentVisible = false">取消</el-button>
          <el-button type="primary" @click="dialogdelentVisible = false">
            提交
          </el-button>
        </div>
      </template>
    </el-dialog> -->
  </div>
</template>

<script>
import { resourceApi } from '@/api/resource'
import FileUpload from '@/components/FileUpload.vue'
import wangeditor from '@/components/wangeditor.vue'
export default {
name: 'admin_Resouce_data',
components:{FileUpload,wangeditor},
data(){
    return {
        resouce_data:[],
        dialogFormVisible:false,
        resouce_from: {
          name: '',
          url: '',
          tab: '',
          img: '' ,
          desc:'',
        },
        file_list:[],
        resouce_update_id: '',
        resouce_delete_id: '',
        resourceFileId:"",
    }
},
methods:{
    async getData() {
      try {
        const res = await resourceApi.getResources()
        this.resouce_data = res.data
      } catch (error) {
        console.error('获取资源列表失败:', error)
      } finally {
      }
    },
    // 更新资源 updateResource(data,id)
    async updateResource(data,id){
      
      try{
        const res = await resourceApi.updateResource(data,id)
        if(res.code === 200){
          console.log('更新资源成功',res)
          this.$message.success('更新资源成功')
        }else{
          console.log('更新资源失败',res)
          this.$message.success('更新资源失败')
        }
      } catch(erro) {

      }
      this.dialogFormVisible = false
      this.getData()
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
    // 根据id获取资源 getResourceById(id)
    async getResourceById(id){
      try{
        console.log('id',id);
        const res = await resourceApi.getResourceById(id)
        if(res.code === 200){
          console.log('获取资源成功',res)
          this.resouce_from.name = res.data.name
          this.resouce_from.url = res.data.url
          this.resouce_from.tab = res.data.tab
          this.resouce_from.img = res.data.img
          this.resouce_from.desc = res.data.desc
          this.resourceFileId = res.data.resourceFileId
          this.file_list = res.data.fileData
          console.log(this.resourceFileId);
        }else{
          console.log('获取资源失败',res)
        }
      } catch(erro) {
          console.log("获取请求失败",erro);
      }
    },
    handleEdit(id){
      console.log('编辑',id)
      this.resouce_update_id = id
      this.dialogFormVisible = true
      this.getResourceById(id)
      this.getData()
    },
    handleDelete(id){
      console.log('删除',id)
      this.resouce_delete_id = id
      this.$confirm('此操作将永久删除该资源, 是否继续?', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning'
      }).then(() => {
        this.deleteResource(id)
        this.$message({
          type: 'success',
          message: '删除成功!'
        });
      }).catch(() => {
        this.$message
      });
    },
    async deleteFile(id){
      try{
        this.$confirm('此操作将永久删除该文件, 是否继续?', '提示', {
          confirmButtonText: '确定',
          cancelButtonText: '取消',
          type: 'warning'
        }).then(async () => {
          await resourceApi.deleteResourceFile(id);
          this.$message.success('删除成功');
        this.getData(); // 刷新数据
        })
      } catch(error){
        console.log("删除失败",error);
      }
    }
},

//组件挂载成功后调用获取数据的方法


mounted(){
    this.getData()
},
}
</script>

<style>

</style>