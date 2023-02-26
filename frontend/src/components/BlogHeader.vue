<template>
  <div id="header">
    <div class="grid">
      <div></div>
      <h1 class="main-title">
        <router-link :to="{ name: 'Home' }">My Drf-Vue Blog</router-link>
      </h1>
      <SearchBox></SearchBox>
    </div>
    <hr />
    <div class="login">
      <!-- <div v-if="userName">欢迎你~{{ userName }}</div> -->
      <div v-if="hasLogin">
        <div class="dropdown">
          <button class="dropbtn">欢迎, {{ userName }}!</button>
          <div class="dropdown-content">
            <router-link :to="{ name: 'UserCenter', params: { username: userName } }">
              用户中心
            </router-link>
          </div>
        </div>
      </div>
      <div v-else>
        <router-link to="/login" class="login-link">注册/登录</router-link>
      </div>
    </div>
  </div>
</template>

<script setup>
import SearchBox from "./SearchBox.vue"

import { ref, onMounted } from "vue"
import authorization from "@/utils/authorization"

let userName = ref("")
let hasLogin = ref(false)

onMounted(() => {
  authorization().then((data) => ([hasLogin.value, userName.value] = data))
  // const storage = localStorage
  // const expireTime = Number(storage.getItem("expiredTime.myblog")) // 过期时间
  // const refreshToken = storage.getItem("refresh.myblog") // 刷新令牌
  // // token未过期
  // if (expireTime > Date.now()) {
  //   userName.value = storage.getItem("username.myblog")
  // } else if (refreshToken) {
  //   // 有刷新令牌，重新申请令牌
  //   sendPostReq("/token/refresh", { refresh: refreshToken })
  //     .then((res) => {
  //       const nextExpiredTime = Date.now() + 60000
  //       storage.setItem("access.myblog", res.data.access)
  //       storage.setItem("expiredTime.myblog", nextExpiredTime)
  //       storage.removeItem("refresh.myblog")
  //       userName.value = storage.getItem("username.myblog")
  //     })
  //     .catch(() => {
  //       storage.clear()
  //       userName.value = ""
  //     })
  // } else {
  //   // 无效token
  //   storage.clear()
  //   userName.value = ""
  // }
})
</script>

<style scoped>
/* 样式来源: https://www.runoob.com/css/css-dropdowns.html* /
    /* 下拉按钮样式 */
.dropbtn {
  background-color: mediumslateblue;
  color: white;
  padding: 8px 8px 30px 8px;
  font-size: 16px;
  border: none;
  cursor: pointer;
  height: 16px;
  border-radius: 5px;
}
/* 容器 <div> - 需要定位下拉内容 */
.dropdown {
  position: relative;
  display: inline-block;
}
/* 下拉内容 (默认隐藏) */
.dropdown-content {
  display: none;
  position: absolute;
  background-color: #f9f9f9;
  min-width: 120px;
  box-shadow: 0 8px 16px 0 rgba(0, 0, 0, 0.2);
  text-align: center;
}
/* 下拉菜单的链接 */
.dropdown-content a {
  color: black;
  padding: 12px 16px;
  text-decoration: none;
  display: block;
}
/* 鼠标移上去后修改下拉菜单链接颜色 */
.dropdown-content a:hover {
  background-color: #f1f1f1;
}
/* 在鼠标移上去后显示下拉菜单 */
.dropdown:hover .dropdown-content {
  display: block;
}
/* 当下拉内容显示后修改下拉按钮的背景颜色 */
.dropdown:hover .dropbtn {
  background-color: darkslateblue;
}
</style>

<style scoped>
#header {
  text-align: center;
  margin-top: 20px;
}

.main-title a {
  color: black;
  text-decoration: none;
}

.grid {
  display: grid;
  grid-template-columns: 1fr 4fr 1fr;
}

.login-link {
  color: black;
}

.login {
  text-align: right;
  padding-right: 5px;
}
</style>
