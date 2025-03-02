<template>
    <div class="admin-update-log-data">
      <div class="add-log">
        <el-alert class="board-rids-10" title="系统信息管理模块涉及重要信息，删除操作不可逆，默认无法直接删除" type="info" show-icon />
      </div>
      <div class="all-log">
       <el-table :data="sys_info_data">
          <el-table-column prop="infoTitle" label="系统信息主题"  />
          <el-table-column prop="infoP" label="信息字段" />
          <el-table-column prop="infoView" label="信息字段值"  />
          <el-table-column prop="infoDesc" label="信息文本说明" />
          <el-table-column prop="infoType" label="信息状态" />
          <el-table-column prop="infoCreateTime" label="信息创建时间" />
          <el-table-column prop="infoUpdateTime" label="信息更新时间" />
          <el-table-column prop="infoId" label="操作">
            <template #default="scope">
              <el-button size="small" @click="handleEdit(scope.row.infoId)">编辑</el-button>
              <el-button size="small" disabled type="danger" @click="handleDelete(scope.row.logId)" > 删除 </el-button>
            </template>
          </el-table-column>
        </el-table>
        <!-- 更新系统信息 -->
        <el-dialog v-model="dialogFormVisible" title="更新系统信息" width="500">
            <el-form  label-position="top" label-width="80px" :model="from_sys_info_data">
                <el-form-item label="系统信息主题:">
                  <el-input v-model="from_sys_info_data.infoTitle" placeholder="请输入系统信息主题" />
                </el-form-item>
                <el-form-item label="信息字段:">
                  <el-input v-model="from_sys_info_data.infoP" placeholder="请输入信息字段" />
                </el-form-item>
                <el-form-item label="信息字段值:">
                  <el-input v-model="from_sys_info_data.infoView" placeholder="请输入信息字段值" />
                </el-form-item>
                <el-form-item label="信息文本说明:">
                  <el-input v-model="from_sys_info_data.infoDesc" placeholder="请输入信息文本说明" />
                </el-form-item>
                <el-form-item label="信息状态:">
                  <el-select
                  v-model="from_sys_info_data.infoType"
                  placeholder="Select"
                  size="large"
                  style="width: 240px"
                >
                  <el-option
                    v-for="(item , index) in sys_info_type"
                    :key="index"
                    :label="item"
                    :value="item"
                  />
                </el-select>
                </el-form-item>
            </el-form>
            <template #footer>
                <div class="dialog-footer">
                <el-button @click="dialogFormVisible = false">取消</el-button>
                <el-button type="primary" @click="postFrom()">提交</el-button>
                </div>
            </template>
            </el-dialog>
      </div>
    </div>
  </template>
  
  <script>
  import {sysinfoApi} from '@/api/sys_info'
  export default {
    name:"admin_sysinfo_date",
      data(){
          return{
            dialogVisible:false,
            dialogFormVisible:false,
            from_sys_info_data:{
                infoTitle:"",
                infoP:"",
                infoView:"",
                infoDesc:"",
                infoType:""
            },
            from_sys_info_data_id:0,
            sys_info_data:[],
            sys_info:{},
            sys_info_type:["success","info","warning","danger"],
            }
      },
      methods:{
        async addUpdatesysinfodata(){

        },
        async getsysinfodata(){
            try {
                const res = await sysinfoApi.getAllSysInfo();
                this.sys_info_data=res.data;

                console.log(res.data);
            } catch (error) {
                console.log(error);
            }
        },
        // 编辑数据
        handleEdit(id){
          console.log(id);
          const log = this.findLogById(id);
          console.log(log);
          this.sys_info = log;
          this.from_sys_info_data_id=log.infoId;
          this.from_sys_info_data.infoDesc=log.infoDesc;
          this.from_sys_info_data.infoView=log.infoView;
          this.from_sys_info_data.infoType=log.infoType;
          this.from_sys_info_data.infoTitle=log.infoTitle;
          this.from_sys_info_data.infoP=log.infoP;
          this.dialogFormVisible= true;
        },
        // 提交更新数据
        async postFrom(){
          try {
            await sysinfoApi.updateSysInfo(this.from_sys_info_data_id, this.from_sys_info_data);
            this.getsysinfodata();
            this.dialogFormVisible = false;
            this.$message.success("更新成功");
            this.getsysinfodata();
          } catch (error) {
            console.log(error);
            this.$message.success("更新失败"+error);
            this.getsysinfodata();
          }
        },
        // 删除数据
        // handleDelete(id){},
        // 传入id-根据id寻找log_date中对应id是数据-返回数据
        findLogById(id) {
          const inoo = this.sys_info_data.find(info => info.infoId === id);
          return inoo;
        }
  
  
      },
      created(){
          this.getsysinfodata();
          
      },
      mounted(){
          
      }
  }
  </script>
  
  <style>
  
  </style>