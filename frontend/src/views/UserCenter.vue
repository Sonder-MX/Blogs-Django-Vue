<template>
  <BlogHeader :welcomeName="welcomeName" />
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

      <div class="form-elem">
        <button class="btn-danger" v-on:click.prevent="deleteUser">注销用户</button>
      </div>
    </form>
  </div>
  <BlogFooter />
</template>

<script setup>
import BlogHeader from "@/components/BlogHeader.vue"
import BlogFooter from "@/components/BlogFooter.vue"

import authorization from "@/utils/authorization"
import { sendPatchReq, sendDeleteReq } from "@/http"
import { ref, reactive, onMounted } from "vue"
import { useRouter } from "vue-router"

const router = useRouter()
const storage = localStorage
let userData = reactive({
  username: "",
  password: "",
  token: "",
})
let welcomeName = ref("")

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
        welcomeName.value = storage.getItem("username.myblog")
        router.push({ name: "UserCenter", params: { username: uname } })
      })
    }
  })
}

function deleteUser() {
  if (confirm("确定要删除用户吗？")) {
    authorization().then((res) => {
      if (res[0]) {
        userData.token = storage.getItem("access.myblog")
        sendDeleteReq("/user/" + userData.username + "/", {
          headers: { Authorization: "Bearer " + userData.token },
        }).then(() => {
          storage.clear()
          router.push({ name: "Home" })
        })
      }
    })
  }
}

onMounted(() => {
  userData.username = storage.getItem("username.myblog")
})
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

.btn-danger {
  background-color: rgb(246, 65, 65);
}
</style>
