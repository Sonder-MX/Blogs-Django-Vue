<template>
  <BlogHeader />
  <div id="user-center">
    <h3>更新资料信息</h3>
    <form>
      <div class="form-elem">
        <span>用户名：</span>
        <input v-model="userData.username" type="text" placeholder="输入用户名" />
      </div>

      <div class="form-elem">
        <span>新密码：</span>
        <input v-model="userData.password" type="password" placeholder="输入密码" />
      </div>

      <div class="form-elem">
        <button v-on:click.prevent="changeInfo">更新</button>
      </div>
    </form>
  </div>
  <BlogFooter />
</template>

<script setup>
import BlogHeader from "@/components/BlogHeader.vue"
import BlogFooter from "@/components/BlogFooter.vue"

import authorization from "@/utils/authorization"
import { sendPatchReq } from "@/http"
import { reactive, onMounted } from "vue"
import { useRouter } from "vue-router"

const router = useRouter()
const storage = localStorage
let userData = reactive({
  username: "",
  password: "",
  token: "",
})

onMounted(() => {
  userData.username = storage.getItem("username.myblog")
})

function changeInfo() {
  // 验证登录状态
  authorization().then((response) => {
    // 检查登录状态
    // 若登录已过期则不执行后续操作
    if (!response[0]) {
      alert("登录已过期，请重新登录")
      return
    }
    // 密码不能小于 6 位
    if (userData.password.length < 6) {
      alert("Password too short.")
      return
    }
    // 旧的 username 用于向接口发送请求
    const oldName = storage.getItem("username.myblog")
    // 获取令牌
    userData.token = storage.getItem("access.myblog")
    if (userData.username !== "" && userData.password !== "") {
      let url = "/user/" + oldName + "/"
      sendPatchReq(
        url,
        { username: userData.username, password: userData.password },
        { headers: { Authorization: "Bearer " + userData.token } }
      ).then((resp) => {
        const uname = resp.data.username
        storage.setItem("username.myblog", uname)
        router.push({ name: "UserCenter", params: { username: uname } })
      })
    }
  })
}
</script>

<style scoped>
#user-center {
  text-align: center;
}
.form-elem {
  padding: 10px;
}
input {
  height: 25px;
  padding-left: 10px;
}
button {
  height: 35px;
  cursor: pointer;
  border: none;
  outline: none;
  background: gray;
  color: whitesmoke;
  border-radius: 5px;
  width: 200px;
}
</style>
