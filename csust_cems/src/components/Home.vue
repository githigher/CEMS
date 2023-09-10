<template>
  <el-container >
    <el-header>
      <HomeHeader/>
    </el-header>
    <el-container>
      <el-aside width="250px">
        <HomeAside/>
      </el-aside>
      <el-main>
        <router-view></router-view>
      </el-main>
    </el-container>
  </el-container>
</template>

<script>
import HomeAside from './HomeAside.vue';
import HomeHeader from './HomeHeader.vue';

export default {
  components: {
    HomeAside,
    HomeHeader
  }
}
</script>

<style>
.el-header{
  background-color: #B3C0D1;
  color: #333;
  text-align: center;
  line-height: 60px;
}
.el-aside {
  background-color: #E9EEF3;
  color: #333;
  text-align: center;
  line-height: 160px;
}
html,body,#app,.demo,.el-container {
  height: 100%;
  width: 100%;
}
</style>
