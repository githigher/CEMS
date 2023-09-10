<template>
  <div>
    <el-button @click="visible = true">
      修改密码
    </el-button>
    <el-drawer v-model="visible" :show-close="false">
      <template #header="{ close, titleId, titleClass }">
        <h4 :id="titleId" :class="titleClass">修改密码</h4>
        <el-button type="danger" @click="close">
          关闭
        </el-button>
      </template>
      <form>
        新密码:<br>
        <input type="text" name="new_password" v-model="new_password"><br><br>
        确认密码:<br>
        <input type="text" name="again_password" v-model="again_password">
        <br><br>
        <input type="submit" value="提交" @click="changePassword">
      </form>
    </el-drawer>
  </div>
</template>

<script>
import { ref } from 'vue'
import { ElButton, ElDrawer } from 'element-plus'
import Cookies from 'js-cookie'

export default{
  name: 'ModifyPassword',
  data() {
    return {
      visible : ref(false),
      new_password: '',
      again_password: ''
    };
  },
  methods: {
    changePassword(){
      axios.post('http://127.0.0.1:8000/ChangePassword', {id: Cookies.get('UserId'), new_password: this.new_password, again_password: this.again_password})
            .then(response =>{
              if (response.data.code == "001"){
                alert("修改密码成功")
              }else if (response.data.code == "002"){
                alert("Something went wrong...")
              }else{
                alert("两次密码输入不一致")
              }
            })
            .catch(error =>{
              alert("Something went wrong...")
            })
    }
  }
};
</script>
