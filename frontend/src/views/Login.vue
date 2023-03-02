<template>
  <BlogHeader></BlogHeader>

  <div id="grid">
    <div id="signup">
      <h3>注册账号</h3>
      <form>
        <div class="form-elem">
          <span>账号：</span>
          <input v-model="signupName" type="text" placeholder="输入用户名" />
        </div>
        <div class="form-elem">
          <span>密码：</span>
          <input v-model="signupPwd" type="password" placeholder="输入密码" />
        </div>
        <div class="form-elem">
          <span>密码：</span>
          <input v-model="againPwd" type="password" placeholder="再次输入密码" />
        </div>
        <div class="form-elem">
          <button type="button" @click.prevent="signup">提交</button>
        </div>
      </form>
      <div class="err-msg" v-show="errorMsg.length > 0">{{ errorMsg }}</div>
    </div>

    <div>
      <div id="signin">
        <h3>登录账号</h3>
        <form>
          <div class="form-elem">
            <span>账号：</span>
            <input v-model="signinName" type="text" placeholder="输入用户名" />
          </div>

          <div class="form-elem">
            <span>密码：</span>
            <input v-model="signinPwd" type="password" placeholder="输入密码" />
          </div>

          <div class="err-msg">{{ loginErr }}</div>

          <div class="form-elem">
            <button v-on:click.prevent="signin">登录</button>
          </div>
        </form>
      </div>
    </div>
  </div>

  <BlogFooter></BlogFooter>
</template>

<script setup>
import BlogHeader from "@/components/BlogHeader.vue"
import BlogFooter from "@/components/BlogFooter.vue"
import { ref } from "vue"
import { sendPostReq, sendGetReq } from "@/http"
import { useRouter } from "vue-router"

const router = useRouter()
let signupName = ref("")
let signupPwd = ref("")
let againPwd = ref("")
let signupResponse = ref("")
let signinName = ref("")
let signinPwd = ref("")
let errorMsg = ref("")
let loginErr = ref("")

function signup() {
  if (signupName.value.length > 0 && signupPwd.value.length > 0 && againPwd.value.length > 0) {
    errorMsg.value = ""
    if (signupPwd.value !== againPwd.value) {
      againPwd.value = ""
      errorMsg.value = "两次密码不一致，请重新输入！"
      return
    }
    sendPostReq("/user/", { username: signupName.value, password: signupPwd.value })
      .then((res) => {
        errorMsg.value = ""
        signupResponse.value = res.data
        alert("注册成功！快去登录吧")

        signinName.value = signupName.value
        signinPwd.value = againPwd.value
        signupName.value = ""
        signupPwd.value = ""
        againPwd.value = ""
      })
      .catch((_) => (errorMsg.value = "注册失败，请重试！！！"))
  } else {
    errorMsg.value = "输入用户名或密码完成注册！！！"
  }
}

function signin() {
  sendPostReq("/token/", { username: signinName.value, password: signinPwd.value })
    .then((res) => {
      // 使用localStorage存储token
      const storage = localStorage
      // Date.parse(...) 返回1970年1月1日UTC以来的毫秒数
      // Token 被设置为1h，因此这里加上60000 * 60毫秒
      const expiredTime = Date.now() + 60000 * 60
      storage.setItem("access.myblog", res.data.access)
      storage.setItem("refresh.myblog", res.data.refresh)
      storage.setItem("expiredTime.myblog", expiredTime)
      storage.setItem("username.myblog", signinName.value)
      sendGetReq("/user/" + signinName.value + "/").then((resp) => {
        storage.setItem("isSuperuser.myblog", resp.is_superuser)
        // 路由跳转，登录成功后跳转到首页
        router.push({ name: "Home" })
      })
    })
    .catch((err) => {
      console.log(err.message)
      loginErr.value = "登录失败，请检查账号和密码是否正确！"
    })
}
</script>

<style scoped>
#grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
}

#signin {
  text-align: center;
}

#signup {
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
  width: 60px;
}

.err-msg {
  color: red;
}
</style>
