<template>
  <header class="header">
    <div class="header-title">计通学院综合测评管理系统</div>
    <div class="user-info">
      <span class="username">{{username}}</span>
      <ModifyPassword />
      <button class="logout-button" @click="logout">退出登录</button>
    </div>
  </header>
</template>

<script>
import {onMounted,getCurrentInstance } from "vue";
import Cookies from 'js-cookie'
import ModifyPassword from './ModifyPassword.vue'

export default {
  name: 'HeaderComponent',
  components: {
    ModifyPassword
  },
  data() {
    return {
      username: Cookies.get("UserId"),
    };
  },
  methods: {
    logout() {
      this.$router.push('/')
    }
  }
}
</script>

<style scoped>
/* 在这里添加你的样式 */
.header {
  background-color: #B3C0D1;
  color: #333;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.header-title {
  font-size: 20px;
  font-weight: bold;
}

.user-info {
  display: flex;
  align-items: center;
}

.username {
  margin-right: 10px;
}

.logout-button {
  background-color: transparent;
  color: #fff;
  border: none;
  cursor: pointer;
  font-size: 14px;
}
</style>
