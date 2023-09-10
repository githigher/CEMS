<template>
  <div id="app">
    <div class="container">
      <!-- 左侧图片部分 -->
      <div class="left-section">
        <img src="..\assets\SchoolLogo.png" alt="Website Logo" width="125" height="125"/>
        <p class="text">综合测评管理系统</p>
      </div>

      <!-- 竖线分割 -->
      <div class="divider"></div>

      <!-- 右侧登录模块部分 -->
      <div class="right-section">
        <h2>账号登录</h2>
        <form @submit.prevent="submitForm">
          <div class="form-group">
            <label for="username">学号:</label>
            <input type="text" id="username" v-model="username" required />
          </div>
          <div class="form-group">
            <label for="password">密码:</label>
            <input type="password" id="password" v-model="password" required />
          </div>
          <button type="submit">登录</button>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import { getCurrentInstance } from 'vue';
import Cookies from 'js-cookie'

export default {
  data() {
    return {
      username: '',
      password: '',
    };
  },
  methods: {
    submitForm() {
      axios.post('http://127.0.0.1:8000/login', {id: this.username, password: this.password})
      .then(response =>{
        if (response.data.code == "001"){
          // 登陆成功的逻辑
          Cookies.set('UserId', this.username)
          this.$router.push('/home/HomePage')
        }else if(response.data.code == "003"){
          Cookies.set('UserId', "admin" + this.username)
          this.$router.push('/home/examine')
        }else{
          alert("账号密码错误")
        }
      })
      .catch(error =>{
        alert("Something went wrong...")
      })
    },
  },
};
</script>

<style>
.left-section {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  text-align: center;
}

.text {
  margin-top: 10px;
}

body, html {
  height: 100%;
  margin: 0;
  display: flex;
  justify-content: center;
  align-items: center;
}

#app {
  height: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
}

.container {
  display: flex;
  justify-content: center;
  align-items: center;
  max-width: 800px; /* 设置页面最大宽度，可根据需要调整 */
}

.left-section {
  flex: 1;
  padding-right: 50px; /* 调整图片和竖线之间的距离 */
  display: flex;
  justify-content: center;
  align-items: center;
}

.left-section{
  max-width: 100%;
  max-height: 100%;
}

.divider {
  width: 1px;
  height: 100px; /* 设置竖线的高度，可根据需要调整 */
  background-color: #ccc;
}

.right-section {
  flex: 1;
  padding-left: 50px; /* 调整登录模块和竖线之间的距离 */
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.right-section h2 {
  text-align: center;
}

.form-group {
  margin-bottom: 15px;
}

label {
  display: block;
  margin-bottom: 5px;
}

input[type="text"],
input[type="password"] {
  width: 100%;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 5px;
}

button {
  background-color: #4CAF50;
  color: white;
  padding: 10px 15px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

button:hover {
  background-color: #45a049;
}
</style>
