<template>
  <div id="header">
    <div class="grid">
      <div></div>
      <h1>My Drf-Vue Blog</h1>
      <div class="search">
        <form>
          <label>
            <input type="text" v-model="searchText" placeholder="输入搜索内容..." />
          </label>
          <button type="button" @click.prevent="searchArticle"></button>
        </form>
      </div>
    </div>
    <hr />
    <div class="login">
      <div v-if="userName">欢迎你~{{ userName }}</div>
      <div v-else>
        <router-link to="/login" class="login-link">注册/登录</router-link>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue"
import { useRouter } from "vue-router"
import { sendPostReq } from "@/http"

const router = useRouter()
let searchText = ref("")
let userName = ref("")

onMounted(() => {
  const storage = localStorage
  const expireTime = Number(storage.getItem("expiredTime.myblog")) // 过期时间
  const refreshToken = storage.getItem("refresh.myblog") // 刷新令牌
  // token未过期
  if (expireTime > Date.now()) {
    userName.value = storage.getItem("username.myblog")
  } else if (refreshToken) {
    // 有刷新令牌，重新申请令牌
    sendPostReq("/token/refresh", { refresh: refreshToken })
      .then((res) => {
        const nextExpiredTime = Date.now() + 60000
        storage.setItem("access.myblog", res.data.access)
        storage.setItem("expiredTime.myblog", nextExpiredTime)
        storage.removeItem("refresh.myblog")
        userName.value = storage.getItem("username.myblog")
      })
      .catch(() => {
        storage.clear()
        userName.value = ""
      })
  } else {
    // 无效token
    storage.clear()
    userName.value = ""
  }
})

function searchArticle() {
  if (searchText.value.trim()) {
    router.push({ name: "Home", query: { title: searchText.value.trim() } })
  }
}
</script>

<style scoped>
#header {
  text-align: center;
  margin-top: 20px;
}

.grid {
  display: grid;
  grid-template-columns: 1fr 4fr 1fr;
}

.search {
  padding-top: 22px;
}

* {
  box-sizing: border-box;
}

form {
  position: relative;
  width: 200px;
  margin: 0 auto;
}

input,
button {
  border: none;
  outline: none;
}

input {
  width: 100%;
  height: 35px;
  padding-left: 13px;
  padding-right: 46px;
}

button {
  height: 35px;
  width: 35px;
  cursor: pointer;
  position: absolute;
}

.search input {
  border: 2px solid gray;
  border-radius: 5px;
  background: transparent;
  top: 0;
  right: 0;
}

.search button {
  background: gray;
  border-radius: 0 5px 5px 0;
  width: 45px;
  top: 0;
  right: 0;
}

.search button:before {
  content: "搜索";
  font-size: 13px;
  color: white;
}

.login-link {
  color: black;
}

.login {
  text-align: right;
  padding-right: 5px;
}
</style>
